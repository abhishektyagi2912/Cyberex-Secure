import os
import logging

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import errors

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('u_auto_delete_it.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

SCOPES = 'https://mail.google.com/'
SERVICE = None


class AutoDeleteException(Exception):
    pass  # This class exists for this module to raise for AutoDelete-specific problems.


def init(user_id='me', token_file='token.json', credentials_file='credentials.json'):


    global SERVICE

    if not os.path.exists(credentials_file):
        raise AutoDeleteException('Can\'t find credentials file at %s. You can download this file from https://developers.google.com/gmail/api/quickstart/python and clicking "Enable the Gmail API"' % (os.path.abspath(credentials_file)))

    store = file.Storage(token_file)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(credentials_file, SCOPES)
        creds = tools.run_flow(flow, store)
    SERVICE = build('gmail', 'v1', http=creds.authorize(Http()))


def search(query, user_id='me'):


    if SERVICE is None:
        init()

    try:
        response = SERVICE.users().messages().list(userId=user_id,
                                                   q=query).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = SERVICE.users().messages().list(userId=user_id, q=query,
                                                       pageToken=page_token).execute()
            messages.extend(response['messages'])

        return messages


    except errors.HttpError as e:
        logger.exception(f'An error occurred:{e}')


def delete_messages(query, user_id='me'):
    """Deletes the message matching the query
       Parameters
       __________
       query : str
           The string Exactly you will use in Gmail's Search Box
           label:UNREAD
           from:username@email.com
           subject:hello
           has:attachment
           more described at https://support.google.com/mail/answer/7190?hl=en
       user_id : str
           User id of the Gmail User (default is 'me')
        """
    messages = search(query)
    if messages:
        for message in messages:
            SERVICE.users().messages().delete(userId=user_id, id=message['id']).execute()
            logger.info(f'Message with id: {message["id"]} deleted successfully.')
    else:
        logger.info("There was no message matching the query.")


if __name__ == '__main__':
    logger.info("Deleting messages from abc@gmail.com.")
    delete_messages('from:abc@gmail.com\
                    subject:"Go Shopping"\
                     older_than:1d'
                   )

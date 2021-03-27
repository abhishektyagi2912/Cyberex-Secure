from datetime import datetime as dt

host_path = "C:\Windows\System32\drivers\etc\hosts"
rediect = "127.0.0.1"

website_list = ("facebook.com", "www.facebook.com")

while True:

    if dt(dt.now().year, dt.now().month, dt.now().day):

        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(rediect+" "+website+"\n")

        print("website are blocked")
        break
    else:

        with open(host_path, "r+")as file:
            content = file.readline()
            file.seek(0)

            for line in content:

                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()
            print("website are ublock")
            break

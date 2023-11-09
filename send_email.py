import smtplib, ssl

def send_emailll(message):
    host = "smtp.gmail.com"  # faptul ca utilizam gmail
    port = 465  # e standart

    username = "iojosiojo912@gmail.com"
    password = "ixws uwot xbbr omiy"

    receiver = "stefiarko803@gmail.com"
    my_context = ssl.create_default_context()  # pt securitatea trimiterii


    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


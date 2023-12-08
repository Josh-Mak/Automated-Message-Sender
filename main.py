import pushbullet
import random
import schedule
import time
import imaplib
import email

# region Daily Messages Setup
pb = pushbullet.Pushbullet("")

list_of_body_messages = [
    "Remember to stay hydrated!",
    "Don't work too hard! Take a break!",
    "Have you checked in on Manjeet recently? Give her a text!",
]

title = "Daily Notes:"


def send_message():
    body = random.choice(list_of_body_messages)
    pb.push_note(title, body)


times_dict = {
    'Morning Hours': (8, 11),
    'Afternoon Hours': (12, 18),
    'Night Hours': (19, 22),
    'Minutes': (0, 59),
}


def pick_morning_time():
    mhi = random.randint(*times_dict['Morning Hours'])
    if mhi < 10:
        mhs = str(mhi)
        mhs = "0" + mhs
    else:
        mhs = str(mhi)
    mmi = random.randint(*times_dict['Minutes'])
    if mmi < 10:
        mms = str(mmi)
        mms = "0" + mms
    else:
        mms = str(mmi)

    picked_time = mhs + ":" + mms
    return picked_time


def pick_afternoon_time():
    ahi = random.randint(*times_dict['Afternoon Hours'])
    ahs = str(ahi)
    ami = random.randint(*times_dict['Minutes'])
    if ami < 10:
        ams = str(ami)
        ams = "0" + ams
    else:
        ams = str(ami)

    picked_time = ahs + ":" + ams
    return picked_time


def pick_night_time():
    nhi = random.randint(*times_dict['Night Hours'])
    nhs = str(nhi)
    nmi = random.randint(*times_dict['Minutes'])
    if nmi < 10:
        nms = str(nmi)
        nms = "0" + nms
    else:
        nms = str(nmi)

    picked_time = nhs + ":" + nms
    return picked_time


def set_message():
    morning_time = pick_morning_time()
    afternoon_time = pick_afternoon_time()
    night_time = pick_night_time()

    print(f"Set schedule to send messages for the day: {morning_time, afternoon_time, night_time}.")

    schedule.every().day.at(morning_time).do(send_message)
    schedule.every().day.at(afternoon_time).do(send_message)
    schedule.every().day.at(night_time).do(send_message)


schedule.every().day.at("00:00").do(set_message)
# endregion

# region daily quote as image from email
imap_server = "imap.gmail.com"
email_address = "@gmail.com"
password = ""

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")


def send_quote_from_email():
    msg_content = []
    _, msgnums = imap.search(None, "ALL")
    for msgnum in msgnums[0].split():
        _, data = imap.fetch(msgnum, "(RFC822)")

        message = email.message_from_bytes(data[0][1])
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                msg_content.append(part)

    imap.close()

    quote = ""
    for msg in msg_content:
        msg = str(msg)
        if len(msg) >= 7:
            if msg[0:5] == "Content":
                pass
            else:
                quote = quote + msg + "\n"

    pb.push_note("Daily Quote:", quote)


schedule.every().day.at("08:00").do(send_quote_from_email)
# endregion


while True:
    schedule.run_pending()
    time.sleep(60)

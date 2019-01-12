from urllib import request
from bs4 import BeautifulSoup
import time
import datetime
# import os
import ctypes
from twilio.rest import Client


ind = 1

def attempt():
    quote_page = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=19W&subj_area_cd=ECON%20%20%20&crs_catlg_no=0148%20%20%20%20&class_id=180590201&class_no=%20002%20%20'
    page = request.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')

    i = 0

    for box in soup.findAll('div', attrs={"class":"span1"}):
        if box.text == "Closed: Class Full (115)":
            i = 1
        else:
            pass
            # print("Hope~")

    if (i == 0):
        # print("NOISE!!")
        ind = 0

t = 0
while ind:
    attempt()
    time.sleep(10)
    print("Current time: ", datetime.datetime.now())
    # t = t + 1
    # print(t)
    # if (t == 2):
    #     break

# Send SMS
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Econ 148 is AVAILABLE!",
                     from_='+10000000000',
                     to='+10000000000'
                 )

print(message.sid)

print("Available at ", datetime.datetime.now())
ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True )

# # Play Sound
# dir = 'C:\\Users\\fzc20\\Downloads\\fire-truck-air-horn_daniel-simion.mp3'
# # winsound.PlaySound(dir, winsound.SND_FILENAME)
# os.system("start " + dir)


# Send email

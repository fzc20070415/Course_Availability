from urllib import request
from bs4 import BeautifulSoup
import time
import datetime
# import os
import ctypes
from twilio.rest import Client
import course_avail_config as config
# import thread

ind1 = 1
ind2 = 1
ind3 = 1
ind4 = 1

def alert_report(text):
    # Send SMS
    account_sid = config.account_sid
    auth_token = config.auth_token
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=text,
                         from_=config.from_,
                         to=config.to
                     )

    print(message.sid)
    print(text)
    print("Available at ", datetime.datetime.now())
    ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True )

    # # Play Sound
    # dir = 'C:\\Users\\fzc20\\Downloads\\fire-truck-air-horn_daniel-simion.mp3'
    # # winsound.PlaySound(dir, winsound.SND_FILENAME)
    # os.system("start " + dir)


    # Send email







################ TEMP #################



def attempt1():
    # Math 156 Lec 1
    quote_page = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=19S&subj_area_cd=CHIN%20%20%20&crs_catlg_no=0040%20%20%20%20&class_id=259120200&class_no=%20001%20%20'
    page = request.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')

    i = 0

    for box in soup.findAll('div', attrs={"class":"span1"}):
        print(box.text)
        if box.text == "Closed: Class Full (40)":
            i = 1
            break
        else:
            pass

    if (i == 0):
        global ind
        ind = 0

def attempt2():
    quote_page = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=19W&subj_area_cd=ECON%20%20%20&crs_catlg_no=0148%20%20%20%20&class_id=180590201&class_no=%20002%20%20'
    page = request.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')

    i = 0

    for box in soup.findAll('div', attrs={"class":"span1"}):
        print(box.text)
        if box.text == "Closed: Class Full (115)":
            i = 1
        else:
            pass

    if (i == 0):
        global ind
        ind = 0

def alert1():
    # Chinese 40
    print("CHIN40")
    quote_page = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=19S&subj_area_cd=CHIN%20%20%20&crs_catlg_no=0040%20%20%20%20&class_id=259120200&class_no=%20001%20%20'
    page = request.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')

    for box in soup.findAll('div', attrs={"class":"span1"}):
        if box.text[0] == 'O':
            print(box.text)
            # print(box.text[4], box.text[5], box.text[6])
            if (len(box.text)==20 and int(box.text[6])<4) or len(box.text)<20:
                global ind1
                ind1 = 0
                alert_report("CHIN40 has <40 spots left!!")
            break

def alert2():
    # Economics 144
    print("ECON144")
    quote_page = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=19S&subj_area_cd=ECON%20%20%20&crs_catlg_no=0144%20%20%20%20&class_id=180593200&class_no=%20001%20%20'
    page = request.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')

    for box in soup.findAll('div', attrs={"class":"span1"}):
        if box.text[0] == 'O':
            print(box.text)
            # print(len(box.text))
            # for i in range(len(box.text)):
            #     print (i, box.text[i])
            if (len(box.text)==20 and int(box.text[6])<3) or len(box.text)<20:
                global ind2
                ind2 = 0
                alert_report("ECON144 has <30 spots left!!")
            break

def alert3():
    # CS 168
    print("CS168")
    quote_page = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=19S&subj_area_cd=COM%20SCI&crs_catlg_no=0168%20%20%20%20&class_id=187712200&class_no=%20001%20%20'
    page = request.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    for box in soup.findAll('div', attrs={"class":"span1"}):
        if box.text[0] == 'O':
            print(box.text)
            # print(len(box.text))
            # for i in range(len(box.text)):
            #     print (i, box.text[i])
            if (len(box.text)==19 and box.text[6]==1 and int(box.text[7])<5) or len(box.text)<19:
                global ind3
                ind3 = 0
                alert_report("CS168 has <15 spots left!!")
            break

def wl_alert1():
    # CS 188
    print("CS188")
    quote_page = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=19S&subj_area_cd=COM%20SCI&crs_catlg_no=0188%20%20%20%20&class_id=187827202&class_no=%20002%20%20'
    page = request.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')

    for box in soup.findAll('div', attrs={"class":"span1"}):
        if box.text[0] == 'O':
            print(box.text)
            break

    for box in soup.findAll('div', attrs={"class":"span2"}):
        size = len(box.text)
        # print(size)
        # print(box.text[size-5:])
        if box.text[size-5:] == 'Taken':
            print(box.text)
            # print(box.text[4], box.text[5], box.text[6])
            # if size<14:
            #     global ind4
            #     ind4 = 0
            #     alert_report("CS188 has <10 waitlist spots left!!")
            break

def test1():
    quote_page = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=19S&subj_area_cd=CHIN%20%20%20&crs_catlg_no=0040%20%20%20%20&class_id=259120200&class_no=%20001%20%20'
    page = request.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    for box in soup.findAll('div'):
        print(box.text)

################ TEMP ################################




def extract_number(st):
    ind = 1
    start1 = -1
    end1 = -1
    start2 = -1
    end2 = -1
    for i in range(len(st)):
        if ind and st[i].isdigit():
            # print("i=", i)
            # print(st[i])
            if start1 == -1:
                start1 = i
                ind = 0
            elif start2 == -1:
                start2 = i
                ind = 0
        elif not ind and not st[i].isdigit():
            if end1 == -1:
                end1 = i
                ind = 1
            elif end2 == -1:
                end2 = i
                break
    # print(start1, end1, start2, end2)
    # print(int(st[start1:end1]), int(st[start2:end2]))
    return int(st[start1:end1]), int(st[start2:end2])

def general_info(course, page, THRESHOLD=-1, alert=0, info=0):
    if info != 0 and THRESHOLD <= 0:
        print("ERROR: Invalid THRESHOLD")
        exit(1)

    quote_page = page
    page = request.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    # Class Name
    temp = soup.find('div', attrs={"id":"subject_class"})
    print(temp.text)
    # Class Data
    temp = soup.find('div', attrs={"id":"enrl_mtng_info"})
    temp = temp.find('div', attrs={"class":"data-row"})
    # Status
    temp1 = temp.find('div', attrs={"class":"span1"})
    print(temp1.text)
    # Waitlist Status
    temp2 = temp.find('div', attrs={"class":"span2"})
    print(temp2.text)
    print(extract_number(temp2.text))

    INDICATOR = -1
    WL_INDICATOR = -1

    # Analyze Situation
    if "Closed" in temp1.text:
        print("Class Full Detected")
        INDICATOR = 0
    elif "Waitlist" in temp1.text:
        print("Waitlist Detected")
        INDICATOR = 1
    else:
        print("Available Spots Detected")
        INDICATOR = 2

    if "Taken" in temp2.text:
        WL_INDICATOR = 1
    else:
        WL_INDICATOR = 0

    # Send alert (i.e. prevent class become full)
    if alert:
        if INDICATOR==2: #Course open
            start, end = extract_number(temp1.text)
            if start < THRESHOLD:
                wl = -1
                if WL_INDICATOR:
                    wls, wle = extract_number(temp2.text)
                    wl = wle - wls
                report = course + " - Open Spot: " + str(start) + " ; Waitlist Spot: " + str(wl)
                alert_report(report)
                return 0
        elif INDICATOR==1: #Course WL
            start, end = extract_number(temp2.text)
            left = end - start
            if left < THRESHOLD:
                report = course + " - Waitlist Spot: " + str(left)
                alert_report(report)
                return 0
        else:
            pass
    # Send info only
    elif info:
        pass
    # Check if the class become available
    else:
        if INDICATOR==1: # Course WL
            start, end = extract_number(temp2.text)
            left = end - start
            report = course + " - Waitlist Spot: " + str(left)
            alert_report(report)
            return 0
        elif INDICATOR==2: # Course Open
            start, end = extract_number(temp1.text)
            report = course + " - Open Spot: " + str(start)
            alert_report(report)
            return 0

    return 1


# [Course_Name, Course_URL]
# GLOBAL_TABLE = []


def main():
    # main:
    print("Start at: ", datetime.datetime.now())
    t = 0
    while ind1 or ind2 or ind3 or ind4:
        try:
            if ind1:
                alert1()
            else:
                print("Alert1 triggered")
            if ind2:
                alert2()
            else:
                print("Alert2 triggered")
            if ind3:
                alert3()
            else:
                print("Alert3 triggered")
            if ind4:
                wl_alert1()
            else:
                print("WL_Alert1 triggered")
            # test1()
            # quote_page = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=19S&subj_area_cd=COM%20SCI&crs_catlg_no=0188%20%20%20%20&class_id=187827202&class_no=%20002%20%20'
            #
            # general_info("TEST Course", quote_page)
            # attempt2()
        except Exception as e:
            print(e)
            ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True )

        print("Last Update: ", (datetime.datetime.now()))
        time.sleep(60)
        # t = t + 1
        # print(t)
        # if (t == 2):
        #     break
    # for i in range(len(GLOBAL_TABLE)):
    #     try:
    #         thread.start_new_thread(general_info, (GLOBAL_TABLE[i][0], GLOBAL_TABLE[i][1]))



if __name__ == "__main__":
    main()

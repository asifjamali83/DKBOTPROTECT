#utf_8 *lineX [prankBots Creator]

"""
all of this data is copied from creator production PrankBots
don't forget to always support the prabkbots channel
SUBSCRABE HERE https://bit.ly/2xbVxlh
MY ID LINE :: http://line.me/ti/p/~Adiputra.95
Copy Righ :: http://github.com/Aprank
Country :: INDONESIA.
Response by acil


MENERIMA PEMESANAN SCRIPT
BOT PROTECT
BOT WAR
SELFBOT
BOT OFFICIAL TEMPLATE

PEMBUATAN BOT BEBAS REQUEST COMMANT, MODE BACKUP DLL.
JIKA KAMU MINAT CHAT KE ID LINE
line.me/ti/p/~Adiputra.95
[TIDAK MENERIMA CALL ATAU UNDANGAN GRUP [AUTO REJECET AKTIF]]

BIASAKAN CHAT DENGAN SOPAN WALAWPUN MENGGUNAKAN BAHAS FORMAL (LO,GW)
SELENGEAN ANE GAK RESPON.
YANG MAU KEPOIN GW JUGA BOLEH WKWKWK

"""
from Rank.lineX import *
from Rank.service.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from threading import Thread
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
_session = requests.session()
botStart = time.time()
settingsOpen = codecs.open("PrankBots.json","r","utf-8")
PrankBots = json.load(settingsOpen)
settingsOpen = codecs.open("Abouts.json","r","utf-8")
Abouts = json.load(settingsOpen)
ownerOpen = codecs.open("owner.json","r","utf-8")
Owner = json.load(ownerOpen)
adminOpen = codecs.open("admin1.json","r","utf-8")
admin = json.load(adminOpen)
kris = LINE()
kris.log("Auth Token : " + str(kris.authToken))
kr = LINE()
kr.log("Auth Token : " + str(kr.authToken))
kr1 = LINE()
kr1.log("Auth Token : " + str(kr1.authToken))
kr2 = LINE()
kr2.log("Auth Token : " + str(kr2.authToken))
kr3 = LINE()
kr3.log("Auth Token : " + str(kr3.authToken))
kr4 = LINE()
kr4.log("Auth Token : " + str(kr4.authToken))
kr5 = LINE()
kr5.log("Auth Token : " + str(kr3.authToken))
kr6 = LINE()
kr6.log("Auth Token : " + str(kr4.authToken))
print ("LOGIN SUCCESS [KRIS PASUKAN KEMENG CYBER ARMY BOT]")
oepoll = OEPoll(kris)
krisMID = kris.profile.mid
krMID = kr.profile.mid
kr1MID = kr1.profile.mid
kr2MID = kr2.profile.mid
kr3MID = kr3.profile.mid
kr4MID = kr4.profile.mid
Bots = [krisMID,krMID,kr1MID,kr2MID,kr3MID,kr4MID]
krBots = [kris,kr,kr1,kr2,kr3,kr4]
asist = [kr,kr1,kr2,kr3,kr4]
batara = [Bots, Owner, admin]
for bot1 in krBots:
    for bot2 in Bots:
        try:
            bot1.findAndAddContactsByMid(bot2)
        except:
            pass
def restart_program():
    backupData()
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    kris.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "tolsember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("Error.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))
    return
def backupData():
    try:
        backup = Owner
        f = codecs.open('owner.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = admin
        f = codecs.open('admin1.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = akun
        f = codecs.open('tilakun.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = pswd
        f = codecs.open('pass.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        kris.log("[ERROR] : " + str(error))
        return False
def help():
    with open('help.txt', 'r') as f:
        text = f.read()
    helpMsg = text
    return helpMsg
def command(text):
    krtext = text.lower()
    return krtext
#=======najong=========
#=======najong=========
def tajong(group, target):
    try:
        kr.kickoutFromGroup(group, [target])
    except:
        try:
            kr1.kickoutFromGroup(group, [target])
        except:
            try:
                kr2.kickoutFromGroup(group, [target])
            except:
                try:
                    kr3.kickoutFromGroup(group, [target])
                except:
                    try:
                       kr4.kickoutFromGroup(group, [target])
                    except:
                        try:
                           kr5.kickoutFromGroup(group, [target])
                        except:
                            try:
                              kr6.kickoutFromGroup(group, [target])
                            except:
                              pass
#=======batal=========
def batal(group, target):
    try:
        kr.cancelGroupInvitation(group, [target])
    except:
        try:
            kr1.cancelGroupInvitation(group, [target])
         except:
              try:
                kr2.cancelGroupInvitation(group, [target])
            except:
                try:
                    kr3.cancelGroupInvitation(group, [target])
                except:
                    try:
                       kr4.cancelGroupInvitation(group, [target])
                    except:
                        try:
                          kr5.cancelGroupInvitation(group, [target])
                        except:
                            try:
                              kr6.cancelGroupInvitation(group, [target])
                            except:
                              pass
#=======najong=========
def undang(group, target):
    try:
        kr.findAndAddContactsByMid(target)
        kr.inviteIntoGroup(group, [target])
    except:
        try:
            kr1.findAndAddContactsByMid(target)
            kr1.inviteIntoGroup(group, [target])
        except:
            try:
                kr2.findAndAddContactsByMid(target)
                kr2.inviteIntoGroup(group, [target])
            except:
                try:
                    kr3.findAndAddContactsByMid(target)
                    kr3inviteIntoGroup(group, [target])
                except:
                    try:
                       kr4.findAndAddContactsByMid(target)
                       kr4.inviteIntoGroup(group, [target])
                    except:
                        try:
                           kr5.findAndAddContactsByMid(target)
                           kr5.inviteIntoGroup(group, [target])                           
                        except:
                            try:
                              kr6.findAndAddContactsByMid(target)
                              kr6.inviteIntoGroup(group, [target])
                            except:
                              pass
def krisundangall(group, target):
    try:
        kris.inviteIntoGroup(group, [krMID,kr1MID,kr2MID,kr3MID,kr4MID,kr5MID,kr6MID])
        if target == krMID:
            kr.acceptGroupInvitation(group)
        if target == kr1MID:
            kr1.acceptGroupInvitation(group)
        if target == kr2MID:
            kr2.acceptGroupInvitation(group)
        if target == kr3MID:
            kr3.acceptGroupInvitation(group)
        if target == kr4MID:
            kr4.acceptGroupInvitation(group)
        if target == kr5MID:
            kr5.acceptGroupInvitation(group)
        if target == kr6MID:
            kr6.acceptGroupInvitation(group)
    except:
        try:
            kr.inviteIntoGroup(group, [krisMID,kr1MID,kr2MID,kr3MID,kr4MID,kr5MID,kr6MID])
            if target == krisMID:
                kris.acceptGroupInvitation(group)
            if target == kr1MID:
                kr1.acceptGroupInvitation(group)
            if target == kr2MID:
                kr2.acceptGroupInvitation(group)
            if target == kr3MID:
                kr3.acceptGroupInvitation(group)
            if target == kr4MID:
                kr4.acceptGroupInvitation(group)
            if target == kr3MID:
                kr5.acceptGroupInvitation(group)
            if target == kr4MID:
                kr6.acceptGroupInvitation(group)
        except:
            try:
                kr1.inviteIntoGroup(group, [krisMID,krMID,kr2MID,kr3MID,kr4MID,kr5MID,kr6MID])
                if target == krisMID:
                    kris.acceptGroupInvitation(group)
                if target == krMID:
                    kr.acceptGroupInvitation(group)
                if target == kr2MID:
                    kr2.acceptGroupInvitation(group)
                if target == kr3MID:
                    kr3.acceptGroupInvitation(group)
                if target == kr4MID:
                    kr4.acceptGroupInvitation(group)
                if target == kr5MID:
                    kr5.acceptGroupInvitation(group)
                if target == kr6MID:
                    kr6.acceptGroupInvitation(group)
            except:
                try:
                    kr2.inviteIntoGroup(group, [krisMID,krMID,kr1MID,kr3MID,kr4MID,kr5MID,kr6MID])
                    if target == krisMID:
                        kris.acceptGroupInvitation(group)
                    if target == krMID:
                        kr.acceptGroupInvitation(group)
                    if target == kr1MID:
                        kr1.acceptGroupInvitation(group)
                    if target == kr3MID:
                        kr3.acceptGroupInvitation(group)
                    if target == kr4MID:
                        kr4.acceptGroupInvitation(group)
                    if target == kr6MID:
                        kr5.acceptGroupInvitation(group)
                    if target == kr6MID:
                        kr6.acceptGroupInvitation(group)
                except:
                    try:
                        kr3.inviteIntoGroup(group, [krisMID,krMID,kr1MID,kr2MID,kr4MID,kr5MID,kr6MID])
                        if target == krisMID:
                            kris.acceptGroupInvitation(group)
                        if target == krMID:
                            kr.acceptGroupInvitation(group)
                        if target == kr1MID:
                            kr1.acceptGroupInvitation(group)
                        if target == kr2MID:
                            kr2.acceptGroupInvitation(group)
                        if target == kr4MID:
                            kr4.acceptGroupInvitation(group)
                        if target == kr5MID:
                            kr5.acceptGroupInvitation(group)
                        if target == kr6MID:
                            kr6.acceptGroupInvitation(group)
                    except:
                        try:
                            kr4.inviteIntoGroup(group, [krisMID,krMID,kr1MID,kr2MID,kr3MID,kr5MID,kr6MID])
                            if target == krisMID:
                                kris.acceptGroupInvitation(group)
                            if target == krMID:
                                kr.acceptGroupInvitation(group)
                            if target == kr1MID:
                                kr1.acceptGroupInvitation(group)
                            if target == kr2MID:
                                kr2.acceptGroupInvitation(group)
                            if target == kr3MID:
                                kr3.acceptGroupInvitation(group)
                            if target == kr5MID:
                                kr5.acceptGroupInvitation(group)
                            if target == kr6MID:
                                kr6.acceptGroupInvitation(group)
                        except Exception as error:
                            print ("[ERROR] : " + str(error))
def lockqr(group):
    G = kris.getGroup(group)
    G.preventedJoinByTicket = True
    try:
        kr6.updateGroup(G)
    except:
        try:
            kr5.updateGroup(G)
        except:
            try:
                kr4.updateGroup(G)
            except:
                try:
                    kr3.updateGroup(G)
                except:
                    try:
                       kr2.updateGroup(G)
                    except:
                        try:
                           kr1.updateGroup(G)
                        except:
                            try:
                              kr.updateGroup(G)
                            except:
                              pass
def black(target):
    if target not in settings["blacklist"]:
        settings["blacklist"][target] = True
    print("> PΔSUKΔN KΣMΣNG TARGET BLACKLIST <")
def botpoll(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 11:
            if op.param2 in settings["blacklist"]:
                if op.param2 in batara:
                    pass
                else:
                    t1 = Thread(target=lockqr, args=(op.param1,))
                    t1.start()
                    t2 = Thread(target=black, args=(op.param2,))
                    t2.start()
                    t3 = Thread(target=tajong, args=(op.param1, op.param2))
                    t3.start()
                return
            if settings["qr"] == True:
                if op.param2 in batara:
                    pass
                else:
                    t1a = Thread(target=lockqr, args=(op.param1,))
                    t1a.start()
                    t2a = Thread(target=black, args=(op.param2,))
                    t2a.start()
                    t3a = Thread(target=tajong, args=(op.param1, op.param2))
                    t3a.start()
                return
        if op.type == 13:
            if op.param3 in settings["blacklist"]:
                if op.param2 in batara:
                    t4 = Thread(target=batal, args=(op.param1, op.param3))
                    t4.start()
                else:
                    t5 = Thread(target=black, args=(op.param2,))
                    t5.start()
                    t6 = Thread(target=batal, args=(op.param1, op.param3))
                    t6.start()
                    t7 = Thread(target=tajong, args=(op.param1, op.param2))
                    t7.start()
                return
            if settings["cancel"] == True:
                if op.param2 in batara:
                    t4a = Thread(target=batal, args=(op.param1, op.param3))
                    t4a.start()
                else:
                    t5a = Thread(target=black, args=(op.param2,))
                    t5a.start()
                    t6a = Thread(target=batal, args=(op.param1, op.param3))
                    t6a.start()
                    t7a = Thread(target=tajong, args=(op.param1, op.param2))
                    t7a.start()
                return
            if krisMID in op.param3:
                if op.param2 in Owner:
                    kris.acceptGroupInvitation(op.param1)
                return
            if krisMID in op.param3:
                if op.param2 in Bots:
                    kris.acceptGroupInvitation(op.param1)
                return
            if krMID in op.param3:
                if op.param2 in Bots:
                    kr.acceptGroupInvitation(op.param1)
                return
            if kr1MID in op.param3:
                if op.param2 in Bots:
                    kr1.acceptGroupInvitation(op.param1)
                return
            if kr2MID in op.param3:
                if op.param2 in Bots:
                    kr2.acceptGroupInvitation(op.param1)
                return
            if kr3MID in op.param3:
                if op.param2 in Bots:
                    kr3.acceptGroupInvitation(op.param1)
                return
            if kr4MID in op.param3:
                if op.param2 in Bots:
                    kr4.acceptGroupInvitation(op.param1)
                return
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
                t8 = Thread(target=tajong, args=(op.param1, op.param2))
                t8.start()
                return
            if settings["pro"] == True:
                if op.param2 in batara:
                    pass
                else:
                    t9 = Thread(target=tajong, args=(op.param1, op.param2))
                    t9.start()
                return
        if op.type == 19:
            if op.param3 in krisMID:
                if op.param2 in batara:
                    t10 = Thread(target=undang, args=(op.param1, op.param3))
                    t10.start()
                else:
                    t11 = Thread(target=black, args=(op.param2,))
                    t11.start()
                    try:
                        t12 = Thread(target=krisundangall, args=(op.param1, op.param3))
                        t12.start()
                        tjong = Thread(target=tajong, args=(op.param1, op.param2))
                        tjong.start()
                    except:
                        try:
                            tjong1 = Thread(target=tajong, args=(op.param1, op.param2))
                            tjong1.start()
                            t13 = Thread(target=krisundangall, args=(op.param1, op.param3))
                            t13.start()
                        except:
                            try:
                                t14 = Thread(target=krisundangall, args=(op.param1, op.param3))
                                t14.start()
                                tjong2 = Thread(target=tajong, args=(op.param1, op.param2))
                                tjong2.start()
                            except:
                                try:
                                    tjong3 = Thread(target=tajong, args=(op.param1, op.param2))
                                    tjong3.start()
                                    t15 = Thread(target=krisundangall, args=(op.param1, op.param3))
                                    t15.start()
                                except:
                                    try:
                                        G = random.choice(asist).getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        random.choice(asist).updateGroup(G)
                                        Ticket = random.choice(asist).reissueGroupTicket(op.param1)
                                        kris.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        tjong4 = Thread(target=tajong, args=(op.param1, op.param2))
                                        tjong4.start()
                                        G = kris.getGroup(op.param1)
                                        G.preventedJoinByTicket = True
                                        kris.updateGroup(G)
                                        Ticket = kris.reissueGroupTicket(op.param1)
                                    except:
                                        pass
                return
            if op.param3 in krMID:
                if op.param2 in batara:
                    t16 = Thread(target=undang, args=(op.param1, op.param3))
                    t16.start()
                else:
                    t17 = Thread(target=black, args=(op.param2,))
                    t17.start()
                    try:
                        tjong5 = Thread(target=tajong, args=(op.param1, op.param2))
                        tjong5.start()
                        t18 = Thread(target=krisundangall, args=(op.param1, op.param3))
                        t18.start()
                    except:
                        try:
                            t19 = Thread(target=krisundangall, args=(op.param1, op.param3))
                            t19.start()
                            tjong6 = Thread(target=tajong, args=(op.param1, op.param2))
                            tjong6.start()
                        except:
                            pass
                return
            if op.param3 in kr1MID:
                if op.param2 in batara:
                    t20 = Thread(target=undang, args=(op.param1, op.param3))
                    t20.start()
                else:
                    t21 = Thread(target=black, args=(op.param2,))
                    t21.start()
                    try:
                        tjong7 = Thread(target=tajong, args=(op.param1, op.param2))
                        tjong7.start()
                        t22 = Thread(target=krisundangall, args=(op.param1, op.param3))
                        t22.start()
                    except:
                        try:
                            t23 = Thread(target=krisundangall, args=(op.param1, op.param3))
                            t23.start()
                            tjong8 = Thread(target=tajong, args=(op.param1, op.param2))
                            tjong8.start()
                        except:
                            pass
                return
            if op.param3 in kr2MID:
                if op.param2 in batara:
                    t24 = Thread(target=undang, args=(op.param1, op.param3))
                    t24.start()
                else:
                    t25 = Thread(target=black, args=(op.param2,))
                    t25.start()
                    try:
                        tjong9 = Thread(target=tajong, args=(op.param1, op.param2))
                        tjong9.start()
                        t26 = Thread(target=krisundangall, args=(op.param1, op.param3))
                        t26.start()
                    except:
                        try:
                            t27 = Thread(target=krisundangall, args=(op.param1, op.param3))
                            t27.start()
                            tjong10 = Thread(target=tajong, args=(op.param1, op.param2))
                            tjong10.start()
                        except:
                            pass
                return
            if op.param3 in kr3MID:
                if op.param2 in batara:
                    t28 = Thread(target=undang, args=(op.param1, op.param3))
                    t28.start()
                else:
                    t29 = Thread(target=black, args=(op.param2,))
                    t29.start()
                    try:
                        tjong11 = Thread(target=tajong, args=(op.param1, op.param2))
                        tjong11.start()
                        t30 = Thread(target=krisundangall, args=(op.param1, op.param3))
                        t30.start()
                    except:
                        try:
                            t31 = Thread(target=krisundangall, args=(op.param1, op.param3))
                            t31.start()
                            tjong12 = Thread(target=tajong, args=(op.param1, op.param2))
                            tjong12.start()
                        except:
                            pass
                return
            if op.param3 in kr4MID:
                if op.param2 in batara:
                    t32 = Thread(target=undang, args=(op.param1, op.param3))
                    t32.start()
                else:
                    t33 = Thread(target=black, args=(op.param2,))
                    t33.start()
                    try:
                        tjong13 = Thread(target=tajong, args=(op.param1, op.param2))
                        tjong13.start()
                        t34 = Thread(target=krisundangall, args=(op.param1, op.param3))
                        t34.start()
                    except:
                        try:
                            t35 = Thread(target=krisundangall, args=(op.param1, op.param3))
                            t35.start()
                            tjong14 = Thread(target=tajong, args=(op.param1, op.param2))
                            tjong14.start()
                        except:
                            pass
                return
            if op.param3 in kr5MID:
                if op.param2 in batara:
                    t24 = Thread(target=undang, args=(op.param1, op.param3))
                    t24.start()
                else:
                    t25 = Thread(target=black, args=(op.param2,))
                    t25.start()
                    try:
                        tjong9 = Thread(target=tajong, args=(op.param1, op.param2))
                        tjong9.start()
                        t26 = Thread(target=krisundangall, args=(op.param1, op.param3))
                        t26.start()
                    except:
                        try:
                            t27 = Thread(target=krisundangall, args=(op.param1, op.param3))
                            t27.start()
                            tjong10 = Thread(target=tajong, args=(op.param1, op.param2))
                            tjong10.start()
                        except:
                            pass
                return
            if op.param3 in kr6MID:
                if op.param2 in batara:
                    t28 = Thread(target=undang, args=(op.param1, op.param3))
                    t28.start()
                else:
                    t29 = Thread(target=black, args=(op.param2,))
                    t29.start()
                    try:
                        tjong11 = Thread(target=tajong, args=(op.param1, op.param2))
                        tjong11.start()
                        t30 = Thread(target=krisundangall, args=(op.param1, op.param3))
                        t30.start()
                    except:
                        try:
                            t31 = Thread(target=krisundangall, args=(op.param1, op.param3))
                            t31.start()
                            tjong12 = Thread(target=tajong, args=(op.param1, op.param2))
                            tjong12.start()
                        except:
                            pass
                return
            if op.param3 in Owner:
                if op.param2 in batara:
                    pass
                else:
                    to = Thread(target=tajong, args=(op.param1, op.param2))
                    to.start()
                    to1 = Thread(target=black, args=(op.param2,))
                    to1.start()
                    to2 = Thread(target=undang, args=(op.param1, op.param3))
                    to2.start()
                return
            if settings["pro"] == True:
                if op.param3 not in batara:
                    if op.param2 in batara:
                        pass
                    else:
                        too = Thread(target=tajong, args=(op.param1, op.param2))
                        too.start()
                        too1 = Thread(target=black, args=(op.param2,))
                        too1.start()
                    return
        if op.type == 32:
            if op.param3 in Bots:
                if op.param2 in batara:
                    tt1 = Thread(target=undang, args=(op.param1, op.param3))
                    tt1.start()
                else:
                    tt2 = Thread(target=tajong, args=(op.param1, op.param2))
                    tt2.start()
                    tt3 = Thread(target=black, args=(op.param2,))
                    tt3.start()
                    tt4 = Thread(target=undang, args=(op.param1, op.param3))
                    tt4.start()
                return
            if op.param3 in Owner:
                if op.param2 in batara:
                    pass
                else:
                    tt5 = Thread(target=tajong, args=(op.param1, op.param2))
                    tt5.start()
                    tt6 = Thread(target=black, args=(op.param2,))
                    tt6.start()
                    tt7 = Thread(target=undang, args=(op.param1, op.param3))
                    tt7.start()
                return
            if settings["cancel"] == True:
                if op.param3 not in batara:
                    if op.param2 in batara:
                        pass
                    else:
                        tt8 = Thread(target=tajong, args=(op.param1, op.param2))
                        tt8.start()
                        tt9 = Thread(target=black, args=(op.param2,))
                        tt9.start()
                    return
        if op.type == 26:
            msg = op.message
            to = msg.to
            if msg.contentType == 1:
                if settings['Upfoto'] == True:
                    path = kris.downloadObjectMsg(msg.id)
                    path = kr.downloadObjectMsg(msg.id)
                    path = kr1.downloadObjectMsg(msg.id)
                    path = kr2.downloadObjectMsg(msg.id)
                    path = kr3.downloadObjectMsg(msg.id)
                    path = kr4.downloadObjectMsg(msg.id)
                    path = kr5.downloadObjectMsg(msg.id)
                    path = kr6.downloadObjectMsg(msg.id)
                    kris.updateProfilePicture(path)
                    kr.updateProfilePicture(path)
                    kr1.updateProfilePicture(path)
                    kr2.updateProfilePicture(path)
                    kr3.updateProfilePicture(path)
                    kr4.updateProfilePicture(path)
                    kr5.updateProfilePicture(path)
                    kr6.updateProfilePicture(path)
                    kr.sendMessage(to,"Update picture success")
                    kr1.sendMessage(to,"Update picture success")
                    kr2.sendMessage(to,"Update picture success")
                    kr3.sendMessage(to,"Update picture success")
                    kr4.sendMessage(to,"Update picture success")
                    kr5.sendMessage(to,"Update picture success")
                    kr6.sendMessage(to,"Update picture success")
                    settings['Upfoto'] = False
        if op.type in [25,26]:
            msg = op.message
            text = msg.text
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != kris.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = kr.findGroupByTicket(ticket_id)
                                group = kr1.findGroupByTicket(ticket_id)
                                group = kr2.findGroupByTicket(ticket_id)
                                group = kr3.findGroupByTicket(ticket_id)
                                group = kr4.findGroupByTicket(ticket_id)
                                group = kr5.findGroupByTicket(ticket_id)
                                group = kr6.findGroupByTicket(ticket_id)
                                kr.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr1.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr2.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr3.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr4.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr5.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr6.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr.sendMessage(to, "Masuk : %s" % str(group.name))
                                break
        if op.type in [25,26]:
            msg = op.message
            text = msg.text
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != kris.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        try:
                            krtext = command(text)
                            if krtext == "til keys":
                                if sender in Owner:
                                    random.choice(asist).sendMessage(to, str(help()))
                            elif krtext == "til speed":
                                if sender in Owner:
                                    start = time.time()
                                    kris.sendMessage(to, "Prosses...")
                                    elapsed_time = time.time() - start
                                    kris.sendMessage(to,"%s" % (elapsed_time))
                            elif krtext == "til sp":
                                if sender in Owner:
                                    start = time.time()
                                    kris.sendMessage(to, "Prosses...")
                                    elapsed_time = time.time() - start
                                    random.choice(asist).sendMessage(to,format(str(elapsed_time)))
                            elif krtext == "til lebet":
                                if sender in Owner:
                                    if msg.toType == 2:
                                        G = kris.getGroup(to)
                                        G.preventedJoinByTicket = False
                                        kris.updateGroup(G)
                                        Ticket = kris.reissueGroupTicket(to)
                                        for army in asist:
                                            try:
                                                army.acceptGroupInvitationByTicket(to, Ticket)
                                            except:
                                                pass
                                        G.preventedJoinByTicket = True
                                        random.choice(asist).updateGroup(G)
                                        random.choice(asist).sendMessage(to, "=> PΔSUKΔN KΣMΣNG \nSuccess!!!")
                            elif krtext == "pentil":
                                if sender in Owner:
                                    krrr = "u53b5b8dff081036a09b537fc92df5985"
                                    kris.findAndAddContactsByMid(krrr)
                                    kris.inviteIntoGroup(msg.to,[krrr])
                            elif krtext == "til backup":
                                if sender in Owner:
                                    kris.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kris.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kris.findAndAddContactsByMid(krMID)
                                    kris.findAndAddContactsByMid(kr1MID)
                                    kris.findAndAddContactsByMid(kr2MID)
                                    kris.findAndAddContactsByMid(kr3MID)
                                    kris.findAndAddContactsByMid(kr4MID)
                                    kr.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kr.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kr.findAndAddContactsByMid(krisMID)
                                    kr.findAndAddContactsByMid(kr1MID)
                                    kr.findAndAddContactsByMid(kr2MID)
                                    kr.findAndAddContactsByMid(kr3MID)
                                    kr.findAndAddContactsByMid(kr4MID)
                                    kr1.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kr1.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kr1.findAndAddContactsByMid(krisMID)
                                    kr1.findAndAddContactsByMid(krMID)
                                    kr1.findAndAddContactsByMid(kr2MID)
                                    kr1.findAndAddContactsByMid(kr3MID)
                                    kr1.findAndAddContactsByMid(kr4MID)
                                    kr2.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kr2.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kr2.findAndAddContactsByMid(krisMID)
                                    kr2.findAndAddContactsByMid(krMID)
                                    kr2.findAndAddContactsByMid(kr1MID)
                                    kr2.findAndAddContactsByMid(kr3MID)
                                    kr2.findAndAddContactsByMid(kr4MID)
                                    kr3.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kr3.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kr3.findAndAddContactsByMid(krisMID)
                                    kr3.findAndAddContactsByMid(krMID)
                                    kr3.findAndAddContactsByMid(kr1MID)
                                    kr3.findAndAddContactsByMid(kr2MID)
                                    kr3.findAndAddContactsByMid(kr4MID)
                                    kr4.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kr4.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kr4.findAndAddContactsByMid(krisMID)
                                    kr4.findAndAddContactsByMid(krMID)
                                    kr4.findAndAddContactsByMid(kr1MID)
                                    kr4.findAndAddContactsByMid(kr2MID)
                                    kr4.findAndAddContactsByMid(kr3MID)
                                    random.choice(asist).sendMessage(to, "Backup done...")
                            elif krtext == "til masuk":
                                if sender in Owner:
                                    try:
                                        kris.findAndAddContactsByMid(krMID)
                                        kris.inviteIntoGroup(to,[krMID])
                                        kr.acceptGroupInvitation(to)
                                        kr.findAndAddContactsByMid(kr1MID)
                                        kr.inviteIntoGroup(to,[kr1MID])
                                        kr1.acceptGroupInvitation(to)
                                        kr1.findAndAddContactsByMid(kr2MID)
                                        kr1.inviteIntoGroup(to,[kr2MID])
                                        kr2.acceptGroupInvitation(to)
                                        kr2.findAndAddContactsByMid(kr3MID)
                                        kr2.inviteIntoGroup(to,[kr3MID])
                                        kr3.acceptGroupInvitation(to)
                                        kr3.findAndAddContactsByMid(kr4MID)
                                        kr3.inviteIntoGroup(to,[kr4MID])
                                        kr4.acceptGroupInvitation(to)
                                        kr4.findAndAddContactsByMid(kr5MID)
                                        kr4.inviteIntoGroup(to,[kr5MID])
                                        kr5.acceptGroupInvitation(to)
                                        kr5.findAndAddContactsByMid(kr6MID)
                                        kr5.inviteIntoGroup(to,[kr6MID])
                                        kr6.acceptGroupInvitation(to)
                                    except:
                                        pass
                            elif krtext == "til asup":
                                if sender in Owner:
                                    try:
                                        G = kris.getGroup(to)
                                        G.preventedJoinByTicket = False
                                        kris.updateGroup(G)
                                        Ticket = kris.reissueGroupTicket(to)
                                        kr.acceptGroupInvitationByTicket(to,Ticket)
                                        kr1.acceptGroupInvitationByTicket(to,Ticket)
                                        kr2.acceptGroupInvitationByTicket(to,Ticket)
                                        kr3.acceptGroupInvitationByTicket(to,Ticket)
                                        kr4.acceptGroupInvitationByTicket(to,Ticket)
                                        kr5.acceptGroupInvitationByTicket(to,Ticket)
                                        kr6.acceptGroupInvitationByTicket(to,Ticket)
                                        G = kris.getGroup(to)
                                        G.preventedJoinByTicket = True
                                        kris.updateGroup(G)
                                        Ticket = kris.reissueGroupTicket(to)
                                    except:
                                        pass
                            elif krtext.startswith("til cium "):
                                if sender in Owner:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        if target in Owner:
                                            pass
                                        else:
                                            try:
                                                kr1.sendMessage(to, "Maaf ya izin mencumbu...")
                                                settings["blacklist"][target] = True
                                                kr1.kickoutFromGroup(to,[target])
                                            except:
                                                try:
                                                    kr2.sendMessage(to, "Maaf ya izin merayu...")
                                                    settings["blacklist"][target] = True
                                                    kr2.kickoutFromGroup(to,[target])
                                                except:
                                                    try:
                                                        kr3.sendMessage(to, "Maaf ya izin memadu...")
                                                        settings["blacklist"][target] = True
                                                        kr3.kickoutFromGroup(to,[target])
                                                    except:
                                                        try:
                                                            kr4.sendMessage(to, "Maaf ya izin mengentu...")
                                                            settings["blacklist"][target] = True
                                                            kr4.kickoutFromGroup(to,[target])
                                                        except:
                                                             try:
                                                                 kr5.sendMessage(to, "Maaf ya izin merayu...")
                                                                 settings["blacklist"][target] = True
                                                                  kr5.kickoutFromGroup(to,[target])
                                                               except:
                                                                    try:
                                                                        kr6.sendMessage(to, "Maaf ya izin merayu...")
                                                                        settings["blacklist"][target] = True
                                                                         kr6.kickoutFromGroup(to,[target])
                                                                       except:
                                                                          random.choice(asist).sendMessage(to, "LIMIT")
                            elif krtext == "bl":
                                if sender in Owner:
                                    if settings["blacklist"] == {}:
                                        random.choice(asist).sendMessage(to,"Tidak Ada kontak blacklist")
                                    else:
                                        mc = "Daftar Blacklist "
                                        num=1
                                        ragets = kris.getContacts(settings["blacklist"])
                                        for mi_d in ragets:
                                            mc+="\n%i. %s" % (num, mi_d.displayName)
                                            num=(num+1)
                                        mc+="\n\n Total %i Blacklist " % len(ragets)
                                        random.choice(asist).sendMessage(to, mc)
                            elif krtext == "cbl":
                                if sender in Owner:
                                    settings["blacklist"] = {}
                                    random.choice(asist).sendMessage(to,"sukses membersihkan blacklist..!!")
                            elif krtext == "til respon":
                                if sender in Owner:
                                    kr.sendMessage(to, "1")
                                    kr1.sendMessage(to, "2")
                                    kr2.sendMessage(to, "3")
                                    kr3.sendMessage(to, "4")
                                    kr4.sendMessage(to, "5")
                                    kr5.sendMessage(to, "6")
                                    kr6.sendMessage(to, "7")
                            elif krtext == "til absen":
                                if sender in Owner:
                                    kr1.sendMessage(to, " Hadir..!!!")
                                    kr2.sendMessage(to, " Hadir..!!!")
                                    kr.sendMessage(to, " Hadir..!!!")
                                    kr3.sendMessage(to, " Hadir..!!!")
                                    kr4.sendMessage(to, " Hadir..!!!")
                                    kr5.sendMessage(to, " Hadir..!!!")
                                    kr6.sendMessage(to, " Hadir..!!!")
                            elif krtext == "til changepp on":
                                if sender in Owner:
                                    settings['Upfoto'] = True
                                    kris.sendMessage(to,"Send Pict For UpPict")
                            elif krtext == "til changepp off":
                                if sender in Owner:
                                    settings['Upfoto'] = False
                                    kris.sendMessage(to,"Send Pict Already Off")
                            elif krtext == "ping":
                                if sender in Owner:
                                    text0 = (" Pong..!!")
                                    kr.sendMessage(to, text0)
                                    text1 = (" Pong..!!")
                                    kr1.sendMessage(to, text1)
                                    text2 = (" Pong..!!")
                                    kr2.sendMessage(to, text2)
                                    text3 = (" Pong..!!")
                                    kr3.sendMessage(to, text3)
                                    text4 = (" Pong..!!")
                                    kr4.sendMessage(to, text4)
                                    text3 = (" Pong..!!")
                                    kr5.sendMessage(to, text5)
                                    text5 = (" Pong..!!")
                                    kr6.sendMessage(to, text6)
                                    text6 = (" Pong..!!")
                            elif krtext == "til cabut":
                                if sender in Owner:
                                    random.choice(asist).sendMessage(to, "Hmm..., pamit dah...")
                                    kr1.leaveGroup(msg.to)
                                    kr2.leaveGroup(msg.to)
                                    kr3.leaveGroup(msg.to)
                                    kr4.leaveGroup(msg.to)
                                    kr5.leaveGroup(msg.to)
                                    kr6.leaveGroup(msg.to)
                                    kr.leaveGroup(msg.to)
                                    kris.leaveGroup(msg.to)
                            elif krtext == "til kabur":
                                if sender in Owner:
                                    random.choice(asist).sendMessage(to, "Hmm... di suruh pergi,, Ok lah kalau gitu, pamit...")
                                    kr1.leaveGroup(msg.to)
                                    kr2.leaveGroup(msg.to)
                                    kr3.leaveGroup(msg.to)
                                    kr4.leaveGroup(msg.to)
                                    kr5.leaveGroup(msg.to)
                                    kr6.leaveGroup(msg.to
                                    kr.leaveGroup(msg.to)
                            elif krtext == "til jointicket on":
                                if sender in Owner:
                                    settings["autoJoinTicket"] = True
                                    kris.sendMessage(to,"Join Ticket Set To On")
                            elif krtext == "til jointicket off":
                                if sender in Owner:
                                    settings["autoJoinTicket"] = False
                                    kris.sendMessage(to,"Join Ticket Set To Off")
                            elif krtext == "til on":
                                if sender in Owner:
                                    settings["qr"] = True
                                    settings["pro"] = True
                                    settings["cancel"] = True
                                    random.choice(asist).sendMessage(to,"til Siap digelitikin => Status On")
                            elif krtext == "til off":
                                if sender in Owner:
                                    settings["qr"] = False
                                    settings["pro"] = False
                                    settings["cancel"] = False
                                    random.choice(asist).sendMessage(to,"til Siap digelitikin => Status Off")
                            elif krtext == "til restart":
                                if sender in Owner:
                                    kris.sendMessage(msg.to, 'Restarting Prosses..')
                                    print ("Restarting")
                                    restart_program()
                            elif krtext == "til ancur":
                                if sender in Owner:
                                    if msg.toType == 2:
                                        gs = kr.getGroup(msg.to)
                                        gs = kr1.getGroup(msg.to)
                                        gs = kr2.getGroup(msg.to)
                                        gs = kr3.getGroup(msg.to)
                                        gs = kr4.getGroup(msg.to)
                                        gs = kr5.getGroup(msg.to)
                                        gs = kr6.getGroup(msg.to)
                                        time.sleep(0.0002)
                                        targets = []
                                        for g in gs.members:
                                            if targets in g.displayName:
                                                targets.append(g.mid)
                                        if targets == []:
                                            random.choice(asist).sendMessage(to,"LIMIT.!!!")
                                        else:
                                            for target in targets:
                                                if target not in Bots:
                                                    if target not in Owner:
                                                        try:
                                                            klist=[kr,kr1,kr2,kr3,kr4,kr5,kr6]
                                                            kicker=random.choice(klist)
                                                            kicker.kickoutFromGroup(to,[target])
                                                            print (to,[g.mid])
                                                        except:
                                                            pass
                            elif krtext.startswith("adminadd @"):
                                if sender in Owner:
                                    print ("[Command]Menambahkan admin")
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for g in key["MENTIONEES"]:
                                        targets.append(g["M"])
                                    for target in targets:
                                        if target in admin:
                                            kris.sendMessage(to, "Sudah Terdaftar di Admin")
                                        else:
                                            for target in targets:
                                                try:
                                                    admin.append(target)
                                                    kris.sendMessage(to,"Admin Ditambahkan")
                                                except Exception as error:
                                                    kris.sendMessage(to, str(error))
                                else:
                                    kris.sendMessage(to,"Perintah Ditolak.")
                                    kris.sendMessage(to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                            elif krtext.startswith("admindell @"):
                                if sender in Owner:
                                    print ("[Command]Menghapus admin")
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for g in key["MENTIONEES"]:
                                        targets.append(g["M"])
                                    for target in targets:
                                        if target not in admin:
                                            kr.sendMessage(to, "Belum Terdaftar di Admin")
                                        else:
                                            for target in targets:
                                                try:
                                                    admin.remove(target)
                                                    kris.sendMessage(to,"Admin Dihapus")
                                                except Exception as error:
                                                    kris.sendMessage(to, str(error))
                                else:
                                    kris.sendMessage(to,"Perintah Ditolak.")
                                    kris.sendMessage(to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                            elif krtext == "adminlist":
                                if sender in Owner:
                                    if admin == []:
                                        kris.sendMessage(to,"The Adminlist is empty")
                                    else:
                                        kris.sendMessage(to,"Tunggu...")
                                        mc = "╔═══════════════\n╠❂➣♥ Kris - Cyber Army Bot ♥\n╠❂➣══✪〘 Admin List 〙✪═══\n"
                                        for mi_d in admin:
                                            mc += "╠❂➣✪ " +kris.getContact(mi_d).displayName + "\n"
                                        kris.sendMessage(to,mc + "╠❂➣═══════════════\n╠❂➣✪〘 line://ti/p/~krissthea 〙\n╚═══════════════")
                            elif krtext == "til rejectall":
                                if sender in Owner:
                                    ginvited = kris.getGroupIdsInvited()
                                    ginvited = kr.getGroupIdsInvited()
                                    ginvited = kr1.getGroupIdsInvited()
                                    ginvited = kr2.getGroupIdsInvited()
                                    ginvited = kr3.getGroupIdsInvited()
                                    ginvited = kr4.getGroupIdsInvited()
                                    if ginvited != [] and ginvited != None:
                                        for gid in ginvited:
                                            kris.rejectGroupInvitation(gid)
                                            kr.rejectGroupInvitation(gid)
                                            kr1.rejectGroupInvitation(gid)
                                            kr2.rejectGroupInvitation(gid)
                                            kr3.rejectGroupInvitation(gid)
                                            kr4.rejectGroupInvitation(gid)
                                            kris.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                            kr.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                            kr1.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                            kr2.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                            kr3.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                            kr4.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                    else:
                                        kr.sendMessage(to, "Tidak ada undangan yang tertunda")
                            elif "changenametil: " in krtext:
                                if sender in Owner:
                                    name = krtext.split(": ")
                                    change = krtext.replace(name[0] + ": ","")
                                    cll0 = kris.getProfile()
                                    cll1 = kr.getProfile()
                                    cll2 = kr1.getProfile()
                                    cll3 = kr2.getProfile()
                                    cll4 = kr3.getProfile()
                                    cll5 = kr4.getProfile()
                                    cll0.displayName = change
                                    cll1.displayName = change
                                    cll2.displayName = change
                                    cll3.displayName = change
                                    cll4.displayName = change
                                    cll5.displayName = change
                                    kris.updateProfile(cll0)
                                    kr.updateProfile(cll1)
                                    kr1.updateProfile(cll2)
                                    kr2.updateProfile(cll3)
                                    kr3.updateProfile(cll4)
                                    kr4.updateProfile(cll5)
                                    kris.sendMessage(to," Update Name Success to " + str(change))
                                    kr.sendMessage(to," Update Name Success to " + str(change))
                                    kr1.sendMessage(to," Update Name Success to " + str(change))
                                    kr2.sendMessage(to," Update Name Success to " + str(change))
                                    kr3.sendMessage(to," Update Name Success to " + str(change))
                                    kr4.sendMessage(to," Update Name Success to " + str(change))
                            elif "changenametil0: " in krtext:
                                if sender in Owner:
                                    name = krtext.split(": ")
                                    change = krtext.replace(name[0] + ": ","")
                                    cll0 = kris.getProfile()
                                    cll0.displayName = change
                                    kris.updateProfile(cll0)
                                    kris.sendMessage(to," Update Name Success to " + str(change))
                            elif "changenametil1: " in krtext:
                                if sender in Owner:
                                    name = krtext.split(": ")
                                    change = krtext.replace(name[0] + ": ","")
                                    cll1 = kr.getProfile()
                                    cll1.displayName = change
                                    kr.updateProfile(cll1)
                                    kr.sendMessage(to," Update Name Success to " + str(change))
                            elif "changenametil2: " in krtext:
                                if sender in Owner:
                                    name = krtext.split(": ")
                                    change = krtext.replace(name[0] + ": ","")
                                    cll2 = kr1.getProfile()
                                    cll2.displayName = change
                                    kr1.updateProfile(cll2)
                                    kr1.sendMessage(to," Update Name Success to " + str(change))
                            elif "changenametil3: " in krtext:
                                if sender in Owner:
                                    name = krtext.split(": ")
                                    change = krtext.replace(name[0] + ": ","")
                                    cll3 = kr2.getProfile()
                                    cll3.displayName = change
                                    kr2.updateProfile(cll3)
                                    kr2.sendMessage(to," Update Name Success to " + str(change))
                            elif "changenametil4: " in krtext:
                                if sender in Owner:
                                    name = krtext.split(": ")
                                    change = krtext.replace(name[0] + ": ","")
                                    cll4 = kr3.getProfile()
                                    cll4.displayName = change
                                    kr3.updateProfile(cll4)
                                    kr3.sendMessage(to," Update Name Success to " + str(change))
                            elif "changenametil5: " in krtext:
                                if sender in Owner:
                                    name = krtext.split(": ")
                                    change = krtext.replace(name[0] + ": ","")
                                    cll5 = kr4.getProfile()
                                    cll5.displayName = change
                                    kr4.updateProfile(cll5)
                                    kr4.sendMessage(to," Update Name Success to " + str(change))
                            elif krtext == "til cek":
                                if sender in Owner:
                                    try:kris.inviteIntoGroup(to, [krisMID]);has = "OK"
                                    except:has = "NOT"
                                    try:kris.kickoutFromGroup(to, [krisMID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat 😎"
                                    else:sil = "Lemes 😥"
                                    if has1 == "OK":sil1 = "Sehat 😎"
                                    else:sil1 = "Lemes 😥"
                                    kris.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                                    try:kr.inviteIntoGroup(to, [krMID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr.kickoutFromGroup(to, [krMID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat 😎"
                                    else:sil = "Lemes 😥"
                                    if has1 == "OK":sil1 = "Sehat 😎"
                                    else:sil1 = "Lemes 😥"
                                    kr.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                                    try:kr1.inviteIntoGroup(to, [kr1MID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr1.kickoutFromGroup(to, [kr1MID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat 😎"
                                    else:sil = "Lemes 😥"
                                    if has1 == "OK":sil1 = "Sehat 😎"
                                    else:sil1 = "Lemes 😥"
                                    kr1.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                                    try:kr2.inviteIntoGroup(to, [kr2MID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr2.kickoutFromGroup(to, [kr2MID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat 😎"
                                    else:sil = "Lemes 😥"
                                    if has1 == "OK":sil1 = "Sehat 😎"
                                    else:sil1 = "Lemes 😥"
                                    kr2.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                                    try:kr3.inviteIntoGroup(to, [kr3MID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr3.kickoutFromGroup(to, [kr3MID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat 😎"
                                    else:sil = "Lemes 😥"
                                    if has1 == "OK":sil1 = "Sehat 😎"
                                    else:sil1 = "Lemes 😥"
                                    kr3.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                                    try:kr4.inviteIntoGroup(to, [kr4MID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr4.kickoutFromGroup(to, [kr4MID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat 😎"
                                    else:sil = "Lemes 😥"
                                    if has1 == "OK":sil1 = "Sehat 😎"
                                    else:sil1 = "Lemes 😥"
                                    kr4.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                                    try:kr5.inviteIntoGroup(to, [kr3MID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr5.kickoutFromGroup(to, [kr3MID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat 😎"
                                    else:sil = "Lemes 😥"
                                    if has1 == "OK":sil1 = "Sehat 😎"
                                    else:sil1 = "Lemes 😥"
                                    kr5.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                                    try:kr6.inviteIntoGroup(to, [kr4MID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr6.kickoutFromGroup(to, [kr4MID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat 😎"
                                    else:sil = "Lemes 😥"
                                    if has1 == "OK":sil1 = "Sehat 😎"
                                    else:sil1 = "Lemes 😥"
                                    kr6.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                        except Exception as e:
                            print (e)
    except Exception as error:
        kris.log("[ERROR] : " + str(error))
        if op.type == 59:
            print (op)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops != None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread1 = threading.Thread(target=botpoll, args=(op,))
                thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        print (e)
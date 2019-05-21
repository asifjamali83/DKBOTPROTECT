# -*- coding: utf-8 -*-

from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib3, urllib, urllib.parse
from threading import Thread
from googletrans import Translator
#==============================================================================#
mulai = time.time()

line = LINE("token")
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))



ki = LINE(token, appName="2")
ki.log("Auth Token : " + str(ki.authToken))
ki.log("Timeline Token : " + str(ki.tl.channelAccessToken))


ki2 = LINE(token, appName="3")
ki2.log("Auth Token : " + str(ki2.authToken))
ki2.log("Timeline Token : " + str(ki2.tl.channelAccessToken))


ki3 = LINE(token, appName="4")
ki3.log("Auth Token : " + str(ki3.authToken))
ki3.log("Timeline Token : " + str(ki3.tl.channelAccessToken))


ki4 = LINE(token, appName="5")
ki4.log("Auth Token : " + str(ki4.authToken))
ki4.log("Timeline Token : " + str(ki4.tl.channelAccessToken))


ki5 = LINE(token, appName="6")
ki5.log("Auth Token : " + str(ki5.authToken))
ki5.log("Timeline Token : " + str(ki5.tl.channelAccessToken))

ki6 = LINE(token, appName="7")
ki6.log("Auth Token : " + str(ki6.authToken))
ki6.log("Timeline Token : " + str(ki6.tl.channelAccessToken))


print ("Login succes ")

KAC = [line,ki,ki2,ki3,ki4,ki5,ki6]
lineMID = line.profile.mid
kiMID = ki.profile.mid
ki2MID = ki2.profile.mid
ki3MID = ki3.profile.mid
ki4MID = ki4.profile.mid
ki5MID = ki5.profile.mid
ki6MID = ki6.profile.mid

lineProfile = line.getProfile()
kiProfile = ki.getProfile()
ki2Profile = ki2.getProfile()
ki3Profile = ki3.getProfile()
ki4Profile = ki4.getProfile()
ki5Profile = ki5.getProfile()
ki6Profile = ki6.getProfile()

Bots = [lineMID,kiMID,ki2MID,ki3MID,ki4MID,ki5MID,ki6MID]
lineSettings = line.getSettings()
kiSettings = ki.getSettings()
ki2Settings = ki2.getSettings()
ki3Settings = ki3.getSettings()
ki4Settings = ki4.getSettings()
ki5Settings = ki5.getSettings()
ki6Settings = ki6.getSettings()

admin =["u7e99c5b3e4f01c95c104d0993fc41998"]

oepoll = OEPoll(line)
oepoll1 = OEPoll(ki)
oepoll2 = OEPoll(ki2)
oepoll3 = OEPoll(ki3)
oepoll4 = OEPoll(ki4)
oepoll5 = OEPoll(ki5)
oepoll6 = OEPoll(ki6)

responsename = line.getProfile().displayName
responsename1 = ki.getProfile().displayName
responsename2 = ki2.getProfile().displayName
responsename3 = ki3.getProfile().displayName
responsename4 = ki4.getProfile().displayName
responsename5 = ki5.getProfile().displayName
responsename6 = ki6.getProfile().displayName

welcome = []
responPc = []
autoRespon = []
autoResponImage = []
autoResponPm = []
msg_dict = {}
#==============================================================================#
settings = {
    "autoAdd": False,
    "autoJoin": False,
    "contact":False,
    "autoblock": False,
    "autoRespon": False,    
    "autoResponImage": False,
    "autoResponPm": False,
    "simiSimi": {},
    "autoLeave": False,
    "autojj": False,
    "leavemsg": False,
    "welcomemsg": False,
    "responPc": False,
    "keluar":"sᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ....\nsᴇᴍᴏɢᴀ ᴋᴀᴍᴜ ʙᴀɪᴋ2 ᴅɪʟᴜᴀʀ sᴀɴᴀ\nsᴀᴍᴘᴀɪ ᴊᴜᴍᴘᴀ 👌👌👌",
    "autoRead": False,
    "protect": False,
    "qrprotect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "tag": "Maaf aku sedang sibuk ",
    "tag2": "Ada apa kak tag saya",
    "tag3": "Ada apasih ka Pm mulu",
    "detectMention": False,
    "autorejc": False,
    "welcome":"sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ʏᴀ...\nsᴀʟᴀᴍ ᴋᴇɴᴀʟ ᴅᴀʀɪ sᴀʏᴀ 😘",
    "responpc": "Tag terus",
    "checkSticker": False,
    "TagMention": False,
    "TagMention2": False,
    "unsendMessage":False,
     "autoBalas": False,
    'wellcome':False,
    'bymsg':{},
    "lang":"JP",
    "autoJoinTicket": {},
    "changeGroupPicture":True,
    "Mute": True,    
    "changePicture": {},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
     "copy": False,
     "status": False,
     "target": {}
    }
}
wait = {
    "Sider":{},
    "limit": 1,
    "Mute": False,
    "contact": False,
    "timeline":False,
    "selfbot":True,    
    "sukaPost":True,
    "comment":"Autolike by: Team Dk Protection",    
    "welcomeOn":False,    
    "lang":"JP",
}

like = {
    "like":True,
    "likeOn":True,
    "liked":True,
    }
    
tikel = {
   'sid':"48198",
   'spkg':"2000000"
   }
   
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
    }
    


myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus

myProfile["displayName"] = kiProfile.displayName
myProfile["statusMessage"] = kiProfile.statusMessage
myProfile["pictureStatus"] = kiProfile.pictureStatus

myProfile["displayName"] = ki2Profile.displayName
myProfile["statusMessage"] = ki2Profile.statusMessage
myProfile["pictureStatus"] = ki2Profile.pictureStatus

myProfile["displayName"] = ki3Profile.displayName
myProfile["statusMessage"] = ki3Profile.statusMessage
myProfile["pictureStatus"] = ki3Profile.pictureStatus

myProfile["displayName"] = ki4Profile.displayName
myProfile["statusMessage"] = ki4Profile.statusMessage
myProfile["pictureStatus"] = ki4Profile.pictureStatus

myProfile["displayName"] = ki5Profile.displayName
myProfile["statusMessage"] = ki5Profile.statusMessage
myProfile["pictureStatus"] = ki5Profile.pictureStatus

myProfile["displayName"] = ki6Profile.displayName
myProfile["statusMessage"] = ki6Profile.statusMessage
myProfile["pictureStatus"] = ki6Profile.pictureStatus
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def restart_program(): 
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)    


def waktu(secs):
      mins, secs = divmod(secs,60)
      hours, mins = divmod(mins,60)
      return '%02d : Jam, ♪ %02d : Menit, ♪ %02d : Detik ♪' % (hours, mins, secs)
      
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)
    elif days > 0 and weaks == 0:
        return '%02d Hari %02d Jam %02d Menit %02d Detik' %(days, hours, mins, secs)
    elif days > 0 and weaks > 0:
        return '%02d Minggu %02d Hari %02d Jam %02d Menit %02d Detik' %(weaks, days, hours, mins, secs)
    
def a2():
    now2 = datetime.datetime.now()
    nowT = datetime.datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
        

def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "❨✪❩ ᴅk mentions ❨✪❩ \n\n1. ".format(str(len(mid)))
        textx2 ="╭════════════════╮\n ✍ ᴛᴏᴛᴀʟ {} ᴍᴇᴍʙᴇʀs".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        jp1 = line.getContact(lineMID).displayName
        line.sendMessage(to, textx2 + "\n ✍ ᴍᴇɴᴛɪᴏɴᴇs ʙʏ : " + jp1 + "\n╰════════════════╯")
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))
 
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╭════════════════╮\n   ❨✪❩ ᴅk mentions ❨✪❩ \n║\n║◍ 1. ".format(str(len(mid)))
        ginfo = line.getGroup(to)

        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "║◍ {}. ".format(str(no))
            else:
                textx += "\n「 Total {} Member 」\n╰════════════════╯".format(str(len(mid)))
        line.sendMessage(to, textx, {'AGENT_NAME':'「 Creator 」', 'AGENT_LINK': 'line://ti/p/~eg_2'.format(line.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + line.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@jeck "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = line.getAllContactIds()
        gid = line.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n🔰 Group : "+str(len(gid))+"\n🔰 Teman : "+str(len(teman))+"\n🔰 Expired : In "+hari+"\n🔰 Version : Saints Bot\n🔰 Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n🔰 Runtime : \n • "+bot
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    myid = line.getProfile().mid
    if myid in nm:
      nm.remove(myid)
    for mm in nm:
      akh = akh + 6
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 7
      akh = akh + 1
      bb += "@nrik "
    aa = (aa[:int(len(aa)-1)])
    text = bb
    try:
       line.sendMessage(to, text, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
       print(error)

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    line.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
        
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item) #Append all the links in the list named 'Links'
            #time.sleep(0.1) #Timer could be used to slow down the request for#image downloads
            page = page[end_content:]
    return items
    
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
    
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                line.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            

#atexit.register(atend)            
            
    
def helpmessage():
    helpMessage = """
╭═════════════
║[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]
╠═════════════
║✍ ᴍᴇ
║✍ sᴘ
║✍ sᴇᴛ
║✍ ᴘᴘ
║✍ ɴᴋ:
║✍ ɢɪᴅ
║✍ ᴋɪᴄᴋ @
║✍ ᴠᴋɪᴄᴋ @
║✍ ɴᴜᴋᴇ
║✍ Dkbots
║✍ ɢᴜʀʟ
║✍ ʜᴇʟᴘ
║✍ ᴍɪᴅ
║✍ ᴍɪᴅ @
║✍ ᴍᴜsɪᴄ
║✍ ᴍᴏᴠɪᴇ
║✍ ʀᴇᴊᴇᴄᴛ
║✍ ᴄᴀɴᴄᴇʟ
║✍ ɢᴘɪᴄᴛ
║✍ ᴄᴏᴠᴇʀ
║✍ ᴘɪᴄᴛ @
║✍ ᴄᴏᴠᴇʀ @
║✍ ᴄᴏᴘʏ @
║✍ ɢᴄᴀʟʟ
║✍ sᴘᴀᴍ
║✍ ʙᴀᴄᴋᴜᴘ
║✍ ʏᴏᴜᴛᴜʙᴇ
║✍ ɪᴍᴀɢᴇ:
║✍ ɪɴsᴛᴀɢʀᴀᴍ
║✍ ᴋᴀʟᴋᴜʟᴀᴛᴏʀ
║✍ ʙʀᴏᴀᴅᴄᴀsᴛ
║✍ Tag\Tag all\Desah
╠═════════════
║ʀᴇʟᴀᴛᴇᴅ ɢʀᴏᴜᴘ 
╠═════════════
║✍ ʀᴇʙᴏᴏᴛ
║✍ ʀᴜɴᴛɪᴍᴇ
║✍ ᴀʙᴏᴜᴛ
║✍ ᴄʀᴇᴀᴛᴏʀ
║✍ ᴍʏɴᴀᴍᴇ
║✍ ᴍʏʙɪᴏ
║✍ ᴍʏᴠɪᴅ
║✍ ɢᴇᴛʙɪᴏ @
║✍ ɢᴄʀᴇᴀᴛᴏʀ
║✍ ɢɴᴀᴍᴇ
║✍ ᴍᴇᴍʟɪsᴛ
║✍ ɢʀᴏᴜᴘs
║✍ ᴀᴜᴛᴏʟɪᴋᴇ
║✍ ʟɪɴᴋ ᴏɴ/ᴏғғ
║✍ ɢᴇᴛɴᴀᴍᴇ @
║✍ ᴜᴘᴅᴀᴛᴇ ᴘɪᴄᴛ
║✍ ɢᴇᴛ ᴄᴏɴᴛᴀᴄᴛ @
║✍ ʀᴇᴍᴏᴠᴇᴄʜᴀᴛ
║✍ ɢᴇᴛ ᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ
║✍ ᴜᴘᴅᴀᴛᴇ ᴘɪᴄᴛ ɢʀᴏᴜᴘ
║✍ ᴀʟʟsᴇᴛᴛɪɴɢs ᴍᴏᴅᴇ ᴏɴ
║✍ ᴀʟʟsᴇᴛᴛɪɴɢs ᴍᴏᴅᴇ ᴏғғ
║✍ ᴛᴀɢ /ʜɪ /ʜᴀɪ /ʜᴇᴍ /ᴅᴋ
╠═════════════
║Mimic Command
╠═════════════
║✍ ᴍɪᴍɪᴄᴀᴅᴅ
║✍ ᴍɪᴍɪᴄᴅᴇʟ
║✍ ᴍɪᴍɪᴄʟɪsᴛ
║✍ ᴍɪᴍɪᴄ ᴏɴ/ᴏғғ
╠═════════════
║Set Respon Dk
╠═════════════
║✍ sᴇᴛ ʀᴇsᴘᴏɴ1
║✍ ᴄᴇᴋ ʀᴇsᴘᴏɴ1
║✍ sᴇᴛ ʀᴇsᴘᴏɴ2
║✍ ᴄᴇᴋ ʀᴇsᴘᴏɴ2
║✍ sᴇᴛ ʀᴇsᴘᴏɴ3
║✍ ᴄᴇᴋ ʀᴇsᴘᴏɴ3
║✍ sᴇᴛ ʀᴇsᴘᴏɴᴘᴄ
║✍ ᴄᴇᴋ ʀᴇsᴘᴏɴᴘᴄ
║✍ sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ 
║✍ ᴄᴇᴋ ᴡᴇᴋᴄᴏᴍᴇ
║✍ sᴇᴛ ʟᴇᴀᴠᴇᴍsɢ
║✍ ᴄᴇᴋ ʟᴇᴀᴠᴇᴍsɢ
╠═════════════
║Command Kicker DK 
╠═════════════
║✍ ᴍʏʙᴏᴛ
║✍ ᴀʟʟʙᴏᴛ
║✍ ᴘɪɴɢ
║✍ ᴘᴏɴɢ
║✍ ʙᴏᴛs ᴍᴇ
║✍ ʀᴇsᴘᴏɴs
║✍ ɴᴜᴋᴇᴀʟʟ
║✍ ʙᴏᴛ①/⑤ ʜᴇʟᴘ
║✍ ʟᴇᴀᴠᴇᴀʟʟɢʀᴏᴜᴘs
║✍ ʙᴏᴛs ᴜᴘᴅɴᴀᴍᴇ
║✍ ʙᴏᴛs ᴜᴘᴅsᴛᴀᴛᴜs
║✍ Dk.masuk 
║✍ Dk.pulang
║✍ ʙᴏᴛs ᴄᴏᴘʏ @
║✍ ʙᴏᴛs ʙᴀᴄᴋᴜᴘ
║✍ ʙᴏᴛs ɢʀᴏᴜᴘs
║✍ ᴘᴜʟᴀɴɢ/ʙʏᴇ ᴀʟʟ
╠═════════════
║Command Protect 
╠═════════════
║✍ ᴘʀᴏᴛᴇᴄᴛ sᴇᴛ
║✍ ᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ
║✍ ʟɪɴᴋᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ
║✍ ᴄᴀɴᴄᴇʟᴀʟʟ ᴏɴ/ᴏғғ
║✍ ɪɴᴠɪᴛᴇᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ
║✍ ᴘʀᴏᴛᴇᴄᴛᴀʟʟ ᴏɴ/ᴏғғ
║✍ Promo
║✍ Kibar
║✍ Dkbot
║✍ Mybot
╚════════════
"""
    return helpMessage
#==============================================================================#


def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                line.sendMessage(op.param1, "ʜᴀʟʟᴏ {} ᴛx ғᴏʀ ᴀᴅᴅ ᴍᴇ\nʙʏ: ᴛᴇᴀᴍ ᴅᴋᴢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ".format(str(line.getContact(op.param1).displayName)))

        if op.type == 15:
            print ("[ 15 ] MEMBER LEAVE GROUP")
            if settings["leavemsg"] == True:
                contact = line.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                text = "ɢᴏᴏᴅ ʙʏᴇ @!\n{}".format(str(settings["keluar"]))
                sendMentionV2(op.param1, text, [op.param2])
                line.sendImageWithURL(op.param1,image)
 
#____________________                
        if op.type == 17:
            print ("[ 17 ] MEMBER JOIN GROUP")
            if settings["welcomemsg"] == True:
                group = line.getGroup(op.param1)
                contact = line.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                text = "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ☛ " + str(group.name) + "\nʜᴀʟʟᴏ @!{}\n".format(str(settings["welcome"]))
                sendMentionV2(op.param1, text, [op.param2])
                line.sendImageWithURL(op.param1,image)
            
        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if settings["autoblock"] == True:
                line.sendMessage(op.param1, "Halo {} \nThank yah \nSory akun saya Autoblock ".format(str(line.getContact(op.param1).displayName)))
                line.blockContact(op.param1)                
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            group = line.getGroup(op.param1)
            if settings["autoJoin"] == True:
                line.acceptGroupInvitation(op.param1)
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)
        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                elif text.lower() == 'menu':
                    helpMessage = helpmessage()
                    jp1 = line.getContact(lineMID).displayName
                    line.sendMessage(to,str(helpMessage) + "╭════════════════════╮\n❨✪❩ ᴠɪᴇᴡ sᴇᴛᴛɪɴɢs = sᴇᴛ \n❨✪❩ ᴠɪᴇᴡ ɪɴғᴏ ʙᴏᴛ = ᴀʙᴏᴜᴛ \n❨✪❩ ʜᴇʟᴘᴍᴇssᴀɢᴇ ʙʏ : " + jp1+ "\n╰════════════════════╯\n         ™ ᴛᴇᴀᴍ ᴅᴋ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ™\n")
                    #line.sendContact(to, "u6c878e91cef2d76e95d5f63da51b2193")
                elif text.lower() == 'bot1 help':
                    helpMessage = helpmessage()
                    jp1 = ki.getContact(kiMID).displayName
                    ki.sendMessage(to,str(helpMessage) + "╭════════════════════╮\n❨✪❩ ᴠɪᴇᴡ sᴇᴛᴛɪɴɢs = sᴇᴛ \n❨✪❩ ᴠɪᴇᴡ ɪɴғᴏ ʙᴏᴛ = ᴀʙᴏᴜᴛ \n❨✪❩ ʜᴇʟᴘᴍᴇssᴀɢᴇ ʙʏ : " + jp1+ "\n╰════════════════════╯\n         ™ ᴛᴇᴀᴍ ᴅᴋ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ™\n")
                    #line.sendContact(to, "u6c878e91cef2d76e95d5f63da51b2193")
                elif text.lower() == 'bot2 help':
                    helpMessage = helpmessage()
                    jp1 = ki2.getContact(ki2MID).displayName
                    ki2.sendMessage(to,str(helpMessage) + "╭════════════════════╮\n❨✪❩ ᴠɪᴇᴡ sᴇᴛᴛɪɴɢs = sᴇᴛ \n❨✪❩ ᴠɪᴇᴡ ɪɴғᴏ ʙᴏᴛ = ᴀʙᴏᴜᴛ \n❨✪❩ ʜᴇʟᴘᴍᴇssᴀɢᴇ ʙʏ : " + jp1+ "\n╰════════════════════╯\n         ™ ᴛᴇᴀᴍ ᴅᴋ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ™\n")
                    #line.sendContact(to, "u6c878e91cef2d76e95d5f63da51b2193")
                elif text.lower() == 'bot3 help':
                    helpMessage = helpmessage()
                    jp1 = ki3.getContact(ki3MID).displayName
                    ki3.sendMessage(to,str(helpMessage) + "╭════════════════════╮\n❨✪❩ ᴠɪᴇᴡ sᴇᴛᴛɪɴɢs = sᴇᴛ \n❨✪❩ ᴠɪᴇᴡ ɪɴғᴏ ʙᴏᴛ = ᴀʙᴏᴜᴛ \n❨✪❩ ʜᴇʟᴘᴍᴇssᴀɢᴇ ʙʏ : " + jp1+ "\n╰════════════════════╯\n         ™ ᴛᴇᴀᴍ ᴅᴋ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ™\n")
                    #line.sendContact(to, "u6c878e91cef2d76e95d5f63da51b2193")
                elif text.lower() == 'bot4 help':
                    helpMessage = helpmessage()
                    jp1 = ki4.getContact(ki4MID).displayName
                    ki4.sendMessage(to,str(helpMessage) + "╭════════════════════╮\n❨✪❩ ᴠɪᴇᴡ sᴇᴛᴛɪɴɢs = sᴇᴛ \n❨✪❩ ᴠɪᴇᴡ ɪɴғᴏ ʙᴏᴛ = ᴀʙᴏᴜᴛ \n❨✪❩ ʜᴇʟᴘᴍᴇssᴀɢᴇ ʙʏ : " + jp1+ "\n╰════════════════════╯\n         ™ ᴛᴇᴀᴍ ᴅᴋ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ™\n")
                    #line.sendContact(to, "u6c878e91cef2d76e95d5f63da51b2193")
                    
                elif text.lower() == 'bot5 help':
                    helpMessage = helpmessage()
                    jp1 = ki5.getContact(ki5MID).displayName
                    ki5.sendMessage(to,str(helpMessage) + "╭════════════════════╮\n❨✪❩ ᴠɪᴇᴡ sᴇᴛᴛɪɴɢs = sᴇᴛ \n❨✪❩ ᴠɪᴇᴡ ɪɴғᴏ ʙᴏᴛ = ᴀʙᴏᴜᴛ \n❨✪❩ ʜᴇʟᴘᴍᴇssᴀɢᴇ ʙʏ : " + jp1+ "\n╰════════════════════╯\n         ™ ᴛᴇᴀᴍ ᴅᴋ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ™\n")
                    #line.sendContact(to, "u6c878e91cef2d76e95d5f63da51b2193")  

                elif text.lower() == 'bot6 help':
                    helpMessage = helpmessage()
                    jp1 = ki6.getContact(ki5MID).displayName
                    ki6.sendMessage(to,str(helpMessage) + "╭════════════════════╮\n❨✪❩ ᴠɪᴇᴡ sᴇᴛᴛɪɴɢs = sᴇᴛ \n❨✪❩ ᴠɪᴇᴡ ɪɴғᴏ ʙᴏᴛ = ᴀʙᴏᴜᴛ \n❨✪❩ ʜᴇʟᴘᴍᴇssᴀɢᴇ ʙʏ : " + jp1+ "\n╰════════════════════╯\n         ™ ᴛᴇᴀᴍ ᴅᴋ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ™\n")
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "progres...")
                    elapsed_time = time.time() - start
                    line.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki2.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki3.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki4.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki5.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki6.sendMessage(to,format(str(elapsed_time))+" seconds")
                    
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, "progres...")
                    elapsed_time = time.time() - start
                    line.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki2.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki3.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki4.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki5.sendMessage(to,format(str(elapsed_time))+" seconds")
                    ki6.sendMessage(to,format(str(elapsed_time))+" seconds")

                elif text.lower() == 'reboot':
                    line.sendMessage(to, "I'II come back latter")
                    line.sendMessage(to, "Restarted done ♪")
                    restartBot()
                    
                elif text.lower() == 'runtime':
                     eltime = time.time() -mulai
                     van = "╭════════════════════╮\n     Mybot sudah berjalan selama\n     " +waktu(eltime)+"\n╰════════════════════╯"
                     line.sendMessage(to,van)  
                    
#___________                        
                elif text.lower() == 'tagmem' or text.lower() == 'up' or text.lower() == 'hi' or text.lower() == 'dk' or text.lower() == 'dor' or text.lower() == 'hem' or text.lower() == 'absen' or text.lower() == 'muach' or text.lower() == 'hai':
                    group = line.getGroup(msg.to)
                    members = [contact.mid for contact in group.members]
                    tags = []
                    for i in range(0, len(members), 20):
                        tags.append(list(members[i:i+20]))
                    for t in tags:
                        msg = ttypes.Message(to=to)
                        tst ="❨✪❩ ᴅᴋ ᴍᴇɴᴛɪᴏɴs ❨✪❩ \n\n"
                        tst += u''
                        s=len(tst)
                        d=[]
                        for i in range(len(t)):
                            d.append({"S":str(s), "E" :str(s+4), "M":t[i]})
                            s += 5
                            tst +=u'@jek\n'
                        msg.text = tst.rstrip()
                        msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                        line.talk.sendMessage(0,msg)
                        jp = line.getContact(lineMID).displayName
                    else:
                    	line.sendMessage(to,"╭════════════════╮\n❨✪❩ ᴍᴇɴᴛɪᴏɴᴇs ʙʏ DK : " + jp+"\n╰════════════════╯")
                        
                           
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u7e99c5b3e4f01c95c104d0993fc41998"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "____________________________\n❨✪❩ Impormation Selfbot ❨✪❩\n____________________________"
                        ret_ += "\n┃❨✪❩ Line Name : {}".format(contact.displayName)
                        ret_ += "\n┃❨✪❩ Groups : {}".format(str(len(grouplist)))
                        ret_ += "\n┃❨✪❩ Friends : {}".format(str(len(contactlist)))
                        ret_ += "\n┃❨✪❩ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n┃❨✪❩ Version1 : Python3"
                        ret_ += "\n┃❨✪❩ Version2 : Premium server"
                        ret_ += "\n┃❨✪❩ Masa Aktif : 00-00-2018"
                        ret_ += "\n┃❨✪❩ Creator : {}".format(creator.displayName)
                        ret_ += "\n____________________________"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'settings' or text.lower() == 'myset':
                    try:
                        ret_ = "╭═════════════════╮\n"
                        ret_ += "  ❨✪❩ Settings Mybot ❨✪❩\n"
                        ret_ += "╰═════════════════╯\n"
                        if settings["autoAdd"] == True: ret_ += "01.┃❨✪❩ Autoadd On \n"
                        else: ret_ += "01.┃❨✪❩ Autoadd Off \n"
                        if settings["autoblock"] == True: ret_ += "02.┃❨✪❩ AutoBlock On \n"
                        else: ret_ += "02.┃❨✪❩ AutoBlock Off \n"         
                        if settings["contact"] == True: ret_ += "03.┃❨✪❩ Contact On \n"
                        else: ret_ += "03.┃❨✪❩ Contact Off \n"
                        if settings["autoJoin"] == True: ret_ += "04.┃❨✪❩ AutoJoin On \n"
                        else: ret_ += "04.┃❨✪❩ AutoJoin Off \n"
                        if settings["mimic"]["status"] == True: ret_ += "05.┃❨✪❩ Mimic On \n"
                        else: ret_ += "05.┃❨✪❩ Mimic Off \n"
                        if settings["welcomemsg"] == True: ret_+= "06.┃❨✪❩ Welcome On \n"
                        else: ret_ +="06.┃❨✪❩ Welcome Off \n"
                        if settings["leavemsg"] == True: ret_+= "07.┃❨✪❩ Leavemsg On \n"
                        else: ret_ +="07.┃❨✪❩ Leavemsg Off \n"                     
                        if settings["autoLeave"] == True: ret_ += "08.┃❨✪❩ AutoLeave On \n"
                        else: ret_ += "08.┃❨✪❩ AutoLeave Off \n"
                        if settings["autoRead"] == True: ret_ += "09.┃❨✪❩ AutoRead On \n"
                        else: ret_ += "09.┃❨✪❩ AutoRead Off \n"
                        if settings["checkSticker"] == True: ret_ += "10.┃❨✪❩ CekSticker On \n"
                        else: ret_ += "10.┃❨✪❩ CekSticker Off \n"                     
                        if settings["autoRespon"] == True: ret_ += "11.┃❨✪❩ Respon1 On \n"
                        else: ret_ += "11.┃❨✪❩ Respon1 Off \n"
                        if settings["autoResponImage"] == True: ret_ += "12.┃❨✪❩ Respon2 On \n"
                        else: ret_ += "12.┃❨✪❩ Respon2 Off \n"
                        if settings["autoResponPm"] == True: ret_ += "13.┃❨✪❩ Respon3 On \n"
                        else: ret_ += "13.┃❨✪❩ Respon3 Off \n"                     
                        if settings["responPc"] == True: ret_ += "14.┃❨✪❩ ResponPc On \n"
                        else: ret_ += "14.┃❨✪❩ ResponPc Off \n"
                        if settings["autorejc"] == True: ret_ += "15.┃❨✪❩ AutoReject On \n"
                        else: ret_ += "15.┃❨✪❩ AutoReject Off "
                        ret_ += "\n╭═══════════════════╮"
                        jp = line.getContact(lineMID).displayName
                        line.sendMessage(to, str(ret_)+"\n ❨✪❩ Line Name: "+jp+"\n ❨✪❩ ᴅᴋ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ❨✪❩\n╰═══════════════════╯")
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
 
#==============================================================================#
                elif text.lower() == 'protect set':
                    try:
                        ret_ = "Group Settings:\n\n"
                        if settings["protect"] == True: ret_ += " Protect : On \n"
                        else: ret_ += " Protect : Off\n"
                        if settings["qrprotect"] == True: ret_ += "  Linkprotect : On \n"
                        else: ret_ += "  Linkprotect : Off \n"         
                        if settings["inviteprotect"] == True: ret_ += "   Inviteprotect : On \n"
                        else: ret_ += "   Inviteprotect : Off \n"
                        if settings["cancelprotect"] == True: ret_ += "    Cancelall : On \n"
                        else: ret_ += "    Cancelall : Off \n"
                        line.sendMessage(to, str(ret_))
                        ki.sendMessage(to, str(ret_))
                        ki2.sendMessage(to, str(ret_))
                        ki3.sendMessage(to, str(ret_))
                        ki4.sendMessage(to, str(ret_))
                        ki5.sendMessage(to, str(ret_))
                        ki6.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                       
                elif text.lower() == 'allsettings mode on':
                    settings["autoAdd"] = True
                    settings["autoblock"] = True
                    settings["contact"] = True
                    settings["autoJoin"] = True
                    settings["mimic"]["status"] = True
                    settings["welcomemsg"] = True
                    settings["leavemsg"] = True
                    settings["autoLeave"] = False
                    settings["autoRead"] = True
                    settings["checkSticker"] = True
                    settings["autoRespon"] = True
                    settings["autoResponImage"] = True
                    settings["autoResponPm"] = True
                    settings["responPc"] = True
                    settings["autorejc"] = True
                    line.sendMessage(to, "All Setting Bot Mode On")
                    
                elif text.lower() == 'allsettings mode off':
                    settings["autoAdd"] = False
                    settings["autoblock"] = False
                    settings["contact"] = False
                    settings["autoJoin"] = False
                    settings["mimic"]["status"] = False
                    settings["welcomemsg"] = False
                    settings["leavemsg"] = False
                    settings["autoLeave"] = False
                    settings["autoRead"] = False
                    settings["checkSticker"] = False
                    settings["autoRespon"] = False
                    settings["autoResponImage"] = False
                    settings["autoResponPm"] = False
                    settings["responPc"] = False
                    settings["autorejc"] = False
                    line.sendMessage(to, "All Setting Bot Mode Off")
                    
                                         
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "AutoAdd already On")
                    
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "AutoAdd already Off")
    
                elif text.lower() == 'autoblock on':
                    settings["autoblock"] = True
                    line.sendMessage(to, "AutoBlock already On")
                    
                elif text.lower() == 'autoblock off':
                    settings["autoblock"] = False
                    line.sendMessage(to, "AutoBlock already Off")
           
                elif text.lower() == 'autojoin on':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "AutoJoin already On")
                    
                elif text.lower() == 'autojoin off':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "AutoJoin already Off")
                    
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "AutoLeave already On")
                    
                elif text.lower() == 'autoleave off':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "AutoLeave already Off")
                    
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    line.sendMessage(to, "Autoread Chat already On")
                    
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    line.sendMessage(to, "Autoread Chat already Off")
                    
                elif text.lower() == 'ceksticker on':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "CekStiker already On")
                    
                elif text.lower() == 'ceksticker off':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "CekStiker already Off")
                    
                elif text.lower() == 'respon1 on':
                    if sender in lineMID:
                        settings["autoRespon"] = True
                        line.sendMessage(to, "Autorespon1 Text di Aktifkan")
                        
                elif text.lower() == 'respon1 off':
                    if sender in lineMID:
                        settings["autoRespon"] = False
                        line.sendMessage(to, "Autorespon1 Text Off")
                        
                elif text.lower() == 'respon2 on':
                    if sender in lineMID:
                        settings["autoResponImage"] = True
                        line.sendMessage(to, "Autorespon2 TagImage di Aktifkan")
                        
                elif text.lower() == 'respon2 off':
                    if sender in lineMID:
                        settings["autoResponImage"] = False
                        line.sendMessage(to, "Autorespon2 Image Off")
                        
                elif text.lower() == 'respon3 on':
                    if sender in lineMID:
                        settings["autoResponPm"] = True
                        line.sendMessage(to, "Autorespon3 PM di Aktifkan")
                        
                elif text.lower() == 'respon3 off':
                    if sender in lineMID:
                        settings["autoResponPm"] = False
                        line.sendMessage(to, "Autorespon3 PM Off")  
                        
                elif text.lower() == 'responpc on':
                    if sender in lineMID:
                        settings["responPc"] = True
                        line.sendMessage(to, "Autorespon Tagpc di Aktifkan")
                        
                elif text.lower() == 'responpc off':
                    if sender in lineMID:
                        settings["responPc"] = False
                        line.sendMessage(to, "Autorespon Tagpc Off")
                        
#-------------------------------------------------------------------------------
                elif text.lower() == 'protect on':
                    if sender in lineMID:	
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to," Protection Already On")
                                ki.sendMessage(to," Protection Already On")
                                ki2.sendMessage(to," Protection Already On")
                                ki3.sendMessage(to," Protection Already On")
                                ki4.sendMessage(to," Protection Already On")
                                ki5.sendMessage(to," Protection Already On")
                                ki6.sendMessage(to," Protection Already On")
                            else:
                                line.sendMessage(to,"Protection Already On")
                                ki.sendMessage(to," Protection Already On")
                                ki2.sendMessage(to," Protection Already On")
                                ki3.sendMessage(to," Protection Already On")
                                ki4.sendMessage(to," Protection Already On")
                                ki5.sendMessage(to," Protection Already On")
                                ki6.sendMessage(to," Protection Already On")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Protection Already On")
                                ki.sendMessage(to," Protection Already On")
                                ki2.sendMessage(to," Protection Already On")
                                ki3.sendMessage(to," Protection Already On")
                                ki4.sendMessage(to," Protection Already On")
                                ki5.sendMessage(to," Protection Already On")
                                ki6.sendMessage(to," Protection Already On")
                            else:
                                line.sendMessage(to,"Protection Already On")
                                ki.sendMessage(to," Protection Already On")
                                ki2.sendMessage(to," Protection Already On")
                                ki3.sendMessage(to," Protection Already On")
                                ki4.sendMessage(to," Protection Already On")
                                ki5.sendMessage(to," Protection Already On")
                                ki6.sendMessage(to," Protection Already On")
                                
                elif text.lower() == 'protect off':
                    if sender in lineMID:
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to," Protection Already Off ")
                                ki.sendMessage(to," Protection Already Off ")
                                ki2.sendMessage(to," Protection Already Off ")
                                ki3.sendMessage(to," Protection Already Off ")
                                ki4.sendMessage(to," Protection Already Off ")
                                ki5.sendMessage(to," Protection Already Off ")
                                ki6.sendMessage(to," Protection Already Off ")
                            else:
                                line.sendMessage(to,"Protection Already Off ")
                                ki.sendMessage(to," Protection Already Off ")
                                ki2.sendMessage(to," Protection Already Off ")
                                ki3.sendMessage(to," Protection Already Off ")
                                ki4.sendMessage(to," Protection Already Off ")
                                ki5.sendMessage(to," Protection Already Off ")
                                ki6.sendMessage(to," Protection Already Off ")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Protection Already Off ")
                                ki.sendMessage(to," Protection Already Off ")
                                ki2.sendMessage(to," Protection Already Off ")
                                ki3.sendMessage(to," Protection Already Off ")
                                ki4.sendMessage(to," Protection Already Off ")
                                ki5.sendMessage(to," Protection Already Off ")
                                ki6.sendMessage(to," Protection Already Off ")
                            else:
                                line.sendMessage(to,"Protection Already Off ")
                                ki.sendMessage(to," Protection Already Off ")
                                ki2.sendMessage(to," Protection Already Off ")
                                ki3.sendMessage(to," Protection Already Off ")
                                ki4.sendMessage(to," Protection Already Off ")
                                ki5.sendMessage(to," Protection Already Off ")
                                ki6.sendMessage(to," Protection Already Off ")                                
                                
 #----------------------------------------------------------------------------------------                        
                elif text.lower() == 'linkprotect on':
                    if sender in lineMID:
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Linkprotect Already On ")
                                ki.sendMessage(to,"Linkprotect Already On ")
                                ki2.sendMessage(to,"Linkprotect Already On ")
                                ki3.sendMessage(to,"Linkprotect Already On ")
                                ki4.sendMessage(to,"Linkprotect Already On ")
                                ki5.sendMessage(to,"Linkprotect Already On ")
                                ki6.sendMessage(to," Protection Already On ")
                            else:
                                line.sendMessage(to,"Linkprotect Already On ")
                                ki.sendMessage(to,"Linkprotect Already On ")
                                ki2.sendMessage(to,"Linkprotect Already On ")
                                ki3.sendMessage(to,"Linkprotect Already On ")
                                ki4.sendMessage(to,"Linkprotect Already On ")
                                ki5.sendMessage(to,"Linkprotect Already On ")
                                ki6.sendMessage(to," Protection Already On ")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Linkprotect Already On ")
                                ki.sendMessage(to,"Linkprotect Already On ")
                                ki2.sendMessage(to,"Linkprotect Already On ")
                                ki3.sendMessage(to,"Linkprotect Already On ")
                                ki4.sendMessage(to,"Linkprotect Already On ")
                                ki5.sendMessage(to,"Linkprotect Already On ")
                                ki6.sendMessage(to," Protection Already On ")
                            else:
                                line.sendMessage(to,"Linkprotect Already On ")
                                ki.sendMessage(to,"Linkprotect Already On ")
                                ki2.sendMessage(to,"Linkprotect Already On ")
                                ki3.sendMessage(to,"Linkprotect Already On ")
                                ki4.sendMessage(to,"Linkprotect Already On ")
                                ki5.sendMessage(to,"Linkprotect Already On ")
                                ki6.sendMessage(to," Protection Already On ")
                                
                elif text.lower() == 'linkprotect off':
                    if sender in lineMID:
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Linkprotect Already Off ")
                                ki.sendMessage(to,"Linkprotect Already Off ")
                                ki2.sendMessage(to,"Linkprotect Already Off")
                                ki3.sendMessage(to,"Linkprotect Already Off ")
                                ki4.sendMessage(to,"Linkprotect Already Off")
                                ki5.sendMessage(to,"Linkprotect Already Off")
                            else:
                                line.sendMessage(to,"Linkprotect Already Off ")
                                ki.sendMessage(to,"Linkprotect Already Off ")
                                ki2.sendMessage(to,"Linkprotect Already Off")
                                ki3.sendMessage(to,"Linkprotect Already Off ")
                                ki4.sendMessage(to,"Linkprotect Already Off")
                                ki5.sendMessage(to,"Linkprotect Already Off")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Linkprotect Already Off ")
                                ki.sendMessage(to,"Linkprotect Already Off ")
                                ki2.sendMessage(to,"Linkprotect Already Off")
                                ki3.sendMessage(to,"Linkprotect Already Off ")
                                ki4.sendMessage(to,"Linkprotect Already Off")
                                ki5.sendMessage(to,"Linkprotect Already Off")
                            else:
                                line.sendMessage(to,"Linkprotect Already Off ")
                                ki.sendMessage(to,"Linkprotect Already Off ")
                                ki2.sendMessage(to,"Linkprotect Already Off")
                                ki3.sendMessage(to,"Linkprotect Already Off ")
                                ki4.sendMessage(to,"Linkprotect Already Off")
                                ki5.sendMessage(to,"Linkprotect Already Off")
                                
                                
#-------------------------------------------------------------------------------
                elif text.lower() == 'inviteprotect on':
                    if sender in lineMID:
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"Protection Invite Already On")
                                ki.sendMessage(msg.to,"Protection Invite Already On")
                                ki2.sendMessage(msg.to,"Protection Invite Already On")
                                ki3.sendMessage(msg.to,"Protection Invite Already On")            
                                ki4.sendMessage(msg.to,"Protection Invite Already On")
                                ki5.sendMessage(msg.to,"Protection Invite Already On") 
                            else:
                                line.sendMessage(msg.to,"Protection Invite Already On")
                                ki.sendMessage(msg.to,"Protection Invite Already On")
                                ki2.sendMessage(msg.to,"Protection Invite Already On")
                                ki3.sendMessage(msg.to,"Protection Invite Already On")
                                ki4.sendMessage(msg.to,"Protection Invite Already On")      
                                ki5.sendMessage(msg.to,"Protection Invite Already On")      
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"Protection Invite Already On")
                                ki.sendMessage(msg.to,"Protection Invite Already On")
                                ki2.sendMessage(msg.to,"Protection Invite Already On")
                                ki3.sendMessage(msg.to,"Protection Invite Already On")
                                ki4.sendMessage(msg.to,"Protection Invite Already On")
                                ki5.sendMessage(msg.to,"Protection Invite Already On") 
                            else:
                                line.sendMessage(msg.to,"Protection Invite Already On")
                                ki.sendMessage(msg.to,"Protection Invite Already On")
                                ki2.sendMessage(msg.to,"Protection Invite Already On")
                                ki3.sendMessage(msg.to,"Protection Invite Already On")
                                ki4.sendMessage(msg.to,"Protection Invite Already On")
                                ki5.sendMessage(msg.to,"Protection Invite Already On")
                                
                elif text.lower() == 'inviteprotect off':
                    if sender in lineMID:
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"Protection Invite Already Off")
                                ki.sendMessage(msg.to,"Protection Invite Already Off")
                                ki2.sendMessage(msg.to,"Protection Invite Already Off")
                                ki3.sendMessage(msg.to,"Protection Invite Already Off")
                                ki4.sendMessage(msg.to,"Protection Invite Already Off")
                                ki5.sendMessage(msg.to,"Protection Invite Already Off")
                            else:
                                line.sendMessage(msg.to,"Protection Invite Already Off")
                                ki.sendMessage(msg.to,"Protection Invite Already Off")
                                ki2.sendMessage(msg.to,"Protection Invite Already Off")
                                ki3.sendMessage(msg.to,"Protection Invite Already Off")
                                ki4.sendMessage(msg.to,"Protection Invite Already Off")
                                ki5.sendMessage(msg.to,"Protection Invite Already Off")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"Protection Invite Already Off")
                                ki.sendMessage(msg.to,"Protection Invite Already Off")
                                ki2.sendMessage(msg.to,"Protection Invite Already Off")
                                ki3.sendMessage(msg.to,"Protection Invite Already Off")
                                ki4.sendMessage(msg.to,"Protection Invite Already Off")
                                ki5.sendMessage(msg.to,"Protection Invite Already Off")
                            else:
                                line.sendMessage(msg.to,"Protection Invite Already Off")
                                ki.sendMessage(msg.to,"Protection Invite Already Off")
                                ki2.sendMessage(msg.to,"Protection Invite Already Off")
                                ki3.sendMessage(msg.to,"Protection Invite Already Off")
                                ki4.sendMessage(msg.to,"Protection Invite Already Off")
                                ki5.sendMessage(msg.to,"Protection Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'cancelall on':
                    if msg._from in admin:
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki2.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki3.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki4.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki5.sendMessage(msg.to,"Protection Cancel Invite Already On")
                            else:
                                ki.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki2.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki3.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki4.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki5.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                line.sendMessage(msg.to,"Protection Cancel Invite Already On")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki2.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki3.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki4.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki5.sendMessage(msg.to,"Protection Cancel Invite Already On")
                            else:
                                line.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki2.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki3.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki4.sendMessage(msg.to,"Protection Cancel Invite Already On")
                                ki5.sendMessage(msg.to,"Protection Cancel Invite Already On")

                                
                elif text.lower() == 'cancelall off':
                    if msg._from in admin:
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki2.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki3.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki4.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki5.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                            else:
                                line.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki2.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki3.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki4.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki5.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki2.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki3.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki4.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki5.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                            else:
                                line.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki2.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki3.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki4.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                ki5.sendMessage(msg.to,"Protection Cancel Invite Already Off")
                                
                            #-------------------------------------------------------------------------------
                elif text.lower() == 'protectall on':
                    if msg._from in admin:
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        line.sendMessage(msg.to,"All Protect Turned On")
                        ki.sendMessage(msg.to,"All Protect Turned On")
                        ki2.sendMessage(msg.to,"All Protect Turned On")
                        ki3.sendMessage(msg.to,"All Protect Turned On")
                        ki4.sendMessage(msg.to,"All Protect Turned On")
                        ki5.sendMessage(msg.to,"All Protect Turned On")
                    else:
                        line.sendMessage(msg.to,"Just for Owner")
                        		            
                elif text.lower() == 'protectall off':
                    if msg._from in admin:
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        line.sendMessage(msg.to,"All Protect Turned Off")
                        ki.sendMessage(msg.to,"All Protect Turned Off")
                        ki2.sendMessage(msg.to,"All Protect Turned Off")
                        ki3.sendMessage(msg.to,"All Protect Turned Off")
                        ki4.sendMessage(msg.to,"All Protect Turned Off")
                        ki5.sendMessage(msg.to,"All Protect Turned Off")
                        ki6.sendMessage(msg.to,"All Protect Turned Off")
                    else:
                        line.sendMessage(msg.to,"Just for Owner")    

                elif text.lower() == 'desah':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Zero \n'
                        line.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "╔══════════╗\n  ❨✪Jumlah {} ✪❩\n╚══════════╝".format(str(len(nama))))

                elif text.lower() == 'tag':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Zero \n'
                        line.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "╔══════════╗\n  ❨✪Jumlah {} ✪❩\n╚══════════╝".format(str(len(nama))))

                elif text.lower() == 'tag all':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Zero \n'
                        line.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "╔══════════╗\n  ❨✪Jumlah {} ✪❩\n╚══════════╝".format(str(len(nama))))

                elif text.lower() == 'dkbots':
                    if msg._from in admin:
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        line.sendMessage(msg.to,"╚☆Ⓢⓘⓐⓟ☆╗")
                        ki.sendMessage(msg.to,"╚☆╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗")
                        ki2.sendMessage(msg.to,"╚☆Ⓢⓘⓐⓟ☆╗")
                        ki3.sendMessage(msg.to,"╚☆╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗")
                        ki4.sendMessage(msg.to,"╚☆Ⓐⓜⓐⓝ-☆╗")
                        ki5.sendMessage(msg.to,"╚ⒷⓄⓈ☆╮╗")
                    else:
                        line.sendMessage(msg.to,"Just for Owner")
  #==============================================================================#
                elif text.lower() == "responsname":
                    line.sendMessage(msg.to,responsename)
                    ki.sendMessage(msg.to,"꧁༺şℎαℎ̿̿ Żαίη࿐➻❥1")
                    ki2.sendMessage(msg.to,"꧁༺şℎαℎ̿̿ Żαίη࿐➻❥2")
                    ki3.sendMessage(msg.to,"꧁༺şℎαℎ̿̿ Żαίη࿐➻❥3")
                    ki4.sendMessage(msg.to,"꧁༺şℎαℎ̿̿ Żαίη࿐➻❥4")
                    ki5.sendMessage(msg.to,"꧁༺şℎαℎ̿̿ Żαίη࿐➻❥5")
                    ki6.sendMessage(msg.to,"꧁༺şℎαℎ̿̿ Żαίη࿐➻❥6")
                   
                elif msg.text.lower() == 'mybots':
                    if msg._from in lineMID:
                        line.sendContact(to, kiMID)
                        line.sendContact(to, ki2MID)
                        line.sendContact(to, ki3MID)
                        line.sendContact(to, ki4MID)
                        line.sendContact(to, ki5MID)
                        line.sendContact(to, ki6MID)
                        
                elif msg.text.lower() == 'allbot':
                    if msg._from in lineMID:
                        ki.sendContact(to, kiMID)   
                        ki2.sendContact(to, ki2MID)
                        ki3.sendContact(to, ki3MID)
                        ki4.sendContact(to, ki4MID)
                        ki5.sendContact(to, ki5MID)
                        ki6.sendContact(to, ki6MID)

                elif msg.text.lower() == 'mybot':
                    if msg._from in lineMID:
                        ki.sendContact(to, kiMID)   
                        ki2.sendContact(to, ki2MID)
                        ki3.sendContact(to, ki3MID)
                        ki4.sendContact(to, ki4MID)
                        ki5.sendContact(to, ki5MID)
                        ki6.sendContact(to, ki6MID)
                        
                elif msg.text.lower() == 'bots me':
                    if msg._from in lineMID:
                        line.sendContact(to, kiMID)   
                        ki.sendContact(to, kiMID)   
                        ki2.sendContact(to, ki2MID)
                        ki3.sendContact(to, ki3MID)
                        ki4.sendContact(to, ki4MID)
                        ki5.sendContact(to, ki5MID)
                        ki6.sendContact(to, ki6MID)
                        
                elif msg.text.lower() == 'kibar':
                    if msg._from in lineMID:
                        line.sendContact(to, lineMID)   
                        line.sendContact(to, kiMID)
                        line.sendContact(to, ki2MID)
                        line.sendContact(to, ki3MID)
                        line.sendContact(to, ki4MID)
                        line.sendContact(to, ki5MID)
                        line.sendContact(to, ki6MID)
                        line.sendMessage(to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
 "ASSALAMUALAIKUM\n"
"  ╭━Ⓓ✒Ⓡ✒ⒼⓄ✒Ⓝ✒\n"
"  ╰╮┏━┳┳┓┏┳┳┓┏┳┳┳┓\n"
"  ┏┻╋━┻┻┫┣┻┻┫┣┻┻┻┫\n"
"  ┃HLO▪┃KMI DTANG LGI┃\n"
"  ┗ⓞⓞ┻┻ⓞ━━ⓞ┻┻ⓞ━╯\n"
"UNTUK MENGGUSUR\nROOM KALIAN\n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[██████████████████]\n"
"◥⊙⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"👿━━━━━━━━━━━━━👿"
"Ⓣⓜⓟⓐ Ⓑⓐⓢⓐ_Ⓑⓐⓢⓘ\n"
"Ⓡⓐⓣⓐ ⓖⓐ ⓡⓐⓣⓐ\n" 
"Ⓨⓖ ⓟⓝⓣⓘⓝⓖ ⓚⓘⓑⓐⓡ\n"
"Ⓣⓐⓝⓖⓚⓘⓢ Ⓖⓞⓑⓛⓞⓚ\n"
"👿━━━━━━━━━━━━━👿\n"
	"╔══╗╔═╗╔══╗╔═╦═╗\n"
	"╚╗╔╝║╦╝║╔╗║║║║║║\n"
	"━║║━║╩╗║╠╣║║║║║║\n"
	"━╚╝━╚═╝╚╝╚╝╚╩═╩╝\n"
"👿━━━━━━━━━━━━━👿\n"
	"╔══╗         ╔╦╗\n"
	"╚╗╗║         ║╔╝\n"
	"╔╩╝║         ║╚╗\n"
	"╚══╝         ╚╩╝\n"
"👿━━━━━━━━━━━━━👿\n"        
"Ⓓⓡⓐⓖⓞⓝ_Ⓚⓘⓛⓛⓔⓡ\n"
"Ⓟⓤⓝⓨⓐ👿━━👿Ⓡⓐⓣⓐ Ⓝⓘ\n" 
"Ⓜⓐⓗ━👿━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
">>>Ⓑⓨⓔ_Ⓑⓨⓔ ⒼⒸ Ⓛⓐⓚⓝⓐⓣ>><\nⒹⓝⓓⓐⓜ Ⓒⓐⓡⓘ Ⓚⓜⓘ\n<<<<<<<<<>>\nhttp://line.me/ti/p/~reza.p.i.p\nhttp://line.me/ti/p/ryansakra_m1")


                elif msg.text.lower() == 'ping':
                    if msg._from in lineMID:
                        ki2.sendMessage(to, "pong")
                        ki3.sendMessage(to, "pong")
                        ki4.sendMessage(to, "pong")
                        ki5.sendMessage(to, "pong")
                        ki.sendMessage(to, "pong")

                elif msg.text.lower() == 'dkbot':
                    if msg._from in lineMID:
                        line.sendMessage(to, "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]")
                        ki2.sendMessage(to, "╚☆Ⓢⓘⓐⓟ☆╗\n╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗")
                        ki3.sendMessage(to, "╚☆Ⓢⓘⓐⓟ☆╗\n╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗")
                        ki4.sendMessage(to, "╚☆Ⓢⓘⓐⓟ☆╗\n╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗")
                        ki5.sendMessage(to, "╚☆Ⓢⓘⓐⓟ☆╗\n╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗")
                        ki.sendMessage(to, "╚☆Ⓐⓜⓐⓝ-☆╗\n╚ⒷⓄⓈ☆╮╗")

                elif msg.text.lower() == 'promo':
                    if msg._from in lineMID:
                        line.sendMessage(to, "──────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\n➣ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-11 ʙᴏᴛ ᴀꜱɪꜱᴛ\n➣ɴᴇᴡ ꜱᴄʀɪᴘᴛ\n➣ʜʀɢᴀ ʙɪꜱᴀ ɴᴇɢᴏ\n─────────┅┅─────────\n  ✯❇͜͡❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡❇͜͡❇✯\nline.me/ti/p/~reza.p.i.p\nline.me/ti/p/~reza.p.i.p\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅────────")
                        line.sendMessage(to, "╭══════════\n║⚫─[     DAFTAR HARGA     ]─⚫ \n║SELFBOT ONLY = 75K /BLN\n║2 ASSIST = 100K /BLN\n║5 ASSIST = 200K /BLN\n║10 ASSIST = 300K /BLN\n║\n║PROTECT ANTIJS\n║\n║2 BOT + ANTIJS = 150K /BLN\n║5 BOT + ANTIJS = 300K /BLN\n║10 BOT + ANTIJS = 500K /BLN\n║\n║═ই\═ANDA BERMINAT\n║ SILAHKAN ADD CONTACT \n║ DIBAWAH INI   \n║\n║http://line.me/ti/p/~reza.p.i.p\n║       TERIMA KASIH      \n║\n╰════════════")

                        
                elif msg.text.lower() == 'pong':
                    if msg._from in lineMID:
                        ki2.sendMessage(to, "ping")
                        ki3.sendMessage(to, "ping")
                        ki4.sendMessage(to, "ping")
                        ki5.sendMessage(to, "ping")
                        ki.sendMessage(to, "ping")
 
                        
                elif text.lower() == 'dk.pulang' or text.lower() == '.byeall' or text.lower() == '0':
                  if msg._from in lineMID:
                    ki.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                    ki3.leaveGroup(msg.to)
                    ki4.leaveGroup(msg.to)
                    ki5.leaveGroup(msg.to)
                    ki6.leaveGroup(msg.to)
               
                elif text.lower() == 'dk.masuk' or text.lower() == '.join' or text.lower() == '1':
                  if msg._from in lineMID:
                    G = line.getGroup(msg.to)
                    ginfo = line.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    line.updateGroup(G)
                    invsend = 0
                    Ticket = line.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = line.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    line.updateGroup(G)

                elif "tagall " in msg.text:
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Zero \n'
                        line.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(msg.to, "The number of members is pushed".format(str(len(nama))))

                elif "dk " in msg.text:
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Zero \n'
                        line.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(msg.to, "Jumlah Member didesah".format(str(len(nama))))

#____________                              
                elif "Bots updname " in msg.text:         
                  if msg._from in lineMID:
                    separate = msg.text.split("Bots updname ")
                    string = msg.text.replace(separate[0] + "Bots updname ","")
                  if len(string) <= 10000000000:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki.sendMessage(msg.to,"Name changed to " + string + "")
                    ki2.sendMessage(msg.to,"Name changed to " + string + "")
                    ki3.sendMessage(msg.to,"Name changed to " + string + "")
                    ki4.sendMessage(msg.to,"Name changed to " + string + "")
                    ki5.sendMessage(msg.to,"Name changed to " + string + "")
                    ki6.sendMessage(msg.to,"Name changed to " + string + "")                
                                         
#____________                              
                elif "Bots updstatus " in msg.text:         
                  if msg._from in lineMID:
                    separate = msg.text.split("Bots updstatus ")
                    string = msg.text.replace(separate[0] + "Bots updstatus ","")
                  if len(string) <= 10000000000:
                    profile = ki.getProfile()
                    profile.statusMessage= string
                    ki.updateProfile(profile)
                    profile = ki2.getProfile()
                    profile.statusMessage= string
                    ki2.updateProfile(profile)
                    profile = ki3.getProfile()
                    profile.statusMessage= string
                    ki3.updateProfile(profile)
                    profile = ki4.getProfile()
                    profile.statusMessage= string
                    ki4.updateProfile(profile)
                    profile = ki5.getProfile()
                    profile.statusMessage= string
                    ki5.updateProfile(profile)
                    profile = ki6.getProfile()
                    profile.statusMessage= string
                    ki6.updateProfile(profile)
                    ki.sendMessage(msg.to,"Status replaced so " + string + "")
                    ki2.sendMessage(msg.to,"Status replaced so " + string + "")
                    ki3.sendMessage(msg.to,"Status replaced so " + string + "")
                    ki4.sendMessage(msg.to,"Status replaced so " + string + "")
                    ki5.sendMessage(msg.to,"Status replaced so " + string + "")
                    ki6.sendMessage(msg.to,"Status replaced so " + string + "")
#==============================================================================#
                elif text.lower() == 'me':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    
                elif text.lower() == 'aku':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus) 
                    
                elif text.lower() == 'mid':
                    line.sendMessage(msg.to,lineMID)
                    
                elif text.lower() == 'tagme':
                	sendMessageWithMention(to, lineMID)
                    
                elif text.lower() == 'creator':
                	line.sendContact(to, "u7e99c5b3e4f01c95c104d0993fc41998")
                    
                elif text.lower() == 'myname':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"DisplayName:\n\n" + me.displayName)
                    
                elif text.lower() == "update pict":
                    settings["changePicture"] = True
                    line.sendMessage(to, "Send image")
                    
                elif text.lower() == "update pict group":
                    if msg.toType == 2:
                        if to not in settings["changeGroupPicture"]:
                            settings["changeGroupPicture"].append(to)
                        line.sendMessage(to, "Send image ")
                        
                elif text.lower() == 'mybio':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"StatusMessage:\n\n" + me.statusMessage)
                    
                elif text.lower() == 'pp':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    
                elif text.lower() == 'myvid':
                    me = line.getContact(lineMID)                  
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                    
                elif text.lower() == 'cover':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
   
#___________________UNSEND_______________
                elif text.lower() == 'unsend:on':
                    if msg._from in lineMID:
                        settings["unsendMessage"] = True
                        line.sendMessage(msg.to, "Unsend message enable")
                elif text.lower() == 'unsend:off':
                    if msg._from in lineMID:
                        settings["unsendMessage"] = False
                        line.sendMessage(msg.to, "Unsend message disable")
                 
                elif msg.text.lower().startswith("getcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                            
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            ret_ = ls
                        line.sendMessage(msg.to, str(ret_))
                        
                elif msg.text.lower().startswith("getname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                            
                elif msg.text.lower().startswith("getbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                            
                elif msg.text.lower().startswith("pict "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                            
                elif msg.text.lower().startswith("get videoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                            
                            
#_______________VKICK______________________                            
                elif "vkick" in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:                              
                                line.kickoutFromGroup(msg.to, [mention['M']])
                                line.inviteIntoGroup(msg.to,[mention['M']])
                                line.cancelGroupInvitation(msg.to,[mention['M']])
                            except:
                                line.sendMessage(to, "Error")
 
#_____________KICK____________________                               
                elif "kick" in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                line.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                line.kickoutFromGroup(msg.to, [mention['M']])
                        else:
                            pass                               

                elif "dk1" in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                ki.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                ki.kickoutFromGroup(msg.to, [mention['M']])
                        else:
                            pass

                elif "dk2" in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                ki2.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                ki2.kickoutFromGroup(msg.to, [mention['M']])
                        else:
                            pass

                elif "dk3" in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                ki3.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                ki3.kickoutFromGroup(msg.to, [mention['M']])
                        else:
                            pass

                elif "dk4" in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                ki4.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                ki4.kickoutFromGroup(msg.to, [mention['M']])
                        else:
                            pass

                elif "dk5" in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                ki5.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                ki5.kickoutFromGroup(msg.to, [mention['M']])
                        else:
                            pass

                elif "dk6" in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                ki6.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                ki6.kickoutFromGroup(msg.to, [mention['M']])
                        else:
                            pass

                elif "dk" in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                ki.kickoutFromGroup(msg.to, [mention['M']])							
                                ki2.kickoutFromGroup(msg.to, [mention['M']])
                                ki3.kickoutFromGroup(msg.to, [mention['M']])
                                ki4.kickoutFromGroup(msg.to, [mention['M']])
                                ki5.kickoutFromGroup(msg.to, [mention['M']])
                                ki6.kickoutFromGroup(msg.to, [mention['M']])
                            except:
                                ki.kickoutFromGroup(msg.to, [mention['M']])							
                                ki2.kickoutFromGroup(msg.to, [mention['M']])
                                ki3.kickoutFromGroup(msg.to, [mention['M']])
                                ki4.kickoutFromGroup(msg.to, [mention['M']])
                                ki5.kickoutFromGroup(msg.to, [mention['M']])
                                ki6.kickoutFromGroup(msg.to, [mention['M']])
                        else:
                            pass


#_____________NUKE_________________
                elif "Nuke" in msg.text:
                    if msg.toType == 2:
                    #print "ok"
                        _name = msg.text.replace("Nuke","")
                        gs = line.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            line.sendMessage(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    line.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    pass
                                    
#_____________NK________________
                elif "Nk:" in msg.text:
                    if msg.toType == 2:
                    #print "ok"
                        _name = msg.text.replace("Nk:","")
                        gs = line.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            line.sendMessage(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    line.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    pass                                    
                            
                elif msg.text.lower().startswith("cover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                                
 #____________COPY__________________________________                               
                elif msg.text.lower().startswith("copy "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                           try:
                               line.cloneContactProfile(mention['M'])
                               jp = line.getContact(mention["M"]).displayName
                               line.sendMessage(to, "Succes Copy Profile "+jp)
                           except:
                               line.sendMessage(msg.to, "Eror")
                            
                elif text.lower() == 'backup':
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, lineProfile.pictureStatus)
                        line.updateProfile(lineProfile)
                        line.sendMessage(msg.to, "Done Backup Profile ")
                    except:
                        line.sendMessage(msg.to, "Invalid")
                        
  #____________COPY__________________________________                               
                elif msg.text.lower().startswith("bots copy "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                           try:
                               ki.cloneContactProfile(mention['M'])
                               ki2.cloneContactProfile(mention['M'])
                               jp = line.getContact(mention["M"]).displayName
                               ki.sendMessage(to, "Succes Copy Profile "+jp)
                               ki2.sendMessage(to, "Succes Copy Profile "+jp)
                           except:
                               line.sendMessage(msg.to, "Eror")
                            
                elif text.lower() == 'bots backup':
                    try:
                        kiProfile.displayName = str(myProfile["displayName"])
                        kiProfile.statusMessage = str(myProfile["statusMessage"])
                        kiProfile.pictureStatus = str(myProfile["pictureStatus"])
                        ki.updateProfileAttribute(8, kiProfile.pictureStatus)
                        ki.updateProfile(kiProfile)
                        ki2Profile.displayName = str(myProfile["displayName"])
                        ki2Profile.statusMessage = str(myProfile["statusMessage"])
                        ki2Profile.pictureStatus = str(myProfile["pictureStatus"])
                        ki2.updateProfileAttribute(8, ki2Profile.pictureStatus)
                        ki2.updateProfile(ki2Profile)
                        ki3Profile.displayName = str(myProfile["displayName"])
                        ki3Profile.statusMessage = str(myProfile["statusMessage"])
                        ki3Profile.pictureStatus = str(myProfile["pictureStatus"])
                        ki3.updateProfileAttribute(8, ki3Profile.pictureStatus)
                        ki3.updateProfile(ki2Profile)
                        ki4Profile.displayName = str(myProfile["displayName"])
                        ki4Profile.statusMessage = str(myProfile["statusMessage"])
                        ki4Profile.pictureStatus = str(myProfile["pictureStatus"])
                        ki4.updateProfileAttribute(8, ki2Profile.pictureStatus)
                        ki4.updateProfile(ki4Profile)
                        ki5Profile.displayName = str(myProfile["displayName"])
                        ki5Profile.statusMessage = str(myProfile["statusMessage"])
                        ki5Profile.pictureStatus = str(myProfile["pictureStatus"])
                        ki5.updateProfileAttribute(8, ki2Profile.pictureStatus)
                        ki5.updateProfile(ki5Profile)
                        ki6Profile.displayName = str(myProfile["displayName"])
                        ki6Profile.statusMessage = str(myProfile["statusMessage"])
                        ki6Profile.pictureStatus = str(myProfile["pictureStatus"])
                        ki6.updateProfileAttribute(8, ki2Profile.pictureStatus)
                        ki6.updateProfile(ki5Profile)
                        ki.sendMessage(msg.to, "Done Backup Profile ")
                        ki2.sendMessage(msg.to, "Done Backup Profile ")
                        ki3.sendMessage(msg.to, "Done Backup Profile ")
                        ki4.sendMessage(msg.to, "Done Backup Profile ")
                        ki5.sendMessage(msg.to, "Done Backup Profile ")
                        ki6.sendMessage(msg.to, "Done Backup Profile ")
                    except:
                        line.sendMessage(msg.to, "Invalid")                      

#____________________________________________                                          
                #elif text.lower() == 'leaveallgroups':
                #gid = ki.getGroupIdsJoined()
                #gid = ki2.getGroupIdsJoined()
                #gid = ki3.getGroupIdsJoined()
                #gid = ki4.getGroupIdsJoined()
                #gid = ki5.getGroupIdsJoined()
                #for i in gid:
                    #ki.leaveGroup(i)
                    #ki2.leaveGroup(i)
                    #ki3.leaveGroup(i)
                    #ki4.leaveGroup(i)
                    #ki5.leaveGroup(i)
                #if wait["lang"] == "JP":
                    #line.sendMessage(to,"Bots Sudah Leave Dari Semua Group")
                #else:
                    #line.sendMessage(to,"He declined all invitations")
                        
                elif text.lower() == 'pmpict':
                    contact = line.getContact(msg.to)
                    path =("http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                    line.sendImageWithURL(msg.to, path)
                    
                elif text.lower() == 'pmcover':
                    contact = line.getContact(msg.to)
                    cu = line.getProfileCoverURL(msg.to)
                    cu = channel.getProfileCoverURL(msg.to)
                    h = client.getHome(msg.to)
                    path = str(cu)
                    line.sendImageWithURL(msg.to, path)            

                elif msg.text.lower().startswith("gcall "):
                        if msg.toType == 2:
                            sep = text.split(" ")
                            strnum = text.replace(sep[0] + " ","")
                            num = int(strnum)
                            line.sendMessage(to, "Inviting in call group!" %str(num))
                            for var in range(0,num):
                                group = line.getGroup(to)
                                members = [contact.mid for contact in group.members]
                                line.acquireGroupCallRoute(to)
                                line.inviteIntoGroupCall(to, contactIds=members)
                                
                elif msg.text.lower().startswith("jumlahtag: "):
                  if wait["selfbot"] == True:
                   if sender in lineMID:
                        proses = text.split(":")
                        strnum = text.replace(proses[0] + ":","")
                        num =  int(strnum)
                        Setmain["RAlimit"] = num
                        line.sendMessage(msg.to,"♻Total Spamtag Diubah Menjadi " +strnum)

                elif msg.text.lower().startswith("colek "):
                  if wait["selfbot"] == True:
                   if sender in lineMID:
                       if 'MENTION' in msg.contentMetadata.keys()!=None:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            zx = ""
                            zxc = " "
                            zx2 = []
                            pesan2 = "@a"" "
                            xlen = str(len(zxc))
                            xlen2 = str(len(zxc)+len(pesan2)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':key1}
                            zx2.append(zx)
                            zxc += pesan2
                            msg.contentType = 0
                            msg.text = zxc
                            lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                            msg.contentMetadata = lol
                            jmlh = int(Setmain["RAlimit"])
                            if jmlh <= 1000:
                                for x in range(jmlh):
                                    try:
                                        line.sendMessage1(msg)
                                    except Exception as e:
                                        line.sendMessage(msg.to,str(e))
                            else:
                                line.sendMessage(msg.to,"Jumlah melebihi 1000")
                                
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                            for x in range(jmlh):
                                line.sendMessage(msg.to, teks)
                            else:
                                line.sendMessage(msg.to, "")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "")
                            
                elif msg.text in ["Hi"]:
                    line.sendMessage(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")

                elif msg.text in ["Hello"]:
                    line.sendMessage(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")            
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                            
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[◑ The End  ◑]")

                elif "autoreject " in msg.text.lower():
                    xpesan = msg.text.lower()
                    xres = xpesan.replace("autoreject ","")
                    if xres == "off":
                        settings['autorejc'] = False
                        line.sendMessage(msg.to,"AutoReject already Off")
                    elif xres == "on":
                        settings['autorejc'] = True
                        line.sendMessage(msg.to,"AutoReject already On")
                        
                elif text.lower() == 'contact on':
                    if wait["contact"] == True:
                        if wait["lang"] == "JP":
                            line.sendMessage(to,"Contact turned On")
                        else:
                            line.sendMessage(to,"Contact turned On")
                    else:
                        wait["contact"] = True
                        if wait["lang"] == "JP":
                            line.sendMessage(to,"Contact turned On")
                        else:
                            line.sendMessage(to,"Contact turned On")
                elif text.lower() == 'contact off':
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            line.sendMessage(to,"Contact turned Off")
                        else:
                            line.sendMessage(to,"Contact turned Off")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            line.sendMessage(to,"Contact turned Off")
                        else:
                            line.sendMessage(to,"Contact turned Off")
                        
                elif "mimic " in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Reply Message On")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Reply Message Off")

                elif msg.text.lower().startswith("sider on"):
                    try:
                        del cctv['point'][msg.to]
                        del cctv['sidermem'][msg.to]
                        del cctv['cyduk'][msg.to]
                    except:
                        pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"Sider turned On")

                elif msg.text.lower().startswith("sider off"):
                    if msg.to in cctv['point']:
                        cctv['cyduk'][msg.to]=False
                        line.sendMessage(msg.to, "ᴄᴄᴛv ʏᴀɴɢ ᴛᴇʀᴛᴀɴɢᴋᴀᴘ:\n"+cctv['sidermem'][msg.to])
                        line.sendMessage(to,"Sider turned Off")
                    else:
                        line.sendMessage(msg.to, "On aja belum ")

#==============================================================================#                       
                elif text.lower() == 'welcome on':
                  if settings["welcomemsg"] == True:
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"WelcomeMessage Turned On")
                  else:
                    settings["welcomemsg"] = True
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"WelcomeMessage Turned On")
                        
                elif text.lower() == 'welcome off':
                  if settings["welcomemsg"] == False:
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"WelcomeMessage Turned Off")
                  else:
                    settings["welcomemsg"] = False
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"WelcomeMessage Turned Off")

#==============================================================================#                       
                elif text.lower() == 'leavemsg on':
                  if settings["leavemsg"] == True:
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"LeaveMessage Turned On")
                  else:
                    settings["leavemsg"] = True
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"LeaveMessage Turned On")
                        
                elif text.lower() == 'leavemsg off':
                  if settings["leavemsg"] == False:
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"LeaveMessage Turned Off")
                  else:
                    settings["leavemsg"] = False
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"LeaveMessage Turned Off")
#--------------------------------------------------------
                elif 'Set welcome ' in msg.text:
                   if msg._from in lineMID:
                      spl = msg.text.replace('Set welcome ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Failed to replace Welcome")
                      else:
                          settings["welcome"] = spl
                          line.sendMessage(msg.to, "WelcomeMessage is changed to :\n\n{}".format(str(spl)))
                          
                          
                elif text.lower() == "cek welcome":
                    if msg._from in lineMID:
                       line.sendMessage(msg.to, "WelcomeMessage :\n\n" + str(settings["welcome"]))


 #--------------------------------------------------------
                elif 'Set leavemsg ' in msg.text:
                   if msg._from in lineMID:
                      spl = msg.text.replace('Set leavemsg ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Failed to replace LeaveMsg")
                      else:
                          settings["keluar"] = spl
                          line.sendMessage(msg.to, "LeaveMessage is changed to :\n\n{}".format(str(spl)))
                          
                          
                elif text.lower() == "cek leavemsg":
                    if msg._from in lineMID:
                       line.sendMessage(msg.to, "LeaveMessage :\n\n" + str(settings["keluar"]))
#=============RESPON1=============================                      
                elif 'Set respon1 ' in msg.text:
                   if sender in lineMID:
                      spl = msg.text.replace('Set respon1 ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti Respon1")
                      else:
                          settings["tag"] = spl
                          line.sendMessage(msg.to, "Respon1 Text Diubah Menjadi :\n\n{}".format(str(spl)))
                          
                elif text.lower() == "cek respon1":
                    if sender in lineMID:
                            line.sendMessage(msg.to, "Respon1 Text Kamu :\n\n" + str(settings["tag"]))
                       
 #=============RESPON2=============================                      
                elif 'Set respon2 ' in msg.text:
                   if sender in lineMID:
                      spl = msg.text.replace('Set respon2 ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti Respon2")
                      else:
                          settings["tag2"] = spl
                          line.sendMessage(msg.to, "Respon2 Image Diubah Menjadi :\n\n{}".format(str(spl)))
                          
                elif text.lower() == "cek respon2":
                    if sender in lineMID:
                       line.sendMessage(msg.to, "Respon2 TagImage Kamu :\n\n" + str(settings["tag2"]))

  #=============RESPON3============================                      
                elif 'Set respon3 ' in msg.text:
                   if sender in lineMID:
                      spl = msg.text.replace('Set respon3 ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti Respon3")
                      else:
                          settings["tag3"] = spl
                          line.sendMessage(msg.to, "Respon3 PM Diubah Menjadi :\n\n{}".format(str(spl)))
                          
                elif text.lower() == "cek respon3":
                    if sender in lineMID:
                       line.sendMessage(msg.to, "Respon3 PM Kamu :\n\n" + str(settings["tag3"]))    
 
                elif 'Set responpc ' in msg.text:
                   if sender in lineMID:
                      spl = msg.text.replace('Set responpc ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti ResponPc")
                      else:
                          settings["responpc"] = spl
                          line.sendMessage(msg.to, "Respon Pc replaced so :\n\n".format(str(spl)))
                          
                          
                elif text.lower() == "cek responpc":
                    if sender in lineMID:
                       line.sendMessage(msg.to, "Respon Pc mu :\n\n"+ str(settings["responpc"]))

            
                elif text.lower() == 'gcreator':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    
                elif text.lower() == 'gid':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "[ID Group : ]\n" + gid.id)
                    
                elif text.lower() == 'gpict':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                    
                elif text.lower() == 'gname':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                    
                elif text.lower() == 'url':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            line.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                            
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "Grup qr already opened")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "Successful Open group qr")
                            
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "Grup qr already closed")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "Successful Close qr")
                            
                elif text.lower() == 'reject':                            
                    gid = line.getGroupIdsInvited()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        line.sendMessage(msg.to,"Reject GroupInvited Done")
                    else:
                        line.sendMessage(msg.to,"Done")
     
                elif text.lower() == 'cancelall':
                       if msg._from in lineMID: 
                        if msg.toType == 2:
                            group = line.getGroup(msg.to)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                line.cancelGroupInvitation(msg.to,[_mid])
                            line.sendMessage(msg.to,"I pretended to cancel and canceled.")
       
                elif msg.text.lower().startswith("Bots say "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    line.sendMessage(to,say)
            
                elif text.lower() == 'ginfo':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                    
                elif text.lower() == 'memlist':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                        
                        
                elif text.lower() == 'groups':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))
                        
                elif text.lower() == 'bots groups':
                        groups = ki.groups
                        groups = ki2.groups
                        groups = ki3.groups
                        groups = ki4.groups
                        groups = ki5.groups
                        groups = ki6.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ki.getGroup(gid)
                            group = ki2.getGroup(gid)
                            group = ki3.getGroup(gid)
                            group = ki4.getGroup(gid)
                            group = ki5.getGroup(gid)
                            group = ki6.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        ki.sendMessage(to, str(ret_))
                        ki2.sendMessage(to, str(ret_))
                        ki3.sendMessage(to, str(ret_))
                        ki4.sendMessage(to, str(ret_))  
                        ki5.sendMessage(to, str(ret_))
                        ki6.sendMessage(to, str(ret_))                       
                        
                elif msg.text in ["Autolike"]:
                  if sender in lineMID:
                    print ("[Command]Like executed")
                    line.sendMessage(msg.to,"Auto Like\nDone Bos")
                    try:
                      autolike()
                    except:
                      pass                        

                        
                elif "/ti/g/" in msg.text.lower():
                    if settings["autoJoinTicket"] == True:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            group = line.findGroupByTicket(ticket_id)
                            line.acceptGroupInvitationByTicket(group.id,ticket_id)
                            line.sendMessage(to, "Successful masuk ke group %s" % str(group.name))
                        # Check viewers command
     

 #
     
#==============================================================================#   
                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 

                elif text.lower() == "remove chat":
                  #if wait["selfbot"] == True:
                    if msg._from in lineMID:
                       try:
                           line.removeAllMessages(op.param2)
                           line.sendMessage(msg.to,"Chat dibersihkan...")
                       except:
                           pass
 
#-------------------------------------------------------------------------------
                elif text.lower() == '.nukeall':
                    if msg._from in admin:
                        if msg.toType == 2:
                            print ("[ 19 ] NUKE")
                            _name = msg.text.replace(".nukeall","")
                            gs = ki.getGroup(msg.to)
                            gs = ki2.getGroup(msg.to)
                            gs = ki3.getGroup(msg.to)
                            gs = ki4.getGroup(msg.to)
                            gs = ki5.getGroup(msg.to)
                            gs = ki6.getGroup(msg.to)
                            ki.sendMessage(msg.to,"Group cleansed")
                            ki2.sendMessage(msg.to,"Wan")
                            ki3.sendMessage(msg.to,"chu") 
                            ki4.sendMessage(msg.to,"tri")
                            ki5.sendMessage(msg.to,"goooo!") 
                            ki6.sendMessage(msg.to,"goooo!") 
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendMessage(msg.to,"Not Found")
                                ki2.sendMessage(msg.to,"Not Found")
                                ki3.sendMessage(msg.to,"Not Found")
                                ki4.sendMessage(msg.to,"Not Found")
                                ki5.sendMessage(msg.to,"Not Found")
                                ki6.sendMessage(msg.to,"Not Found")
                            else:
                                for target in targets:
                                    if not target in Bots:                    
                                            if not target in admin:
                                                try:
                                                    klist=[ki,ki2,ki3,ki4,ki5,ki6]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    line.sendMessage(msg.to,"") 
             
                elif msg.text.lower().startswith("music "):
                            try:
                                search = msg.text.lower().replace("fullmusic ","")
                                r = requests.get("https://farzain.xyz/api/joox.php?apikey=412uH5fxAT7jsNaUwCkVwH4qEUn2Dz&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "☠ Hasil Music ☠ \n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                hasil += "\n\n☠ Lyric Lagu:\n\n{}".format(str(data["lirik"]))
                                hasil += "\n\n☠ Please Wait For Downloading...!!! \n"
                                line.sendImageWithURL(msg.to, str(data["gambar"]))
                                line.sendMessage(msg.to, str(hasil))
                                line.sendMessage(msg.to, "Result MP3 ")
                                line.sendAudioWithURL(msg.to, str(audio["mp3"]))
                            except Exception as error:
                            	line.sendMessage(msg.to, "Result Error:\n" + str(error))

                elif "kalkulator" in msg.text.lower():
                    try:
                        sep = msg.text.split(" ")
                        cal = msg.text.replace(sep[0] + " ","")
                        result = requests.get("http://calcatraz.com/calculator/api?c="+urllib.parse.quote(cal))
                        data = result.text
                        line.sendMessage(to,"Hasil:\n\n"+ cal+ " = " +str(data))
                    except Exception as error:
                        logError(error)
                        line.sendMessage(to, str(error))
                    
                elif "instagram" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            line.sendImageWithURL(to, str(path))
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "Pengguna tidak ditemukan")

                elif msg.text.lower().startswith("movie"):
                    try:
                        sep = msg.text.split(" ")
                        search = msg.text.replace(sep[0] + " ","")
                        apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
                        api = requests.get("https://farzain.xyz/api/film.php?apikey={}&id={}".format(str(apiKey), str(search)))
                        data = api.text
                        data = json.loads(data)
                        if data["status"] == "success":
                            anu = "[ Result Film ]"
                            anu += "\nTitle : {}".format(str(data["Title"]))
                            anu += "\nYear : {}".format(str(data["Year"]))
                            anu += "\nRated : {}".format(str(data["Rated"]))
                            anu += "\nReleased : {}".format(str(data["Released"]))
                            anu += "\nDuration : {}".format(str(data["Runtime"]))
                            anu += "\nGenre : {}".format(str(data["Genre"]))
                            path = str(data["Poster"])
                            line.sendImageWithURL(msg.to, str(path))
                            line.sendMessage(msg.to, str(anu))
                        else:
                            sendMentionV2(msg.to, "Maaf @!,hasil pencarin tidak ditemukan", [sender])
                    except Exception as error:
                        line.sendMessage(msg.to, str(error))

 #___________BROADCAST_______________
                elif msg.text.lower().startswith("broadcast "):   
                   sep = text.split(" ")
                   txt = text.replace(sep[0] + " ","")
                   groups = line.groups
                   for group in groups:
                       line.sendMessage(group, "Broadcast:\n\n{}".format(str(txt)))


#____________________________________

                elif "image: " in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))

                elif "youtube" in msg.text.lower():
                          if msg._from in lineMID:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "💿 Judul 🎼〘 " + vid.title + " 〙"
                                    author = '\n\n✏ Author : ' + str(vid.author)
                                    durasi = '\n📟 Duration : ' + str(vid.duration)
                                    suka = '\n👍 Likes : ' + str(vid.likes)
                                    rating = '\n⭐ Rating : ' + str(vid.rating)
                                    deskripsi = '\n📋 Deskripsi : ' + str(vid.description)
                                line.sendVideoWithURL(msg.to, me)
                                line.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                line.sendMessage(msg.to,str(e))                                

            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    
            elif wait["contact"] == True:
                msg.contentType = 0
                line.sendMessage(msg.to,msg.contentMetadata["mid"])
                if 'displayName' in msg.contentMetadata:
                    contact = line.getContact(msg.contentMetadata["mid"])
                    try:
                        cu = line.channel.getCover(msg.contentMetadata["mid"])
                    except:
                        cu = ""
                    line.sendMessage(to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                else:
                    contact = line.getContact(msg.contentMetadata["mid"])
                    try:
                        cu = line.channel.getCover(msg.contentMetadata["mid"])
                    except:
                        cu = ""
                    line.sendMessage(to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 1:
                if settings["changePicture"] == True:
                    path = line.downloadObjectMsg(msg_id)
                    settings["changePicture"] = False
                    line.updateProfilePicture(path)
                    line.sendMessage(to, "Successful mengubah foto profile")

                if msg.toType == 2:
                    if to in settings["changeGroupPicture"]:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changeGroupPicture"].remove(to)
                        line.updateGroupPicture(to, path)
                        line.sendMessage(to, "Successful mengubah foto group")
                        
            elif msg.contentType == 16:
                    mid = data["actorId"]
                    postId = data["activityExternalId"]
                    line.likePost(to, mid, postId, likeType=1001)
                    line.createComment(to, mid, postId, "AutoLike by: Team Dkz Protection ")
#==============================================================================#
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in lineMID:
                    pass
                ginfo = line.getGroup(op.param1)
                contact = line.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                line.sendImageWithURL(op.param1, image)
                
        if op.type == 13:
            if lineMID in op.param3:
              if settings["autojj"] == "wl":
                if op.param2 in periksa["wl"]:
                  line.acceptGroupInvitation(op.param1)
                else:
                    if settings['autorejc'] == True:
                        line.rejectGroupInvitation(op.param1)
                    else:
                        pass
              elif settings["autojj"] == "all":
                  line.acceptGroupInvitation(op.param1)
              else:
                  if settings['autorejc'] == True:
                        line.rejectGroupInvitation(op.param1)
                  else:
                        pass

        if op.type == 26:
          if wait["Mute"] == False:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                if settings["autoBalas"] == True:
                    if msg.toType == 0:                	
                        line.sendChatChecked(sender,msg_id)
                        contact = line.getContact(sender)
                        mids = [contact.mid]
                        text = "[ Auto Respon ]\n\nHallo @!\nMohon Maaf Saya Sedang Sibuk, Ini Adalah Pesan Otomatis, Jika Ada Yang Penting Mohon Hubungi Saya Nanti, Terimakasih..."
                        summon(op.param1)
                else:
                    to = receiver
            else:
                to = receiver
                if msg.contentType == 0:
                    if settings["autoRead"] == True:
                        line.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)                        
                if settings["unsendMessage"] == True:
                    try:
                        msg = op.message
                        if msg.toType == 0:
                            line.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                        else:
                            line.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                            msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    except Exception as error:
                        logError(error)          

                if msg.contentType == 0:
                    if text is None:
                        return
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = line.findGroupByTicket(ticket_id)
                                line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                line.sendMessage(to, "Successful join ke group %s" % str(group.name))

#___________________RESPON TEXT__________________
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                if settings["autoRespon"]:
                                    contact = line.getContact(sender)
                                    line.sendMessage(to, settings["tag"])
                                break
                                
   #___________________RESPON IMAGE_________________
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                if settings["autoResponImage"]:
                                    contact = line.getContact(sender)
                                    anu = contact.displayName
                                    path = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                                    line.sendMessage(to, settings["tag2"])
                                    line.sendImageWithURL(msg.to, str(path))
                                break
                                                             
  #___________________RESPON PM________________
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                if settings["autoResponPm"]:
                                    contact = line.getContact(sender)
                                    line.sendMessage(sender, settings["tag3"])
                                break              
                                
#___________________________                             
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                if msg.to in responPc:
                                    G = line.getGroup(to)
                                    contact = line.getContact(sender)
                                    anu = contact.displayName
                                    #sid = str(tikel["sid"])
                                    #spkg = str(tikel["spkg"])
                                    anu = contact.displayName
                                    line.sendMessage(sender, settings["responpc"])
                                    #line.sendSticker(sender, spkg, sid)
                                break                           
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)

#________________
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = line.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "Send Message cancelled."
                                ret_ += "\nSender : @!"
                                ret_ += "\nSend At : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nType : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nText : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            line.sendMessage(at,"SentMessage cancelled,But I didn't have log data.\nSorry > <")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)


#============================================================================
        if op.type == 19:
            print ("[ 19 ] KICKOUT JP MESSAGE")
            try:
                if op.param3 in lineMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
#------------------------------------------------------------------------------
                elif op.param3 in lineMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
#------------------------------------------------------------------------------
                elif op.param3 in lineMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
#-------------------------------------------------------------------------------
                elif op.param3 in lineMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        
  #------------------------------------------------------------------------------
                elif op.param3 in lineMID:
                    if op.param2 in ki5MID:
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)                      
#=============================================================================
                elif op.param3 in lineMID:
                    if op.param2 in ki6MID:
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)                      
#=============================================================================
                if op.param3 in kiMID:
                    if op.param2 in lineMID:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
                    else:
                        G = line.getGroup(op.param1)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
#-------------------------------------------------------------------------------
                elif op.param3 in kiMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
#-------------------------------------------------------------------------------
                elif op.param3 in kiMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
#------------------------------------------------------------------------------
                elif op.param3 in kiMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        
#=====================================================================
 #------------------------------------------------------------------------------
                elif op.param3 in kiMID:
                    if op.param2 in ki5MID:
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)                  
#=============================================
                elif op.param3 in kiMID:
                    if op.param2 in ki6MID:
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)                  
#=============================================
                if op.param3 in ki2MID:
                    if op.param2 in lineMID:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
                    else:
                        G = line.getGroup(op.param1)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
#-----------------------------------------------------------------------------
                elif op.param3 in ki2MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
#------------------------------------------------------------------------------
                elif op.param3 in ki2MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------------------------------------
                elif op.param3 in ki2MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        
   #------------------------------------------------------------------------------
                elif op.param3 in ki2MID:
                    if op.param2 in ki5MID:
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)                     
#=======================================
                elif op.param3 in ki2MID:
                    if op.param2 in ki6MID:
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)                     
#=======================================
                if op.param3 in ki3MID:
                    if op.param2 in lineMID:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
                    else:
                        G = line.getGroup(op.param1)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
#-----------------------------------------------------------------------------
                elif op.param3 in ki3MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------------------------------------
                elif op.param3 in ki3MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
#-------------------------------------------------------------------------------
                elif op.param3 in ki3MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        
  #------------------------------------------------------------------------------
                elif op.param3 in ki3MID:
                    if op.param2 in ki5MID:
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)                      
#================================================================
                elif op.param3 in ki3MID:
                    if op.param2 in ki6MID:
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)                      
#================================================================
                if op.param3 in ki4MID:
                    if op.param2 in lineMID:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
                    else:
                        G = line.getGroup(op.param1)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
#-------------------------------------------------------------------------------
                elif op.param3 in ki4MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
#-------------------------------------------------------------------------------
                elif op.param3 in ki4MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
#------------------------------------------------------------------------------
                elif op.param3 in ki4MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        
#-------------------------------------------------------------------------------
                elif op.param3 in ki4MID:
                    if op.param2 in ki5MID:
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)

#==============================================
                elif op.param3 in ki4MID:
                    if op.param2 in ki6MID:
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)

#==============================================
                if op.param3 in ki5MID:
                    if op.param2 in lineMID:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)  
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
                    else:
                        G = line.getGroup(op.param1)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
                        
#------------------------------------------------------------------------------
                elif op.param3 in ki5MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)

#-------------------------------------------------------------------------------
                elif op.param3 in ki5MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)              

 #------------------------------------------------------------------------------
                elif op.param3 in ki5MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        
  #------------------------------------------------------------------------------
                elif op.param3 in ki5MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)                           
#==============================================
                elif op.param3 in ki5MID:
                    if op.param2 in ki6MID:
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)                           
#==============================================
                if op.param3 in ki6MID:
                    if op.param2 in lineMID:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)  
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
                    else:
                        G = line.getGroup(op.param1)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
                        
#------------------------------------------------------------------------------
                elif op.param3 in ki6MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)

#-------------------------------------------------------------------------------
                elif op.param3 in ki6MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)              

 #------------------------------------------------------------------------------
                elif op.param3 in ki6MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        
  #------------------------------------------------------------------------------
                elif op.param3 in ki6MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
  #------------------------------------------------------------------------------
                elif op.param3 in ki6MID:
                    if op.param2 in ki5MID:
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)
                    
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"(U)(P)")
                        
                else:
                    pass
            except:
                pass
    #==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots:
                    pass
                elif settings["qrprotect"] == True:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(KAC).updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    line.sendMessage(op.param1,"Woiiiiiiiiiiiii")
            else:
                line.sendMessage(op.param1,"")
#==============================================================================#            
                

#==============================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass


        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = line.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n☛ " + Name
                                summon(op.param1,[op.param2])
                                zxn=["Tercyduk juga dirimu\nSUBHANALLAH "," Sini ka jangan ngintip mele\nMASYA ALLAH","Mau lari kemana lo\nAnda ttap kecydut Bot\nSUBHANALLAH","Turun kak ikut chat sini\nYA ELLAH ","Dirimu krtangkap basah cctv\nSUBHANNALLAH","Sider MUlu dirimu\nASTAGHFIRULLAH","Istighfar bro\nJgn CCTV mele\nMasya allah","Loha\nSini ikut Ngopi ","Hai idolaku ayo sini ngobrol"]
                                say = random.choice(zxn) +" "+ Name
                                line.sendMessage(op.param1, say)
                                contact = line.getContact(op.param2).picturePath
                                image = 'http://dl.profile.line.naver.jp'+contact
                                line.sendImageWithURL(op.param1, image)
                                #cl.sendMessage(to, None, contentMetadata={"STKID":"26538898","STKPKGID":"10272","STKVER":"1"}, contentType=7)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
        else:
            pass

        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                line.sendMessage(msg.to, "[̟]: " + data['result']['response'].encode('utf-8'))
                                
    except Exception as error:
        logError(error)
#==============================================================================#
def autolike():
    count = 1
    while True:
        try:
           for posts in line.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                   line.likePost(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print ("Like")
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          line.createComment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def autoLike():
    count = 1
    while True:
        try:
           for posts in cl.getFeed(postLimit=10, commentLimit=1, likeLimit=1, order='TIME')["result"]["feed"]:
             if hasil["postInfo"]["homeId"]["postId"] is False:
                if wait["sukaPost"] == True:
                   line.likePost(hasil["userMid"]["writerMid"], hasil["postInfo"]["postId"], likeType=1001)
                   print ("Like")
                   if wait["commentOn"] == True:
                      if hasil["homeId"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          line.createComment(posts["userMid"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
            
def autoLiked():
	if settings["sukaPost"] == True:
		lastTimeLiking = time.time()
		if time.time() - lastTimeLiking >= 60*60:
			listLikeType = 1001
			myComment = "[ Auto Like by: Team Dk Protection ]"
			feed = client.getFeed()
			if feed["message"] != 'succes':
				lastTimeLiking = time.time()
				return True
			del feed["result"]["feedInfos"]
			result = ["result"]["feeds"]
			for res in result:
				postInfo = res["post"]["postInfo"]
				homeId = postInfo["homeId"]
				postId = postInfo["postId"]
				likeStat = postInfo["liked"]
				if likeStat == True:
					continue
				else:
					line.likePost(homeId, postId, listLikeType)
					line.createComment(homeId, postId, myComment)
					lastTimeLiking = time.time()

thread1 = threading.Thread(target=autoLike)
thread1.daemon = True
thread1.start()         
while True:
  try:
      Ops = line.poll.fetchOperations(line.revision, 50)
      for op in Ops:
        if op.type != 0:
          line.revision = max(line.revision, op.revision)
          lineBot(op)
  except Exception as E:
    E = str(E)
    if "reason=None" in E:
      print (E)
      time.sleep(60)
      restart_program()
        
        

        
        

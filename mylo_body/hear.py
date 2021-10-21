import socket
import json
import azure.cognitiveservices.speech as speechsdk
import time
import speak as vocalize
import bodyinfo as info
import settings as set
import time

host = '192.168.1.8'
cport = 19216
eport = 19217

sk, sr = "f1231e8177cd4bb98e3f3063d81e7f7b", "eastus"
speechconfig = speechsdk.SpeechConfig(subscription=sk, region=sr)
recognizer = speechsdk.SpeechRecognizer(speech_config=speechconfig)
eserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



while True:
    eserver.connect((host, eport))
    clientName = f"{info.currentUser} || {set.placement}" 
    time.sleep(0.5)
    print("Listening")
    result = recognizer.recognize_once()
    if result:
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            if not info.queryRequired:
                if set.hotwordNeeded and not info.hotwordUsed:
                    returnRes = info.hotwordCheck(result.text)
                    if returnRes:
                        info.hotwordUsed = True
                        info.hotwordStamp = int(time.time())
                elif set.hotwordNeeded and info.hotwordUsed:
                    grab = int(time.time())
                    if grab - info.hotwordStamp >= (set.hotwordTimeMin * 60):
                        returnRes = info.hotwordCheck(result.text)
                        if returnRes:
                            info.hotwordUsed = True
                            info.hotwordStamp = int(time.time())
                        else:
                            info.hotwordUsed = False
                if info.currentUser is None and "login" not in str(result.text).lower() and (set.hotwordNeeded and info.hotwordUsed or not set.hotwordNeeded):
                    vocalize.process("It seems like there's no user logged in currently. Please login by using the login command with your name.")
                elif "login" in str(result.text).lower() and info.currentUser is None:
                    speak = str(result.text).lower()
                    whitelist = set('abcdefghijklmnopqrstuvwxyz ')
                    speak = ''.join(filter(whitelist.__contains__, speak))
                    speak = speak.split(" ")
                    name = speak[speak.index("login")+1]
                    if name not in info.userLogs:
                        vocalize.process(vocalize.decide([
                            f"Creating a new login profile for you, {name}. I apologize for the inconvenience; how may I help you?",
                            f"I am creating a new login for you, {name}. How may I assist you?",
                            f"Sorry for the inconvenience, {name}. I've created a new login for you. How may I assist you?"]))
                        info.currentUser = name
                        info.userLogs.append(name)
                    elif name in info.userLogs:
                        vocalize.process(vocalize.decide([
                            f"I've logged you in, {name}. How may I assist you?",
                            f"Alright, I've got you logged in {name}. How can I help?",
                            f"You're logged in now, {name}. How can I help you?"
                        ]))
                        info.currentUser = name













            cserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cserver.connect((host, cport))
            print(result.text)
            request = {
            'request' : 'command',
            'profile' :'nate',
            'command' : result.text}
            request = json.dumps(request)
            cserver.send(request.encode('utf-8'))
            result = cserver.recv(2024).decode('utf-8')
            result = json.loads(result)
            vocalize.process(result['phrase'])
            cserver.close()
    excess = eserver.recv(2024).decode('utf-8')
    if excess is not None or len(excess)>0:
        excess = json.loads(excess)
        print(repr(excess))
    eserver.close()
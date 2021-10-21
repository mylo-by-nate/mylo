import settings

if settings.logout == True:
    currentUser = None
else:
    currentUser = settings.defaultUser

loginStamp = 0
hotwordStamp = 0
userLogs = []
queryKeys = []
queryRequired = False
assistant = "mylo"
hotwordUsed = False
pronounciation = [["my", "love"], "mila", "milo", ["my", "low"]]
hotwords = []
if settings.hotwordNeeded:
    for key in pronounciation:
        if type(key) is list:
            hotwords.append(f"hey {key[0]} {key[1]}")
            hotwords.append(f"{key[0]} {key[1]}")
            hotwords.append(f"hello {key[0]} {key[1]}")
        else:
            hotwords.append(f"hey {key}")
            hotwords.append(f"{key}")
            hotwords.append(f"hello {key}")

    hotwords.append(f"hey {assistant}")
    hotwords.append(f"{assistant}")
    hotwords.append(f"hello {assistant}")

def hotwordCheck(words):
    words = words.lower()
    whitelist = set('abcdefghijklmnopqrstuvwxyz ')
    words = ''.join(filter(whitelist.__contains__, words))
    if words in hotwords:
        return words
    else:
        for sentence in hotwords:
            if sentence in words:
                return words.replace(sentence, "")
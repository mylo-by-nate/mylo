
nate = { #MB
    "info": { #FOLD
        "personal": { #CELL
            "templatephrase": ["nate's NAME is ANSWER.", "well since you're so curious, nate's NAME is ANSWER.",
                "I remember nate's NAME being ANSWER.", "I currently have nate's NAME saved as ANSWER."],
            'templatekeys':['what is nates NAME', 'is nates NAME ANSWER', 'can you tell me nates NAME', 'do you remember nates NAME'],
            
            "age": { #NEURON
                'addkeys': ['how old is nate', 'what is nates age', 'how old is nathan'],
                'addphrase': ["If I remember right, I think he's 20.", "I have his age remembered as 20."],
                'ans': '20',
                'fire': None,
                'phrases': None,
            },
            "birthday": { #NEURON
                'addkeys': ['what is nates birthday', 'when is nates birthday'],
                'addphrase': ['I believe its August 16th, 2001.', 'Im pretty sure its August 16th, 2001.'],
                'ans': 'August 16th, 2001',
                'fire': None,
                'phrases': None
            },
        },
        "favorites":{
            "templatephrase":["nate's favorite NAME is ANSWER.", "i have nate's favorite NAME saved as ANSWER.", "i remember nate's favorite NAME being ANSWER."],
            "templatekeys":["what is nates favorite NAME", "does nate like ANSWER", "is nates favorite NAME ANSWER", "do you remember nates favorite NAME"],
            
            "color": { #NEURON
                'addkeys': None,
                'addphrase': None,
                'ans': 'blue',
                'fire': None,
                'phrases': None
            },
            "food": { #NEURON
                'addkeys': None,
                'addphrase': None,
                'ans': 'chicken',
                'fire': None,
                'phrases': None},
        },
    }
}
friends = {
    'daigen': {
        "personal": {
            "templatephrase":["NAMEs NEURON is ANSWER", "I remember NAMEs NEURON being ANSWER.", "I have NAMEs NEURON saved as ANSWER."],
            "templatekeys":["what is NAMEs NEURON", "is NAMEs NEURON ANSWER", "do you remember NAMEs NEURON"],

            "hair":{
                'addkeys':["what color is NAMEs hair", "color NAMEs hair", "what is NAMEs hair color"],
                'addphrase': ["I'm pretty sure Daigen's hair color is blonde.", "Daigen has blonde hair if I remember right."],
                'ans': "blonde",
                "fire": None,
                "phrases": None,
            },
            "eye":{
                'addkeys':["what color are NAMEs eyes", "what color is NAMEs eyes", "what is NAMEs eye color"], 
                'addphrase': ["I haven't seen them, but I believe they're blue.", "I'm pretty sure Daigen has blue eyes."],
                'ans': 'blue',
                'fire': None,
                'phrases': None,
            }
        }
    }
}
self = {
    "info": {
        "personal": {
            "templatephrase":None,
            "templatekeys":["what is your NEURON", "is your NEURON ANSWER", "do you remember your NEURON"],

            "name":{
                'addkeys':["what is your name", "who are you", "whats your name"],
                'addphrase': ["My name is Mylo.", "My name is Mylo; thanks for asking."],
                'ans': "mylo",
                "fire": None,
                "phrases": None,
            },
            "programmed":{
                'addkeys':["how were you made", "programmed", "how are you programmed", "what are you made with", "how are you made"], 
                'addphrase': [
                    "Uh, nobody really asks me that. I am running thanks to Python and Ubuntu. Typically all the requests you make are" + 
                    " handled locally by your device. They then get sent to my server where I process and connect it to an answer. I then send it back to your device" + 
                    " and vocalize the answer."],
                'ans': "python",
                'fire': None,
                'phrases': None,
            },
            "more":{
                'addkeys':["tell me about yourself", "how do you work", "whats your process"], 
                'addphrase': [
                    "I'm glad you asked. Any command you vocalize to me will be handled and translated on your device. Your command then gets sent "+
                    "to my server where I connect the dots and create a solution. I then send a data packet back to your device and vocalize any information.",
                    "Typically when you ask me a question, I process and translate your command locally. Your request then goes to my server where I can process " + 
                    "the translate command. I shoot your device a sentence as a data packet that then gets vocalized."],
                'ans': None,
                'fire': None,
                'phrases': None,
            },
        }
    }
}
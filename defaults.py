
nate = { #MB
    "info": { #FOLD
        "personal": { #CELL
            "templatephrase": ["nate's NAME is ANSWER.", "well since you're so curious, nate's NAME is ANSWER.",
                "I remember nate's NAME being ANSWER.", "I currently have nate's NAME saved as ANSWER."],
            'templatekeys':['what is nates NAME', 'is nates NAME ANSWER', 'can you tell me nates NAME', 'do you remember nates NAME'],
            "age": { #NEURON
                'addkeys': ['how old is nate', 'what is nates age', 'how old is nathan'],
                'ans': '20',
                'fire': None,
                'phrase': None,
            },
            "birthday": { #NEURON
                'addkeys': ['what is nates birthday', 'when is nates birthday'],
                'ans': 'August 16th, 2001',
                'fire': None,
                'phrase': None
            },
        },
        "favorites":{
            "templatephrase":["nate's favorite NAME is ANSWER.", "i have nate's favorite NAME saved as ANSWER.", "i remember nate's favorite NAME being ANSWER."],
            "templatekeys":["what is nates favorite NAME", "does nate like ANSWER", "is nates favorite NAME ANSWER", "do you remember nates favorite NAME"]
        }
    }
}
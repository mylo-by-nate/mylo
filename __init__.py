import time
print("\033[92m\033[1m\n \n \n \n \n \n \n"
"\n######################################################################" +
"\n#                 #####       #####            ##                    #"
"\n#                  ###         ###             ##                    #"
"\n#                  ###         ###             ##                    #"
"\n#                  ###         ###     ##      ##                    #"
"\n#                  ###############     ##      ##                    #"
"\n#                  ###############             ##                    #"
"\n#                  ###         ###    ###      ##                    #"
"\n#                  ###         ###      #      ##                    #"
"\n#                  ###         ###      #                            #"
"\n#                  ###         ###      #      ##                    #"
"\n#                 #####       #####   #####    ##                    #"
"\n#                                                                    #"
"\n#                made and scripted by nate tanner :)                 #"
"\n#         all resources were gathered from youtube and api           #"
"\n#         references online. i attempted to stray from using         #"
"\n#         pre-made software so and instead stuck with code so        #"
"\n#                           there's a lot!                           #"
"\n#                                                                    #"
"\n#                           started:8/2021                           #"
"\n######################################################################\n\033[0m")
time.sleep(2)
print(f"{' ' * 15} Starting Mylo Init")
time.sleep(0.5)
from stem import callosum
from temporal.longterm import friends
from temporal.longterm import nate
from temporal.longterm import self
from temporal.longterm import profiles
from temporal.longterm import weather
from temporal import shortterm
from temporal import grab
from parietal import process
from temporal import induct
from frontal.uni import functions

print(f"{' ' * 10} Success basic Mylo imports")
time.sleep(0.5)
print(f"{' ' * 15} Starting defaults init")
time.sleep(0.5)
import defaults

for fold in defaults.nate:
    for cell in defaults.nate[fold]:
        for neuron in defaults.nate[fold][cell]:
            if not "template" in neuron:
                defaults.nate[fold][cell][neuron]['fire'] = []
                defaults.nate[fold][cell][neuron]['phrases'] = []
                if defaults.nate[fold][cell]['templatekeys'] is not None: 
                    for key in defaults.nate[fold][cell]['templatekeys']: 
                        key = key.replace('ANSWER', (defaults.nate[fold][cell][neuron]['ans'] or "None"))
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.nate[fold][cell][neuron]['fire'].append(key)
                if defaults.nate[fold][cell][neuron]['addkeys'] is not None:
                    for key in defaults.nate[fold][cell][neuron]['addkeys']: 
                        key = key.replace('ANSWER', (defaults.nate[fold][cell][neuron]['ans'] or "None"))
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.nate[fold][cell][neuron]['fire'].append(key)
                if defaults.nate[fold][cell]['templatephrase'] is not None: 
                    for key in defaults.nate[fold][cell]['templatekeys']: 
                        key = key.replace('ANSWER', (defaults.nate[fold][cell][neuron]['ans'] or "None"))
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.nate[fold][cell][neuron]['phrases'].append(key)
                if defaults.nate[fold][cell][neuron]['addphrase'] is not None:
                    for key in defaults.nate[fold][cell][neuron]['addkeys']: 
                        key = key.replace('ANSWER', (defaults.nate[fold][cell][neuron]['ans'] or "None"))
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.nate[fold][cell][neuron]['phrases'].append(key)
                induct.ltCommit({'saveplace':["nate", fold, cell], 'savename': neuron, 'savetype': 'neuron', 'save': defaults.nate[fold][cell][neuron]})

print(f"{' ' * 10} Nate default init complete")
time.sleep(0.3)

for fold in defaults.friends:
    for cell in defaults.friends[fold]:
        for neuron in defaults.friends[fold][cell]:
            if not "template" in neuron:
                defaults.friends[fold][cell][neuron]['fire'] = []
                defaults.friends[fold][cell][neuron]['phrases'] = []
                if defaults.friends[fold][cell]['templatekeys'] is not None: 
                    for key in defaults.friends[fold][cell]['templatekeys']: 
                        key = key.replace('ANSWER', defaults.friends[fold][cell][neuron]['ans'])
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.friends[fold][cell][neuron]['fire'].append(key)
                if defaults.friends[fold][cell][neuron]['addkeys'] is not None:
                    for key in defaults.friends[fold][cell][neuron]['addkeys']: 
                        key = key.replace('ANSWER', defaults.friends[fold][cell][neuron]['ans'])
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.friends[fold][cell][neuron]['fire'].append(key)
                if defaults.friends[fold][cell]['templatephrase'] is not None: 
                    for key in defaults.friends[fold][cell]['templatekeys']: 
                        key = key.replace('ANSWER', defaults.friends[fold][cell][neuron]['ans'])
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.friends[fold][cell][neuron]['phrases'].append(key)
                if defaults.friends[fold][cell][neuron]['addphrase'] is not None:
                    for key in defaults.friends[fold][cell][neuron]['addkeys']: 
                        key = key.replace('ANSWER', defaults.friends[fold][cell][neuron]['ans'])
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.friends[fold][cell][neuron]['phrases'].append(key)
                induct.ltCommit({'saveplace':["friends", fold, cell], 'savename': neuron, 'savetype': 'neuron', 'save': defaults.friends[fold][cell][neuron]})

print(f"{' ' * 10} Friends default init complete")
time.sleep(0.3)

for fold in defaults.self:
    for cell in defaults.self[fold]:
        for neuron in defaults.self[fold][cell]:
            if not "template" in neuron:
                defaults.self[fold][cell][neuron]['fire'] = []
                defaults.self[fold][cell][neuron]['phrases'] = []
                if defaults.self[fold][cell]['templatekeys'] is not None: 
                    for key in defaults.self[fold][cell]['templatekeys']: 
                        key = key.replace('ANSWER', (defaults.self[fold][cell][neuron]['ans'] or "None"))
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.self[fold][cell][neuron]['fire'].append(key)
                if defaults.self[fold][cell][neuron]['addkeys'] is not None:
                    for key in defaults.self[fold][cell][neuron]['addkeys']: 
                        key = key.replace('ANSWER', (defaults.self[fold][cell][neuron]['ans'] or "None"))
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.self[fold][cell][neuron]['fire'].append(key)
                if defaults.self[fold][cell]['templatephrase'] is not None: 
                    for key in defaults.self[fold][cell]['templatekeys']: 
                        key = key.replace('ANSWER', (defaults.self[fold][cell][neuron]['ans'] or "None"))
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.self[fold][cell][neuron]['phrases'].append(key)
                if defaults.self[fold][cell][neuron]['addphrase'] is not None:
                    for key in defaults.self[fold][cell][neuron]['addkeys']: 
                        key = key.replace('ANSWER', (defaults.self[fold][cell][neuron]['ans'] or "None"))
                        key = key.replace('NAME', (fold or "None"))
                        key = key.replace("NEURON", (neuron or "None"))
                        defaults.self[fold][cell][neuron]['phrases'].append(key)
                induct.ltCommit({'saveplace':["self", fold, cell], 'savename': neuron, 'savetype': 'neuron', 'save': defaults.self[fold][cell][neuron]})

print(f"{' ' * 10} Self default init complete")
time.sleep(0.3)
print(f"{' ' * 10} Success finalizing Mylo init")
time.sleep(0.25)
print(f"{' ' * 15} Success beginning")


from spinal import recieve

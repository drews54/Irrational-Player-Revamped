#from platform import system
#if system() == 'Windows':
#    import winsound
#else:
#    print('This software is currently only compatible with Windows OS')
#    exit()
from decimal import getcontext, Decimal
from random import randint
from miditime.miditime import MIDITime

getcontext().prec = 60

number = Decimal(input('Enter a positive number: '))
root = number.sqrt()
playstring = str(root).replace('.', '', 1)

bpm = int(input('Enter rhythm in BPM: '))
midiout = MIDITime(bpm, 'irrational_music.mid')
notes = (68, 69, 71, 72, 74, 76, 77, 80, 81, 83)

velocity = int(input('Enter note velocity (loudness) 0-127: '))
midinotes = []
for time in range(len(playstring)):
    midinotes.append([
        time,
        notes[int(playstring[time])],
        velocity,
        1
    ])
midiout.add_track(midinotes)
midiout.save_midi()
#winsound.PlaySound('irrational_music.mid', winsound.SND_FILENAME)
#TODO: Implement playback of the created .mid file.
print('Find the resulting "irrational_music.mid" file in the program folder')
from decimal import getcontext, Decimal
from random import randint
from miditime.miditime import MIDITime
from pathlib import Path

getcontext().prec = 60
midifile = Path.home().joinpath('Desktop', 'irrational_music.mid')

number = Decimal(input('Enter a positive number: '))
bpm = int(input('Enter rhythm in BPM: '))
velocity = int(input('Enter note velocity (loudness) 0-127: '))

playstring = str(number.sqrt()).replace('.', '', 1)
midiout = MIDITime(bpm, midifile)
notes = (68, 69, 71, 72, 74, 76, 77, 80, 81, 83)

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
print('You can find the resulting "irrational_music.mid" file at your desktop')

from midi_playback import player_init
player_init(midifile)

print('Thank you for listening!')
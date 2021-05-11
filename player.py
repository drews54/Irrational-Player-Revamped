from decimal import getcontext, Decimal
from pathlib import Path
from os import system
from miditime.miditime import MIDITime

getcontext().prec = 60
FILENAME = 'irrational_music.mid'
MIDIPATH = Path.home()
if MIDIPATH.joinpath('Desktop').exists():
    MIDIPATH = MIDIPATH.joinpath('Desktop', FILENAME)
else:
    MIDIPATH = MIDIPATH.joinpath(FILENAME)

number = abs(Decimal(
    input("Enter a positive number that doesn't have an integer square root: ")))
bpm = min(
    abs(int(input("Enter rhythm (speed) in BPM (beats per minute) 0-600: "))), 600)
velocity = min(
    abs(int(input("Enter note velocity (loudness) 0-127: "))), 127)

PLAYSTRING = str(number.sqrt()).replace(".", "", 1)
midiout = MIDITime(bpm, MIDIPATH)
NOTES = (68, 69, 71, 72, 74, 76, 77, 80, 81, 83)

midinotes = []
for time, note in enumerate(PLAYSTRING):
    midinotes.append([
        time,
        NOTES[int(note)],
        velocity,
        1
    ])

midinotes[len(PLAYSTRING) - 1][2:3] = velocity//2, 4

midiout.add_track(midinotes)
midiout.save_midi()

if input("Do you want to play the file? [y/N]: ").startswith('y'):
    system(str(MIDIPATH))

print(f"You can find the resulting file in {MIDIPATH}\n"
      "Thank you for listening!")

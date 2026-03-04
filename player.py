"""Accepts a number, bpm and velocity. Produces 'irrational_music.mid' in Desktop or homedir."""

from decimal import Decimal, InvalidOperation, getcontext
from pathlib import Path
from sys import platform

if platform == "win32":
    from os import startfile
else:
    from subprocess import Popen

from miditime.MIDITime import MIDITime

getcontext().prec = 60
FILENAME = "irrational_music.mid"
MIDIPATH = Path.home()
if MIDIPATH.joinpath("Desktop").exists():
    MIDIPATH = MIDIPATH.joinpath("Desktop", FILENAME)
else:
    MIDIPATH = MIDIPATH.joinpath(FILENAME)

try:
    number = abs(
        Decimal(
            input("Enter a positive number that doesn't have an integer square root: ")
        )
    )
except InvalidOperation:
    print("Invalid input. Using 7 as default.")
    number = Decimal(7)

try:
    bpm = min(
        abs(int(input("Enter rhythm (speed) in BPM (beats per minute) 0-600: "))), 600
    )
except ValueError:
    print("Invalid input. Using 300 as default.")
    bpm = 300

try:
    velocity = min(abs(int(input("Enter note velocity (loudness) 0-127: "))), 127)
except ValueError:
    print("Invalid input. Using 63 as default.")
    velocity = 63

PLAYSTRING = str(number.sqrt()).replace(".", "", 1)
midiout = MIDITime(bpm, MIDIPATH)
NOTES = (68, 69, 71, 72, 74, 76, 77, 80, 81, 83)

midinotes = []
for time, note in enumerate(PLAYSTRING):
    midinotes.append([time, NOTES[int(note)], velocity, 1])

midinotes[len(PLAYSTRING) - 1][2:3] = velocity // 2, 4

midiout.add_track(midinotes)
midiout.save_midi()

if input("Do you want to play the file? [y/N]: ").startswith("y"):
    if platform == "win32":
        startfile(MIDIPATH)
    elif platform == "darwin":
        Popen(["open", MIDIPATH])
    else:
        try:
            Popen(["xdg-open", MIDIPATH])
        except OSError:
            print(f"Cannot open file {FILENAME} automatically on this platform.")

print(f"You can find the resulting file as {MIDIPATH}\nThank you for listening!")

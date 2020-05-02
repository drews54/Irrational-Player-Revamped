from decimal import getcontext, Decimal
from random import randint
import musicalbeeps

getcontext().prec = 60

number = Decimal(input('Enter a number in range 0-99: '))
duration = float(input('Enter duration of each note: '))
root = number.sqrt()
playstring = str(root).replace('.', '', 1)

player = musicalbeeps.Player(volume = 0.3, mute_output = True)
noteTuple = ('G4#', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5#', 'A6', 'B6')

for digit in playstring:
    print(digit, end = '')
    player.play_note(noteTuple[int(digit)], duration)

print('\nThanks for playing!')
from random import randint

diceFaces ={1:''' ------- 
|       |
|   •   |
|       |
 -------''',
2:''' ------- 
|•      |
|       |
|      •|
 -------''',
3:''' ------- 
|•      |
|   •   |
|      •|
 -------''',
4:''' ------- 
|•     •|
|       |
|•     •|
 -------''',
5:''' ------- 
|•     •|
|   •   |
|•     •|
 -------''',
6:''' -------   
|•  •  •|  
|       |  
|•  •  •|  
 -------'''}

numberToText = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six'}

def rollDie():
    diceRoll = randint(1,6)
    diceOutput = diceFaces.get(diceRoll, None)
    diceTextOutput = numberToText.get(diceRoll, None)
    print(diceOutput)
    print(f'Rolled :: {diceRoll} ({diceTextOutput})\n')

print('Press Q to Quit, Enter to Roll.')
userIn = None
while userIn != 'q':
    userIn = input('> ').lower()
    if userIn == '':
        rollDie()
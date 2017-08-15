#!/usr/bin/python

import random,time,sys

locs = ['Somerset','Northampton','Southampton','Dulwich','Space','Anglesey']
p1wins = 0
p2wins = 0

def getPlayer(player):
    return raw_input(player + ', Enter your name: ')

list = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            list.append(k)
for i in range (1,10):
    for j in range (10,100):
        list.append(j)
for i in range(100,1000):
    list.append(i)

def guess_number(player):
    while True:
        guess = raw_input('{}: '.format(player))
        try:
            guess = float(guess)
            break
        except:
            print("That's NOT Numberwang!")
    return guess

def numPlayers():
    while True:
        numPlayers = raw_input('How many players? [1/2]: ')
        numPlayers = int(numPlayers)
        if numPlayers == 1 or numPlayers == 2:
            break
    return numPlayers

print('Hello, and welcome to Numberwang, the maths quiz that simply everyone is talking about!')

players = numPlayers()
p1 = getPlayer("Player 1")

if players == 2:
    p2 = getPlayer("Player 2")
elif players == 1:
    p2 = random.choice(['Julie','Simon'])
    while p1 == p2:
        p2 = random.choice(['Julie','Simon'])


print('Our contestants today are {} from {}, and {}{} from {}.'.format(p1,random.choice(locs),p2,random.choice(['',', also']),random.choice(locs)))
time.sleep(1)
print("Okay! Well, if you're ready, let's play Numberwang!")
time.sleep(1)
print('{} to play first'.format(p1))

def scores():
    print("Let's check the scores.")
    time.sleep(0.5)
    print("{} has {} wins, and {} has {} wins".format(p1,p1wins,p2,p2wins))

def isNumberwang():
    if random.choice(range(10)) == 1:
        return True
    else:
        return False

numberwang = False
while numberwang == False:
    if players == 2:
        for player in p1, p2:
            time.sleep(1)
            guess_number(player)
            if isNumberwang() == True:
                winner = player
                break
    elif players == 1:
        guess_number(p1)
        if isNumberwang() == True:
            winner = p1
            break
        time.sleep(0.3)
        p2guess = str(random.choice(list))
        sys.stdout.write(p2)
        sys.stdout.write(': ')
        for char in p2guess:
            time.sleep(0.3)
            sys.stdout.write(char)
            sys.stdout.flush()
        print('\n')
        if isNumberwang() == True:
            winner = p2
            break
        time.sleep(0.5)
print("That's Numberwang!")
if winner == p1:
    p1wins += 1
elif winner == p2:
    p2wins += 1
print("{} is the winner of round one.".format(winner))
time.sleep(0.5)
scores()
time.sleep(0.5)
print("And now it's time for Round Two so let's")
time.sleep(0.5)
print("Rotate the Board!")


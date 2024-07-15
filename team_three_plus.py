#this file shows the syntax used to split a list up into more than 2 random lists

import random

players = ['Martin', 'Craig', 'Sue', 
           'Claire', 'Dave', 'Alice',
           'Sonakshi', 'Harry', 'Jack',
           'Rose', 'Lexi', 'Maria',
           'Thomas', 'James', 'William',
           'Ada', 'Grace', 'Jean', 
           'Marissa', 'Alan']

print('Welcome to Team Allocator!')

while True:

    random.shuffle(players)

    team1 = players[:len(players)//3] #be aware of this syntax for dividing the list and assigning

    print('\nTeam 1 captain: ' + random.choice(team1))

    print('\nTeam 1: ')
    for player in team1:
        print(player)

    team2 = players[len(players)//3:(len(players)//3)*2] #it changes here

    print('\nTeam 2 captain: ' + random.choice(team2))

    print('\nTeam 2: ')
    for player in team2:
        print(player)

    team3 = players[(len(players)//3)*2:] #and here
    print('\nTeam 3 captain: ' + random.choice(team3))
    print('\nTeam 3: ')
    for player in team3:
        print(player)

    response = input('Pick teams again? Type y or n: ')
    if response == 'n':
        break
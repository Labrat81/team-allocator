import random

players = ['Martin', 'Craig', 'Sue', 
           'Claire', 'Dave', 'Alice',
           'Sonakshi', 'Harry', 'Jack',
           'Rose', 'Lexi', 'Maria',
           'Thomas', 'James', 'William',
           'Ada', 'Grace', 'Jean', 
           'Marissa', 'Alan']

print('Welcome to Team/Player Allocator!')

while True:

    random.shuffle(players)

    response = input('Is it a team or individual sport? \
                     \nType team or individual: ')
    
    if response == 'team': 
        team1 = players[:len(players)//2]
        team2 = players[len(players)//2:]

        print('\nTeam 1 captain: ' + random.choice(team1))
        print('\nTeam 1: ')
        for player in team1:
            print(player)

        print('\nTeam 2 captain: ' + random.choice(team2))
        print('\nTeam 2: ')
        for player in team2:
            print(player)

    else:
        print('\nIndividual Matches:')
        for i in range(0, len(players), 2): #range takes 3 parameters, the index range (the list of players) and the increment (2 at a time)
            print(players[i] + ' vs ' + players[i + 1])

            start = random.randrange(i, i+2)
            print(players[start] + ' starts')

    response = input('Pick teams/matches again? Type y or n: ')
    if response == 'n':
        break

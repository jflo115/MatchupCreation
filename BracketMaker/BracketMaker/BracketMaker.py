import random

#Creates Matches based upon user input. These matches have no seeds. Purely 
#random pairings. If not even number, last person to be assigned a match 
#will have a BYE.
#Participants - array of player names to be assigned to match
def createMatches(participants):
    matchup = []
    while len(participants) != 0:
        participant = random.choice(participants)
        print(participant)
        matchup.append(participant)
        participants.remove(participant)
        if len(matchup) == 2:
            print(matchup[0] + " will be facing " + matchup[1])
            matchup.clear()
    if len(matchup) != 0:
        print(matchup[0] + " will hava a bye this round")

#Will create matches with seeded players. Seeded players will be matched
# with a nonseeded player. Whoevre is not left with a match will get a bye.
def createSeedMatches(participants,seeds):
    matchup = []
    while len(participants) != 0 and len(seeds) != 0:
        participant = random.choice(participants)
        print(participant)
        matchup.append(participant)
        participants.remove(participant)
        seed = seeds[0]
        print(seed)
        matchup.append(seed)
        seeds.remove(seed)
        print(matchup[1] + " will be facing " + matchup[0])
        matchup.clear()
    while len(participants) != 0:
       participant = random.choice(participants)
       print(participant)
       matchup.append(participant)
       participants.remove(participant)
       if len(matchup) == 2:
           print(matchup[0] + " will be facing " + matchup[1])
           matchup.clear()
    if len(matchup) != 0:
        print(matchup[0] + " will have a bye this round")
    while len(seeds) != 0:
        seed = seeds[0]
        print(seed + " will have a bye this round")
        seeds.remove(seed)

#Startup Prompt
print("Create your Bracket V1.0")
input("Press Enter to Start a new Bracket: ")

#Promt to ask for amount of total players in bracket and if any seeded
try:
    x = int(input("How many participants will take part in this bracket: "))
except ValueError: x = int(input("Please input a number:"))
tempx = x
participants = []
seeds = []
try:
    y = int(input("How many participants will be seeded in this bracket?\nNote that seeds cannot exceend the number of participants:"))
except ValueError: y = int(input("Please input a number:"))
if y > x:
    print("Number of seeds cannot exceed number of participants!")
    try:
       y = int(input("Input a acceptable number"))
    except ValueError: y = int(input("Please input an actual number"))
tempy = y
tempx = tempx-y
while y > 0:
    name = input("Insert seed name: ")
    seeds.append(name)
    y = y - 1
while tempx > 0:
    name = input("Insert participant name: ")
    participants.append(name)
    tempx = tempx - 1
print("Creating Matches...")
if tempy == 0:
    print("creating a nonseeded bracket")
    createMatches(participants)
else:
    print("created a seeded bracket")
    createSeedMatches(participants,seeds)


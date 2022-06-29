from random import randint

totalRounds = 100 #numero de rodadas a serem feitas seguindo o princípio de Marilyn Vos Savant
wins = 0          #portas acertadas

for i in range (0, totalRounds):
    doors = [0] * 3
    prizeDoor = randint (0,2)
    doors[prizeDoor] = 1

    chosenDoor = randint(0,2)

    discardedDoor = randint(0,2)
    while(discardedDoor == chosenDoor or doors[discardedDoor] == 1):
        discardedDoor = randint(0,2)

    newChosenDoor = randint(0,2)
    while(newChosenDoor == chosenDoor or newChosenDoor == discardedDoor):
        newChosenDoor = randint(0,2)

    if(doors[newChosenDoor] == 1):
        wins = wins + 1
    
print( str(wins/totalRounds*100) + "% de vitórioas em " + str(totalRounds) + " rounds")
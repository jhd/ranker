import sqlite3 as sqlite

def printMenu():
    output = "1) Show database\n"
    output += "2) Add games to a database\n"
    output += "3) Exit"
    print output
    return

#Print out the contents of the database of games
def viewDatabase():
    print "Rank Name        Wins   Losses Win%   Rating \n"
    for i in database:
        print

    return

#Add records of games to the database
def addRecords():
    orderDatabase()
    return

#Order database based on rank
def orderDatabase():
    for i in database:
        ratePlayer(database[i].player)

    return

#Rate a player based in past games
def ratePlayer(player):
    games = []
    return

choice = 0
while choice != 3:
    printMenu()
    choice = int(raw_input("> "))
    if choice == 1:
        viewDatabase()
    elif choice == 2:
        addRecords()

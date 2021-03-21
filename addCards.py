## Add cards to specified deck
import sys

# Obtain deck from cmd line arguments
try:
    deck = sys.argv[1]
except:
    print("Please enter a card deck argument")
    exit()
  
# Open the deck and add front/back side based on input
with open(f'decks/{deck}.txt', "r+") as file:
    front = input("Front side: ")
    back = input("Back side: ")

    # Here, position is initially at the beginning
    # After reading, the position is pushed toward the end
    # Check if card already exists
    for line in file:
        existingFront = line.split("\t")[0]
        print(existingFront)
        if existingFront == front:
            print("Card already exists")
            exit()

    file.write(front + "\t" + back + "\n")
    print("Card added")

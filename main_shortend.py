import random as rd
while True:
    computer = rd.choice([-1, 0, 1])
    youstr = input("Enter your choice: ")
    youDict = {"s" : 1, "w" : -1, "g" : 0}
    reverseDict={1 : "Snake", -1 : "Water", 0 : "Gun"}
    you = youDict[youstr] #Rturns the corresponding value of the key and stores in the variable
    print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
    if computer == you:
        print("It's a Draw!")
    else: 
        if (computer - you)==-1 or (computer - you)==2:
            print("You Loose!")
        elif (computer - you)==1 or (computer - you)==-2:
            print("You Win!")
        else: 
            print("Something went wrong.")
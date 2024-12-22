import random as rd
# 1 for snake
# -1 for water
# 0 for gun
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
        if computer==0 and you==1:
            print("You Loose!")
        elif computer==0 and you==-1:
            print("You Win!")
        elif computer==1 and you==-1:
            print("You Loose!")
        elif computer==1 and you==0:
            print("You Win!")
        elif computer==-1 and you==1:
            print("You Win!")
        elif computer==-1 and you==0:
            print("You Loose!")
        else: 
            print("Something went wrong.")
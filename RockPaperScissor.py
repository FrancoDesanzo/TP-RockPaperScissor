import random

print("Welcome to Rock Paper Scissors")
print("-------------------------------")
print("1) Rock 🗻")
print("2) Paper 🧾")
print("3) Scissors ✂️")
print("-------------------------------")
print("")
elec = 99

#this is a flag to keep the program working until i select 0
while elec != 0:
    resp = random.randint(1, 3) #Here we pick a random number between 1-3 i put it in the while loop to renew the number
    elec = int(input("Select an option (0 to exit): ")) #We choose our option
    print("")
    
    #Here we define every case posible
    if (elec == 1) and (resp == 1):
        print("You Choose Rock 🗻")
        print("🤖 Robot Choose Rock 🗻")
        print("")
        print("It's a TIE !!!")
    elif (elec == 2) and (resp == 1):
        print("You Choose Paper 🧾")
        print("🤖 Robot Choose Rock 🗻")
        print("")
        print("You WIN ✔️ !!!")
    elif (elec == 3) and (resp == 1):
        print("You Choose Scissors ✂️")
        print("🤖 Robot Choose Rock 🗻")
        print("")
        print("You LOSE ❌️ !!!")
    elif (elec == 1) and (resp == 2):
        print("You Choose Rock 🗻")
        print("🤖 Robot Choose Paper 🧾")
        print("")
        print("You LOSE ❌️ !!!")
    elif (elec == 2) and (resp == 2):
        print("You Choose Paper 🧾")
        print("🤖 Robot Choose Paper 🧾")
        print("")
        print("It's a TIE !!!")
    elif (elec == 3) and (resp == 2):
        print("You Choose Scissors ✂️")
        print("🤖 Robot Choose Paper 🧾")
        print("")
        print("You WIN ✔️ !!!")
    elif (elec == 1) and (resp == 3):
        print("You Choose Rock 🗻")
        print("🤖 Robot Choose Scissors ✂️")
        print("")
        print("You WIN ✔️ !!!")
    elif (elec == 2) and (resp == 3):
        print("You Choose Paper 🧾")
        print("🤖 Robot Choose Scissors ✂️")
        print("")
        print("You LOSE ❌️ !!!")
    elif (elec == 3) and (resp == 3):
        print("You Choose Scissors ✂️")
        print("🤖 Robot Choose Scissors ✂️")
        print("")
        print("It's a TIE !!!")
    #Option to EXIT
    elif elec == 0:
        print("¡Thanks for playing! 👋")
        


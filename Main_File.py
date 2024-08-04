Locations = ["Victim's house" , "Town Hall" , "Library" , "Cafe" ] #order needs to be fixed
Inventory = []

Name = str(input("Enter your name: "))
print("Welcome to Maplewood!")
print (print ("Welcome to Maplewood, Detective "Name "You've been called to investigate the murder of Mr. John Hastings, a well-respected townsperson. Your goal is to gather clues, interview suspects, and find the murderer. You have four key locations to investigate: Town Hall, Library, Café, and the Victim’s House") #game briefing (Details, game handles including inventory 
print("Press Enter to begin")
input()
print (Locations)
print("Choose a location to investigate")
loc1 = str(input("Enter the location name: "))
if loc1.lower() == "victim's house" or loc1.lower() == "victims house":
    print ("VICTIM'S HOUSE")
    print("Choose an action:")
    act1 = int(input("1 = Interview suspect \n2 = Collect clues \n "))
    while (act1):
        if(act1 == 1):
            print ("HI") #character dialogue
            act2 = int(input("Choose next action \n2 = Collect clues \n"))
            while (act2 != 2):
                print ("invalid entry, try again")
                act2 = int(input("Choose next action \n2 = Collect clues \n"))
            print("clue details")
            Inventory.append ("reciept")
            break
        elif(act1 == 2):
            print ("Clue details") #clue details
            Inventory.append ("reciept") #?
            act2 = (input("Choose next action \n 1 = Interview suspect \n i = inventory"))
            while (act2):
                if (act2 == 'i'):
                    print(Inventory)
                    act2 = (input("Choose next action \n 1 = Interview suspect \n i = inventory")) #soha    let come 
                    continue 
                elif(act2 == '1'):
                    print ('Dialogue')
                    break
                else:
                    print ("invalid entry, try again")
                    break
            break
        else:
            print ("invalid entry, try again")
            act1 = int(input("1 = Interview suspect \n 2 = Collect clues"))

print("Outside loop")
    

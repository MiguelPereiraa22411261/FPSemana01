#chinfo = []

#while (True):
 #   print("Input name: " )
 #     name = input()
  #  print("Input health points: ")
   # hp = input()
    #print("Input defense stat: ")
    #defstat = input()
    #chinfoadd = [[name, (hp, defstat)]]
    #chinfo += chinfoadd
    #print("Do you wish to add another character? (yes/no) ")
    #command = input()
    #if command == "no":
    #    chinfoadd = [[name, (hp, defstat)]]
    #    break
    #elif command == "yes":
    #    chinfoadd = [[name, (hp, defstat)]]
    #else:
    #    while command != "yes" and command != "no":
    #        print("I don't recognise that response...")
    #        print("Do you wish to add another character? (yes/no) ")
    #        command = input()
#print(chinfo)

chname1 = str(input("Input the name of the first character: "))
chhp1 = int(input("Input the health points of the first character: "))
chlevel1 = int(input("Input the level of the first character: "))
print("\nVery well...\n")
chname2 = str(input("Input the name of the second character: "))
chhp2 = int(input("Input the health points of the second character: "))
chlevel2 = int(input("Input the level of the second character: "))
print("\nI see...\n")
chname3 = str(input("Input the name of the third character: "))
chhp3 = int(input("Input the health points of the third character: "))
chlevel3 = int(input("Input the level of the third character: "))
print("\nNo more, that's enough...\n")

chcomp = [
    [chname1, (chhp1, chlevel1)],
    [chname2, (chhp2, chlevel2)],
    [chname3, (chhp3, chlevel3)]
]

print("This is your first creation:", "\nName: ", chname1, "\nHealth points: ", chhp1, "\nLevel: ", chlevel1)
print("\nThis is your second creation:", "\nName: ", chname2, "\nHealth points: ", chhp2, "\nLevel: ", chlevel2)
print("\nThis is your third creation:", "\nName: ", chname3, "\nHealth points: ", chhp3, "\nLevel: ", chlevel3)
print("\nHere's a more compact list...\n", chcomp)

if chlevel1 > chlevel2 and chlevel1 > chlevel3:
        print("\nThe character with the biggest level is ", chname1)
        if chlevel2 > chlevel3:
            print(" then ", chname2)
            print(" and then ", chname3)
        else:
         print(" then ", chname3)
         print(" and then ", chname2)
elif chlevel2 > chlevel1 and chlevel2 > chlevel3:
        print("\nThe character with the biggest level is ", chname2)
        if chlevel1 > chlevel3:
            print(" then ", chname1)
            print(" and then ", chname3)
        else:
         print(" then ", chname3)
         print(" and then ", chname1)
elif chlevel3 > chlevel2 and chlevel3 > chlevel1:
        print("\nThe character with the biggest level is ", chname3)
        if chlevel2 > chlevel1:
            print("Then ", chname2)
            print("And then ", chname1)
        else:
         print("Then ", chname1)
         print("And then ", chname2)
         
input("My work here is now done, you can now leave ")
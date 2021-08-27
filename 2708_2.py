print("Sinovac >> SV")
print("Astrazeneca >> AZ")
print("Sinopharm >> SP")
print("Not vaccinated >> NONE")
print("Have been infected before >> YES")
print("Never been infected before >> NO")

x = input("First dose: ")
y = input("Second dose: ")
z = input("Third dose: ")
Q = input("Have you ever been infected before?: ")

if(x == "SV" and y == "SV" and z == "NONE"):
    print("You get 1 pfizer as a booster")
elif (x == "SP" and y == "SP" and z == "NONE"):
    print("You get 1 pfizer as a booster")
elif (x == "SV" and y == "NONE" and z == "NONE"):
    print("You get 1 pfizer as a booster")
elif (x == "AZ" and y == "NONE" and z == "NONE"):
    print("You get 1 pfizer as a booster")
elif (x == "SP" and y == "NONE" and z == "NONE"):
    print("You get 1 pfizer as a booster")
elif (x == "NONE" and y == "NONE" and z == "NONE" and Q =="NO"):
    print("You get 1 pfizer as a booster")
elif (x == "NONE" and y == "NONE" and z == "NONE" and Q == "YES"):
    print("You get 1 pfizer as a booster")
elif (x == "SV" and y == "SV" and z == "AZ"):
    print("You don't get pfizer as a booster")
elif (x == "SV" and y == "AZ" and z == "NONE"):
    print("You don't get pfizer as a booster")
elif (x == "AZ" and y == "AZ" and z == "NONE"):
    print("You don't get pfizer as a booster")
else:
    print("ERROR")

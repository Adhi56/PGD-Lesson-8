number1=(input("Write a number for a set, don't do the same twice"))
number2=(input("Write a number for a set, don't do the same twice"))
number3=(input("Write a number for a set, don't do the same twice"))

setA= set([number1,number2,number3])
print("SetA = ", setA)

number4=(input("Write a number for another set, don't do the same twice"))
number5=(input("Write a number for another set, don't do the same twice"))
number6=(input("Write a number for another set, don't do the same twice"))

setB= set([number4,number5,number6])
print("SetB= ", setB)

operation=str(input("Choose an operation to do to SetA and SetB: \n1) Add \n2) Subtract \n3) Union \n4) Intersection \n5) Difference \n6) Symmetric Difference"))

if operation == "Add":
    set_add=str(input("Which Set would you like to add to?"))
    if set_add == "SetA":
        A_ADD=int(input("How much do you want to add?"))
        print("Set A + ", A_ADD , "=" , setA.add(A_ADD) )
    elif set_add == "SetB":
        B_ADD=int(input("How much do you want to add"))
        print("Set B + ", B_ADD , "=" , setB.add(B_ADD) )
    else:
        print("Invalid Set.")
elif operation == "Subtract":
    set_subtract=str(input("Which Set would you like to Subtract from?"))
    if set_subtract == "SetA":
        A_SUBTRACT=int(input("How much would you like to subtract."))
        print("Set A +" , A_SUBTRACT , "=" , setA.discard(A_SUBTRACT))
    elif set_subtract == "SetB":
        B_SUBTRACT=int(input("How much would you like to subtract"))
        print("Set B"+ B_SUBTRACT , "=" , setB.discard(B_SUBTRACT))
elif operation == "Union":
    set_union=str(input("Which Set would you like to do a union from?"))
    if set_union == "SetA":
        print("SetB | SetA =", setB|setA)
    elif set_union  == "SetB":
        print("SetA | Set B =", setA|setB)
elif operation == "Intersection":
    print(setA & setB)
elif operation == "Difference":
    set_difference=str(input("Which set would you want to do the difference from?"))
    if set_difference == "SetA":
        print("The Difference between A and B is ", setA-setB)
    if set_difference == "SetB":
        print("The Difference between B and A is", setB-setA)
elif operation == "Symmetrical Difference":
    set_symdifference=str(input("Which set would you want to do the symmentrical difference from?"))
    if set_symdifference == "SetA":
        print("The Symmetrical Difference between A and B is ", setA^setB)
    if set_symdifference == "SetB":
        print("The Symmentrical Difference between B and A is", setB^setA)
else:
    print("Invalid Operations!")



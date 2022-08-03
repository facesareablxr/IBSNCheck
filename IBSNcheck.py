multiList = []
valid = False

def menuOptions():
    print("""Would you like to check an IBSN-10 or IBSN-13 number?
    1 - IBSN-10
    2 - IBSN-13
    3 - QUIT""")
    inputVal = input()
    if inputVal.isdigit() != True:
        print("Invalid, try again")
        menuOptions()
    elif inputVal == "1":
        print("OPTION 1")
        inputNumber(10)
    elif inputVal == "2":
        print("OPTION 2")
        inputNumber(13)
    elif inputVal == "3":
        print("OPTION 3")
        quit()
    else:
        print("Invalid, try again")
        menuOptions()

def inputNumber(rangeV: int):
    IBSN = input("Enter your " + str(rangeV) + " digit IBSN number: ")
    if IBSN.isdigit() != False:
       
        if len(IBSN) == rangeV:
              if rangeV == 10:
                IBSN10(rangeV, IBSN)
              else:
                IBSN13(rangeV, IBSN)
        else:
            print("This is not a valid IBSN number, try again!")
            inputNumber(rangeV)
    else:
        print("Invalid input")
        inputNumber(rangeV)
       
def IBSN10(rangeV: int, IBSN: str):
    ibsnList = [int(a) for a in str(IBSN)]
    i= 1
    while i<=rangeV:
       x = 0
       for x in range(len(ibsnList)):
           multiList.append(ibsnList[x] * i)
           i +=1
           x +=1
    sumOfMod = sum(multiList[0:len(multiList)])
    sumOfMod = sumOfMod % 11
    if sumOfMod != 0:
        print("This is not a valid IBSN-10 number")
    else:
        print("This is a valid IBSN-10 number")
       

def IBSN13(rangeV: int, IBSN: str):
    ibsnList = [int(a) for a in str(IBSN)]
    i = 0
    while i < 12:
        if i % 2 == 0:
            multiList.append(ibsnList[i])
            i +=1
        else:
            multiList.append(ibsnList[i] * 3)
            i +=1
    sumForMod = sum(multiList[0:len(multiList)])
    checkVal = 10 - (sumForMod % 10)
    if checkVal == ibsnList[12]:
        print("This is a valid IBSN-13 number")
    else:
        print("This is not a valid IBSN-13 number")
           
menuOptions()



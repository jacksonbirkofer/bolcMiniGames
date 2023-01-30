#19jan23 fucking around file; jackson birkofer

#method under main func
def printFunc():
    numberLoops = input("How many numbers would you like to print: ")
    numberPrint = input("What would you like to print: ")
    for x in range(int(numberLoops)):
        print(numberPrint)

#method under main func
def simpleMath():
    var1 = input("Enter a number:")
    var2 = input("Enter another number:")
    output = 0
    print("+, -, *, %")
    operation = input("What simple math operation would you like to do: ")
    if(operation == "+"):
        output  = float(var1) + float(var2)
        print(output)
    elif(operation == "-"):
        output  = float(var1) - float(var2)
        print(output)
    elif(operation == "*"):
        output  = float(var1) * float(var2)
        print(output)
    elif(operation == "%"):
        output  = float(var1) % float(var2)
        print(output)
    else:
        print("you failed")

#tictactoe
def ticTacToe():
    #             0   1   2   3   4   5   6   7   8  
    row1 = ["_0","_1","_2"]
    row2 = ["_3","_4","_5"]
    row3 = ["_6","_7","_8"]
   
    symbolLoop = 1
    while(symbolLoop == 1):
        playerSymbol = input("X or O: ")
        if(playerSymbol == "X" or playerSymbol == "0"):
            print("You have chosen " + str(playerSymbol))
            symbolLoop = 0
        else:
            print("Please enter an 'X' or an 'O'")

    tempCtr = 0
    tacGameLoop = 1
    while(tacGameLoop == 1):
        ctr = 0
        
        #this is being printed wrong
        for x in row1:
            print(row1[ctr] + row2[ctr] + row3[ctr])
            ctr = ctr+1 
        placement = input("Where would you like to place your " + str(playerSymbol))
        print("012")
        print("345")
        print("678")

        #this is not updating the array correctly
        if(placement == 0 or placement == 1 or placement == 2):
            row1.pop(placement)
            row1.insert(placement)
        elif(placement == 3 or placement == 4 or placement == 5):
            row2.pop(placement)
            row2.insert(placement)
        elif(placement == 6 or placement == 7 or placement == 8):
            row3.pop(placement)
            row3.insert(placement)

        tempCtr= tempCtr + 1
        if(tempCtr == 2):
            tacGameLoop = 0
        
#neptune's prided calculator
def neptuneCalc():
    nepLoop = 1
    while(nepLoop == 1):
        print("1: Manufacuring Calculator ")
        print("2: Economy Calculator Calculator ")
        print("3: Experimentation Calculator ")
        print("4: Scanning Calculator ")
        print("5: Hyperspace Calculator ")
        print("0: Exit")
        nepInput = input("Choose an option: ")
        
        if(nepInput == "1"):
           manLoop = 1
           while(manLoop == 1):
                x = input("What is your manufacturing level: ")
                y = input("What is the industry at your star: ")
                manPerHour = y*(x+5)
                print("Your star will produce " + manPerHour + " per hour.")
                again = input("Type q if you want to quit, if not press enter.")
                if(again == "q"):
                    manLoop = 0
        elif(nepInput == "2"):
            printFunc() 
        elif(nepInput == "3"):
            ticTacToe()
        elif(nepInput == "4"):
            neptuneCalc()
        else:
            nepLoop = 0





#main options menu
def main():
    mainLoop = 1
    timer = 1
    while(mainLoop == 1):
        print("1: Simple math")
        print("2: Fun with printing")
        print("3: TicTacToe")
        print("4: Neptune's Pride Calculator")
        print("0: Close program") 
        userInput = input("What do you want to do?: ") 
        
        if(userInput == "1"):
           simpleMath()
        elif(userInput == "2"):
            printFunc() 
        elif(userInput == "3"):
            ticTacToe()
        elif(userInput == "4"):
            neptuneCalc()
        else:
            mainLoop = 0

#run the main function
main()

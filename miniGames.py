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
    row1 = ["X","_","_"]
    row2 = ["_","O","_"]
    row3 = ["X","X","X"]
   
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
        for x in row1:
            print(row1[ctr] + row2[ctr] + row3[ctr])
            ctr = ctr+1 
        placement = input("Where would you like to place your " + str(playerSymbol))
        print("012")
        print("345")
        print("678")

        if(placement == 0 or placement == 1 or placement == 2):
            row1[placement] = playerSymbol
        elif(placement == 3 or placement == 4 or placement == 5):
            row2[placement] = playerSymbol
        elif(placement == 6 or placement == 7 or placement == 8):
            row3[placement] = playerSymbol

        tacGameLoop = 0
        



#main options menu
def main():
    mainLoop = 1
    timer = 1
    while(mainLoop == 1):
        print("1: Simple math")
        print("2: Fun with printing")
        print("3: TicTacToe")
        print("0: Close program") 
        userInput = input("What do you want to do?: ") 
        
        if(userInput == "1"):
           simpleMath()
        elif(userInput == "2"):
            printFunc() 
        elif(userInput == "3"):
            ticTacToe()
        else:
            mainLoop = 0
        print(" ")

#run the main function
main()

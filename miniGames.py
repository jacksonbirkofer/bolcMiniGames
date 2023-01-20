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
    output
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

#main options menu
def main():
    mainLoop = 1
    timer = 1
    while(mainLoop == 1):
        print("1: Simple math")
        print("2: Fun with printing")
        print("0: Close program") 
        userInput = input("What do you want to do?: ") 
        
        if(userInput == "1"):
           simpleMath()
        elif(userInput == "2"):
            printFunc() 
        else:
            mainLoop = 0
        print(" ")
main()

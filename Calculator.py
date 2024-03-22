# Addition method
def addition(num1, num2):
    res = num1 + num2
    
    return res
   
# Multiplication Method 
def multiplication(num1, num2):
    res = num1*num2
    
    return res

# Subtraction Method
def subtraction(num1, num2):
    res = num1 - num2
    
    return res

# Division method
def division(num1, num2):
    if num2 == 0:
        return "ZeroDivisionError is Occured !"
    else:
        res = num1 / num2
        return res

def calculator():
    while True:
        print("Select Options from Menu:")
        print("\na. Addition")
        print("b. Subtraction")
        print("c. Multiplication")
        print("d. Division")
        print("e. Quit")
        
        option = input("Select your option from Menu : ")
        
        if option in ('a', 'b', 'c', 'd'):
            num1 = input("Enter num1  to perform operation : ")
            num2 = input('Enter num2 to perform operations : ')
            
            if num1.isdigit() and num2.isdigit():
                num1 = float(num1)
                num2 = float(num2)
                
                if option == 'a':
                    print("Addition result : ", addition(num1, num2))
                elif option == 'b':
                    print("Subtraction result : ", subtraction(num1, num2))
                elif option == 'c':
                    print("Multiplication result : ", multiplication(num1, num2))
                elif option == 'd':
                    print("Division result : ", division(num1, num2))
            else:
                print('Please Provide int or float values to the inputs!!')
                
        elif option == 'e':
            print("We are Exiting from calculator!")
            break
        else:
            print("Please select options from 1 to 5")

calculator()
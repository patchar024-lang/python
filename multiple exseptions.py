try:
    num1 , num2 = eval(input("Enter two numbers, seperated by a coma: "))
    result = num1 / num2  
    print("result is" , result)

except ZeroDivisionError:
    print("Division by zero is error ! !")

except SyntaxError:
     print("Comma is missing. Enter a numbers seporarted by a comma like this 1,2")


except:
    print("Wrong input")

else:
    print("No exceptions")
finally:
    print("This will exicute no matter what")


    
try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)

except ValueError as ex:
    print("Exception:", ex)

try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma :"))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing.Enter numbers seperated by comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")

valid = False
while not valid:
  
  try:
      n=int(input("Enter a number: "))
      while n%2==0:

        print("bye")
      valid = True
  except ValueError:
    print("Invalid")
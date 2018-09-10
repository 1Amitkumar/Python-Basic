try:
    n1, n2 = eval(input("enter two numbers, separated by a comma : "))
    result = n1 / n2
    print("result is", result)

except ZeroDivisionError:
    print("division by zero error !!")

except SyntaxError:
    print("comma is missing. enter numbers separated by comma like this 1, 2")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("this will execute no matter what")

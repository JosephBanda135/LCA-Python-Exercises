x = 10
y = 3

x += 3
y *= 2
result = x/y
print(result)
#question 2
a = 8
b = 4
c = 6

condition1 = a > b 
condition2 = a % b == 0
condition3 = c <= a
final_condition = condition1 or ( condition2 and condition3)

print(final_condition)

score = int(input("Enter your test score(0-100): "))

if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 60:
  grade = "D"
else:
  grade ="F" 

  print("Your grade is:",grade) 


num1 = input("10:")
num2 = input("4:")
operation =input("+:") 

if operation == "+":
    result = num1 + num2
elif operation == "-":    
  result = num1 - num2
elif operation == "*": 
  result = num1 * num2
elif operation == "/":
  if num2 != 0:
    result = num1 / num2
  else:
    result = "Error: Division by zero"   
else:
  result = "Invalid operation"

  print("Result:", result)

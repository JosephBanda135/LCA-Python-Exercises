def greet():
  greeting = "Hello , world!"
  print(greeting)

greet()



#question 2
def personalized_greeting(name):
  print("What's up "+ name )


personalized_greeting('Thabo')



#Question 3
def square(number):
  return number * number 

print(square(5))



#Question 4
def rectangle_area(length, width):
  return length * width

print(rectangle_area(4,5))



#Question 5
def apply_operation(function, number):
  return function(number)



def double(number):
  return number + number 


print(apply_operation(double, 7))

print(apply_operation(square, 3))




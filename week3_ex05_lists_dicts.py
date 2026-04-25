#Question 1

fruits = ['apple', "banana", "orange", "grapes", "peach"] # create list 

fruits.append("cherry")#add fruit to the end 

fruits.insert(0,"blueberry") #insert fruit at the beginning 

fruits.remove("orange") #remove a fruit
print(fruits)

#Question 2
 
numbers = [ 1, 2, 3, 4, 5] #create list
 
for number in numbers:  #Create list with number squared
  print(number * number)


sum = 0 
for number in numbers: #find the sum
  sum = sum + number 
  print(sum)

  average = sum / len(numbers) #find the average 
  print(average)


#Question 3
 
countries = {
  "South Africa": "Pretoria",
  "Japan": "Tokyo",
  "France" : "Paris"

} #Dic...of countries and capitals

countries["Germany"] = "Berlin"  #Add new country and capital

countries["South Africa"] = "Cape town" #Update capital

countries.pop("France") #Remove a country

print(countries)

 
#Question 4 
fruits = {
  "apple": "red",
  "banana": "yellow",
  "grape": "purple"

}

print(fruits.keys())

print(fruits.values())

for fruit in fruits:
  print(fruit, fruits[fruit])


  if "apple" in fruits:
   print("apple is", fruits["apple"])



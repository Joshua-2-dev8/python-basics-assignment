
##Variables and Data Types
# String Variable
Name = "Ojarotade Joshua"
print (f"Name:{Name},Type:{type(Name)}")

# Integer
Age = 18
print(f"Age:{Age}, Type: {type(Age)} ")

# float
height = 1.75
print(f"Height: {height}, Type: {type(height)}")

# Boolean 
is_eligible = True
print(f"is eligible: {is_eligible}, Type: {type(is_eligible)}")


#list
Cars = ["Benz","Lexus","Kia","Brabus"]
print(f"Cars: {Cars}, Type:{type(Cars)}")

##User Input & Conditional Statements
Age= int(input("kindly state your age  "))
if Age >= 18:
  print("You are eligible to vote")
else :
  print("You are not eligible to vote")

  # Loops
## Write a for loop that prints numbers from 1 to 10

for numbers in range(1, 11):
  print(numbers)

### Write a while loop that prints even numbers between 1 and 20

i = 2
while i<20:
  print(i)
  i+=2

 ## Task 4: Mini Challenge

fruits = ('ORANGE', 'APPLE', 'BANANA', 'GRAPE')
for fruits in fruits:
  if fruits == "BANANA":
   continue
  print(fruits)





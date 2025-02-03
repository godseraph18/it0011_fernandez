fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

fullname = fname + " " + lname
greeting = "Greeting Message: Hello, {0}! Welcome. You are {1} years old."

print("Full name: ", fname + " " + lname)
print("Sliced name: ", fullname[0:3])
print(greeting.format(fullname[0:3], age)) 



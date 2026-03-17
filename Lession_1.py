# integers are immutable (cannot be changed)
# Variable Initialization 
a = 10 
b = a
print(a,b)
a = 20
print(a,b)

age = 20
user_name = "Ali"
student1 = "Sara"
_total = 100
print(age,user_name,student1,_total)

print(f"My name is {user_name} and I am {age} years old")

x = y = z =10
print(x,y,z)

# List is mutable (can be changed)
names = ["Sara","Ali","John"]
names.insert(0,"Amna")
names.sort()
print(names)

# Dictionary is mutable (can be changed)
person = {"Student1":{"name":"Sara","age":20}, "Student2":{"name":"Ali","age":21}}
# print(person.keys())
# print(person.values())
# print(person.items())

for key , student in person.items():
    print(f"{key} is {student['name']} and is {student['age']} years old")

# Conditional Statements
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")

# The if Statement
# if-elif-else (Multiple Conditions)
# Comparison Operators
# ==	equal to
# !=	not equal
# >	greater than
# <	less than
# >=	greater or equal
# <=	less or equal

# Logical Operators
# and	both conditions must be True
# or	at least one True
# not	reverses condition

age = 22
citizen = True

if age >= 18 or citizen:
    print("Eligible to vote")

# Ternary Conditional Operator
age = 22
status = "Adult" if age >= 18 else "Minor"
print(status)


# Lets Move Towards Loops
for i in range(0,5,2):
    print(i)

student = {
    "name": "Ali",
    "age": 21
}


for key, value in student.items():
    print(key, value)

for i in range(3):
    print(i)
else:
    print("Loop completed")



# Lets move towards functions
def add(*args):
    a = 0
    for arg in args:
        a += arg
    return a
result = add(5,10,15)
print(result)

def printdict(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

printdict(name="Sara", age=20, city="Karachi")

def example(argc , *args, **kwargs):
    print(f"argc: {argc}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

example(10, 20, 30, name="Sara", age=20)


# Lambda Functions
fictorial = lambda x: 1 if x ==0 else x * fictorial(x-1)
print(fictorial(5))

numbers = [1,2,3,4,5]
squares = list(map(lambda x:x*x , numbers))
print(squares)

def add(a: int, b: int) -> int:
    return a + b

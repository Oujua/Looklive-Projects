#multi variable assignment
x, y, z = 1, 2, 3
# Capital variables are considered constants, UpperCamelCase is used for classes, and double
# underscore is used for things not meant to be touched

# ****** VARIABLES DO NOT NEED NAME PREFACES ******

yes = True #bool
x = 0 #int
name = "Mattiece" #string
a = [1,2,3] #arrays

print (yes)
print(x)
print(name)
print(a[1])

#Unlike C++, python code does not follow a static definition, meaning you can switch
#types without making a new variable

y = True
print(y)
y = "Hello"
print(y)
y = 22/7
print(y)

#newline
message = "Hello. \n I am Mattiece."

#double quotes
yeet = "Yeet \"yeet\""
print(yeet)

#concatenation
story_time = "There once was a man "
story_time += "from gilnaeas."
print(story_time)

#working with numbers in a string (interpolation)
answer = f"Welcome {name}, your x value is {x}."
print(answer)

#converting data types
num = 99.98812
numf = 99
print (round(num)) #rounds to the nearest number
print (round(num, 2)) #rounds to 2 decimal points
print (int(num))
print (float(numf))

#how to get input
ans = input("What is your name? ")
print (f"hello,{ans}")

if ans == "Matt":
    print("Hello Mattiece.")
elif ans == "Kevin":
    print("Go away Kevin.")
else:
    print("Who are you?!")

# and, or, not

if x and y:
    print("Yeah")
if x or y:
    print("Oh yeah")
if not x:
    print("Oh yeah yeah")

#is checks memory, not value

b = [1,2,3]
c = [1,2,3]
d = c
check1 = (b == c)
check2 = (b is c)
check3 = (c is d)
print(check1)
print(check2)
print(check3)

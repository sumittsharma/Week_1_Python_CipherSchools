# Question 1
print("this is \\\ double backslash")
# Question 2
print("/\\/\\/\\/\\/\\")
# Question 3
print("he is    awesome")
# Question 4
print(" \\\" \\n \\t \\\' ")
first_name = "Harshit"
last_name = "Vashishta"
full_name = first_name+""+last_name
#print(full_name)
#print(first_name + 3)
#print(first_name+"3")
#print(first_name+str(3))
#print(first_name*3)
# user input
# input function
name = input("type your name")
print("hello"+name)
#string
age=input("what is your age?")
#24 , "24"
print("your age is "+age)
("number_one = int(input("enter first number")) #4
number_two = int(input("enter second number")) #4
total = number_one+number_two #8
print("total is" + str(total))
# total = "4"+"4"=44

number_1=str(4)
number_2=float("44")
number_3=int("33")
print(number_2+number_3) #float
#Lecture 23 - More about variables in python
name , age = "harshit" , 24
print("hello"+name+"your age is"+age)
x=y=z=1
print(x+y+z)

#Lecture 24 - Two or more input in one line in python
name = input("enter your name: ")
age = input("enter your age: ")
name , age = input("enter your name and age").split()
print(name)
print(age)
#Lecture 25 - String formatting
#nomral way 
name = "harshit"
age = 24
print("hello"+name+"your age is"+str(age)) #ugly syntax
# using string formatting
print("hello {} your age is {}".format(name,age))
#3.6
print(f"hello {name} your age is {age}") #clean
number_1 = int(input("enter number 1: "))
num_2 = int(input("enter number 2: "))
num_3 = int(input("enter number 3: "))
print(f"{number_1+num_2+num_3 / 3}")
# Lecture 28 and 29 and 30 - String indexing and string slicing and step argument
language = "Python"
print(language[2])

# Lecture 29
lang = "Python"
print(lang[0:2])

# Lecture 30
print("Sandarbh"[0:5:2]) 
print("Sandarbh"[5::-1])
print("Sandarbh"[-1::-1])
# Lecture 31 - Chapter 2 exercise 2
username = input("enter your name = ")
reverse = username[::-1]
print(f"{reverse}")
# Lecture 33 and 36 and 37 and 38 and 39 - String methods till strings are mutable
name = "SaNdaRbh BaJPai"
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.count("a"))

# Lecture 36
name , character = input("enter name and a character comma separated: ").split(",")
print(f"length of your name is : {len(name)}")
print(f"character count : {name.strip().lower().count(character.strip().lower())}")

# Lecture 37
string="She is beautiful and she is a good dancer"
print(string.replace(" ","-"))
print(string.find("is"))
#find positon of is other than 1st
is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1 + 1) 
print(is_pos2)

# Lecture 38
name = "Sandarbh"
print(name.center(12, "*"))

name = input("enter your name : ")
print(name.center(len(name)+8, "*"))

# Lecture 39
string="string"
print(string.replace('t','T'))
print(string)
# Lecture 34 - Chapter 2 exercise 3
name , character = input("enter name and a character comma separated: ").split(",")
print(f"length of your name is : {len(name)}")
print(f"character count : {name.lower().count(character.lower())}")
# Lecture 40 - Assignment operatiors
name = "harsh"
name = name + "it" #name  += "it"
print(name)
age=20 
age += 1
print(age)
# Lecture 42 and 43 and 44 - If statement , pass statement , if-else statement

age = int(input())
if age>=14:
    print("you are above 14")



# Lecture 43
x=18
if x>18:
    pass


# Lecture 44
age = int(input())
if age>=14:
    print("you are above 14")
else:
    print("not eligible")
# Lecture 45 - Chapter 3 Exercise 1 (NUMBER GUESSING GAME)
winning_number = 17
input_number = int(input("Enter a number: "))
if input_number==winning_number:
    print("YOU WIN!!!")
else:
    if input_number>winnig_number:
        print("Too High")
    else:
        print("Too Low")
# Lecture 47 - And or operator in python
name = 'abc'
age = 18
if name == 'abc' and age==18:
    print("condition true")
else:
    print("condition false")

# Or operatoer (if one is true then output is true)
if name == 'abc' or age==18:
    print("condition true")
else:
    print("condition false")
# Lecture 48 - Chapter 3 Exercise 2 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if name[0]=='a' or name[0]=='A' and int(age)>10:
    print("you can watch coco movie")
else:
    print("sorry , you cannot watch coco")
# Lecture 50 and 51 and 52 - If ElifElse statement and keywords and empty or not
age = int(input("Please input your age: "))
if age==0:
    print("You cannot watch")

if 0<age<=3:
    print("Ticket price : Free")
elif 3<age<=10:
    print("Ticket Price; 150")
elif 10<age<=600:
    print("Ticket Price : 250")
else:
    print("Ticket Price : 200")

# Lecture 51
name = "Sandarbh"
if 'a' in name:
    print("a is present in name")
else:
    print("not present")

# Lecture 52
name = input("enter your name: ")
if name: 
    print(f"your name is {name}")
else:
    print("you did not type anything")
# LEcture 53 and 54 - While loop and sum of numbers
#print("hello world") #10 times
i=1
while i<=10:
    print("Hello world")
    i = i+1

# Lecture 54
total = 0
i = 1
while i<=10:
    total = total + i
    i = i+ 1
print(total)
# Lecture 55 - Chapter three exercise 3
n = int(input("enter a number: "))
sum = 0 
i = 1
while i<=n:
    sum += i
    i += 1
print(sum)    
# Lecture 57 - Chapter 3 exercise 4 
num_1= input("Enter more than one digit number: ")
sum_of_digits = 0
i = 0
while i<len(num_1):
    sum_of_digits += int(num_1[i])
    i +=1
print(sum_of_digits)
# Lecture 58 - chapter 3 exercise 5
name = input("Enter your name: ")
temp = ""
i = 0 
while i<len(name):
    if name[i] not in temp:
        temp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i +=1

# Lecture 61 and 62 : Infinite loop and For loop
i = 1
while i <=10:
    print("Hello world")
    i += 1

#Lecture 62 
for i in range(1,11):
    print(f"Hello world : {i}")
    print("this is line \n")
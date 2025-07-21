print("Hello, World!")
 ##process to run 1.save the file with filename.py ,2.now run the file using f5 or run

##2.rule-1:cannot contain special characters like @,-,$
##eg: correct : price_value
price_value=350
print(price_value)
## incorrect: price-value,$price --> - and $ are invalid in variable names
price-value=350
print(price-value)
##rule-2:don't spaces in variable names
##eg: correct: user_age
user_age=45
print(user_age)
##incorrect:user  age spaces are not allowed in variable names
user  age=45
print(user  age)

#3.assigning variables
name="Sudha"
age=21
Python_beginner=True
#Printing each variable
print("My name is",name)
print("I am ",age," years old.")
print("Beginner in Python: ",Python_beginner)


#4.Algorithm: A step by step process to solve a problem
#example: step1:Take input
#step2: Multiply by 2
#step3:Display result
#code:Actual instruction written in programming language
#example:
num=10
print(num*2)
#program:A complete runnable set of code that solves a problem
num=10
result=num*2
print("result is:",result)


#5.
123=10 # syntax error:cannot assign to literal
print(123)

@test="hello" #syntax error:invalid syntax
print(@test)

_xyz2 = 3.14  #output: 3.14
print(_xyz2)

{{{ = [1, 2, 3] #syntax error:invalid syntax
print({{{)
    
True = False #syntax error:cannot assign to True
print(True)
    
my.name = "Alice" #syntax error:invalid syntax
print(my.name)
    
break = 10 #syntax error:invalid syntax
print(break)

1st_place = "Gold" #syntax error:invalid decimal literal
print(1st_place)

$price = 99.99 #syntax error:invalid syntax
print($price)

my-var = "test" #syntax error:cannot assign to operator
print(my-var)




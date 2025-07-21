#Variable declaration that follow proper conventions
user_name="Alice"
print(user_name)

__log1=49.99
print(__log1)

is__num2__=True
print(is__num2__)


#variable declarations that not follow proper conventions
@$&=123
print(@$&)

1num="hello"
print(1num)

num@__2=427
print(num@__2)

##python accepts lowercase(a-z),uppercase(A-Z) letters,also numbers(0-9)
##and underscores as variables declarations and it does not start with numbers,it does contain special characters like @$&* etc

x=100
y=100
print(id(x),id(y))
x=200
print(id(x),id(y))
#Python caches same memory location for the value 100.so initially x and y point to the same object. After reassignment, x gets a new memory location.


interger_val=50
print(interger_val)

string_val="Python"
print(string_val)

boolean_val= False
print(boolean_val)

list_val=[1,2,3]
print(list_val)

#Literal is a fixed value (50, "Python").

#Variable is a name that holds a value and can change.

a=15
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
print(a==b,a!=b,a>b,a<b,a<=b,a>=b)


print("hello) #syntax error


num=10
num1="hello"
print(num1+num)

#Syntax Error: Mistake in code structure (e.g., missing symbols).

#Type Error: Wrong type operation (e.g., adding string to integer).

num=10
dec=7.90
val=12.3
print(val+dec)
print(val*num)
print(num-dec)

bigint=10**1000
print(bigint)

#In python we can store very large integers without overflow Python can store very, very big numbers

#There is no fixed size limit (like 32-bit or 64-bit)

#It automatically uses more memory if the number is large















      

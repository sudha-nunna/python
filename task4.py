# prints a greating that includes initail and three letters of last name
first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
last_part=last_name[:3]
print("Hello",first_name,"Welcome to python class",last_part)

###Basic password validator
def validate_password():
    password=input("Enter your password:".strip())
    if len(password)<8:
        print("password is too short")
    elif password.isdigit():
        print("password consist only digits")
    elif "password" in password.lower():
        print("password contains common word")
    else:
        print("password looks good")
validate_password()

#code without function
password=input("Enter your password:".strip())
if len(password)<8:
    print("password is too short")
elif password.isdigit():
    print("password consist only digits")
elif "password" in password.lower():
    print("password contains common word")
else:
    print("password looks good")


#simple file name parser
def  parse_file():
    full_filename=input("upload your file:".strip())
    #name_part,extension=full_filename.strip()
    if full_filename.endswith(".txt") or full_filename.endswith(".csv "):
        print("Uploaded successful")
    else:
        print("File:Unsupported Type")
parse_file()



                

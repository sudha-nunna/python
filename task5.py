#write a python script named parse_email that asks the user to input an email address

parse_email = input("Enter your email address: ").strip()
if parse_email.count("@") == 1:
    at_index = parse_email.index("@")
    username = parse_email[:at_index]
    domain = parse_email[at_index + 1:]
    if "." in domain:
        print("Valid Email Address")
        print("Username:", username)
        print("Domain:", domain)
    else:
        print("Invalid Email Address")
else:
    print("Invalid Email Address")

#write a python function named count_vowels that takes a string as input
    
def count_vowel():
    string=input()
    if string==" ":
        print("Empty string")
    vowels=["a","e","i","o","u"]
    string=string.lower()
    for i in vowels:
        count=string.count(i)
        print(i,":",count)
count_vowel()

#write a pythn function named parse_url_path that takes a url path as input
def parse_url_path():
    path=input().strip()
    if path.startswith("/"):
        path=path[1:]
    part=path.split("/")
    print("Total number of parts:",len(part))
    for p in part:
        print(p)
parse_url_path()


#write a python script that requests a message from the user
message=input("Enter a message:")
unicode_values=""
for char in message:
    unicode_values +=str(ord(char)) +" "
print(unicode_values.strip())
    



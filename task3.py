#ATM machine that asks a userfor a pin code.the pin is 4321 allow 3 tries
pin_no="4321"
attempt=0
while attempt<3:
    num=input("enter the correct pin number:")
    
    if pin_no==num:
        print("Access granted")
        break
    else:
        print("In correct pin number")
        attempt += 1
if attempt>=3:
    print("Account locked")



#program that collect grocery items from user one by one

items = [" "]
index = 0
while True:
    item = input("Enter a grocery item (or type 'done' to finish): ")
    if item == 'done' or item == 'DONE' or item == 'Done':
        break
    items[index] = item
    index += 1
print("Grocery List:")
for i in range(index):
    print("-", items[i])
    


#Notify customer about order status
status = input("Enter the order status (shipped, delivered, or pending):")
if status == "shipped" or status == "Shipped" or status == "SHIPPED":
    print("Your order has been shipped.")
elif status == "delivered" or status == "Delivered" or status == "DELIVERED":
    print("Your order has been delivered.")
elif status == "pending" or status == "Pending" or status == "PENDING":
    print("Your order is still pending.")
else:
    print("Invalid status")


# login process simulation
username=input("Enter your username:")
password=input("Enter your Password:")
if username=="admin" and password=="1234":
    print("Login successful:")
else:
    print("Invalid credentials")





#unit consumption billing
units = int(input("Enter the number of units consumed: "))
bill = 0
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 8
else:
    bill = 100 * 5 + 100 * 8 + (units - 200) * 10
print("Total bill amount: ₹", bill)


#your are the coach of a basketball team and need to analyse your players score for the season

scores = [24, 18, 21, 19, 27]
print("Original Scores:", scores)
print("Highest score:", max(scores))
print("Lowest score:", min(scores))
print("Total points:", sum(scores))
scores.append(23)
print("after adding new score (23):")
print("Updated Scores:", scores)
print("Highest score:", max(scores))
print("Lowest score:", min(scores))
print("Total points:", sum(scores))


#you have a grocery list:["apples","banana","milk","eggs","cheese","bread"]
grocery_list = ["Apples", "Bananas", "Milk", "Eggs", "Cheese", "Bread"]
item = input("Enter an item to check if it's on the list: ")
if item in grocery_list:
    print(item,"is already on the list!")
else:
    print(item,"is not on the list.")
print("First three items:", grocery_list[:3])
print("Last two items:", grocery_list[-2:])



#you are preparing for a list participants for a content,but due to clerical error,some names appear more than once

participants = ["Anna", "Brian", "Anna", "David", "Brian", "Brian", "Ella"]
unique_participants = []
for name in participants:
    if name not in participants:
        unique_participants.append(name)
print("Original list:", participants)
print("Unique names (no repetitions):", unique_participants)

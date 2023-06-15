import os
# Dictonaries Basics
"""dic = {
    "fruits": "Mango,Banana,Apple",
    "Vegetables": "Potato,Carrot,Onion"
}

# print(dic["fruits"]= "hii")  Gives error

dic["fruits"]= "Pineapple, Orange, Avagado"  # change value of fruits


dic["Animals" ] = "Cow,Dog,Buffalo"  # add new element to the dictonary



for key in dic:
    print(key)
    print(dic[key])"""


# Challenge no 1

"""students = {
    "Harry" : 81,
    "Garry" : 92,
    "Perry" : 75,
    "Sharry": 62,
    "Merry" : 89
}

students_grade = {

}

for key in students:
    if students[key] >=90:
        students_grade[key] = "Outstanding"
    elif students[key] >=80:
        students_grade[key] = "Good"
    elif students[key] >=70:
        students_grade[key] = "Acceptable"
    elif students[key] <70:
        students_grade[key] = "Fail"

for key in students_grade:
    print(f"{key} : {students_grade[key]}")"""

# Nested list and dictonaries

# Nesting dictionies and list in a dictonary
'''food = {
    "chiness": ["Noodles", "Manchurian"],
    "Fast Food": {
        "Burger": ["Ham Burger", "VadaPav", "Aloo Tikki Burger"],
        "Pizza": ["Onian Pizza", "Panner Pizza"],
    },
}
'''

# Nesting dictonaries in a list
'''food = [
    {
        "Food_Type": "FastFood",
        "Burger": ["Ham Burger", "VadaPav", "Aloo Tikki Burger"],
        "Pizza": ["Onian Pizza", "Panner Pizza"],
    },
    {
        "Count": "How many times you eated that food",
        "Burger_eated": 20,
        "Pizza_eated": 15,
    },
]

print(food[0]["Food_Type"])
'''

# Challenge no 2

'''travel = [{
    "country" : "India",
    "visited" : 20,
    "Places" : ['Mumbai', "Delhi", "Hydrabad"]
},{
    "country" : "USA",
    "visited" : 3,
    "Places" : ['New York', "San Fransisco", "Washington DC"]
}]

def add(country, visits, Places):
    add_country = {"country": country, "visited": visits, "Places": Places}

    travel.append(add_country)

add("Russia", 13, ["Mountains", "Mosscow"])
print(travel)'''

# Blind Bid Programme

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         |_________|
                         `'-------'`
                       .-------------.
                      |_______________|
''')
print("Welcome to Blind Bid")


details = {}

end = True
while end:
    name = input("Enter your name ")
    amount = int(input("Enter the Bid Amount $"))
    details[name] = amount
    more_bid = input("Anyone here to add the bid? Type Y for Yes | N for NO-> ")
    os.system('cls')
    if more_bid == "Y":
        continue
    elif more_bid == "N":
        end = False
    else:
        print("Wrong Input!")
        end = False


max_name = ""
max_bid = 0 
for key in details:
    if details[key] > max_bid:
        max_bid = details[key]
        max_name = key
    else:
        continue

print(f"Highest Bid is done by {max_name} which is ${max_bid}")

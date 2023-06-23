# List comprehension
"""numbers = [1,2,3,4]
new_list = [n*n for n in numbers]
print(new_list)"""

# List comprehension using string
"""name = "Amresh Puri"
name_list = [letter for letter in name]
print(name_list)"""

# List comprehenison using conditional statements
"""names = ["Alex", "Harrry", "Carry","Drake","Esabela","Freedy"]
new_list = [name.upper() for name in names if len(name) > 5]
print(new_list)"""

# Challenge no 1
"""numbers = [1,2,3,4,5,6,52,78,98]
new_list = [name for name in numbers if name % 2 == 0]
print(new_list)"""

# Challenge no 2

"""list1 =  [items.rstrip() for items in open("hello.txt")]

list2 =  [items.rstrip() for items in open("hello2.txt")]
 
result  = [int(item) for item in list1 if item in list2]
print(result)"""


# Dictionary comprehension
"""import random
names = ["Alex", "Harrry", "Carry","Drake","Esabela","Freedy"]

new_dic = {stud:random.randint(1,100)  for stud in names}

marks_based_dic = {key: value for (key,value) in new_dic.items() if new_dic[key] > 50}
print(new_dic)
print(marks_based_dic)"""

# Challenge dic comprehension 1
"""string = "What are doing this Sunday?"
string_list = string.split()
string_dic = {item:len(item) for item in string_list}
print(string_dic)"""

# Challenge dic comprehension 2

'''weather_data = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_data_far = {key:value*(9/5)+32 for (key,value) in  weather_data.items()}
print(weather_data_far)'''

# Iterating from Dataframes

'''students_data = {
    "Students":["Amar","Raghav","Rachit"],
    "marks": [78,98,88]
}

for (key,value) in students_data.items():
    print(key)
    print(value)

import pandas as pd
dataframe = pd.DataFrame(students_data)

for (key,value) in dataframe.items(): #column wise iteration
    print(key)
    print(value)

for (index,row) in dataframe.iterrows():
    print(index)  #gives index
    print(row )  #print every row
    print(row.Students) #print every students for every row
    if row.Students == "Amar":
        print(row.marks)'''


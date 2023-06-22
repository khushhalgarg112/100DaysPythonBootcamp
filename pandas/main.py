# with open("weather_data.csv") as f:
#     print(f.readlines())

# import csv

# with open("weather_data.csv") as f:
#     data = csv.reader(f)  # This create a csv obejct which how the data now

#     tempreture = []

#     # for row in data:
#     #     print(row) 

#     for row in data:
#         if row[1] != 'temp':
#             tempreture.append(int(row[1]))

#     print(tempreture)

import pandas as pd

# data = pd.read_csv('weather_data.csv')
# print(data['temp'][1:4])   Slicing using pandas
# print(data)



# Average of a list using traditional method
'''dataset = data['temp'].tolist()
total = sum(dataset)
length = len(dataset)
print(f"Average is {total/length}")'''

# Average using pandas series funcions
# data_mean = data["temp"].mean()
# print(data_mean)

#  Get Data using columns
'''print(data['condition'])
print(data.condition)'''

# Get Data using rows
'''data_row = data[data.temp == 22]
print(data_row)'''

# Challenge no 1
'''max_temp = data[data.temp == data.temp.max()]
print(max_temp)'''

# Create a DataFrame 
'''stud_data = {
    "Students": ['Mohan','Param','Shivam','Rudra'],
    "Marks": [78,87,98,88]
}
data_frame = pd.DataFrame(stud_data)
print(data_frame) # Creating a 2d datafram from raw data
data_frame.to_csv("students_data.csv") # Saving dataframe to a csv file'''

# Working with squirals data

data_of_squiral = pd.read_csv('squiral_Data.csv') 
squiral_data = {
    "FurColor": ["Gray", "Cinnamon","Black"],
    "no_of_squiral": []
}

gray = 0
cinnamon = 0
black = 0 
data_list = data_of_squiral["Primary Fur Color"].tolist()
for color in data_list:
    if color == "Gray":
        gray +=1
    elif color == "Cinnamon":
        cinnamon +=1
    elif color == "Black":
        black +=1

squiral_data["no_of_squiral"] = [gray,cinnamon,black]

dataframe = pd.DataFrame(squiral_data)
dataframe.to_csv("Squiral_count.csv")



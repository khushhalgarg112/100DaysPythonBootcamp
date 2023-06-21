# file = open("hello.txt")  close it as file.close()  
# open the hello .txt file in file varibale and if not exist hen create this 
# In this opening method we have to close this every time thats why we use

with open("hello.txt", mode='w') as file:
    content = file.write("hello bro") # this variable store the nummebr of charcters in the file
    # content1 = file.read() # this line  gives an error because here mode is set to write 

print(content)
with open("hello.txt", mode='r') as file:
    content1 = file.read()

print(content1)

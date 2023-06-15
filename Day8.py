import math

"""
def  greet(a):
    print(f"Hello {a}")
    print(f"hola {a}")
    print(f"Namaste {a}")

greet("Hari")"""

"""def greet_with_loc(name, loc):
    print(f"Hello {name}")
    print(f"You live in {loc}")

# greet_with_loc("Anthony", "Tokyo") positional argument
greet_with_loc(loc="huwai", name="James") # keyword argument"""

# Challenge no 1

"""h = int(input("Enter the height of the wall "))
w = int(input("Enter the width of the wall "))
coverage = 5


def can_used(height, width, cover):
    can = (height * width) / cover
    print(f"Total paint can are used is {math.ceil(can)}")


can_used(height=h, width=w, cover=coverage)"""

# Challenge no 2


'''def prime_check(num):
    count = 0
    for i in range(2, num // 2+1):
        if num % i == 0:
            count += 1
        else:
            continue

    if count != 0:
        print(f"{num} is not a prime number.")
    else:
        print(f"{num} is a prime number.")


number = int(input("Enter the numbr you want to check for:- "))
prime_check(number)'''


# Caesar Cipher

print("Welcome TO CAESAR CIPHER")
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

end = True
while end:
    # Taking inputs
    choose = input("Type 'encode' to encode you code or type 'decode' to decode your code:- ")
    if choose == 'encode':
        code = input("Enter your code to encode it :-  ").lower()
    elif choose =='decode':
        code = input("Enter your code to decode it :-  ").lower()
    else:
        print("Wrong input, Try to run program again and enter corret input")
        break
    # input of spacing
    code_number = int(input("Enter the number of spacing:- "))

    encode = []
    length_of_code = len(code)
    length_of_letters = len(letters)
    # converting input text in a list
    for i in range(0,length_of_code):
        encode.append(code[i])

    result = ""
    # condition for encoding
    if choose == 'encode':
        for j in range(0,length_of_code):
            for k in range(0,length_of_letters):
                if(encode[j] == letters[k]):
                    if(k+code_number >= 26):
                        encode[j] = letters[(k+code_number)-26]
                        # print(encode)
                        # print(letters)
                        result += encode[j]
                        break
                    else:
                        encode[j] = letters[k+code_number]
                        # print(encode)
                        # print(letters)
                        result += encode[j]
                        break
        print(f"Your Encoded code is:- {result}")
    # condition for decoding
    elif choose == 'decode':
        for j in range(0,length_of_code):
            for k in range(0,length_of_letters):
                if(encode[j] == letters[k]):
                    if(k+code_number < 0):
                        encode[j] = letters[26-k-code_number]
                        result += encode[j]
                        break
                    else:
                        encode[j] = letters[k-code_number]
                        result += encode[j]
                        break          

        print(f"Your Decoded code is:- {result}")
    # while loop exit condition
    cont = input("Do you want to continue ? Y or N:- ")
    if cont == 'Y':
        end = True
    elif cont == 'N':
        end = False
    else:
        print("Wrong input")
        break
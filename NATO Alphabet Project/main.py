import pandas

dataset = pandas.read_csv("data.csv")
# print(dataset)

data_dic = {row.letter:row.words for (index,row) in dataset.iterrows()}

on = True
while on:
    try:
        input_word = input("Enter the word-> ").upper()
        result = {let:data_dic[let] for let in input_word}
    except KeyError:
        print("Sorry you entered wrong input")
    else:
        on = False

print(result)






import pandas

dataset = pandas.read_csv("data.csv")
# print(dataset)

data_dic = {row.letter:row.words for (index,row) in dataset.iterrows()}

input_word = input("Enter the word-> ").upper()

result = {let:data_dic[let] for let in input_word}

print(result)
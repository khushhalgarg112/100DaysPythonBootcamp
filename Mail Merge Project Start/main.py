placeholder = "[name]"

with open('/Users/IT/Desktop/Python projects/Mail Merge Project Start/Input/Names/invited_names.txt', mode='r') as names:
    names_list = names.readlines()


with open('/Users/IT/Desktop/Python projects/Mail Merge Project Start/Input/Letters/starting_letter.txt', mode='r') as file:
    greet_text = file.read()
    for items in names_list:
        new_items = items.strip()
        last_message  = greet_text.replace(placeholder,new_items)
        print(last_message)
        with open(f'/Users/IT/Desktop/Python projects/Mail Merge Project Start/Output/ReadyToSend/greet_to_{new_items}.txt', mode='w') as new_file:
            new_file.write(last_message)


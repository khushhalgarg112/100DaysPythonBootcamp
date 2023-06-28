def next_word():
    curr = random.choice(data)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=curr["French"])
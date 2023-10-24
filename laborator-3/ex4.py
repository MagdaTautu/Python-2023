def compose(notes, moves, start):
    print(notes[start])
    index = start
    for move in moves:
        index = index + move
        if(index > len(notes)):
            index = index-len(notes)
        print(notes[index])
compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) 
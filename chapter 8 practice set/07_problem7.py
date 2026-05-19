def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
        return n


l = ["Harry", "Rohan", "Shubham", "Rohit", "an"]
print(rem(l, "an"))


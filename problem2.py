strings_list = ["shelf", "mouse", "skittle", "tree", "piano", "televsion", "pig"]
sorted_strings = sorted(strings_list, key=lambda x: (len(x), x))
print(sorted_strings)
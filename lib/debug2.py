def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
        #print(f"count char {counter[char]}")
        #print(f"char {char}")
        
    letter = sorted(counter.items(), key=lambda item: item[1])[10][0]
    #print(f"letter {letter}")
    #print(f"sorted {sorted(counter.items())}")
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
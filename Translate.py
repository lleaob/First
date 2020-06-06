'''
substitute vowels for g
'''
def trans(w):
    new_w = ""
    for l in w:
        if l in "aeiou":
            l = "g"
            new_w = new_w + l
        elif l in "AEIOU":
            l = "G"
            new_w = new_w + l
        else:
            new_w = new_w + l
    return(new_w)

print("\n" + trans(input("\nType the word you want to change: ")))
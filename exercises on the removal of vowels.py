def remove_vowels(s):
    vowels = "aieuoAUEIO"
    results =""
    for char in s:
        if char not in vowels:
            results+=char
    return results
s_string= input("enter the string:")
output_string = remove_vowels(s_string)
print("the string without vowels is",output_string)
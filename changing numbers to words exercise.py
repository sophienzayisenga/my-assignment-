def number_to_word(n):
    if n < 0:
        return "number is not positive"
    if n == 0:
        return "the number is zero"
    ones=["","one","two","three", "four", "five", "six", "seven", "eight", "nine"]
    teens=["","ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", 
        "seventy", "eighty", "ninety"]
    words=""
    if n >= 100:
        words += ones[ n//100] + "hundred " 
        n%=100
    elif n >= 20:
        words+= tens[ n//10] + " "
        n%=10
    elif n >=10:
        words+= teens[n-10] + " " 
    elif n>=0:
        words+= ones[n] +" "
    return words.strip()
positive_numbers=int(input("enter the positve number:"))
print(f"{positive_numbers} is {number_to_word(positive_numbers)}")


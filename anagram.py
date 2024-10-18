def check_anagram(name1, name2):
    return sorted(name1) == sorted(name2)
first_name =input("enter 1st name:")
second_name =input("enter second name:")
if check_anagram(first_name,second_name):
   print (f"{first_name} and {second_name} are anagrams")   
else:
    print (f"{first_name} and {second_name} are not anagrams")

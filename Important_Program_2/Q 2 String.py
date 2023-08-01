str_=input("Enter the String: ")
my_dict={}

print(f"\n{str}")

for char in str_:
    if char in my_dict:
        my_dict[char]+=1
    else:
        my_dict[char]=1

print(my_dict)

print("\n----------Methood 2----------")

from collections import Counter

result=Counter(str_)

print(result)

replace_character=str_.replace("s","G")
print(f"Replace the character in the string {replace_character}")
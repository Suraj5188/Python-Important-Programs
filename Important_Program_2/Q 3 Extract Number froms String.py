str1="Suraj Gaikwad is trainee in mobiloitte since 17 july 2013"

# Using List comphrension

list1=[i for i in str1.split() if i.isdigit()]

print(list1)
'''
Given an array of N element and integer  K. Your task is to return 
the position of first occurance of k in the given array. 
Inputs should given by the user
'''

list1=[1,2,3,4,5,6,7,8,9,10,11,1,11,2,2,3,4,5,5,5,5]

print(list1.count(100))

# Now suppose you want to add elements in list2

list2=[]

no_of_elements=int(input("Enter Number of Element You want to store: "))

for i in range(no_of_elements):
    n=int(input("Enter Element you want to add: "))
    list2.append(n)

print(list2)

def search_specific_element(element):
    result=list2.count(element)
    print(result)

search_element=int(input("Enter Specific Element you want to search: "))

search_specific_element(search_element)
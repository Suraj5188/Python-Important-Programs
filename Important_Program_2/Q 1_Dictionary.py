


# Create Dictionary and accept input from user
my_dict={}
def create_dict():

    

    while True:

        try:
            key=input("Enter your key: ")
            if key.lower()=='exit':
                break
            value=input("Enter your values:")
            my_dict[key]=value
            print(f"\n Your Dictionary: {my_dict}")

        except Exception as e:
            print(e)           
            print("Error Occured")

    return my_dict



# Now check the key is present in dictionary or not

def key_search():
    
    
    try:
        key_search=input("Enter key to search: ")
        if key_search in my_dict:
            print(f"Its keys and value are {key_search} : {my_dict[key_search]}")
        else:
            print(f"Key does not exit int the dictionary")
    except Exception as e:
        print(f"Sorry Keys not found! {e}")

def main():
    create_dict()
    key_search()

main()
    
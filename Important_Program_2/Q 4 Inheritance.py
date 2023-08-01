class person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name =last_name

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

class employee(person):
    def __init__(self, first_name, last_name,emp_id):
        super().__init__(first_name, last_name)
        self.emp_id =emp_id

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_emp_id(self):
        return self.emp_id
    

# Creating Objects

object1=employee("Suraj","Gaikwad",5188)

print(f"Employee First Name: {object1.get_first_name()}")
print(f"Emplyee Last Name: {object1.get_last_name()}")
print(f"Employee id: {object1.get_emp_id()}")
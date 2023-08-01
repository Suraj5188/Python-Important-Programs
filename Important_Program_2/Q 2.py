'''
LEGB Scope in Python:
In Python, variable names are resolved based on the concept of scope. 
The LEGB rule defines the order in which Python 
looks for variable names in different scopes. The scopes are, in order of precedence:

1. Local (L): Variables declared inside a function have local scope 
and are accessible only within that function.
2. Enclosing (E): Variables in the scope of an enclosing (containing) function, if any.
3. Global (G): Variables declared at the global level 
(outside any function) have global scope and are accessible throughout the entire module.
4. Built-in (B): Predefined names that are built into Python, such as print() or len().

'''

# Question

'''
Explain LEBG rule with their example and their working with list and tuple. 
Explaination should be done using file handling
'''

# LEBG--> Local,Enclosed,Built-in,Global

# Declaring the global variable
global_variable ="I am a global variable"

def fun1():

    # Declaring the local variable
    local_variable ="I am a local variable"

    def fun2():
            
        # Enclosed variable
        enclosed_variable ="I am enclosed variable"

        print(global_variable)
        print(enclosed_variable)
        print(inner_variable)

    inner_variable ="I am inner variable"

    fun2()

fun1()
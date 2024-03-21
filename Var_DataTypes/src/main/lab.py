# src/main/lab.py

def demonstrate_integer():
    my_integer = 4  # Assign any integer value to 'my_integer'
    return my_integer


def demonstrate_float():

    my_float = 4.5  # Assign any floating-point value to 'my_float'
    return my_float


def demonstrate_boolean():
    my_boolean = True  # Assign either True or False to 'my_boolean'
    return my_boolean

def demonstrate_string():
    # Assign a string value to the variable
    my_string = 'Bhargava'
    return my_string

def demonstrate_tuple():

    # Define tuple elements
    element1 = 1
    element2 = 2
    element3 = 3

    # Create the tuple
    my_tuple = (element1, element2, element3)
    
    return my_tuple

def demonstrate_create_areas_list():
    hall = 10
    kit = 20
    liv = 30
    bed = 40
    bath = 15

    areas = [hall, kit, liv, bed, bath]
    
    return areas

def demonstrate_set():

    # Define set elements
    element1 = 'a'
    element2 = 'b'
    element3 = 'c'

    # Create the set
    my_set = {element1, element2, element3}
    
    return my_set



def demonstrate_dictionary():
    # Define dictionary key-value pairs
    key1 = 'key1'
    value1 = 'value1'
    key2 = 'key2'
    value2 = 'value2'

    # Create the dictionary
    my_dict = {key1:'key1', value1:'value1', key2 :'key2', value2:'value2'}
    
    return my_dict

def demonstrate_variable_scope():
    # Global variable declaration
    global_var = "I am a global variable"

    def function1():
        # Local variable declaration within function1
        local_var1 = "I am local to function1"
        
        print("Inside function1 - global_var:", global_var)
        

    function1()  # Call function1 to demonstrate variable scope 
    print("Outside function1 - global_var:", global_var)
    return None

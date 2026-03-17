def split_coords(coordinates):
    x_coord = []
    y_coord = []

    for x, y in coordinates:
        x_coord.append(x)
        y_coord.append(y)
    return x_coord, y_coord

def flatten_list(nested_list):
    new_list = []

    for nest in nested_list:
        if isinstance(nest, list):
            new_list.extend(flatten_list(nest))
        else:
            new_list.append(nest)
    return new_list

def create_id_lookup(user_data):
    return {user : user_data.index(user) for user in user_data}

def top_performer(student_data):
    largest = 0
    string = ""
    for key, value in student_data.items():
        if value > largest:
            largest = value
            string = key 
    return string

def group_by_category(items):
    new_items = {}

    for i in items:
        name = i["name"]
        type = i["type"]
        if type not in new_items:
            new_items[type] = []
        new_items[type].append(name)
    return new_items

def sort_by_length(names):
    return sorted(names, key = len)

def sort_dict_by_value(data):  

    sorted_items = sorted(data.items(), key=lambda item: item[1])  
    # data.items() converts the dictionary into (key, value) tuples
    # Example: {'a':3,'b':1,'c':2} → [('a',3), ('b',1), ('c',2)]
    # sorted() sorts these tuples
    # key=lambda item: item[1] tells Python to sort using the VALUE (index 1 of the tuple)
    # Result: [('b',1), ('c',2), ('a',3)]

    return dict(sorted_items)  


def rotate_list(nums, k):
    if not nums:  # If the list is empty, return an empty list
        return []
    
    k = k % len(nums)  # Adjust k in case it is larger than the list length
    return nums[-k:] + nums[:-k]  # Take last k elements and move them to the front


def sort_emails_by_domain(emails):
    # Sort emails based on the domain (part after '@')
    return sorted(emails, key=lambda email: email.split('@')[1])


def is_subset(list_a, list_b):
    # Check if every item in list_a exists in list_b
    return all(item in list_b for item in list_a)


def remove_dictionary_key(data, key_to_remove):
    if key_to_remove not in data:  # Check if key exists in dictionary
        return "Key not found"  # Return message if key is missing
    
    new_dict = data.copy()  # Create a copy so original dictionary is not modified
    del new_dict[key_to_remove]  # Remove the specified key from the copy
    return new_dict  # Return updated dictionary


def invert_dictionary(data):
    inverted = {}  # Create an empty dictionary to store inverted values
    
    for key, value in data.items():  # Loop through each key-value pair
        inverted[value] = key  # Swap key and value (value becomes key)
    
    return inverted  # Return the inverted dictionary


def recursive_sum(n):
    if n == 1:  # Base case: if n is 1, return 1
        return 1
    return n + recursive_sum(n - 1)  # Add n to the sum of numbers before it


def fibonacci_generator(n):
    if n <= 0:  # If n is 0 or negative, return empty list
        return []
    if n == 1:  # If only one number is needed
        return [0]
    
    fib = [0, 1]  # Start the Fibonacci sequence
    
    while len(fib) < n:  # Keep generating until we have n numbers
        fib.append(fib[-1] + fib[-2])  # Add sum of last two numbers
    
    return fib  # Return the full Fibonacci list
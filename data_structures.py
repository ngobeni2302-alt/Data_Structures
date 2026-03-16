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
    return ''

def sort_emails_by_domain(emails):
    return ''

def is_subset(list_a, list_b):
    return ''

def remove_dictionary_key(data, keys_to_remove):
    return ''

def invert_dictionary(data):
    return ''

def recursive_sum(n):
    return ''

def fibonacci_generator(n):
    return ''
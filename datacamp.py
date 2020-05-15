print("hi simon!")

def add_all(*args):
    """sum all args together"""
    #intialize sum
    sum_all = 0

    for num in args:
        sum_all += num
    
    return sum_all

print(add_all(1,2))

def print_all(**kwargs):

    for key, value in kwargs.items():
        print(key + ":" + value)

print_all(name='dumbledore', job='headmaster')          

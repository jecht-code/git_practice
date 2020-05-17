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

raisetopower = lambda x, y: x **y

a = raisetopower(2,3)
print(a)

### Iterating over iterables
word = 'Da'
it = iter(word)
print(next(it))
print(next(it))

word = "Data"
it = iter(word)
print(*it)

print(10 ** 100)

googol = iter(range(10 ** 100))
print(next(googol))
print(next(googol))

values = range(10, 21)
print(values)
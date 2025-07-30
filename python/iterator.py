# Iterator uses lazy loading.
# You can direct get any element from iterator until you itrate through iteratot.
# it provides a way to access the elements of any collection sequnetially without exposing the underlaying structure.


my_list = [1,2,3,4,5,6,7]
new_iter = iter(my_list)
print(new_iter)
print(type(new_iter))


# print(len(new_iter))
# print(new_iter[3])

for i in new_iter:
    print(i)

# print(next(new_iter))
# print(next(new_iter))
# print(next(new_iter))
# print(next(new_iter))
# print(next(new_iter))
# print(next(new_iter))
# print(next(new_iter))
# print(next(new_iter))


str_iter = iter("hello")
print(next(str_iter))
print(next(str_iter))


"""Generators are the simpler way to create iterators. They use the 'yield' keywords to produce a series of values
lazily, which means they generate values on the fly and do not store them in the memory."""


def create_generators(input):
    for i in input:
        yield i

print(type(create_generators("Rishi"))) #simpler way to make iterator but not iterator.

for i in create_generators("Rishi"):
    print(i)

def test():
    yield 1
    yield 2
    yield 3

print(type(test()))


# closures
# Where we can use functions inside a fucntion and
# we can also use the variables of the other functions which in outer function's context.


def main_welcome(name):
    msg = "Welcome"

    def sub_welcome_method():
        print(f"Hey {name}")
        print("Welcome to new python course.")
        print(msg) # not passing
        print("Please learn attentively.")
    return sub_welcome_method()

main_welcome("Rishi")
print("\n")


def main_welcome(func):
    def sub_welcome_method():
        print("Welcome to new python course.")
        print(func())
        # func()
        print("Please learn attentively.")
    return sub_welcome_method()

def input_func():
    print("Main bahar ka aadmi hu.")

main_welcome(input_func)


def calculate_len(func, lst):
    def inner():
        print("Starting")
        print(func(lst))
        print("Ending")
    return inner()


calculate_len(len, [1,2,3,4,5])



# decorators
# -----------------------------------------------------

def my_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@my_decorator
def do_something():
    print("Did something.")

do_something()



def make_square(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result**2
    return wrapper

@make_square
def addition(a,b):
    return a+b

print(addition(2,3))




# Three layers (decorator with arguments)
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def speak():
    print("Hello")

speak()
# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
# print(add_two(3))

# Applying decorator to a lambda
# print((trace(lambda x: x ** 2))(5))

@trace
def test(*argssadf):
    print("test123124")

test()

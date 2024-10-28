def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)  # Call the original function
        print(f"Function {func.__name__} completed.")
        return result
    return wrapper

@log_function_call #executes log_function_call and pass add func as an arg
def add(a, b):
    return a + b

# Calling the decorated function
result = add(3, 5)
print(f"Result: {result}")
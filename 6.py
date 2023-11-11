# Напишіть декоратор, який обмежує кількість викликів функції.

def limit_calls(max_calls):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.calls < max_calls:
                wrapper.calls += 1
                return func(*args, **kwargs)
            else:
                print(f"{func.__name__} error")

        wrapper.calls = 0

        return wrapper
    return decorator

@limit_calls(3)
def some_function():
    print("Виклик функції")


some_function()
some_function()
some_function()
some_function()

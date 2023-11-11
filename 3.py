def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"eror: {e}")

    return wrapper
@handle_exceptions
def divide(a, b):
    return a / b

divide(5, 0)
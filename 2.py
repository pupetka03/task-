def cache_result(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None

            try:
                with open(file_name, 'r') as file:
                    result = file.read()
                    print(f'{result}')
            except:
                FileNotFoundError
                pass

            if result is None:
                result = func(*args, **kwargs)
                print(f"{result}")

            with open(file_name, 'w') as file:
                file.write(result)
            return result
        return wrapper
    return decorator

@cache_result("cache_result.txt")
def example_function(x, y):
    return x + y

result1 = example_function(2, 6)
print(result1)

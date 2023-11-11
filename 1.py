def name(func):
    def wrapper(*args, **kwargs):
        print("print перед викликом функції")
        result = func(*args, **kwargs)
        print("print після виклику функції")
        return f"{result.title()}"

    return wrapper

@name
def meno(meno):
    return f"ahoj, {meno}"

x = meno("Ihor Holodenko")
print(x)

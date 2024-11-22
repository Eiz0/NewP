def greet(name):
    return f"Hello, {name}!"

def greet_all(names):
    return [f"Hello, {name}!" for name in names]

if __name__ == "__main__":
    print(greet("World"))
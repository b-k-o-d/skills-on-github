try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")


try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")


try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print(f"Error: {e}")


try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError as e:
    print(f"Error: Key {e} not found")


try:
    num = 5 + "10"
except TypeError as e:
    print(f"Error: {e}")


try:
    num = int("abc")
except ValueError as e:
    print(f"Error: {e}")


try:
    num = 10
    num.append(5)
except AttributeError as e:
    print(f"Error: {e}")


try:
    import non_existent_module
except ImportError as e:
    print(f"Error: {e}")


try:
    x = int("xyz")
    y = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")


try:
    f = open("test.txt", "r")
    content = f.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
finally:
    print("Execution completed, whether an error occurred or not.")

def read_int(prompt: str, min: int, max: int)-> int:
    while True:
        try:
            data = int(input(prompt))
            #assert evaluates the expression;
            #if the expression evaluates to True, or a non-zero numerical value, or a non-empty string, or any other value different than None, it won't do anything else;
            #otherwise, it automatically and immediately raises an exception named AssertionError
            assert -10 < data < 10
        except ValueError:
            print("Error: wrong input")
            continue
        except AssertionError:
            print("Error: the value is not within permitted range (-10..10)")
            continue
        return data


number = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", number)

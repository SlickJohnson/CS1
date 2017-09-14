def fizz_buzz(start=1, end=100):
    for i in range(start, end+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")

fizz_buzz()

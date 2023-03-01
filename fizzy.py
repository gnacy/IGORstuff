for ggwp in range(1, 101):
    if ggwp % 3 == 0 and ggwp % 5 == 0:
        print("FizzBuzz")
    if ggwp % 3 == 0:
        print("Fizz")
    if ggwp % 5 == 0:
        print("Buzz")
    else:
        print(ggwp)
def tryExcept(x):
    try:
        minimum = 20000
        if x < minimum:
            raise ValueError("Please add money to your account")
        else:
            print("Your daily minimum is maintained")
    except ValueError as e:
        print(e)

tryExcept(19000)
tryExcept(29000)


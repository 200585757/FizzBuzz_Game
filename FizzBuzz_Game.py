target = int(input("Upto what number, do you want to play? Enter that last number: "))
for game in range(1, target+1):
    if game % 3 ==0 and game % 5 == 0:
        print("FizzBuzz")
    elif game % 3 == 0:
        print("Fizz")
    elif game % 5 == 0:
        print("Buzz")
    else:
        print(game)
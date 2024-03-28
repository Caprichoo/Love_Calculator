import random
print("Welcome to Love Calculator")
your_name = input("What's your name: ")
lover_name = input("What's your lover name: ")

love_percentage = random.randint(1,100)

# combined_name = your_name + lover_name
# lower_names = combined_name.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
#
# love_percentage = int(first_digit + second_digit)

if love_percentage < 10 or love_percentage > 90:
    print(f"Your score is {love_percentage}, you go together like coke and mentos.")

elif love_percentage >= 40 and love_percentage >= 50:
    print(f"Your score is {love_percentage}, you are alright together.")

else:
    print(f"Your score is {love_percentage}.")






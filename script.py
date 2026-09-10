# qwe = float(input("enter num:"))
# wer = input("enter sign:")
# ert = float(input("enter second num:"))
# if wer == "+":
#     print(qwe + ert)
# elif wer == "-":
#     print(qwe - ert)
# elif wer == "*":
#     print(qwe * ert)
# elif wer == "/":
#     print(qwe / ert)
# else:
#     print("invalid input")
name = input("what is your name?")
age = int(input("how old are you:"))
town = input("what is your town:")
print("   ")
print("   ")
if age <= 18:
    print("you teenager".upper())
if age >= 65:
        print("you pensioner".upper())
print("  ")
print("Hello " + name)
print("your " + str(age))
print("you from " + town)
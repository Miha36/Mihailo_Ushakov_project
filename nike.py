print("Привет, Python!")
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
name_narrator = "Yan"
cuntry_gf_narrator  = " Germany"
mine = "my"
print("hi, "+ mine + " name " + name_narrator + ".")
print("I lave in Ireland and stade in school.")
mine = "narrator's"
print(  mine + " girlfriend from" + cuntry_gf_narrator +  ",")
mine = name_narrator + "'s"
print(  mine + " the best friend is a professional basketball player.")
print("  ")
print("day 2")
print("  ")
f_phrase = "Power Pain"
print(f_phrase.lower())
phrase = "hooper pain"
print(phrase.upper())
print(phrase.upper().isupper())
print(phrase.index("o"))
print("  ")
print("day 3 & day 6")
print("  ")
print(phrase.replace("hooper", "father's"))
print(f_phrase.replace("Pain", "bank"))
g_phrase = ("I like still water")
print(g_phrase.replace("still", "sparkling").replace("water", "Fanta"))
from math import *
my_num = 2-7
print(str(my_num) + " that's my favorite number ")    # for num and letter on one str
print(abs(my_num))            #num without minus
print(pow (3,9))              #like 3^9
print(round(4.6))             #round number
print(floor(4.9))
print(sqrt(4.8))
print("        ")
print("        ")
print("        ")
# print("_______REGISTRATION_______")
# print("        ")
# print("        ")
# print("        ")
# print("    hello, wath yor name?")
# print("        ")
# name = input("you:")
# true = True
# false = False
# if name == str("Michael"):
#     print("hello Michael")
# else:
#     print("incorrect username")
# while name != str("Michael"):
#     name = input("you:")
# else:
#     print("  ")
#     print("      ")
#     print("Nice to meet you  " + name + "!")
# print("        ")
# age = input("your password:")
# if age == str("tapok1009"):
#     print("all right" + name + ",welcome!")
# else:
#     print("incorrect password")
# while age != str("tapok1009"):
#     name = input("you:")
# else:
#     print("all right " + name + ",welcome!")
#
#
# print("        ")



#you_best_friend = input("Name your's best friend:")
#his_favorite_color = input("hi's or she's favorite color:")
#his_hobby = input("hi's or she's hobby:")
#print("I have once the best friend " + you_best_friend)
#print("hi's favorite color " + his_favorite_color )
#print("every Monday and wednesday hi's go on the " + his_hobby)
print(" ")
print("day 4")
print("  ")
fact_about_me =["I like boys", "I like girls", "i like Rita","8Karen","jim","I like Rita"]
#fact_about_me.remove("I like Rita")      #<~~~~~REMOVE
fact_about_me.insert(3, "Michael")
#fact_about_me.pop()         #write list but without last element
#fact_about_me.clear()
fact_about_me.sort() #sort numbers<uppercase_letters<lowercase_letters
#fack_about_me2 = fact_about_me.copy()    #did independent copy
fact_about_me.append("I like study pyton")       #adds one element to the end of the list
print(fact_about_me)
print(fact_about_me.count("I like Rita"))         #how many these element exactly in this list
print("hello i am Michael i like gum and "  + str(fact_about_me[5]))
print(fact_about_me.index("i like Rita"))
fact_about_me.reverse()
print(fact_about_me)

def seyhi(name,age):
    print("hello "+ name + " you are " + age + "?")


seyhi("Jo,", "30")
print("  ")
print("day 5")
print("  ")
def volume_box(num):
    return num*num+num-20
result = volume_box(10)
print("volume box: " + str(result))
print("  ")
print("day 6 & day 3")
print("  ")
print("day 7")
print("  ")
def lover_sm (num1,num2,num3):
    if num1 <num2 and num1 <num3:
        return num1
    elif num2 <num3 and num2 <num1:
        return num2
    else:
        return num3

print(lover_sm(181,185,169))

def higher_sm(num1,num2,num3):#def — это ключевое слово, с которого начинается создание собственной функции
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    else:
        return num3

print(higher_sm(181,185,169))
print("  ")
# qwe = float(input("your num:"))
# ert = (input("math sisns:"))
# wer = float(input("your second num:"))
# if ert == "-":
#     print(qwe - wer)
# elif ert == "+":
#     print(qwe + wer)
# elif ert == "*":
#     print(qwe * wer)
# elif ert == "/":
#     print (qwe / wer)
print("  ")
print("day 8")
print("  ")
geng_words = {
    1: "saket",
    2: "goon",
    3: "Saketyors",
}
print(geng_words.get(5, "not a valid kay"))
print("  ")

print("Done")
print("   ")
# secret_word = "saket"
# gues = ""
# score_incorrect = 0
# attempt = 3
# mko = False
# while gues != secret_word and not mko:
#     if score_incorrect < attempt:
#         gues = input("try:")
#         score_incorrect += 1
#     else:
#         mko = True
# if mko:
#     print("Loser")
# else:
#     print("Winner")
print("  ")
for letter in "HH I wont to sey", "SEX":
    print(letter[1])
#for name9 in range(99):
#    print(name9)
ujm = ("not", "from","Juice")
for index in range(len(ujm)):
    print(ujm[index])
print("________________________________________")#Функция len() отвечает на один единственный вопрос: "сколько тут вещей?"
friends = ("Jim", "Karen", "Rita")
for mfc in range(0, 10):
    if 3 <= mfc <= 6:
        print("i am gey")
    else:
        print("i am gey but i like girl")
print("     ")
for mfc in range(0, 9):
    if 0 <= mfc <= 5:
        print("i am gey        i am gey")
    else:
        print("i am gey but i like girl")
print("        ")
print("i am gey but i like girl")
for mfc in range(0, 10):     #for — это ключевое слово, с которого начинается цикл — то есть повторение действия несколько раз подряд.
    if (0 <= mfc <= 3):
        print("i am gey             i am gey")
    else:
        print("i am gey")
print("     ")
print("day 9")
print("  ")

def raise_to_power (num1, num2):
    result = 1
    for _ in range(2):
        result = num1 ** num2
    return result
print(raise_to_power(3,4))
print("    ")
num_grind = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in num_grind:
    for col in row:
        print(num_grind)
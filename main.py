from random import randint, choice
from datetime import time

# Test1

WRONG_UNSWER = ["Ні", "Не вірно", "Подумай", "Та де"]
CORRECT_UNSWER = ["Молодець", "Супер",
                  "Красавчик", "Найрозумніша дитина на світі"]
OPERAND = ["-", "+", "*", "/"]
EXIT_OPTIONS = ["exit", "cancel"]
START_NUMBER = ""
END_NUMBER = ""
NEGATIVE_VALUES = False
CORRECT_AMOUNT = 0
WRONG_AMOUNT = 0
EQUATIONS = 0


def choose_excercise():
    while True:
        choose = input(
            "Choose an excercise: \nRandom math - 1 \nExact math - 2 \n>> ")
        if choose in ["1", "2"]:
            return choose
        elif choose in ["exit", "cancel"]:
            return "До наступної зустрічі!"
        else:
            print("Please, choose an excercise")
            continue


def random_math():
    # start = time.now()
    global WRONG_AMOUNT, CORRECT_AMOUNT, EQUATIONS
    while True:
        num1 = str(randint(int(START_NUMBER), int(END_NUMBER)))
        num2 = str(randint(int(START_NUMBER), int(num1)
                   if not NEGATIVE_VALUES else int(END_NUMBER)))
        operand = choice(OPERAND)
        while True:
            answer = input(f"{num1} {operand} {num2} = ")
            if answer in EXIT_OPTIONS:
                # end_time = time.now() - start
                return print(f"Пройдено завдань - {EQUATIONS}\nВірних відповідей - {CORRECT_AMOUNT}\nХибних відповідей - {WRONG_AMOUNT}\nМолодчинка, до наступної зустрічі!")
            if not answer.replace("-", "").isnumeric():
                print(f"{answer} не є числом")
                continue
            if int(answer) == eval(f"{num1}{operand}{num2}"):
                EQUATIONS += 1
                CORRECT_AMOUNT += 1
                print(f"{choice(CORRECT_UNSWER)}")
                break
            else:
                EQUATIONS += 1
                WRONG_AMOUNT += 1
                print(f"{choice(WRONG_UNSWER)}")
                continue


def exact_math():
    global WRONG_AMOUNT, CORRECT_AMOUNT, EQUATIONS
    while True:
        equation = input("Напишіть рівняння: ")
        if equation in EXIT_OPTIONS:
            return print("Молодчинка, до наступної зустрічі!")
        while True:
            try:
                result = eval(equation)
                answer = input(f"{equation} = ")
                if answer in EXIT_OPTIONS:
                    return print(f"Пройдено завдань - {EQUATIONS}\nВірних відповідей - {CORRECT_AMOUNT}\nХибних відповідей - {WRONG_AMOUNT}\nМолодчинка, до наступної зустрічі!")
                if int(result) == int(answer):
                    EQUATIONS += 1
                    CORRECT_AMOUNT += 1
                    print(choice(CORRECT_UNSWER))
                    break
                else:
                    EQUATIONS += 1
                    WRONG_AMOUNT += 1
                    print(choice(WRONG_UNSWER))
                    continue
            except:
                print("Не вірно написане рівняння, спробуйте ще")
                break


def choose_numbers():
    while True:
        global START_NUMBER
        START_NUMBER = input("Введіть початкове число: ")
        if START_NUMBER in EXIT_OPTIONS:
            return "До наступної зустрічі"
        if not START_NUMBER.isnumeric():
            print("Введіть, будь-ласка, число!")
            continue
        else:
            break
    while True:
        global END_NUMBER
        END_NUMBER = input("Введіть кінцеве число: ")
        if END_NUMBER in EXIT_OPTIONS:
            return "До наступної зустрічі!"
        if not END_NUMBER.isnumeric():
            print("Введіть, будь-ласка, число!")
            continue
        elif int(END_NUMBER) < int(START_NUMBER):
            print("Кінцеве число повинне бути більшим за початкове!")
            continue
        else:
            break
    while True:
        global OPERAND
        answer = input(
            "Введіть математичні дії, з якими хочете працювати (+-*/): ")
        if answer in EXIT_OPTIONS:
            return "До наступної зустрічі!"
        OPERAND = [i for i in answer if i in OPERAND]
        print(OPERAND)
        if not OPERAND:
            print("Виберіть хоча би одну дію")
            continue
        else:
            break
    while True:
        global NEGATIVE_VALUES
        answer = input(
            "Ви хочете рахувати з від'ємними значеннями? (y - так, n - ні) ")
        if answer in EXIT_OPTIONS:
            return "До наступної зустрічі!"
        if answer == "y":
            NEGATIVE_VALUES = True
            break
        elif answer == "n":
            NEGATIVE_VALUES = False
            break
        else:
            print("Будь-ласка, оберіть варіант")
            continue


if __name__ == "__main__":
    excercise = choose_excercise()
    if excercise == "1":
        numbers = choose_numbers()
        if numbers != "До наступної зустрічі!":
            random_math()
    elif excercise == "2":
        exact_math()

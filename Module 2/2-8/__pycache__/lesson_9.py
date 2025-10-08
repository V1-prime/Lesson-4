def numbers_sum():
    try:

        number1 = int(input("Input your first number: ")) 
        print(f"{number1} + ")
        number2 = int(input("Input your second number: "))
        print(f"{number1} + {number2} = {number1 + number2}")
    except TypeError as e:
        print(e)

#numbers_sum()

# Завдання 2

# Напиши програму, яка запитує у користувача число і обчислює його 
# квадратний корінь. Оброби помилку, якщо введено від'ємне число. ** 2 num * num

def squear_number():
    
        number = int(input("Input your number: ")) 
        if number < 0:
            print("Number is negative")
            return
        print(f"{number} * {number} = {number ** 2}")
 
    
# Завдання 3

# Створи програму, яка запитує у користувача назву категорії задачі (наприклад, "робота", "домашні справи") і записує її в файл.
#  Оброби помилку, якщо не вдається відкрити файл для запису

def file_writer(file_name, text ):
    try:
        with open(file_name, 'w') as file:
            file.write(text)
    except Exception as e:
        print(e)
file_writer('text.txt','hi')


# Завдання 4

# Напиши програму, яка запитує у користувача два числа і ділить перше на друге.
#  Оброби помилку, якщо друге число дорівнює нулю.

def division(number1, number2):
    try:
        number1 = int(input("enter your first number: "))
        print("{number1} / ")
        number2 = int(input("enter your second number: "))
        print(f"{number1} / {number2} = {number1 / number2}")
    except Exception as e:
        print(" НЕ ДІЛИ НА НУЛЬ!!!")

division(10, 5)
division(10, 0)
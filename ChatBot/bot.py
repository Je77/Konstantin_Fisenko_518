print('Hello! My name is 口ひげを生やした帽子 .')
print('I was created in 2022')
print('Please, remind me your name.')
your_name = input("name:")
print('What a great name you have,' + your_name + '!')
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = (float(input("на 3:")))
remainder5 = (float(input("на 5:")))
remainder7 = (float(input("на 7:")))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')
number = int(input())
number += 1
for i in range(number):
    print(i, "!")
print('Completed, have a nice day!')
print("Let's test your programming knowledge.")
print("Почему мы используем методы?")
print("1. Повторить высказывание несколько раз.")
print("2. Разложить программу на несколько небольших подпрограмм.")
print("3. Определить время выполнения программы.")
print("4. Прервать выполнение программы.")
num = input(":")
while True:
    if num == "2":
        print('Completed, have a nice day!')
        print("Congratulations, have a nice day!")
        break
    else:
        print("Please, try again.")
        num = input(":")

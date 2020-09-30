# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.remove(min(nums))
    return sum(nums)


print(my_func(int(input('Первый аргумент: ')), int(input('Второй аргумент: ')), int(input('Третий аргумент: '))))

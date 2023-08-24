try:
    nums = input("Введите целые числа через пробел: ").split(" ")
    list_numbers = list(map(int,nums))
    number = int(input("Введите целое число: "))
except ValueError:
    print("Введены недопустимые символы!")

def sort (numbs):
    for i in range(1, len(numbs)):
        n = numbs[i]
        ind = i
        while ind > 0 and numbs[ind-1]>n:
            numbs[ind] = numbs[ind-1]
            ind -= 1
        numbs[ind] = n
    return numbs


def searcher(list, number, left, right):
    if left > right:
        return False
    middle = (right+left)//2
    if list[middle] >= number > list[middle-1]:
        return middle-1
    elif number < list[middle]:
        return searcher(list, number, left, middle-1)
    else:
        return searcher(list, number, middle+1, right)

list_numbers = sort(list_numbers)
if number <= list_numbers[0]:
    print("В указанной последовательности нет чисел меньше введённого")
elif number > list_numbers[-1]:
    print(len(list_numbers)-1)
else:
    print(searcher(list_numbers,number,0,len(list_numbers)-1))
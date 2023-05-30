#Вычисление сиракузской последовательности#
print('Программа вычисления сиракузской последовательности '
      'чисел и вычисления максимума в последовательности')
while True:
    try:
        n = int(input("Введите любое натуральное число "))
        if 1 < n <= 10000:
            print('')
            break
        else:
            raise ValueError
    except ValueError:
        print("Вы ввели не число или число не входит в указанный диапазон."
              " Попробуйте снова: ")

def syracuse_sequence(n: int) -> list[int]:
    list_n = [n]
    for n in list_n:
        if n % 2 == 0:
            list_n.append(n // 2)
        elif n % 2 == 1 and n != 1:
            list_n.append(3*n + 1)
    return list_n

def syracuse_max(list_n: list[int]) -> int:
    n_max = list_n[0]
    for n in list_n:
        n_max = n if n > n_max else n_max
    return n_max
def main(n):
    list_n = syracuse_sequence(n)
    for i in list_n:
        print(i, end=" ")
    n_max = syracuse_max(list_n)
    print("\nМаксимум в последовательности:")
    print(n_max)

if __name__ == "__main__":
    print("Cиракузская последовательность:")
    main(n)

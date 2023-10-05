while True:
    try:
        kod = int(input("Выберете задание или выберете 0 для выхода: "))
        match kod:
            case 1:
                def prime(n):
                    prime_numbers = []
                    num = 2
                    while len(prime_numbers) < n:
                        is_prime = True
                        for i in prime_numbers:
                            if num % i == 0:
                                is_prime = False
                                break
                        if is_prime:
                            prime_numbers.append(num)
                        num += 1
                    return prime_numbers[n - 1]


                while True:
                    try:
                        number = int(input("Введите номер простого числа: "))
                        break
                    except ValueError:
                        print("Необходимо ввести натуральное число")
                print(prime(number))
            case 2:
                def check_argument(arg):
                    if isinstance(arg, dict):
                        print(f"Ключ с минимальным значением: {min(arg)}")
                    elif isinstance(arg, list):
                        zero_elements_index = []
                        for i, value in enumerate(arg):
                            if value == 0:
                                zero_elements_index.append(i)
                        if len(zero_elements_index) >= 2:
                            result = arg[zero_elements_index[0] + 1] * arg[zero_elements_index[1] - 1]
                            print(f"Произведение между первым и вторым нулевыми элементами: {result}")
                        else:
                            print("Недостаточно нулевых элементов в списке")
                        unique_list = list(set(arg))
                        print(f"Список без повторяющихся элементов: {unique_list}")
                    elif isinstance(arg, int):
                        divisors = []
                        for i in range(1, arg + 1):
                            if arg % i == 0:
                                divisors.append(i)
                        print(f"Делители числа {arg}: {divisors}")
                    elif isinstance(arg, str):
                        is_palindrome = arg == arg[::-1]
                        print(f"Строка является палиндромом: {is_palindrome}")

                        def count_vowels(string):
                            vowels = ['a', 'e', 'y', 'u', 'i', 'o']
                            count = 0
                            for s in string:
                                if s.lower() in vowels:
                                    count += 1
                            return count

                        def count_consonants(string):
                            vowels = ['a', 'e', 'y', 'u', 'i', 'o']
                            count = 0
                            for char in string:
                                if char.lower() not in vowels and char.isalpha():
                                    count += 1
                            return count

                        vowels_count = count_vowels(arg)
                        consonants_count = count_consonants(arg)
                        print(f"Количество гласных: {vowels_count}")
                        print(f"Количество согласных: {consonants_count}")
                    else:
                        print("Неподдерживаемый тип аргумента")


                dictionary = {"a": 5, "b": 3, "c": 8, "d": 2}
                check_argument(dictionary)

                lst = [1, 0, 2, 3, 0, 4, 5]
                check_argument(lst)

                number = 12
                check_argument(number)

                string = "level"
                check_argument(string)

                check_argument(11.11)
            case 3:
                def input_matrix(m, n):
                    matrix = []
                    for i in range(m):
                        row = []
                        for j in range(n):
                            while True:
                                try:
                                    element = int(input(f"Введите элемент [{i}][{j+1}]: "))
                                    break
                                except ValueError:
                                    print("Необходимо ввести натуральное число")
                            row.append(element)
                        matrix.append(row)
                    return matrix


                def sum_of_rows(matrix):
                    sums = []
                    for row in matrix:
                        row_sum = sum(row)
                        sums.append(row_sum)
                    return sums

                while True:
                    try:
                        m = int(input("Введите количество строк: "))
                        break
                    except ValueError:
                        print("Необходимо ввести натуральное число")
                while True:
                    try:
                        n = int(input("Введите количество столбцов: "))
                        break
                    except ValueError:
                        print("Необходимо ввести натуральное число")

                matrix = input_matrix(m, n)
                for i in range(m):
                    for j in range(n):
                        print(f"\t{matrix[i][j]}", end=" ")
                    print("")

                row_sums = sum_of_rows(matrix)
                for i in range(len(row_sums)):
                    print(f"Сумма {i+1}-ой строки: {row_sums[i]}")
            case 4:
                def divide_numbers(a, b):
                    try:
                        result = a / b
                        print("Результат деления:", result)
                    except ZeroDivisionError:
                        print("Ошибка: Деление на ноль невозможно!")
                    finally:
                        print("Завершение работы программы")

                while True:
                    try:
                        a = int(input("Введите a: "))
                        break
                    except ValueError:
                        print("Необходимо ввести натуральное число")
                while True:
                    try:
                        b = int(input("Введите b: "))
                        break
                    except ValueError:
                        print("Необходимо ввести натуральное число")
                divide_numbers(a, b)
            case 0:
                break
    except ValueError:
        print("Необходимо ввести натуральное число")

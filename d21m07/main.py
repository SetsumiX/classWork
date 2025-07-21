# import threading
#
# def find_max(nums):
#     max_num = max(nums)
#     print(f"Максимальное значение списка {max_num}")
#     return max_num
#
# def find_min(nums):
#     min_num = min(nums)
#     print(f"Минимальное значение списка {min_num}")
#     return min_num
#
# inp_str = input("Введите через пробел числа >>> ")
#
# nums_list = list(map(float, inp_str.split()))
#
# thread_max = threading.Thread(target=find_max, args=(nums_list,))
# thread_min = threading.Thread(target=find_min, args=(nums_list,))
#
# thread_max.start()
# thread_min.start()
# thread_max.join()
# thread_min.join()
import multiprocessing
# import threading
#
# def calculate_sum(nums):
#     total = sum(nums)
#     print(f"Сумма чисел ровна {total}")
#     return total
#
# def calculate_average(nums):
#     average = sum(nums)/len(nums)
#     print(f"Среднее арифметическое {average:.2f}")
#     return average
#
# nums_list = list(map(float, input("Введите через пробел числа >>> ").split()))
#
# thread_sum = threading.Thread(target=calculate_sum, args=(nums_list,))
# thread_average = threading.Thread(target=calculate_average, args=(nums_list,))
#
# thread_sum.start()
# thread_average.start()
# thread_sum.join()
# thread_average.join()



# import threading
#
# def write_even_nums(nums, filename):
#     even_nums = [num for num in nums if num % 2 == 0]
#
#     with open(filename, "w") as file:
#         for num in even_nums:
#             file.write(f"{num}\n")
#
#     print(f"Количество чётных элементов: {len(even_nums)} шт.")
#
# def write_odd_nums(nums, filename):
#     odd_nums = [num for num in nums if num % 2 != 0]
#
#     with open(filename, "w") as file:
#         for num in odd_nums:
#             file.write(f"{num}\n")
#
#     print(f"Количество нечётных чисел: {len(odd_nums)} шт.")
#
# file_path = input("Введите путь к вашему файлу с числами >>> ")
#
# with open(file_path, "r") as file:
#     numbs = [int(line.strip()) for line in file if line.strip()]
#
# thread_even = threading.Thread(target=write_even_nums, args=(numbs, "even_numbers.txt"))
# thread_odd = threading.Thread(target=write_odd_nums, args=(numbs, "odd_numbers.txt"))
#
# thread_even.start()
# thread_odd.start()
#
# thread_even.join()
# thread_odd.join()



# import threading
#
# def search_word(file_path, word): # Не работает, 222
#     try:
#         with open(file_path, "r") as file:
#             content = file.read()
#             count = content.lower().count(word.lower())
#             print(f"Слово - {word}, было найдено - {count} шт.")
#
#     except FileNotFoundError:
#         print("Error - файл не найден")
#
# file_path = input("Введите путь к файлу, или его название >>> ")
# word_to_search = input("Введите слово для поиска >>> ")
# search_thread = threading.Thread(target=search_word, args=(file_path, word_to_search))
#
# search_thread.start()
# search_thread.join()



# import multiprocessing
#
# def calculate_square(numbers, result_queue):
#     squares = [num**2 for num in numbers]
#     result_queue.put(squares)
#
# def main():
#     inp_str = input("Введите числа через пробел >>> ")
#     numbers = list(map(int, inp_str.split()))
#     num_cores = multiprocessing.cpu_count()
#
#     print(f"Используется {num_cores} ядер процессора")
#
#     chunk_size = len(numbers)//num_cores
#     chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
#     result_queue = multiprocessing.Queue()
#
#     processes = []
#     for chunks in chunks:
#         process = multiprocessing.Process(target=calculate_square, args=(chunks, result_queue))
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
#     all_squares = []
#     while not result_queue.empty():
#         all_squares.extend(result_queue.get())
#
#     print(f"\nResults:")
#     for num, square in zip(numbers, sorted(all_squares)):
#         print(f"{num}\u00b2 = {square}")
#
# if __name__ == "__main__":
#     main()




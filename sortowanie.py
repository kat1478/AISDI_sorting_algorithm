# sortowanie.py

import os
import time
import gc
import sys
import matplotlib.pyplot as plt

# Importujemy funkcje sortujące z osobnych plików
from src.bubble_sort import bubble_sort
from src.selection_sort import selection_sort
from src.insertion_sort import insertion_sort
from src.merge_sort import merge_sort
from src.quick_sort import quick_sort

def read_words(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    words = text.split()
    return words[:n]

def measure_time(sort_function, data):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    sorted_data = sort_function(data)
    end = time.process_time()
    if gc_old:
        gc.enable()
    return end - start

def plot_results(sizes, times, algorithm_name):
    plt.figure()
    plt.plot(sizes, times, marker='o')
    plt.title(f'Czas sortowania dla {algorithm_name}')
    plt.xlabel('Liczba elementów')
    plt.ylabel('Czas (sekundy)')
    plt.grid(True)
    plt.savefig(f'images/{algorithm_name}.png')
    plt.close()

def test_sorting_algorithm(sort_function, algorithm_name, data_file):
    sizes = [1000 * i for i in range(1, 11)]  # n = 1000, 2000, ..., 10000
    times = []
    for n in sizes:
        data = read_words(data_file, n)
        time_taken = measure_time(sort_function, data)
        times.append(time_taken)
        print(f'{algorithm_name} - liczba elementów: {n}, czas: {time_taken:.5f} s')
    plot_results(sizes, times, algorithm_name)

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(script_dir, 'pan-tadeusz.txt')
    
    if not os.path.exists(data_file):
        print(f'Plik {data_file} nie istnieje. Upewnij się, że plik znajduje się w odpowiednim katalogu.')
        sys.exit(1)
    
    # Lista funkcji sortujących i ich nazw
    sorting_algorithms = [
        (bubble_sort, 'Bubble Sort'),
        (selection_sort, 'Selection Sort'),
        (insertion_sort, 'Insertion Sort'),
        (merge_sort, 'Merge Sort'),
        (quick_sort, 'Quick Sort'),
    ]
    
    for sort_function, algorithm_name in sorting_algorithms:
        print(f'\nTestowanie algorytmu: {algorithm_name}')
        test_sorting_algorithm(sort_function, algorithm_name, data_file)

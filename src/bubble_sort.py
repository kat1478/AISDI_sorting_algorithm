# sortowanie bąbelkowe

def bubble_sort(lst):
    n = len(lst)
    sorted_lst = lst.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_lst[j] > sorted_lst[j + 1]:
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
    return sorted_lst

# Test sprawdzający poprawność implementacji
if __name__ == '__main__':
    test_list = [3, 5, 1]
    assert bubble_sort(test_list) == [1, 3, 5], "Test nie powiódł się dla listy [3, 5, 1]"
    print("Test bubble_sort przeszedł pomyślnie.")

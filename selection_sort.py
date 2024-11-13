# sortowanie przez wybieranie

def selection_sort(lst):
    sorted_lst = lst.copy()
    n = len(sorted_lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if sorted_lst[j] < sorted_lst[min_idx]:
                min_idx = j
        sorted_lst[i], sorted_lst[min_idx] = sorted_lst[min_idx], sorted_lst[i]
    return sorted_lst

# Test sprawdzający poprawność implementacji
if __name__ == '__main__':
    test_list = [64, 25, 12, 22, 11]
    assert selection_sort(test_list) == [11, 12, 22, 25, 64], "Test nie powiódł się dla listy [64, 25, 12, 22, 11]"
    print("Test selection_sort przeszedł pomyślnie.")

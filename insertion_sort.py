# sortowanie przez wstawianie

def insertion_sort(lst):
    sorted_lst = lst.copy()
    for i in range(1, len(sorted_lst)):
        key = sorted_lst[i]
        j = i - 1
        while j >= 0 and key < sorted_lst[j]:
            sorted_lst[j + 1] = sorted_lst[j]
            j -= 1
        sorted_lst[j + 1] = key
    return sorted_lst

# Test sprawdzający poprawność implementacji
if __name__ == '__main__':
    test_list = [12, 11, 13, 5, 6]
    assert insertion_sort(test_list) == [5, 6, 11, 12, 13], "Test nie powiódł się dla listy [12, 11, 13, 5, 6]"
    print("Test insertion_sort przeszedł pomyślnie.")

# quick_sort

def quick_sort(lst):
    if len(lst) <= 1:
        return lst.copy()
    else:
        pivot = lst[0]
        less = [x for x in lst[1:] if x <= pivot]
        greater = [x for x in lst[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test sprawdzający poprawność implementacji
if __name__ == '__main__':
    test_list = [10, 7, 8, 9, 1, 5]
    assert quick_sort(test_list) == [1, 5, 7, 8, 9, 10], "Test nie powiódł się dla listy [10, 7, 8, 9, 1, 5]"
    print("Test quick_sort przeszedł pomyślnie.")

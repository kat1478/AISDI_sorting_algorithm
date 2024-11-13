# merge

def merge_sort(lst):
    if len(lst) <= 1:
        return lst.copy()
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_lst = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_lst.append(left[i])
            i += 1
        else:
            sorted_lst.append(right[j])
            j += 1
    sorted_lst.extend(left[i:])
    sorted_lst.extend(right[j:])
    return sorted_lst

# Test sprawdzający poprawność implementacji 
# asercja - spr i przerywa działanie przy błedach
if __name__ == '__main__':
    test_list = [38, 27, 43, 3, 9, 82, 10]
    assert merge_sort(test_list) == [3, 9, 10, 27, 38, 43, 82], "Test nie powiódł się dla listy [38, 27, 43, 3, 9, 82, 10]"
    print("Test merge_sort przeszedł pomyślnie.")

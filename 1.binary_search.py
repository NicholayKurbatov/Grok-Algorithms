def binary_search(sort_list: list, num: float | int | str) -> int:
    indx = None
    low = 0
    high = len(sort_list) - 1
    while low <= high:
        mid = (high - low) // 2
        if sort_list[low+mid] == num:
            return low + mid
        elif sort_list[low+mid] > num:
            high = low + mid - 1
        else:
            low = low + mid + 1
    return indx


if __name__ == "__main__":
    test1 = binary_search([1, 4, 5, 6, 7, 8, 30, 100], 30)
    assert test1 == 6, test1
import random


def selection_sort(nums):
    for sorted_idx in range(len(nums)):
        min_val_idx = sorted_idx
        for i in range(sorted_idx + 1, len(nums)):
            if nums[i] < nums[min_val_idx]:
                min_val_idx = i
        nums[sorted_idx], nums[min_val_idx] = nums[min_val_idx], nums[sorted_idx]
    return nums


if __name__ == '__main__':
    unsorted_list = [random.randint(1, 100) for _ in range(20)]
    print(unsorted_list)
    sorted_list = selection_sort(unsorted_list)
    print(sorted_list)
    # Check
    print('Sort OK') if sorted_list == sorted(unsorted_list) else print('Sort FAIL')

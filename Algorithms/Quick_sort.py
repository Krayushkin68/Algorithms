import random


def partition(nums, start, end):
    left_idx = start + 1
    right_idx = end - 1
    while left_idx <= right_idx:
        if nums[left_idx] <= nums[start]:
            left_idx += 1
        else:
            if nums[right_idx] <= nums[start]:
                nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
                left_idx += 1
                right_idx -= 1
            else:
                right_idx -= 1
    nums[start], nums[right_idx] = nums[right_idx], nums[start]

    if len(nums[start:right_idx]) > 1:
        partition(nums, start, right_idx)
    if len(nums[left_idx:end]) > 1:
        partition(nums, left_idx, end)


def quick_sort(nums):
    partition(nums, 0, len(nums))


if __name__ == '__main__':
    unsorted_list = [random.randint(1, 100) for _ in range(20)]
    print(unsorted_list)
    sorted_list = unsorted_list.copy()
    quick_sort(sorted_list)
    print(sorted_list)
    # Check
    print('Sort OK') if sorted_list == sorted(unsorted_list) else print('Sort FAIL')

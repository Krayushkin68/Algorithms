import random


def bubble_sort(nums):
    step_count = 0
    for step in range(len(nums) - 1, 0, -1):
        step_count += 1
        has_swap = False
        for i in range(step):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                has_swap = True
        if not has_swap:
            break
    print(f'{step_count} of {len(nums)} steps')
    return nums


if __name__ == '__main__':
    unsorted_list = [random.randint(1, 100) for _ in range(20)]
    print(unsorted_list)
    sorted_list = bubble_sort(unsorted_list)
    print(sorted_list)
    # Check
    print('Sort OK') if sorted_list == sorted(unsorted_list) else print('Sort FAIL')

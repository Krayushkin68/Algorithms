import random


def merge(left, right):
    result = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) or right_idx < len(right):
        if left_idx >= len(left):
            result.append(right[right_idx])
            right_idx += 1
            continue

        if right_idx >= len(right):
            result.append(left[left_idx])
            left_idx += 1
            continue

        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    return result


def merge_sort(nums):
    left, right = nums[:len(nums) // 2], nums[len(nums) // 2:]
    if len(left) == 1:
        if len(right) == 2:
            if right[0] > right[1]:
                right[0], right[1] = right[1], right[0]
        return merge(left, right)
    else:
        return merge(merge_sort(left), merge_sort(right))


if __name__ == '__main__':
    unsorted_list = [random.randint(1, 100) for _ in range(20)]
    print(unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)
    # Check
    print('Sort OK') if sorted_list == sorted(unsorted_list) else print('Sort FAIL')

import random


def heapify(nums, heap_size, root_idx):
    left_child = 2 * root_idx + 1
    right_child = 2 * root_idx + 2
    max_val_idx = root_idx

    if left_child < heap_size and nums[left_child] > nums[max_val_idx]:
        max_val_idx = left_child
    if right_child < heap_size and nums[right_child] > nums[max_val_idx]:
        max_val_idx = right_child

    if max_val_idx != root_idx:
        nums[root_idx], nums[max_val_idx] = nums[max_val_idx], nums[root_idx]
        # exclude sifting tree elements without children
        if max_val_idx * 2 + 1 < heap_size:
            heapify(nums, heap_size, max_val_idx)


def heap_sort(nums):
    # Build max-heap
    for i in range(len(nums) // 2 - 1, -1, -1):
        heapify(nums, len(nums), i)

    # Move the biggest element to the right and restore new heap
    for i in range(len(nums) - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
    return nums


if __name__ == '__main__':
    unsorted_list = [random.randint(1, 100) for _ in range(20)]
    print(unsorted_list)
    sorted_list = heap_sort(unsorted_list)
    print(sorted_list)
    # Check
    print('Sort OK') if sorted_list == sorted(unsorted_list) else print('Sort FAIL')

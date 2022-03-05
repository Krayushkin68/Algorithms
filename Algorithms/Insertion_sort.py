import random


def insertion_sort(nums):
    for i in range(1, len(nums)):
        ins_el = nums.pop(i)
        for j in range(i, 0, -1):
            if ins_el >= nums[j - 1]:
                nums.insert(j, ins_el)
                break
        else:
            nums.insert(0, ins_el)
    return nums


if __name__ == '__main__':
    unsorted_list = [random.randint(1, 100) for _ in range(20)]
    print(unsorted_list)
    sorted_list = insertion_sort(unsorted_list)
    print(sorted_list)
    # Check
    print('Sort OK') if sorted_list == sorted(unsorted_list) else print('Sort FAIL')

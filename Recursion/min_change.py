def listsum(numlist):
    if len(numlist) > 1:
        return numlist[0] + listsum(numlist[1:])
    else:
        return numlist[0]


def min_change_recursive(coin_values, summ, results={}):
    results = {}
    if summ in coin_values:
        results[summ] = summ
        return 1
    elif summ in results:
        return results[summ]
    else:
        min_changes = []
        for i in [el for el in coin_values if el < summ]:
            cur_min = 1 + min_change_recursive(coin_values, summ - i, results)
            min_changes.append(cur_min)
        results[summ] = min(min_changes)
        return min(min_changes)


def min_change_straight(coin_values, summ):
    change_line = [0] * (summ + 1)
    for val in range(summ + 1):
        min_coins = val
        for coin in [el for el in coin_values if el <= val]:
            if change_line[val - coin] + 1 < min_coins:
                min_coins = change_line[val - coin] + 1
        change_line[val] = min_coins
    return change_line[summ]


print(min_change_straight([1, 5, 10, 25, 21], 63))
print(min_change_recursive([1, 5, 10, 25, 21], 63))

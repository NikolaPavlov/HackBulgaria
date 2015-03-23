def group(items):
    result = []
    while len(items) != 0:
        current_group = take_same(items)
        result.append(current_group)
    items = items[len(current_group):]
    return result

print(group([1,1,1,2,3]))

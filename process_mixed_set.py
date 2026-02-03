def process_mixed_set(input_set):
    """
    处理包含数字和字符串的混合集合
    返回分类后的结果
    """
    numbers = []
    strings = []
    
    for item in input_set:
        if isinstance(item, (int, float)):
            numbers.append(item)
        else:
            strings.append(item)
    
    # 对数字进行排序
    numbers.sort()
    
    # 对字符串进行排序
    strings.sort()
    
    result = {
        'original_set': input_set,
        'numbers': numbers,
        'strings': strings,
        'sum_of_numbers': sum(numbers),
        'count_of_items': len(input_set)
    }
    
    return result

# 测试函数
test_set = {1, 2, 78, 'b', 121, 'a', 9}
result = process_mixed_set(test_set)
print("原始集合:", result['original_set'])
print("数字部分:", result['numbers'])
print("字符串部分:", result['strings'])
print("数字总和:", result['sum_of_numbers'])
print("元素总数:", result['count_of_items'])
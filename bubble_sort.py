def bubble_sort(arr):
    """
    冒泡排序算法
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    """
    # 创建数组的副本以避免修改原始数组
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # 遍历所有数组元素
    for i in range(n):
        # 标记是否发生了交换，用于优化
        swapped = False
        
        # 最后i个元素已经排好序了
        for j in range(0, n - i - 1):
            # 如果当前元素比下一个元素大，则交换它们
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # 如果没有发生交换，说明数组已经排好序了
        if not swapped:
            break
    
    return sorted_arr


def bubble_sort_inplace(arr):
    """
    原地冒泡排序（直接修改原数组）
    
    参数:
        arr: 待排序的列表
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break


# 示例和测试
if __name__ == "__main__":
    # 测试数据
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    # 使用非原地排序
    sorted_array = bubble_sort(test_array)
    print("排序后数组:", sorted_array)
    
    # 使用原地排序
    test_array2 = [64, 34, 25, 12, 22, 11, 90]
    print("\n原始数组:", test_array2)
    bubble_sort_inplace(test_array2)
    print("原地排序后:", test_array2)
    
    # 更多测试用例
    print("\n其他测试用例:")
    print("空数组:", bubble_sort([]))
    print("单元素:", bubble_sort([1]))
    print("已排序:", bubble_sort([1, 2, 3, 4, 5]))
    print("逆序:", bubble_sort([5, 4, 3, 2, 1]))
    print("重复元素:", bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]))


def bubble_sort_2d_to_1d(arr_2d):
    """
    对二维数组的每个子数组进行冒泡排序，然后将所有结果合并成一维数组
    
    参数:
        arr_2d: 二维列表
    
    返回:
        合并后的排好序的一维列表
    """
    result = []
    for sub_array in arr_2d:
        sorted_sub = bubble_sort(sub_array)
        result.extend(sorted_sub)
    return result


# 测试二维数组功能
if __name__ == "__main__":
    print("\n二维数组测试:")
    test_2d_array = [[64, 34, 25], [12, 22, 11], [90, 5]]
    print("原始二维数组:", test_2d_array)
    result_1d = bubble_sort_2d_to_1d(test_2d_array)
    print("排序并合并后的一维数组:", result_1d)
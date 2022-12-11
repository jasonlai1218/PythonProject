# https://steam.oxxostudio.tw/category/python/basic/comprehension.html

if __name__ == '__main__':

    """
    串列(list)生成式
    """
    # 單純寫法
    a = []
    for i in range(1, 10):
        a.append(i*i)
    # [1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(a)

    # 使用串列生成式
    b = [j*j for j in range(1, 10)]
    # [1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(b)

    """
    """

    a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    b = []
    for i in a:
        b.append(max(a) - i)  # 用 a 的最大值減去每個項目
    # [80, 70, 60, 50, 40, 30, 20, 10, 0]
    print(b)

    # 使用串列生成式
    b = [max(a) - i for i in a]
    # [80, 70, 60, 50, 40, 30, 20, 10, 0]
    print(b)

    """
    """

    # 將兩層 for 迴圈的 i 和 j 加在一起，變成新串列的項目
    a = []
    for i in 'abc':
        for j in range(1, 4):
            a.append(i + str(j))
    print(a)  # ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

    # 使用串列生成式
    a = [i + str(j) for i in 'abc' for j in range(1, 4)]
    # ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    print(a)

    # 99乘法表的值
    b = [i*j for i in range(1, 10) for j in range(1, 10)]
    print(b)

    # 串列生成式也可以加入 Python 的內建函式，針對產生的項目做處理
    a = [[100, 200, 300, 400, 500], [100, 200, 500, 2, 1]]
    b = []
    for i in a:
        b.append(min(i))  # 將二維串列中每個串列裡的最小值取出，變成新的串列
    # 1
    print(min(b))

    # 1
    print(min([min(i) for i in a]))

    """
    串列生成式搭配 if 
    如果將 if 放在 for 的前方，就必須加上 else ( 三元運算式 ( 條件運算式 ) 
    """
    # 單純寫法
    a = []
    for i in range(1, 10):
        if i % 2 == 0:
            a.append(i)  # 取出偶數放入變數 a
    # [2, 4, 6, 8]
    print(a)

    # 使用串列生成式
    a = [i for i in range(1, 10) if i % 2 == 0]
    # [2, 4, 6, 8]
    print(a)

    """
    """

    a = []
    for i in range(1, 10):
        if i % 2 == 0:
            a.append(i)  # 取出偶數放入變數 a
        else:
            a.append(100)  # 如果是奇數，將 100 放入變數 a
    # [100, 2, 100, 4, 100, 6, 100, 8, 100]
    print(a)

    # [100, 2, 100, 4, 100, 6, 100, 8, 100]
    a = [i if i % 2 == 0 else 100 for i in range(1, 10)]
    print(a)

    """
    字典(Dictionary)生成式
    result = {key: value for item in iterable}
    result：生成的新字典。
    key：生成的鍵。
    value：生成的值。
    item：從迭代物件裡取出的項目。
    iterable：可迭代的物件。
    """
    # 單純寫法
    a = {}
    for i in range(1, 10):
        a[i] = i * i  # 將 i*i 對應指定的鍵
    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    print(a)

    # 使用字典生成式
    a = {i: i * i for i in range(1, 10)}
    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    print(a)

    """
    集合(set)生成式
    result = {value for item in iterable}
    """
    # {64, 1, 4, 36, 9, 16, 49, 81, 25}
    a = set()
    for i in range(1, 10):
        a.add(i * i)  # 將 i*i 新增到集合裡
    print(a)

    # {64, 1, 4, 36, 9, 16, 49, 81, 25}
    a = {i * i for i in range(1, 10)}
    print(a)

    """
    元組(Tuple)生成式
    variable = tuple(value for item in iterable)
    variable：型別為 tuple 的變數。
    value：生成的值。
    item：從迭代物件裡取出的項目。
    iterable：可迭代的物件。
    """
    a = tuple(i for i in range(10))
    # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(a)

    a = tuple(i * i for i in range(10) if i > 5)
    # (36, 49, 64, 81)
    print(a)



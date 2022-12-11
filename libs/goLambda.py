from functools import reduce


class GoLambda:
    def __init__(self):
        pass

    @staticmethod
    def run_lambda():
        """
        lambda
        (1)lambda關鍵字
        (2)parameter_list(參數清單)
        (3)expression(運算式)

        :後面放條件或是運算式

        Lambda函式與一般函式(Function)的差異為：
        Lambda函式不需要定義名稱，而一般函式(Function)需定義名稱。
        Lambda函式只能有一行運算式，而一般函式(Function)可以有多行運算式。
        Lambda在每一次運算完會自動回傳結果，而一般函式(Function)如果要回傳結果要加上 return 關鍵字。

        適度的使用讓程式碼簡潔了許多。
        不過也建議避免過度使用與撰寫複雜的Lambda函式，不然程式碼將不易維護，
        複雜的邏輯運算，還是優先選擇一般函式(Function)較為理想。
        """
        multipy = lambda x, y: x * y
        # 8
        print(multipy(4, 2))

        """
        immediately invoked function expression
        利用 function expression 的方式來建立函式，並且立即執行它，範例如下
        """
        # 8
        print((lambda x, y: x * y)(4, 2))

        title = "HelloPython"
        # 當Lambda函式經定義後，沒有進行呼叫的動作，他會回傳一個function object且包含了記憶體位址
        # <function <lambda> at 0x7fa6780e8620>
        print(lambda title: print(title))
        # HelloPython
        (lambda title: print(title))(title)

        """
         filter()：在可疊代的物件中，依據條件運算式，選擇特定的元素
        
         filter(lambda parameter: expression, iterable)
        """
        numbers = [50, 2, 12, 30, 27, 4]
        result = filter(lambda x: x > 10, numbers)
        # <filter object at 0x7fbeb810ccc0>
        print(result)
        # [50, 12, 30, 27]
        print(list(result))

        """
         map()：在可疊代的物件中，在可疊代的物件中，套用特定運算式於每一個元素
        
         map(lambda parameter: expression, iterable)
        """
        numbers = [50, 2, 12, 30, 27, 4]
        result = map(lambda x: x * 2, numbers)
        # [100, 4, 24, 60, 54, 8]
        print(list(result))

        """
        reduce()：與map()內建方法同樣在可疊代的物件中，套用特定運算式於每一個元素，但是內部的實作方式不一樣，它的實作步驟為：
        (1)將可疊代物件中的前兩個元素先進行Lambda運算式的運算。
        (2)接著將第一個步驟的運算結果和可疊代物件中的下一個元素(第三個)傳入Lambda函式進行運算。
        (3)依此類推，直到可疊代物件的元素都運算完成。
        
        這需要額外form functools import reduce
        reduce(lambda parameter1, parameter2: expression, iterable)
        """
        numbers = [50, 2, 12, 30, 27, 4]
        result = reduce(lambda x, y: x + y, numbers)
        # 50+2+12+30+27+4
        print(result)

        """
        sorted()：用來排序可疊代物件中的元素
        
        sorted(iterable, key=lambda parameter: expression)
        """
        cars = [
            ("mazda", 2000),
            ("toyota", 1000),
            ("benz", 5000)
        ]
        # [('toyota', 1000), ('mazda', 2000), ('benz', 5000)]
        print(sorted(cars, key=lambda car: car[1]))

        """
        min
        min(dates, key=lambda x: abs(int(x) - int(pivot)))
        """



# 汽車類別
class Cars:
    # 建構式
    def __init__(self, weight):
        self.weight = weight

    # 寫法(一)
    # def get_weight(self):
    #     return self.__weight
    #
    # def set_weight(self, value):
    #     if value <= 0:
    #         raise ValueError("Car weight cannot be 0 or less.")
    #     self.__weight = value

    # 寫法(二) , Pythonic (Python的特點風格)
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Car weight cannot be 0 or less.")
        self.__weight = value

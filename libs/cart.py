
# define object
class Cars:

    # 類別屬性
    door = 4

    # Constructor
    # 初始化物件(Object)的屬性值(Attribute)。至少要有一個self參數，之後利用逗號區隔其他屬性
    # 第一個self參數，Python編譯器會幫我們把目前物件的參考(mazda)傳給建構式(Constructor)
    def __init__(self, color, seat):
        # define Property(屬性)
        self.color = color
        self.seat = seat

    # 實體方法(Instance Method)
    # self參數指向該物件(Object)
    # 簡單說 帶有 instance 為參數的 method
    def drive(self):
        print(f"My Car is {self.color} and {self.seat} seats.")

    # 實體方法(Instance Method)
    def drive2(self):
        self.__class__.door = 5

    # 類別方法(Class Method)
    # 由於類別方法(Class Method)的cls參數指向類別(Class)，
    # 所以類別方法(Class Method)僅能改變類別的狀態，
    # 而無法改變物件(Object)的狀態，
    # 因為它沒有self參數可以存取物件的屬性(Attribute)及方法(Method)
    """
    在 Object Oriented 中，一般來說，一個 class 裡面的所有 method 都叫做 class method！
    但在 Python 裡，有一個概念特別獨立出來稱為 class method ，
    是當一個 method 是帶有 class 本身作為參數傳入時，
    我們稱之為 class method，當然 Python 也已經提供 decorator 
    @classmethod 給我們用囉，很方便對不對！
    """
    # 簡單說 帶有 class 為參數的 method
    @classmethod
    def open_door(cls):
        print(f"{cls} has {cls.door} doors.")

    # 跑車則呼叫跑車類別方法(Class Method)來建立跑車，
    # 至於物件(Object)的初始化過程(建造跑車的過程)封裝在類別方法中(Class Method)，
    # 它會幫我們完成並回傳，就像建立物件(Object)的工廠一樣，
    # 所以類別方法(Class Method)也被稱為工廠方法(Factory Method)，讓程式碼簡潔且易於維護。
    # 廂型車
    @classmethod
    def van(cls):
        return cls("black", 6)

    # 跑車
    @classmethod
    def sports_car(cls):
        return cls("yellow", 4)


class Motorcycle:
    pass




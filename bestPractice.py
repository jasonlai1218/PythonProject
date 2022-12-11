# 進階學習
# https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-2-static-class-abstract-methods%E4%B9%8B%E5%AF%A6%E7%8F%BE-1e3b3998bccf
# https://www.w3schools.com/python/python_datetime.asp
"""
introduce Class
introduce Class (Enum) -> not yet
introduce Lambda
introduce Function -> Typing
introduce Data Type
introduce List -> 可以使用生成式寫法(Comprehension) -> defaultdict
introduce String
introduce Tuples -> 可以使用生成式寫法(Comprehension)
introduce Dict -> 可以使用生成式寫法(Comprehension) -> defaultdict
introduce For - Loop -> 可以使用生成式寫法(Comprehension)
introduce try/except
introduce Assert
introduce Type Cast
introduce beartype
introduce Dates  -> not yet
introduce RegEx  -> not yet
introduce JSON  -> not yet
introduce File I/O  -> not yet

import os
import resource
import inspect
import json
import math
import fastavro
import snappy
from io import BytesIO
from functools import partial
"""


from libs.cart import Cars, Motorcycle
from libs.goFunctions import GoFunction
from libs.goLambda import GoLambda
from collections import defaultdict
from typing import List, Union, Dict, Any, Callable
# python 3.7
# from typing import TypedDict
from beartype import beartype


def introduce_class():
    mazda = Cars('red', 4)

    # isinstance()來判斷類別(Class)與物件(Object)的關係
    # true
    print(isinstance(mazda, Cars))
    # false
    print(isinstance(mazda, Motorcycle))

    # get attribute value in object
    # red
    print(mazda.color)
    # 4
    print(mazda.seat)

    # set attribute value in object
    mazda.color = 'green'
    mazda.seat = 5

    # execute object method
    # My Car is green and 5 seats.
    mazda.drive()

    print("Cars original door: ", Cars.door)
    mazda.drive2()
    print("Cars new door: ", Cars.door)

    van = Cars.van()
    print(f"{van.color} , {van.seat}")
    sports_car = Cars.sports_car()
    print(f"{sports_car.color} , {sports_car.seat}")
    # print("color:" + sports_car.color + " , seat:" + sports_car.seat)


def get_first_char(s: str) -> str:
    return s[1]


def test(x: List[int]):
    pass


# 能夠同時接受字串與數字
def print_something(x: Union[int, str]):
    if isinstance(x, (int, str, )):
        print(f'Got {x}')
    else:
        raise TypeError('Only int & str are accepted')


# key 是字串， value 是整數
def update_count(mapping: Dict[str, int], key: str, count: int):
    mapping[key] = count


# 該字典必須有 username 與 password 2 個 key 存在才行
# class LoginDict(TypedDict):
#     username: str
#     password: str
# login_dict: LoginDict = {
#     'username': 'abc',
#     'password': 'pass123456',
# }
# def valid_username_password(login_dict: LoginDict):
#     pass


# 如果是不限定型別的情況下，可以使用 typing.Any ，譬如 print 其實就很適合可以使用 typing.Any
def print_anything(*args: Any):
    print(*args)


# Callable 作為函數返回值使用，其實只做一個類型檢查的作用，看看返回得值是否可使用
def date(year: int, month: int, day: int) -> str:
    return f'{year}-{month}-{day}'


def get_date_fn() -> Callable[[int, int, int], str]:
    return date

# Generator


@beartype
def test_bear_type(s: str) -> None:
    print(f"str : {s}")


if __name__ == '__main__':

    """
    introduce Class(object/attribute/method)
    """
    introduce_class()

    """
    introduce Class(Enum)
    """

    """
    introduce Lambda
    """
    # use static method
    GoLambda.run_lambda()

    """
    introduce Function
    
    基本上，Python的函式都有回傳值，為什麼會這樣說呢？
    當我們用一個變數來接無回傳值函式的結果時，
    從執行結果可以看到Python隱含回傳了一個None給我們
    
    關鍵字參數(Keyword Argument)：呼叫函式時，在傳入參數值的前面加上函式所定義的參數名稱，
    如下範例。除了提高可讀性外，也可將此種參數打包成字典(Dictionary)資料型態
    
    預設值參數(Default Argument)：在函式定義的參數中，將可以選擇性傳入的參數設定一個預設值，
    當來源端有傳入該資料時，使用來源端的資料，沒有傳入時，則依照設定的預設值來進行運算
    
    當來源端有傳入日期參數資料(2019/10/10)，函式就會使用其值來進行運算。
    特別注意，必要參數(Required Argument)一定要放在預設值參數(Optional Argument)的前面。
    
    當我們要傳入大量的參數時，在函式上定義過多的參數名稱會讓程式碼的可讀性降低，
    可以使用 * 符號來將傳入參數進行打包會將參數資料打包成元組(Tuple)資料型態，
    如果想打包成字典(Dictionary)資料型態，則可以使用 ** 符號
    這邊要注意在呼叫函式時，一定要使用關鍵字參數(Keyword Argument)
    keyword argument -> dict key
    
    在這邊呼籲大家，非必要避免在函式中修改全域變數的值，
    因為永遠不會知道程式的其他地方有沒有使用了這個全域變數來進行運算，
    而在函式中修改了它的值後，
    很容易導致程式的副作用(Side Effect)或錯誤(Bug)。
    """
    # use static method
    # 40
    GoFunction.calculate_number(30)
    result = GoFunction.calculate_number(30)
    # None
    print(result)
    result = GoFunction.calculate_number2(30)
    # 40
    print(result)

    # Mike use the func_A01 on 2019/12/21
    GoFunction.app_log(name="Mike", func_id="func_A01")
    # *符號 變成tuple
    # ('Make', 'func_A01', '2019/10/10')
    GoFunction.service_log("Make", "func_A01", "2019/10/10")
    # ** 符號 變成dict
    # {'name': 'Make', 'func_id': 'func_A01', 'date': '2019/10/10'}
    GoFunction.container_log(name="Make", func_id="func_A01", date="2019/10/10")

    """
    Typing
    
    list 型態的變數傳進 get_first_char 中也未導致任何錯誤，
    證明型別註釋(type annotations)僅是類似註解般的存在，
    沒有任何強迫必須使用特定型別的效果，但即使如此，
    型別註釋也為 Python 帶來更好的可維護性。
    """
    # b
    print(get_first_char('abc'))
    # 2
    print(get_first_char([1, 2, 3]))

    # Callable
    date = get_date_fn()
    print(date(2022, 11, 21))

    """
    introduce Data Type
    
    字串(String)：Python的字串表示方式，就是在文字的前後加上雙引號" 
    或單引號' 兩種都可以，不過建議大家，
    選擇一種來使用就好，避免在程式碼中有些使用單引號，又有些使用雙引號。
    如果要表示多行的文字，則使用三個雙引號"
    
    數值(Number)：就是我們在數學上所使用的數字，
    在Python中，數值的資料又分為兩種，分別是：
    整數(Integer)：只要是沒有小數點的數值，就叫整數。
    浮點數(Float)：相反的，只要是有小數點的數值，就叫浮點數。
    布林值(Boolean)：布林值就像是我們口語中的「是」和「否」，
    在Python中，以True來代表「是」，False代表「否」
    Python是一個區分大小寫的程式語言，舉例來說，True和TRUE是不一樣的，
    所以這邊的「True」和「False」要打得一模一樣才代表布林值唷。
    註解(Comment)
    可以使用#符號開頭，接著後面撰寫想要的文字說明
    如果不想執行某段程式碼，同樣可以在前面加上#符號。
    因為編譯器看到#符號，就不會去執行加在#符號後面的程式碼。
    """
    title = "Learn Code with Jason"
    author = 'Jason'
    content = """
    Hi guys, my name is Jason.
    Welcome to my blog.
    """

    # 整數(Integer)
    price = 100

    # 浮點數(Float)
    rate = 30.2

    # 布林值
    is_male = True
    is_female = False

    """
    introduce List
    List(串列)是一個Python非常重要的資料型態，
    它就像是一個容器，可以用來存放多個不同資料型態的資料(元素)，
    以逗號分隔並且用 [] 符號將所有元素括起來
    串列的特性：
    Iterable(可疊代的)：所以上一篇文章介紹的Python迴圈可以應用在串列上。
    Modifiable(可修改的)：串列中的元素可以透過Python提供的串列方法(Method)
    來進行修改。
    建立串列的方法:直接於 [] 符號中輸入元素資料
    存取串列元素的方法
    新增串列元素的方法
    修改串列元素的方法
    刪除串列元素的方法
    尋找串列元素的方法
    """
    # 建立串列(1)
    numbers = [1, 2, 3, 4]
    numbers = ["Perter", "Harry", "Mike"]
    # 可以存放不同資料型態的資料
    complexes = [1, "Peter", 2, 3, "Mike"]
    # 建立串列(2)
    # 使用Python的list()方法，傳入Iterable(可疊代的)
    # 物件來建立串列。
    title = list("HelloPython")
    # ['H', 'e', 'l', 'l', 'o', 'P', 'y', 't', 'h', 'o', 'n']
    print(title)

    numbers = list(range(10))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers)
    # 使用 [::遞增(減)值]
    # [0, 3, 6, 9]
    print(numbers[::3])

    # 使用 * 符號來建立多個相同元素的串列
    title = ["H"] * 3
    # ['H', 'H', 'H']
    print(title)
    numbers = [1] * 3
    # [1, 1, 1]
    print(numbers)

    # 存取串列元素的方法(1)
    names = ["Peter", "Harry", "Mike", "Marry"]
    # Peter Harry Mike Marry
    print(*names)
    # 存取串列第三個元素
    # Mike
    print(names[2])
    # 存取串列最後一個元素
    # Marry
    print(names[-1])
    # 存取第一個元素到第三個元素
    # [0:3]代表0~2 但不包含3
    # ['Peter', 'Harry', 'Mike']
    print(names[0:3])
    # 存取第二個元素到最後一個元素
    # ['Harry', 'Mike', 'Marry']
    print(names[1:])
    # 複製串列
    # ['Peter', 'Harry', 'Mike', 'Marry']
    print(names[:])
    # 存取串列元素的方法(2)
    # 以透過Python迴圈來讀取串列中的每一個元素，
    # 因為串列也是Iterable(可疊代的)
    for name in names:
        # Peter
        # Harry
        # Mike
        # Marry
        print(name)

    # 新增串列元素的方法(1)
    # 將元素新增至串列最後
    names.append("Jason")
    # ['Peter', 'Harry', 'Mike', 'Marry', 'Jason']
    print(names)
    # 新增串列元素的方法(2)
    # 將元素新增至串列的特定位置，注意Python串列的位置索引值從0開始。
    names.insert(1, "Jason")
    # ['Peter', 'Jason', 'Harry', 'Mike', 'Marry', 'Jason']
    print(names)

    # 修改串列元素的方法
    # 使用 [] 符號存取想修改的索引值，接著指派新的值
    # ['Peter', 10, 'Harry', 'Mike', 'Marry', 'Jason']
    names[1] = 10
    print(names)

    # 刪除串列元素的方法(1)
    # 使用pop()方法，將串列的最後一個元素刪除。
    # 如果想刪除特定位置的元素，則傳入位置索引值。
    names.pop()
    # ['Peter', 10, 'Harry', 'Mike', 'Marry']
    print(names)
    # 刪除 指定第二個元素
    names.pop(1)
    ['Peter', 'Harry', 'Mike', 'Marry']
    print(names)
    # 刪除串列元素的方法(2)
    # 刪除特定範圍的元素，可以使用del 指令，指定要刪除的範圍位置索引值。
    # 刪除 第一個到第二個元素
    del names[0:2]
    # ['Mike', 'Marry']
    print(names)
    # 刪除串列元素的方法(3)
    # 當不知道元素的位置索引值，可以使用Remove()方法，傳入想刪除的元素。
    # 注意如果此元素在串列中有多個，Remove()方法只會刪除第一個出現的。
    names.remove("Marry")
    # ['Mike']
    print(names)
    # 刪除串列元素的方法(4)
    # 清空串列可以使用clear()方法。
    names.clear()
    # []
    print(names)

    # 尋找串列元素的方法
    names = ["Peter", "Harry", "Mike", "Marry"]
    # 2
    print(names.index("Mike"))
    # 如果要尋找的串列元素不在串列中，則會出現錯誤訊息
    # ValueError: 'Jack' is not in list
    # print(names.index("Jack"))
    # 所以比較好的寫法是在取得元素的索引值前，先判斷該元素是否在串列中
    if "Jack" in names:
        print(names.index("Jack"))
    else:
        print("Jack is not in list.")
    # 使用count()方法，可以將要尋找的串列元素傳入，
    # 它會回傳該元素在串列中的個數。
    names = ["Peter", "Harry", "Mike", "Harry"]
    # 2
    print(names.count("Harry"))

    """
    introduce String
    (1)字串連接(String concatenating)
    (2)字串格式化(String formatting)
    (3)字串裁切(String slicing)
    
    (1)upper()：將字串轉為大寫字母
    (2)lower()：將字串轉為小寫字母
    (3)capitalize()：將字串的首字轉為大寫字母
    (4)title()：將字串中的每個單字字首轉為大寫字母
    (5)len()：取得字串的文字總數
    (6)strip()：清除字串的前後空白
    (7)split():字串分割
    (8)replace():字串取代
    (9)contain -> in
    (10)compare -> ==
    (11)reverse() -> [::-1]
    """
    first_name = "Mike"
    last_name = "Ku"
    name = first_name + " " + last_name
    # 字串連接
    # Mike Ku
    print(name)
    # 字串格式化
    # I'm 28 years old.
    print(f"I'm { 20 + 8 } years old.")
    blog_name = "Learn Code with Jason"
    # 第一個字元
    # L
    print(blog_name[0])
    # 最後一個字元
    # n
    print(blog_name[-1])
    # 部分字串 , 取第6~9個字元(從0開始算)
    # Code
    print(blog_name[6:10])
    # 取第6~到最後(從0開始算)
    # Code with Jason
    print(blog_name[6:])
    # 複製原字串
    # Learn Code with Jason
    print(blog_name[:])
    # LEARN CODE WITH JASON
    print(blog_name.upper())
    # learn code with jason
    print(blog_name.lower())
    # Learn code with jason
    print(blog_name.capitalize())
    # Learn Code With Jason
    print(blog_name.title())
    # 21
    print(len(blog_name))
    # Learn Code with Jason
    print(blog_name.strip())
    # Learn
    print(blog_name.split(" ")[0])
    # Learn Code with Mike
    print(blog_name.replace("Jason", "Mike"))
    # Found!
    substring = "h Jas"
    if substring in blog_name:
        print("Found!")
    else:
        print("Not Found!")
    # Match!
    blog_name2 = "Learn Code with Jason"
    if blog_name == blog_name2:
        print("Match!")
    else:
        print("Not Match!")
    # nosaJ htiw edoC nraeL
    print(blog_name[::-1])

    """
    introduce Tuples
    Tuples(元組)是Python另一個資料型態，
    它和List(串列)一樣是一個容器，
    能夠存放多個不同資料型態的資料(元素)，
    同樣以逗號區隔，但是是以 () 符號將所有元素括起來
    
    Tuples(元組)有幾個特性：
    Iterable(可疊代的)：和List(串列)一樣，可以透過Python迴圈來進行讀取。
    Unmodifiable(不可修改的)：這個特性是Tuples(元組)和List(串列)最大的不同，
    Tuples(元組)中的元素不可修改，只能唯讀，
    所以它不像List(串列)有任何可以修改元素的方法(Method)，像是新增、修改及刪除元素。
    主要應用的情境在於防止資料被意外的修改
    
    建立Tuples的方法
    存取Tuples元素的方法
    尋找Tuples元素的方法
    """
    # 建立Tuples(1)
    ages = (26, 30, 40, 50)
    titles = ("HelloPython", "Python Tuples")
    # 可存放不同型別的資料
    values = (10, 20, "HelloPython")
    # 建立Tuples(2)
    # 直接指派資料，並且以逗號區隔
    ages = 26, 30, 40, 50
    # (26, 30, 40, 50)
    print(ages)
    # ages data type:  <class 'tuple'>
    print("ages data type: ", type(ages))
    values = 10,
    # (10,)
    print(values)
    # values data type:  <class 'tuple'>
    print("values data type: ", type(values))
    # 建立Tuples(3)
    # 使用tuple()方法，傳入Iterable(可疊代的)物件來建立Tuples(元組)
    ages = tuple([26, 30])
    # (26, 30)
    print(ages)
    names = tuple("Jason")
    # ('J', 'a', 's', 'o', 'n')
    print(names)
    numbers = tuple(range(10))
    # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(numbers)

    # 存取Tuples元素
    # Tuples(元組)存取元素的方式和List(串列)、String(字串)一樣，
    # 使用 [] 符號並傳入索引值(從0開始計算)來進行存取
    ages = (25, 30, 40, 50)
    # 30
    print(ages[1])
    # 取得特定範圍的Tuples(元組)元素，使用 [:] 符號並傳入索引值
    # (30, 40, 50)
    print(ages[1:])
    # Tuples(元組)和List(串列)、String(字串)一樣
    # 可以透過Python迴圈來讀取每一個元素，
    # 因為Tuples(元組)也是Iterable(可疊代的)
    for age in ages:
        # 25
        # 30
        # 40
        # 50
        print(age)

    # 可以使用index()方法，將要尋找的Tuples元素傳入，來取得該元素的索引值
    # 1
    print(ages.index(30))
    # 在取得Tuples元素索引值前，和List(串列)一樣先判斷該元素是否在Tuples中，
    # 否則當元素不在Tuples中時，會發生ValuesError例外錯誤
    # 100 not in tuples.
    if 100 in ages:
        print(ages.index(100))
    else:
        print("100 not in tuples.")

    # 將要尋找的Tuples元素傳入，來取得該元素在Tuples中的個數
    ages = (25, 30, 40, 25, 60, 25)
    # 3
    print(ages.count(25))

    """
    introduce Dict
    Dictionary(字典)，同樣是一個容器(集合)可以用來存放不同資料型態的資料，
    不過與串列(List)、元組(Tuples)不一樣的地方是，
    它的每一個元素是以鍵(Key)及值(Value)構成，再由 {} 符號將所有元素括起來
    字典的特性：
    Iterable(可疊代的)：和前面介紹的字串(String)、串列(List)及元組(Tuples)一樣是可疊代的物件，
    可以透過Python迴圈來進行元素的讀取。
    Modifiable(可修改的)
    Key-Value pairs(鍵與值)：Dictionary(字典)的每一個元素由鍵(Key)及值(Value)構成。
    鍵(Key)的資料型態通常我們使用String(字串)或Integer(整數)，而值(Value)可以是任何資料型態。
    存取串列元素的方法
    新增串列元素的方法
    修改串列元素的方法
    刪除串列元素的方法
    尋找串列元素的方法
    """
    # 建立Dictionary(1)
    heights = {"Mike": 170, "Peter": 165}
    cars = {1: "nissan", 2: "toyota"}
    # {'Mike': 170, 'Peter': 165}
    print(heights)
    # {1: 'nissan', 2: 'toyota'}
    print(cars)
    # 建立Dictionary(2)
    heights = dict(Mike=170, Peter=165)
    # can't
    # cars = dict(1="nissan", 2="toyota")

    # 存取Dictionary(1)
    # 170
    print(heights["Mike"])
    # 當存取的鍵(Key)名稱不在字典(Dictionary)中時，會發生KeyError的例外錯誤
    # 解決方式(1)先使用Python條件判斷來檢查元素是否在字典(Dictionary)中
    # 解決方式(2)get() -> 不存在就回傳None
    # 方法也提供了第二個參數，來自行設定當鍵(Key)
    # 名稱不存在時，要回傳的值(Value)。
    if "Harry" in heights:
        print(heights["Harry"])

    # None
    print(heights.get("Harry"))
    # 0
    print(heights.get("Harry", 0))
    # 存取Dictionary(2)
    # Python迴圈每一次讀取字典(Dictionary)時，只能存取到鍵(Key)的名稱
    for height in heights:
        # Mike
        # Peter
        print(height)
    # 想要同時存取鍵(Key)與值(Value)的話，有兩種方法
    # 第一種可以使用items()方法，回傳一個Tuples(元組)
    # 第二種方法則可以使用Python的Unpacking()
    for height in heights.items():
        # ('Mike', 170)
        # ('Peter', 165)
        print(height)

    # 新增Dictionary元素
    heights["John"] = 175
    # {'Mike': 170, 'Peter': 165, 'John': 175}
    print(heights)

    # 修改Dictionary元素
    heights["Peter"] = 160
    # {'Mike': 170, 'Peter': 160, 'John': 175}
    print(heights)

    # 刪除Dictionary元素
    del heights["Peter"]
    # {'Mike': 170, 'John': 175}
    print(heights)
    # 使用clear()方法，刪除字典(Dictionary)中的所有元素。
    heights.clear()
    # {}
    print(heights)

    """
    defaultdict
    """
    # 原本寫法
    a_list = ['a', 'b', 'x', 'a', 'a', 'b', 'z']
    counter_dict = {}
    for element in a_list:
        if element not in counter_dict:
            counter_dict[element] = 1
        else:
            counter_dict[element] += 1

    # 新寫法(不用檢查)
    # 記得要 from collections import defaultdict
    better_dict = defaultdict(list)  # default值以一個list()方法產生
    check_default = better_dict['a']
    print(check_default)  # 會輸出list()方法產生的空串列[]

    better_dict['b'].append(1)  # [1]
    better_dict['b'].append(2)  # [1,2]
    better_dict['b'].append(3)  # [1,2,3]
    # [1, 2, 3]
    print(better_dict['b'])

    # 原本寫法
    key_values = [('even', 2), ('odd', 1), ('even', 8), ('odd', 3), ('float', 2.4), ('odd', 7)]

    multi_dict = {}
    for key, value in key_values:
        if key not in multi_dict:
            multi_dict[key] = [value]
        else:
            multi_dict[key].append(value)

    # 新寫法
    multi_dict = defaultdict(list)
    key_values = [('even', 2), ('odd', 1), ('even', 8), ('odd', 3), ('float', 2.4), ('odd', 7)]

    for key, value in key_values:
        multi_dict[key].append(value)

    # 會輸出defaultdict(<class 'list'>, {'float': [2.4], 'even': [2, 8], 'odd': [1, 3, 7]})
    print(multi_dict)
    # [1, 3, 7]
    print(multi_dict["odd"])

    """
    introduce For - Loop
    range(起始值,結束值,遞增(減)值)
    range(20)：起始值預設從0開始，所以會產生0到19的整數序列。
    range(10,20)：起始值從10開始，所以會產生10到19的整數序列。
    range(10,20,3)：起始值從10開始，遞增值為3，所以會產生10,13,16,19的整數序列
    
    可以針對Iterable(可疊代的)物件來進行讀取
    break：直接中斷迴圈，在break指令之後的運算皆不會執行
    """
    for letter in "Mike":
        for number in range(2):
            # M 0
            # M 1
            # i 0
            # i 1
            # k 0
            # k 1
            # e 0
            # e 1
            print(letter, number)
    # While-Loops
    number = 10
    while number < 50:
        number = number * 2
        # 20
        # 40
        # 80
        print(number)

    for number in range(1, 10):
        if number % 3 == 0:
            break
        # 1
        # 2
        print(number)

    for number in range(1, 10):
        if number % 3 == 0:
            continue
        # 1
        # 2
        # 4
        # 5
        # 7
        # 8
        print(number)

    """
    if
    如果要連接多個條件判斷時，就要使用到邏輯運算子，包含and、or及not
    """
    price = 70
    if price > 120:
        print("Don't buy it.")
    elif price > 60:
        print("It's ok.")
    else:
        print("It's cheap.")

    member = True
    admin = False
    # 只要一個是True就可以了
    if member or admin:
        print("You have 50% OFF.")
    member = False
    # 最好選擇正向表列的方式
    if not member:
        print("You don't have discount")

    """
    introduce try/except
    NameError	使用沒有被定義的對象
    IndexError	索引值超過了序列的大小
    TypeError	數據類型 ( type ) 錯誤
    SyntaxError	Python 語法規則錯誤
    ValueError	傳入值錯誤
    KeyboardInterrupt	當程式被手動強制中止
    AssertionError	程式 asset 後面的條件不成立
    KeyError	鍵發生錯誤
    ZeroDivisionError	除以 0
    AttributeError	使用不存在的屬性
    IndentationError	Python 語法錯誤 ( 沒有對齊 )
    IOError	Input/output異常
    UnboundLocalError	區域變數和全域變數發生重複或錯誤
    """
    value = -1
    try:
        if value <= 0:
            raise ValueError("Car weight cannot be 0 or less.")
    except ValueError as msg:
        # print("Car weight cannot be 0 or less.")
        print(msg)
    except NameError:
        print("value is not defined")

    """
    introduce Assert
    """
    value = True
    assert value, "value is False"

    value = False
    try:
        assert value, "value is False"
    except AssertionError as msg:
        print(msg)
    else:
        print("完全沒錯才會執行這行")
    finally:
        print("不論有沒有錯都會執行這行")

    """
    introduce Type Cast
    """
    x = int(1)  # x will be 1
    y = int(2.8)  # y will be 2
    z = int("3")  # z will be 3

    x = float(1)  # x will be 1.0
    y = float(2.8)  # y will be 2.8
    z = float("3")  # z will be 3.0
    w = float("4.2")  # w will be 4.2

    x = str("s1")  # x will be 's1'
    y = str(2)  # y will be '2'
    z = str(3.0)  # z will be '3.0'

    """
    introduce beartype
    """
    test_bear_type("test")
    # cause beartype.roar.BeartypeCallHintParamViolation: @beartyped
    # test_bear_type() parameter s=123 violates type hint <class 'str'>,
    # as 123 not instance of str.
    # test_bear_type(123)


    """
    introduce Dates
    https://www.w3schools.com/python/python_datetime.asp
    """
    # from datetime import date, timedelta

    """
    introduce RegEx
    """

    """
    introduce JSON
    """

    """
    introduce File I/O
    """

    """
    Set/List/Dict -> existence/nonexistence value
    two difference
    """



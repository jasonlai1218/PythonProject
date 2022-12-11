# 全域變數
x = 100


class GoFunction:

    t_length = 10

    def __init__(self):
        pass

    # 靜態方法(Static Method)無法改變類別(Class)
    # 及物件(Object) 的狀態
    # 使用靜態方法(StaticMethod)有幾個優點是，
    # 在開發過程中可以避免新加入的開發人員意外改變類別(Class)或物件(Object)
    # 的狀態(因為方法中無self及cls參數)，而影響到類別(Class)原始的設計。
    # 其二則是靜態方法(Static Method)在類別中是獨立的，所以有助於單元的測試。
    # 簡單說 不帶 instance 以及 class 為參數的 method
    @staticmethod
    def calculate_number(first):
        # 區域變數
        total = 10
        if first % 2 == 0:
            total += first
        print(total)

    @staticmethod
    def calculate_number2(first):
        total = 10
        if first % 2 == 0:
            total += first
        return total

    @staticmethod
    def app_log(name, func_id, date="2019/12/21"):
        # Formatting String
        print(f"{name} use the {func_id} on {date}")

    @staticmethod
    def service_log(*info):
        print(info)

    @staticmethod
    def container_log(**info):
        print(info)

    @staticmethod
    def change_x_number():
        global x
        # 區域變數
        x = 20

    # 若是 static method 的話就無法了，
    # static method 因為沒有 self 和 cls ，
    # 根本無法 access 放在外面的 static member，會直接噴 error
    # NameError: name 't_length' is not defined
    # @staticmethod
    # def pee():
    #     print(f"pee: {t_length}")


# NameError: name 'total' is not defined
# because total is local variable
# print(total)
print(x)


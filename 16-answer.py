class PhoneDevice:
    def __init__(self, brand, ctype, number, com=None):
        self.__brand = brand
        self.__ctype = ctype
        self.__com = com
        self.__number = number
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def ctype(self):
        return self.__ctype

    @property
    def number(self):
        return self.__number

    @property
    def com(self):
        return self.__com
        
    @com.setter     # 也可以设为一个函数，不用属性
    def com(self, com):
        self.__com = com

    def show_info(self):
        print(f"品牌：{self.__brand}；型号：{self.__ctype}；服务商：{self.__com}；号码：{self.__number}。")

    def call(self, person, some_content):
        if self.com is None:
            print("没有网络服务商，无法打电话！")
            return
        print(f"{person.name}:{self.__number}来电：{some_content}")

class MobilePhone(PhoneDevice):
    tag = "手机"
    def __init__(self, brand, ctype, number, com=None, adresses=None, power="off"):
        super().__init__(brand, ctype, number, com)
        if adresses == None:
            self.__adresses = {}
        else:
            self.__adresses = adresses
        self.power = power

    def power_switch(self):
        if self.power == "on":
            self.power = "off"
        else:
            self.power = "on"

    def add_adresses(self, name, number):
        self.__adresses[name] = number
    
    def show_adresses(self):
        for key, value in self.__adresses.items():
            print(f"{key}:{value}")
    
    def call(self, person, some_content):
        if self.power == "on":
            print(f"用手机{self.number}打电话：", end="")
            super().call(person, some_content)
        else:
            print("您的手机没有开机，无法打电话")

class PublicPhone(PhoneDevice):
    def __init__(self, brand, ctype, number, loc="somewhere", com=None):
        if loc in FreePhone.phone_loc:
            raise Exception(f"无法在{loc}创建公用电话")
        else:
            super().__init__(brand, ctype, number, com)
            self.__loc = loc

    @property       # 不设setter，不允许更改地点
    def loc(self):
        return self.__loc
    
    def call(self, person, some_content):
        super().call(person, some_content)
        print("这是公用电话，收费1元。")

class FreePhone(PhoneDevice):
    phone_loc = {"家", "办公室", "寝室"}
    def __init__(self, brand, ctype, number, loc="家", com=None):
        if loc not in FreePhone.phone_loc:
            raise Exception(f"无法在{loc}创建免费电话")
        else:
            super().__init__(brand, ctype, number, com)
            self.__loc = loc

    @property
    def loc(self):
        return self.__loc

    def call(self, person, some_content):
        super().call(person, some_content)
        print("这是免费电话，不收费。")

class Person:
    # 空列表、空字典、空集合等可变数据类型不作为缺省值（防止意外问题），改用None
    def __init__(self, name, gender, age, belongings=None, loc="others"):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__loc = loc
        if belongings == None:              
            self.__belongings = {}
        else:
            self.__belongings = belongings

    @property
    def name(self):
        return self.__name
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def age(self):
        return self.__age
    
    @property
    def loc(self):
        return self.__loc
    
    @property
    def belongings(self):
        return self.__belongings
    
    # @loc.setter
    # def loc(self, new_loc):
    #     self.__loc = new_loc
    def goto_loc(self, new_loc):
        self.__loc = new_loc

    def take(self, something):
        self.__belongings[something.tag] = something

    def intro(self):
        print(f"I am {self.name}.....")
        
    def call_someone(self, device, person, some_content):
        if isinstance(device, MobilePhone):
            if device not in self.__belongings:
                print("你没有手机！")
                return
        else :
            if self.loc != device.loc:
                print(f"你没在{device.loc}，不能用这个电话！")
                return

        device.call(person, some_content)       # 根据不同的device调用不同的电话

def main():
    p = Person("lpy", "male", 100)
    musk = Person("musk", "male", 200)
    mb = MobilePhone("xiaomi","13","139")
    mb.power_switch()
    mb.com = "电信"
    p.take(mb)
    p.call_someone(mb, musk,"helo")
    p.goto_loc("home")
    fb = FreePhone("xxtype", "dsdk", "88888")
    fb.com = "连通"
    p.call_someone(fb, musk,"helo")
    pb = PublicPhone("yyytype","dsdk", "9999")
    pb.com = "连通"
    p.goto_loc("somewhere")
    p.call_someone(pb, musk,"hello")

main()













#---------------给X打call plus------------------------------
class PhoneDevice:
    def __init__(self, brand, ctype, number, com=None):
        self.__brand = brand
        self.__ctype = ctype
        self.__com = com
        self.__number = number
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def ctype(self):
        return self.__ctype

    @property
    def number(self):
        return self.__number

    @property
    def com(self):
        return self.__com
        
    @com.setter     # 也可以设为一个函数，不用属性
    def com(self, com):
        self.__com = com

    def show_info(self):
        print(f"品牌：{self.__brand}；型号：{self.__ctype}；服务商：{self.__com}；号码：{self.__number}。")

    def call(self, person, some_content):
        if not self.com:
            print("没有网络服务商，无法打电话！")
            return
        print(f"{person.name}:{self.__number}来电：{some_content}")

class MobilePhone(PhoneDevice):
    tag = "手机"
    def __init__(self, brand, ctype, number, com=None, adresses=None, power="off"):
        super().__init__(brand, ctype, number, com)
        if adresses == None:
            self.__adresses = {}
        else:
            self.__adresses = adresses
        self.power = power

    def power_switch(self):
        if self.power == "on":
            self.power = "off"
        else:
            self.power = "on"

    def add_adresses(self, name, number):
        self.__adresses[name] = number
    
    def show_adresses(self):
        for key, value in self.__adresses:
            print(f"{key}:{value}")
    
    def call(self, person, some_content):
        if self.power == "on":
            if person.name in self.__adresses:
                print(f"用手机{self.number}打电话：", end="")
                super().call(person, some_content)
            else:
                print(f"没有{person.name}的手机号码！")
        else:
            print("您的手机没有开机，无法打电话")

class PublicPhone(PhoneDevice):
    public_phones = {}   # 存放收费电话实例，{地点：电话, xxx:pp}
    yellow_Pages = {"警察局":110, "消防局":119}
    def __init__(self, brand, ctype, number, loc="somewhere", com=None):
        if loc in FreePhone.phone_loc:
            raise Exception(f"无法在{loc}创建公用电话")
        else:
            super().__init__(brand, ctype, number, com)
            self.__loc = loc
            PublicPhone.public_phones[loc] = self # 实例化一个就存放一个

    @property
    def loc(self):
        return self.__loc
    
    def call(self, person, some_content):
        # add here
        super().call(person, some_content)
        print("这是公用电话，收费1元。")
    
    @classmethod
    def add_item(cls, name, number):
        cls.yellow_Pages[name] = number

class FreePhone(PhoneDevice):
    free_phones = {}     # 存放免费电话实例
    phone_loc = {"家", "办公室", "寝室"}
    adress_list = {"爸爸":139111111, "妈妈":138111111}
    def __init__(self, brand, ctype, number, loc="家", com=None):
        if loc not in FreePhone.phone_loc:
            raise Exception(f"无法在{loc}创建免费电话")
        else:
            super().__init__(brand, ctype, number, com)
            self.__loc = loc
            FreePhone.free_phones[loc] = self # 实例化一个就存放一个

    @property
    def loc(self):
        return self.__loc

    def call(self, person, some_content):
        # add here
        super().call(person, some_content)
        print("这是免费电话，不收费。")

    @classmethod
    def add_item(cls, name, number):
        cls.adress_list[name] = number

class Person:
    # 空列表、空字典、空集合等可变数据类型建议不作为缺省值而改用None
    def __init__(self, name, gender, age, belongings=None, loc="others"):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__loc = loc
        if belongings == None:              
            self.__belongings = {}
        else:
            self.__belongings = belongings

    @property
    def name(self):
        return self.__name
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def age(self):
        return self.__age
    
    @property
    def loc(self):
        return self.__loc
    
    @property
    def belongings(self):
        return self.__belongings
    
    def goto_loc(self):
        self.__loc = input("请输入目的地：")

    def take(self, something):
        self.__belongings[something.tag] = something

    def intro(self):
        print(f"I am {self.name}.....")
        
    def call_someone(self, person, some_content):
        try:
            phone = FreePhone.free_phones[self.__loc]
        except KeyError:
            try:
                phone = PublicPhone.public_phones[self.__loc]
            except KeyError:
                try:
                    phone = self.belongings["手机"]
                except KeyError:
                    print(f"你没有手机！{self.__loc}也没有固定电话")
                    return
        
        phone.call(person, some_content)
    
def main():

    pphone_hospital = PublicPhone("asddsd", "dsdds", 13921212, "校医院")
    
    liupengyuan = Person("lpy", "male", 100)
    musk = Person("musk", "male", 200)
    mphone = MobilePhone("xiaomi","13","139")
    mphone.power_switch()
    mphone.com = "电信"
    mphone.add_adresses("musk", 13900392)
    liupengyuan.take(mphone)

    fphone1 = FreePhone("xxx", "yyy", "8888",com = "com", loc = "家")
    fphone2 = FreePhone("xxx", "yyy", "666",com = "com", loc = "办公室")
    pphone1 = PublicPhone("xxx", "yyy", "8888",com = "com", loc = "小卖铺")
    pphone2 = PublicPhone("xxx", "yyy", "666",com = "com", loc = "车展馆")

    liupengyuan.goto_loc()
    liupengyuan.call_someone( musk,"helo")
    
    
if __name__ == "__main__":
    main()
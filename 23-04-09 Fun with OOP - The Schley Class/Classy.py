class Schley:
    def __init__(self, name, secred_code, age, nickname = "Sparky"):
        self.name = name
        self.nickname = nickname
        self.secret_code = secred_code
        self.age = age
        self.count = 1
    
    def talk(self):
        if self.count%5 == 3:
            print("Poopy pants!!!!!!")
        else:
            print(f"Hi, my name is {self.name}.")
            print(f'My secret code is "{self.secret_code}", \nand I am {self.age} years old.')
        self.count += 1

    def banana(self, name = None):
        import time
        if name == None:
            name = self.name
        print("***drum roll!***")
        for num in range(5):
            print(5-num)
            time.sleep(1)
        name = name.lower()
        s_name = ""
        for (i,letter) in enumerate(name):
            if letter in ["a", "e", "i", "o", "u"]:
                s_name = name[i:]
                break

                
        print(f"{name.title()} bo b{s_name}")
        time.sleep(1)
        if "uck" in s_name.lower():
            print(f"banana fanna fo...", end = "")
            time.sleep(2.4)
            print("?!")
            time.sleep(1)
            print("Hey!")
            time.sleep(1.5)
            print(f"You can't use {name.title()}!")
            return 
        print(f"banana fanna fo f{s_name}")
        time.sleep(2)
        print(f"me, my, mo, m{s_name}")
        time.sleep(2)
        print(f"It's {name.title()}!")
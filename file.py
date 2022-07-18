class MyCompeler:
    def MyPrint(self, str):
        res = str
        print(res[10:])

    def MyScan(self):
        input()


compeler = MyCompeler()

with open("input.txt", "r", encoding='UTF-8') as file:
    for string in file:
        if string.find('spwninfo:') != -1:
            compeler.MyPrint(string)

        elif string.find('plantedinfo:') != -1:
            compeler.MyScan()

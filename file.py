class MyCompeler:
    def MyPrint(self, str):
        res = str
        print(res[res.find("spwninfo:") + 10:])

    def MyScan(self):
        input()


with open("input.txt", "r", encoding='UTF-8') as fin:
    compeler = MyCompeler()
    inputstr = fin.read()
    for string in inputstr:
        if inputstr.find('spwninfo:') != -1:
            compeler.MyPrint(inputstr)
            break

        if inputstr.find('plantedinfo:') != -1:
            compeler.MyScan()
            break

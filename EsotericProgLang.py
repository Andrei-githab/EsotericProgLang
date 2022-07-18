class MyInterpreter:

    def __int__(self):
        pass

    def run(self, code):
        for xs in code:
            self.eval(xs)

    def eval(self, xs):
        if isinstance(xs, list):
            return self.__getattribute__(xs[0])(xs)
        return xs

    def spwninfo(self, xs):
        if len(xs) == 1:
            print()
            return
        l = len(xs) - 1
        for i, x in enumerate(xs[1:]):
            e = self.eval(x)
            if i < l - 1:
                print(e, end="")
            else:
                if e != ",":
                    print(e)
                else:
                    print(e, end="")

    def plantedinfo(self, xs):
        input()


listcode = []

try:
    with open("input.txt", "r", encoding='UTF-8') as file:
        for string in file.readlines():
            listcode.append(string.rstrip('\n').split(':'))

    interpreter = MyInterpreter()
    interpreter.run(listcode)

except IOError as e:
    print("Не удалось открыть файл!")


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


code = [
    ["spwninfo", "Hello World!", "Sky is blue"],
    ["plantedinfo", "c"],
    ["spwninfo", " Конец!!!"]
]

interpreter = MyInterpreter()
interpreter.run(code)

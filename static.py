class Business():
    @staticmethod
    def infulence():
        print("big trade")

    @classmethod
    def earn(cls):
        print("can take a lot of money")


if __name__ == '__main__':
    b1 = Business()
    b1.infulence()
    Business.infulence()
    b1.earn()
    Business.earn()
    print(b1)

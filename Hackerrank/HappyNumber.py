class happyNumber:
    def __init__(self):
        n = int(input("Enter a number"))
        
        if self.validateHappy(n):
            print(n, "is a happy number")
        else:
            print(n, "is not a happy number")

    def validateHappy(self, n):
        chk1, chk2 = n, n
        while (True):
            chk1 = self.getNsquare(chk1)
            chk2 = self.getNsquare(self.getNsquare(chk2))
            # print(chk1, chk2)
            if chk1 != chk2:
                continue
            else:
                break
        if chk1 == 1:
            return True
        else:
            return False

    def getNsquare(self, n):
        num = 0
        while (n > 0):
            num += (n % 10) ** 2
            n = n // 10
        return num



# by Tirtharaj Sinha

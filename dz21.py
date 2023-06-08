# ✔Начальная сумма равна нулю
# ✔Допустимые действия: пополнить, снять, выйти 
# ✔Сумма пополнения и снятия кратны 50 у.е.
# ✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔Нельзя снять больше, чем на счёте
# ✔При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной 
# ✔Любое действие выводит сумму денег


# Напишите программу банкомат.
class Bankomat:
    def __init__(self):
        self.user_balance = 0
        self.counter = 0
        self.bank_profit = 0
        self.check = True

    def add(self, sum):
        self.user_balance += int(sum / 50)
        self.counter += 1
               
    def withdraw(self, sum):
        if sum % 50 != 0:
            print("Сумма должна быть кратна 50 !")
        elif sum <= self.user_balance:
            self.counter += 1
            self.user_balance -= sum 
            if self.counter % 3 == 0:
                self.bank_profit += sum * 0.03 
                self.user_balance -= sum * 0.03 
        
             

    


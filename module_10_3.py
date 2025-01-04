import threading
import time
import random
from random import randint

lock = threading.Lock() # объект класса Lock для блокировки потоков.

class Bank:

    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and lock.locked():
                lock.release()
            x = random.randint(50, 500)
            self.balance += x
            print(f'Пополнение: {x}. Баланс: {self.balance}')
            time.sleep(0.001)

# Методы объекта:
    def take(self):
        for i in range(100):
            x = random.randint(50, 500)
            print(f'Запрос на {x}')
            if x <= self.balance:
                self.balance -= x
                print(f'Снятие: {x}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
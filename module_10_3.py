from random import randint
import threading
from time import sleep


class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            random_number = randint(50, 500)
            self.balance += random_number
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            print(f"Пополнение: {random_number}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            random_number = randint(50, 500)
            print(f"Запрос на {random_number}")

            if random_number <= self.balance:
                self.balance -= random_number
                print(f"Снятие: {random_number}. Баланс: {self.balance}")
                sleep(0.001)
            if random_number > self.balance:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")


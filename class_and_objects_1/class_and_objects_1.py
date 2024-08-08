class Cassa(object):
    cash = 0  
    
    def __init__ (self, ca):
        self.cash = ca

    def top_up(self):
        x = int(input("На сколько пополнить кассу: "))
        self.cash += x
        
        
    def count_1000(self):
        c = self.cash // 1000
        x = " "
        if c == 2 or c == 3 or c == 4:
            x = "тысячи"
        else:
            x = "тысяч"
            
        print(f"Осталось {c} {x}")

    def take_away(self):
        x = int(input("Сколько хотите забрать из кассы: "))
        if x <= self.cash:
            self.cash -= x
        else:
            print("Не достаточно денег в кассе")

cas = Cassa(0)
print(cas.cash)
cas.top_up()
print(cas.cash)
cas.count_1000()
cas.take_away()

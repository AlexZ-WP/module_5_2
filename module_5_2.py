# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        #nf = [i for i in range(1, new_floor+1)] # генератор списка для создания произвольного списка целых чисел
        nf = list(range(1, new_floor+1))
        if new_floor > self.number_of_floors:
           print("Такого этажа не существует")
        else:
            print(*nf[:], sep="\n")

    def __len__(self):
        return  self.number_of_floors

    def __str__(self):
       return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))
from random import randint

__all__ = ['RetrieveOperations']

class RetrieveOperations:
    def __init__(self) -> None:
        pass

    def _random(self, a, b, total):
        list_of_numbers = []
        print('****************')
        for x in range(total):
            res = randint(a, b)
            list_of_numbers.append(res)
            print(f'Numero random {x+1} de {total}: {res}')
        print('****************')
        return list_of_numbers

    def _range(self, list_of_numbers):
        print(f'Numero mas alto: {max(list_of_numbers)}')
        print(f'Numero mas bajo: {min(list_of_numbers)}')
        print('****************')
        return max(list_of_numbers) - min(list_of_numbers)

    def _average(self, list_of_numbers):
        return sum(list_of_numbers)/len(list_of_numbers)

    def _sum(self, list_of_number):
        return sum(list_of_number)

            
    
    def run(self, event):
        print(event)
        random_numbers = self._random(event['a'], event['b'], event['total'])
        if random_numbers:
            print('****************')
            print(f'El Rango es: {self._range(random_numbers)}')
            print(f'El Promedio es: {self._average(random_numbers)}')
            print(f'La suma es: {self._sum(random_numbers)}')
            print('****************')
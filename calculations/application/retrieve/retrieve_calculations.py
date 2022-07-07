import math

__all__ = ['RetrieveCalculations']

class RetrieveCalculations:
    def __init__(self) -> None:
        pass

    def _fibonacci_of(self, n):
        if n in {0, 1}:  # Base case
            return n
        return self._fibonacci_of(n - 1) + self._fibonacci_of(n - 2)  # Recursive case

    def calculaCollatz(self, number):
        print(f'Numero actual: {number}')
 
        if number != 1:
            if number % 2 == 0:
                number = number // 2
            else:
                number = number * 3 + 1
            
            self.calculaCollatz(number)

    def _factorial(self, number):
        return math.factorial(number)

    def _imc(self, kg, height):
        imc = round(kg/math.pow(height,2),1)
        return "Su IMC es de "+str(imc)

    def run(
        self, 
        event
    ):
        if event['event_type'] == "fibonacci":
            for x in range(event['number']):
                print(self._fibonacci_of(x))
            return self._fibonacci_of(event['number'])
        if event['event_type'] == "collatz":
            return self.calculaCollatz(event['number'])
        if event['event_type'] == "factorial":
            return self._factorial(event['number'])
        if event['event_type'] == "imc":
            return self._imc(event['kg'], event['height'])
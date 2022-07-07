
__all__ = ['RetrieveValidations']

class RetrieveValidations:
    def __init__(self) -> None:
        pass

    def _validate_if_fibonacci(self, number):
        if 9 < number <= 99:
            penultimo = 0
            ultimo = 1

            while ultimo < number:
                penultimo, ultimo = ultimo, penultimo + ultimo

            if number == ultimo:
                return "Si pertenece a las serie Fibonacci."

            else:
                return "El numero no pertenece a la serie Fibonacci."

        else:
            return "Debe ingresar un numero de dos digitos"

    def _factorial(self, number):
        if number == 1:
            return "No es factorial"
        else:
            i = 0
            while number > 1:
                i+=1
                number = number / i
            return i

    def _is_prime(self, number):
        for i in range(2,number):
            if (number%i) == 0:
                return 'No es numero primo'
            return 'Es numero primo'

    def run(self, event):
        print(event)
        if event['event_type'] == "fibonacci":
            return self._validate_if_fibonacci(event['number'])
        if event['event_type'] == "factorial":
            return self._factorial(event['number'])
        if event['event_type'] == "prime":
            return self._is_prime(event['number'])
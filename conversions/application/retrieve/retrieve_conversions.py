import math

__all__ = ['RetrieveConversions']

class RetrieveConversions:
    def __init__(self) -> None:
        pass
    
    

    def _temperature(self, number):
        def _celcius():
            print(f'Celcius: {number}')
    
        def _fahrenheit():
            print(f'Fahrenheit: {(number*1.8)+32}')

        def _kelvin():
            print(f'Kelvin: {number+273.15}')
        
        _celcius()
        _fahrenheit()
        _kelvin()

    def _dough(self, number):
        def _grams():
            print(f'Gramos : {number}')

        def _kilogram():
            print(f'Kilos: {number/1000}')

        def _ounce():
            print(f'Onza: {number/28.3495}')

        def _pound():
            print(f'Libra: {number/453.592}')

        _grams()
        _kilogram()
        _ounce()
        _pound()

    def _length(self, number):
        def _centimeters():
            print(f'Centimetros: {number}')
        def _meters():
            print(f'Metros: {number/100}')
        def _kilometres():
            print(f'Kilometros: {number/1000}')
        def _inches():
            print(f'Pulgadas: {number/2.54}')
        def _feet():
            print(f'Pies: {number/30.48}')
        def _yards():
            print(f'Yardas: {number/91.44}')
        def _miles():
            print(f'Millas: {number/160934}')

        _centimeters()
        _meters()
        _kilometres()
        _inches()
        _feet()
        _yards()
        _miles()

    def _volume(self, number):
        def _milliliters():
            print(f'Milimetros: {number}')
        def _liters():
            print(f'Litros: {number/1000}')
        def _gallons():
            print(f'Galones: {number/4546.09}')
        _milliliters()
        _liters()
        _gallons()

    def _storage(self, size_bytes):
        B = float(size_bytes)
        KB = float(1024)
        MB = float(KB ** 2)
        GB = float(KB ** 3) 
        TB = float(KB ** 4)
        print(f'Bytes: {B}')
        print(f'Megabytes: {B/MB}')
        print(f'Gigabytes: {B/GB}')
        print(f'Terabytes: {B/TB}')



    def run(self, event):
        print(event)
        if event['event_type'] == 'temperature':
            self._temperature(event['number'])
        if event['event_type'] == 'dough':
            self._dough(event['number'])
        if event['event_type'] == 'length':
            self._length(event['number'])
        if event['event_type'] == 'volume':
            self._volume(event['number'])
        if event['event_type'] == 'storage':
            self._storage(event['number'])
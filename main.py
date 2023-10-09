import sys
from sys import argv
import csv

try:
    csv_input = sys.argv[1]
    csv_output = sys.argv[2]
    data = []
    changes = [x.split(',') for x in argv[3:]]

    with open(csv_input, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    for x in changes:
        data[int(x[1])][int(x[0])] = x[2]

    with open(csv_output, 'w', newline='') as file:
        writer = csv.writer(file)

        for row in data:
            print(row)
            writer.writerow(row)

except IndexError:
    print('Podaj argumenty w formacie <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>\n'
          '<zmiana_x> - zmiana w postaci "x(kolumna),y(wiersz),wartość"')
except FileNotFoundError:
    print('Podaj prawidłową ścieżkę pliku')
except ValueError:
    print('Współrzędne do zmiany muszą być liczbami całkowitymi')

import random

print("Witaj w grze zgadywania liczby!")
x = random.randint(1, 100)  
b = 0  # Licznik prób

while True:
  wejscie = input("Podaj liczbę: ")

  
  if wejscie.isdigit():
    a = int(wejscie)
    b += 1  
  else:
    print("To nie jest liczba. Spróbuj ponownie.")
    continue  

  
  if a < x:
    print("Twoja liczba jest mniejsza od wylosowanej.")
    print("Liczba prób: ", b)
  elif a > x:
    print("Twoja liczba jest większa od wylosowanej.")
    print("Liczba prób: ", b)
  else:
    print("Gratulacje! Zgadłeś liczbę.")
    print("Liczba prób: ", b)
    break  



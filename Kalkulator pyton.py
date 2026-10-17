import random
print("Witaj w kalkulatorze, podaj dwie liczby a potem działanie jakie chcesz wykonać lub wybierz tryb zgadywania liczby wpisując 'zgadywanie'.")
if input() == "zgadywanie":
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
else:
  a = float(input("Podaj pierwszą liczbę: "))
  b = float(input("Podaj drugą liczbę: "))
  print("Wybierz działanie: dodawanie, odejmowanie, mnożenie, dzielenie")
  dzialanie = input()

  if dzialanie == "dodawanie":
    wynik = a + b
    print("Wynik dodawania:", wynik)
  elif dzialanie == "odejmowanie":
    wynik = a - b
    print("Wynik odejmowania:", wynik)
  elif dzialanie == "mnożenie":
    wynik = a * b
    print("Wynik mnożenia:", wynik)
  elif dzialanie == "dzielenie":
    if b != 0:
      wynik = a / b
      print("Wynik dzielenia:", wynik)
    else:
      print("Nie można dzielić przez zero.")
  else:
    print("Nieznane działanie.")
restart = input("Czy chcesz zrestartować kalkulator? (tak/nie): ")
if restart.lower() == "tak":
  exec(open(__file__).read())
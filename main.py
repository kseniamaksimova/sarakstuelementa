def Atlaide(summa):
  rez =""
  if summa<100:
   rez = "Atlaide nav piešķirte, jāmaksā vēļ" + str(summa)
  elif summa >=100 and summa <200:
   rez = "Atlaide 5%, jāmaksā vēl" + str(summa*0.05)
  else:
    rez = "Atlaide 10%, jāmaksā vēl" + str(summa*0.9)
  return rez

summa = float(input("Ievadiet summa:"))
print(Atlaide(summa))
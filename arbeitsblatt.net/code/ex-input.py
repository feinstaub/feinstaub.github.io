eingabe1 = input("Bitte geben Sie Ihren Namen ein: ")
eingabe2 = input("Hallo {}. Wie geht es Ihnen? ".format(eingabe1))
print("Schön, dass es Ihnen {} geht, {}.".format(eingabe2, eingabe1))

e3s = input("Ganzzahl eingeben (z. B. 15): ")
type(e3s) # <class 'str'>
e3 = int(e3s)
type(e3)  # <class 'int'>

e4s = input("Fließkommazahl eingeben (z. B. 13.45): ")
type(e4s) # <class 'str'>
e4 = float(e4s)
type(e4)  # <class 'float'>

print("{} + {} = {}".format(e3, e4, e3 + e4))
print("{} - {} = {}".format(e3, e4, e3 - e4))

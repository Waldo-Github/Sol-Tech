#Calc funksies
def plus(x, y):
    """Funksie vir plus"""
    return x + y

def minus(x, y):
    """Funksie vir minus"""
    return x - y

def maal(x, y):
    """Funksie vir maal"""
    return x * y

def deel(x, y):
    """Funksie vir deel"""
    if y == 0:
        return "Kan nie deur nul deel nie"
    return x / y

# Hoofprogram
def main():
    print("Welkom by Waldo se sakrekenaar")
    print("Kies een van die volgende: +, -, *, /")
    print("Voer 'q' in om die sakrekenaar te verlaat.")

    while True:
        # Gebruiker input vir die som
        operasie = input("Voer operasie in (+, -, *, /) of 'q' om te verlaat: ")

        # Verlaat die sakrekenaar as die gebruiker 'q' ingetik het
        if operasie == 'q':
            print("Die sakrekenaar is nou af.")
            break

        # Kontroleer of die operasie geldig is
        if operasie not in ['+', '-', '*', '/']:
            print("Is nie n opsie nie. Probeer weer.")
            continue

        # Gebruiker input vir getalle
        try:
            num1 = float(input("Voer eerste getal in: "))
            num2 = float(input("Voer tweede getal in: "))
        except ValueError:
            print("Ongeldige getal. Probeer weer.")
            continue

        # Voer die regte operasie uit volgens die gebruiker se keuse
        if operasie == '+':
            print(f"{num1} + {num2} = {round(plus(num1, num2),3)}")
        elif operasie == '-':
            print(f"{num1} - {num2} = {round(minus(num1, num2),3)}")
        elif operasie == '*':
            print(f"{num1} * {num2} = {round(maal(num1, num2),3)}")
        elif operasie == '/':
            print(f"{num1} / {num2} = {round(deel(num1, num2),3)}")

        # Leër die skerm vir volgende inset
        print()

# Roep die hoofprogramfunksie aan om die sakrekenaar te begin
if __name__ == "__main__":
    main()
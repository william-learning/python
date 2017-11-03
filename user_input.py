#planet = input("What planet are you from? ")
#print(planet)

def currency_converter(rate,euros):
    dollars = rate * euros
    return dollars
    
r = float(input("Enter rate: "))
e = float(input("Enter euros: "))
print(currency_converter(r,e))
'''
False e None são False
Zero em valores númericos: 0, 0.0, 0j
Decimal(0) e Fraction(0, x) são False também
Sets e intervalos vazios: sets{}, range()

'''
x = []
print(bool(x))

y = {}
print(bool(y))

dec = 0.0
print(bool(dec))
print(bool(None))

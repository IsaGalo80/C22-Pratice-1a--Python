user_input = int(input('How many people are coming to your wedding?\n'))

if user_input <= 50:
    price = 4000

print('Your wedding will cost '+str(price)+' dollars')

if price <50  : 
    print('El costo es de $4000')
elif price <100 :
    print('El costo será de 10 000')
elif price <200 :
    print('El costo será de 15 000')
elif price >200:
    print('El costo será de 20 000')
else:
    print ('')


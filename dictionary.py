
capitals = {'USA':'Washington DC','Indonesia':'Jakarta','China':'Beijijng','Rusia':'moscow'}
print(capitals['Rusia'])

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')


# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key,value in capitals.items():
    print(key,value)
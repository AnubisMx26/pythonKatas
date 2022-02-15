#actualizar una key del diccionario
#planet.update({'name': 'Makemake'})

#actualizar una key del diccionario con corchetes
#planet['name'] = 'Makemake'

#agregar otra clave al diccionario
#planet['orbital period'] = 4333

#Elininar una clave del diccionario
#planet.pop('orbital period')

planet = {
    'nombre': 'Marte',
    'lunas': 2
}

print(f'{planet["nombre"]} tiene {planet["lunas"]} lunas')

planet['circunferencia (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(f'{planet["nombre"]} tiene una circunferencia polar de {planet["circunferencia (km)"]["polar"]}')
import requests
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-m", nargs="+")
value = parser.parse_args()




SITE_ID='MLA'

listadoProductos = []
productos = {}



def escribirLog(posicion):
		
	if os.path.isfile(archivo):	
		file = open(archivo, "a")
		file.write(str(listadoProductos[posicion]) + os.linesep)
		file.close()
	else:
		file = open(archivo, "w")
		file.write(str(listadoProductos[posicion]) + os.linesep)
		file.close()


def consultarSELLER_ID():
	print('entro')
	url='https://api.mercadolibre.com/sites/{SITE_ID}/search?seller_id={SELLER_ID}'.format(SITE_ID=SITE_ID,SELLER_ID=SELLER_ID)
	response=requests.get(url)
	
	if response.status_code == 200:
		response.json=response.json()
		cantidadResultados= len(response.json['results'])
		
		for bucleCantidadResultados in range(cantidadResultados):
			productos['ID'] = response.json['results'][bucleCantidadResultados]['id']
			productos['TITLE'] = response.json['results'][bucleCantidadResultados]['title']
			productos['CATEGORY_ID'] = response.json['results'][bucleCantidadResultados]['category_id']
			
			urlProductos = ('https://api.mercadolibre.com/categories/{productosCategoria}').format(productosCategoria=productos['CATEGORY_ID'])
			responseProductos = requests.get(urlProductos)
			if responseProductos.status_code == 200:			
				productos['NAME'] = responseProductos.json()['name']
				listadoProductos.append(productos)
				escribirLog(bucleCantidadResultados)
	else:
		print('El ID del vendedor no es valido o no se encuentra dentro del sitio MLA')

print('procesando, por favor, espere.')

if str(value.m) == 'None':
	SELLER_ID='179571326'
	archivo = SELLER_ID + '.log'	
	consultarSELLER_ID()
else:
	archivo = 'multiusuario.log'
	for bucleCantidadVendedores in value.m:
		SELLER_ID=bucleCantidadVendedores
		consultarSELLER_ID()

print('Se finalizo el procesamiento')		






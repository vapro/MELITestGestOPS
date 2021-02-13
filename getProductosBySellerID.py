import requests
import os


SITE_ID='MLA'
SELLER_ID='179571326'
listadoProductos = []
productos = {}


def escribirLog(posicion):
	
	archivo = SELLER_ID + ".log"
		
	if os.path.isfile(archivo):	
		file = open(archivo, "a")
		file.write(str(listadoProductos[posicion]) + os.linesep)
		file.close()
	else:
		file = open(archivo, "w")
		file.write(str(listadoProductos[posicion]) + os.linesep)
		file.close()


def consultarSELLER_ID():

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


print('Recolectando informacion, por favor, espere.')
consultarSELLER_ID()
print('Se guardo la informacion en ' + str(archivo))		






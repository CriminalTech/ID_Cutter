import easyocr
from PIL import Image
import os

# Definir el directorio con las imágenes
directorio = r'C:\Users\CriminalTech\Documents\CriminalTech\Proyectos Python\PCP\identificaciones'
directorio2 = r'C:\Users\CriminalTech\Documents\CriminalTech\Proyectos Python\PCP\identificaciones\recortes'

# Verificar que el directorio exista
if not os.path.exists(directorio):
    print(f'El directorio {directorio} no existe.')
else:
    print(f'El directorio {directorio} existe.')

    # Listar todos los archivos en el directorio
    archivos = os.listdir(directorio)
    print(f'Archivos encontrados en {directorio}: {archivos}')

    # Filtrar archivos que terminan en 'A.jpg' o 'A.JPG' y tienen números al principio
    archivosA = [f for f in archivos if (f.endswith('A.jpg') or f.endswith('A.JPG')) and f[:-5].isdigit()]
    print(f'Archivos que cumplen el criterio: {archivosA}')

    # Inicializar el lector de EasyOCR
    reader = easyocr.Reader(['es'])  # Inicializar el lector para el idioma español

    # Procesar cada archivo que termina en 'A.jpg' o 'A.JPG'
    for archivoA in archivosA:
        print(f'Procesando {archivoA}...')
        # Cargar la imagen Front
        image_pathF = os.path.join(directorio, archivoA)
        imageF = Image.open(image_pathF)

        # Buscar la imagen Back correspondiente (misma numeración pero termina en 'R.jpg' o 'R.JPG')
        archivoB = archivoA[:-5] + 'R' + archivoA[-4:]
        image_pathB = os.path.join(directorio, archivoB)
        if not os.path.exists(image_pathB):
            print(f'Imagen {archivoB} no encontrada, omitiendo.')
            continue

        imageB = Image.open(image_pathB)

        # Obtener el nombre del archivo sin la extensión
        image_name = os.path.splitext(os.path.basename(image_pathF))[0]

        # Usar EasyOCR para extraer texto
        result = reader.readtext(image_pathF)
        texto = ' '.join([item[1] for item in result])
        print(f'Texto extraído de {archivoA}: {texto}')

        # Verificar si 'FEDERAL' aparece en el texto y realizar acciones en consecuencia
        if 'FEDERAL' in texto:
            print(f'IFE encontrado en {archivoA}')
            # Definir las coordenadas de los recortes (izquierda, arriba, derecha, abajo)
            recorte1 = (653, 164, 958, 562)
            recorte2 = (0, 0, 990, 630)
            recorte3 = (0, 0, 990, 630)

            # Recortar las imágenes
            ife_imagen_recorte1 = imageB.crop(recorte1)
            ife_imagen_recorte2 = imageF.crop(recorte2)
            ife_imagen_recorte3 = imageB.crop(recorte3)

            # Guardar las imágenes recortadas
            ife_imagen_recorte1.save(os.path.join(directorio2, f'{image_name}_huella.jpg'))
            ife_imagen_recorte2.save(os.path.join(directorio2, f'{image_name}_anverso.jpg'))
            ife_imagen_recorte3.save(os.path.join(directorio2, f'{image_name}_reverso.jpg'))
            print(f'Imágenes recortadas guardadas para {archivoA}')

        if 'FEDERAL' in texto and not 'FOLIO' in texto:
            print(f'IFE encontrado en {archivoA}')
            # Definir las coordenadas de los recortes (izquierda, arriba, derecha, abajo)
            recorte1 = (531, 200, 660, 365)
            recorte2 = (0, 0, 990, 630)
            recorte3 = (0, 0, 990, 630)

            # Recortar las imágenes
            ife_imagen_recorte1 = imageB.crop(recorte1)
            ife_imagen_recorte2 = imageF.crop(recorte2)
            ife_imagen_recorte3 = imageB.crop(recorte3)

            # Guardar las imágenes recortadas
            ife_imagen_recorte1.save(os.path.join(directorio2, f'{image_name}_huella.jpg'))
            ife_imagen_recorte2.save(os.path.join(directorio2, f'{image_name}_anverso.jpg'))
            ife_imagen_recorte3.save(os.path.join(directorio2, f'{image_name}_reverso.jpg'))
            print(f'Imágenes recortadas guardadas para {archivoA}')

        elif 'NACIONAL' in texto and not 'ESTADO' in texto:
            print(f'INE encontrado en {archivoA}')
            # Definir las coordenadas de los recortes (izquierda, arriba, derecha, abajo)
            ine_recorte1 = (714, 59, 926, 271)
            ine_recorte2 = (0, 0, 990, 630)
            ine_recorte3 = (0, 0, 990, 630)

            # Recortar las imágenes
            ine_imagen_recorte1 = imageB.crop(ine_recorte1)
            ine_imagen_recorte2 = imageF.crop(ine_recorte2)
            ine_imagen_recorte3 = imageB.crop(ine_recorte3)

            # Guardar las imágenes recortadas
            ine_imagen_recorte1.save(os.path.join(directorio2, f'{image_name}_huella.jpg'))
            ine_imagen_recorte2.save(os.path.join(directorio2, f'{image_name}_anverso.jpg'))
            ine_imagen_recorte3.save(os.path.join(directorio2, f'{image_name}_reverso.jpg'))
            print(f'Imágenes recortadas guardadas para {archivoA}')

        if 'NACIONAL' in texto and 'EMISIÓN' in texto and 'ESTADO' in texto:
            print(f'INE encontrado en {archivoA}')
            # Definir las coordenadas de los recortes (izquierda, arriba, derecha, abajo)
            ine_recorte1 = (531, 200, 660, 365)
            ine_recorte2 = (0, 0, 990, 630)
            ine_recorte3 = (0, 0, 990, 630)

            # Recortar las imágenes
            ine_imagen_recorte1 = imageB.crop(ine_recorte1)
            ine_imagen_recorte2 = imageF.crop(ine_recorte2)
            ine_imagen_recorte3 = imageB.crop(ine_recorte3)

            # Guardar las imágenes recortadas
            ine_imagen_recorte1.save(os.path.join(directorio2, f'{image_name}_huella.jpg'))
            ine_imagen_recorte2.save(os.path.join(directorio2, f'{image_name}_anverso.jpg'))
            ine_imagen_recorte3.save(os.path.join(directorio2, f'{image_name}_reverso.jpg'))
            print(f'Imágenes recortadas guardadas para {archivoA}')
        else:
            print(f'Las palabras "FEDERAL" o "INE" no fueron encontradas en {archivoA}.')

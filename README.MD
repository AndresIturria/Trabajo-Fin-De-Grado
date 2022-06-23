# TFG Sistema De Asistencia A La Decisión Para Béisbol De Fantasía  

## Instrucciones  
1. Se necesita tener Python3 instalado.
2. Se debe crear un virtual enviroment.
   1. Windows: python -m venv /path/to/new/virtual/environment y activar ejecutando el script correspondiente en 
   /venv/Scripts/
   2. Linux: python3 -m venv /path/to/new/virtual/environment y activar con: source /venv/bin/activate
3. Una vez activado el venv instalar las dependencias, se ofrecen 2 ficheros de requirements:
   1. requirements.txt contiene la libreria tensorflow-gpu para poder ejecutar los scripts de generación de los ficheros
   de datos, en caso de no tener un gpu compatible se puede desisntalar con python3 -m pip uninstall tensorflow-gpu e 
   instalar la versión de cpu con python3 -m pip install tensorflow (en el caso de tensorflow cpu el modelo de machine
   learning puede tardar varias horas en entrenarse).
   2. requirements-no-tensorflow.txt si no se quieren ejecutar los scripts de generación de ficheros de datos, (se
   ahorra alrededor de 1GB de espacio de disco duro).
   3. Instalar las dependecias con python3 -m pip install -r nombre-de-fichero-requirements.txt
4. Los ficheros de datos ya vienen incluidos en el repositorio, pero también se encuentran los scripts para generarlos.
Para generarlos ejecutar los scripts en la carpeta data/scripts/ en orden.
5. Para iniciar la aplicación web ejecutar app.py, usará el puerto 5000.

También se puede encontrar la aplicación en la dirección: http://34.148.143.188:5000/
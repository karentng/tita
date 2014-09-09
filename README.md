Instalacion
===========

Instalar los requerimientos

    pip install -r requirements.txt

Sincronizar la base de datos (se recomienda antes borrar los datos de la version anterior ya que muchas tablas han cambiado):
    
    python manage.py syncdb
    
Cargar datos de departamentos y municipios:

    python manage.py loadddata dptos_municipios.json

Ejecutar el servidor:

    python manage.py runserver


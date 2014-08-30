from django.db import models
from convocat.models import Municipio


OPCIONES_GRADO = (  # son enteros, crear campo como IntegerField(choices=OPCIONES_GRADO)
    ( 1, u'Primero'),
    ( 2, u'Segundo'),
    ( 3, u'Tercero'),
    ( 4, u'Cuarto'),
    ( 5, u'Quinto'),
    ( 6, u'Sexto'),
    ( 7, u'Septimo'),
    ( 8, u'Octavo'),
    ( 9, u'Noveno'),
    (10, u'Decimo'),
    (11, u'Once'),
)

class InstitucionEducativa(models.Model):
    municipio = models.ForeignKey(Municipio)
    nombre = models.CharField(max_length=200)

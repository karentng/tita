from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.core import serializers
from convocat.models import * 
from django.db.models import Count
import json


def inscripcion(request):
    return render(request, 'inscripcion/inscripcion.html', {
    })
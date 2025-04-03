from django.shortcuts import render, redirect
from django.http import JsonResponse
from .calculos import calcular_puntajes_formacion_academica, calcular_puntaje_actualizacion_academica, calcular_puntaje_experiencia_profesional, calcular_puntaje_produccion_intelectual

def index(request):
    return render(request, "mi_app/index.html")


def meritos_profesional(request):
    if request.method == "POST":
        def get_int_value(value):
            return int(value) if value else 0

        diplomado = get_int_value(request.POST.get("diplomado"))
        especialidad = get_int_value(request.POST.get("especialidad"))
        maestria = get_int_value(request.POST.get("maestria"))
        doctorado = get_int_value(request.POST.get("doctorado"))
        cursos = get_int_value(request.POST.get("cursos", 0)) 
        antiguedad = get_int_value(request.POST.get("antiguedad", 0))
        servidor_publico = get_int_value(request.POST.get("servidor_publico", 0))
        docente = get_int_value(request.POST.get("docente", 0))
        articulos = get_int_value(request.POST.get("articulos", 0))

        resultados_formacion = calcular_puntajes_formacion_academica(diplomado, especialidad, maestria, doctorado)
        puntaje_actualizacion = calcular_puntaje_actualizacion_academica(cursos)
        resultados_experiencia = calcular_puntaje_experiencia_profesional(antiguedad, servidor_publico, docente)
        puntaje_produccion = calcular_puntaje_produccion_intelectual(articulos)

        resultados = {
            **resultados_formacion,
            "puntaje_actualizacion": puntaje_actualizacion,
            **resultados_experiencia,
            "puntaje_produccion": puntaje_produccion,
            "total_puntaje": resultados_formacion["total_puntaje_formacion_academica"] + puntaje_actualizacion+ resultados_experiencia["total_experiencia"]+ puntaje_produccion,
            "diplomado": diplomado,
            "especialidad": especialidad,
            "maestria": maestria,
            "doctorado": doctorado,
            "cursos": cursos,
            "antiguedad": antiguedad,
            "servidor_publico": servidor_publico,
            "docente": docente,
            "articulos": articulos,

        }

        request.session['resultados'] = resultados

        # Redirige a la misma página para evitar reenvío del formulario
        return redirect('meritos_profesional')  # Cambia 'nombre_de_la_vista' por el nombre de tu URL

    # Si no es POST, renderiza el template sin resultados
    if 'resultados' in request.session:
        # Recupera los resultados de la sesión
        resultados = request.session['resultados']
        # Limpia la sesión
        del request.session['resultados']
    else:
        resultados = {}

    return render(request, "mi_app/index.html", resultados)



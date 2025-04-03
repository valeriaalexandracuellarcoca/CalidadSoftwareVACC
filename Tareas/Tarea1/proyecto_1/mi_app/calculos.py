
def calcular_puntajes_formacion_academica(diplomado, especialidad, maestria, doctorado):

    puntaje_diplomado = 0
    puntaje_especialidad = 0
    puntaje_maestria = 0
    puntaje_doctorado = 0
    total_puntaje_formacion_academica = 0

    if diplomado == 0:
        puntaje_diplomado = 0
    else:
        puntaje_diplomado = min(4, 2 + (diplomado - 1))

    if especialidad == 0:
        puntaje_especialidad = 0
    else:
        puntaje_especialidad = min(6, 4 + (especialidad - 1) * 2)

    if maestria == 0:
        puntaje_maestria = 0
    else:
        puntaje_maestria = min(11, 8 + (maestria - 1) * 3)

    if doctorado == 0:
        puntaje_doctorado = 0
    else:
        puntaje_doctorado = min(12, 12 * doctorado)

    total_puntaje_formacion_academica = puntaje_diplomado + puntaje_especialidad + puntaje_maestria + puntaje_doctorado

    if total_puntaje_formacion_academica > 12:
        total_puntaje_formacion_academica = 12

    return {
        "puntaje_diplomado": puntaje_diplomado,
        "puntaje_especialidad": puntaje_especialidad,
        "puntaje_maestria": puntaje_maestria,
        "puntaje_doctorado": puntaje_doctorado,
        "total_puntaje_formacion_academica": total_puntaje_formacion_academica,
    }


def calcular_puntaje_actualizacion_academica(cantidad_cursos):
    puntaje = cantidad_cursos * 0.5
    return min(puntaje, 6.0)



def calcular_puntaje_experiencia_profesional(antiguedad, servidor_publico, docente):
    puntaje_antiguedad = min(antiguedad, 4)
    puntaje_servidor_publico = min(servidor_publico, 4)
    puntaje_docente = min(docente * 2, 2)

    subtotal = puntaje_antiguedad + puntaje_servidor_publico + puntaje_docente


    total_experiencia = min(subtotal, 10)

    return {
        "puntaje_antiguedad": puntaje_antiguedad,
        "puntaje_servidor_publico": puntaje_servidor_publico,
        "puntaje_docente": puntaje_docente,
        "total_experiencia": total_experiencia,
    }

def calcular_puntaje_produccion_intelectual(articulos):
    return min(articulos, 2)



    
import unittest
from mi_app.calculos import calcular_puntajes_formacion_academica, calcular_puntaje_actualizacion_academica, calcular_puntaje_experiencia_profesional, calcular_puntaje_produccion_intelectual

class TestCalculos(unittest.TestCase):
    def test_formacion_academica_sin_estudios(self):

        resultados = calcular_puntajes_formacion_academica(0, 0, 0, 0)
        self.assertEqual(resultados["total_puntaje_formacion_academica"], 0)

    def test_formacion_academica_un_diplomado(self):

        resultados = calcular_puntajes_formacion_academica(1, 0, 0, 0)
        self.assertEqual(resultados["total_puntaje_formacion_academica"], 2)

    def test_formacion_academica_dos_diplomados(self):

        resultados = calcular_puntajes_formacion_academica(2, 0, 0, 0)
        self.assertEqual(resultados["total_puntaje_formacion_academica"], 3)

    def test_formacion_academica_una_especialidad(self):

        resultados = calcular_puntajes_formacion_academica(0, 1, 0, 0)
        self.assertEqual(resultados["total_puntaje_formacion_academica"], 4)

    def test_formacion_academica_una_maestria(self):

        resultados = calcular_puntajes_formacion_academica(0, 0, 1, 0)
        self.assertEqual(resultados["total_puntaje_formacion_academica"], 8)

    def test_formacion_academica_un_doctorado(self):

        resultados = calcular_puntajes_formacion_academica(0, 0, 0, 1)
        self.assertEqual(resultados["total_puntaje_formacion_academica"], 12)

    def test_formacion_academica_combinacion(self):
        
        resultados = calcular_puntajes_formacion_academica(2, 2, 1, 1)
        self.assertEqual(resultados["total_puntaje_formacion_academica"], 12) 

    def test_sin_cursos(self):
        puntaje = calcular_puntaje_actualizacion_academica(0)
        self.assertEqual(puntaje, 0)

    def test_un_curso(self):

        puntaje = calcular_puntaje_actualizacion_academica(1)
        self.assertEqual(puntaje, 0.5)

    def test_dos_cursos(self):

        puntaje = calcular_puntaje_actualizacion_academica(2)
        self.assertEqual(puntaje, 1.0)

    def test_maximo_cursos(self):

        puntaje = calcular_puntaje_actualizacion_academica(20)  
        self.assertEqual(puntaje, 6.0)

    def test_sin_experiencia(self):
    
        puntaje = calcular_puntaje_experiencia_profesional(0, 0, 0)
        self.assertEqual(puntaje["total_experiencia"], 0)

    def test_antiguedad(self):

        puntaje = calcular_puntaje_experiencia_profesional(3, 0, 0)
        self.assertEqual(puntaje["total_experiencia"], 3)

    def test_servidor_publico(self):

        puntaje = calcular_puntaje_experiencia_profesional(0, 2, 0)
        self.assertEqual(puntaje["total_experiencia"], 2)

    def test_docente_universitario(self):

        puntaje = calcular_puntaje_experiencia_profesional(0, 0, 1)
        self.assertEqual(puntaje["total_experiencia"], 2)

    def test_combinacion(self):

        puntaje = calcular_puntaje_experiencia_profesional(2, 3, 1)
        self.assertEqual(puntaje["total_experiencia"], 7)

    def test_maximos(self):
        puntaje = calcular_puntaje_experiencia_profesional(5, 5, 2)  
        self.assertEqual(puntaje["total_experiencia"], 10)  
        self.assertEqual(puntaje["puntaje_antiguedad"], 4)  
        self.assertEqual(puntaje["puntaje_servidor_publico"], 4) 
        self.assertEqual(puntaje["puntaje_docente"], 2) 

    def test_sin_articulos(self):
        """
        Prueba que el cálculo de puntaje sea correcto cuando no hay artículos.
        """
        puntaje = calcular_puntaje_produccion_intelectual(0)
        self.assertEqual(puntaje, 0)

    def test_un_articulo(self):
        """
        Prueba que el cálculo de puntaje sea correcto con un artículo.
        """
        puntaje = calcular_puntaje_produccion_intelectual(1)
        self.assertEqual(puntaje, 1)

    def test_dos_articulos(self):
        """
        Prueba que el cálculo de puntaje sea correcto con dos artículos.
        """
        puntaje = calcular_puntaje_produccion_intelectual(2)
        self.assertEqual(puntaje, 2)

    def test_maximo_articulos(self):
        """
        Prueba que el cálculo de puntaje sea correcto cuando se alcanza el máximo de 2 puntos.
        """
        puntaje = calcular_puntaje_produccion_intelectual(5)  # Más de 2 artículos
        self.assertEqual(puntaje, 2)

if __name__ == "__main__":
    unittest.main()
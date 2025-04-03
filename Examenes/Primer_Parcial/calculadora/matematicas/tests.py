from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from matematicas.calculos import calcular_area_circulo, es_primo

class MatematicasTests(TestCase):
    #RADIO
    ##pasa las pruebas donde sale false o cero porque en la definicion de la funcion, inicialmente puse false para no dejar vacia la funcion 


    def test_area_circulo_radio_positivo(self):
        self.assertAlmostEqual(calcular_area_circulo(5), 78.54, places=2) #places es  para comproar que es igual en 2 decimales
        
    def test_area_circulo_radio_cero(self):
        self.assertEqual(calcular_area_circulo(0), 0)
        
    def test_area_circulo_radio_negativo(self):
        self.assertIsNone(calcular_area_circulo(-3))  
    
    def test_area_circulo_radio_grande(self):
        self.assertAlmostEqual(calcular_area_circulo(1000), 3141592.65, places=2)
    
    def test_area_circulo_radio_decimal(self):
        self.assertAlmostEqual(calcular_area_circulo(3.5), 38.48, places=2)

   #PRIMOS
   ##pasa las pruebas donde sale false o cero porque en la definicion de la funcion, inicialmente puse false para no dejar vacia la funcion 

    def test_primo_es_primo(self):
        self.assertTrue(es_primo(7))

    def test_primo_no_es_primo(self):
        self.assertFalse(es_primo(4))
    
    def test_primo_numero_negativo(self):
        self.assertFalse(es_primo(-3))
    
    def test_primo_numero_grande(self):   
        self.assertTrue(es_primo(997))

    def test_primo_cero(self):
        self.assertFalse(es_primo(0))
    




import csv
import random
from datetime import datetime, timedelta

# Listas de datos para generar valores aleatorios
nombres_m = ['Juan', 'Carlos', 'Pedro', 'Luis', 'Jorge', 'Miguel', 'Fernando', 'Ricardo', 'Andres', 'Daniel']
nombres_f = ['Maria', 'Laura', 'Ana', 'Sofia', 'Elena', 'Patricia', 'Claudia', 'Gabriela', 'Isabel', 'Carmen']
apellidos = ['Perez', 'Gonzalez', 'Martinez', 'Sanchez', 'Ramirez', 'Lopez', 'Garcia', 'Rodriguez', 'Diaz', 'Morales']
profesiones = ['Ingeniero', 'Doctor', 'Arquitecto', 'Abogado', 'Contador', 'Enfermero', 'Programador', 'Diseñador', 'Profesor', 'Psicologo', 'Chef', 'Electricista', 'Mecanico', 'Analista']

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

start_date = datetime(1960, 1, 1)
end_date = datetime(2000, 12, 31)

with open('datos_registro.csv', 'w', newline='') as csvfile:
    fieldnames = ['carnet', 'nombres', 'apellidos', 'sexo', 'fecha_nac', 'profesion', 'celular', 'direccion']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for i in range(1, 501):
        sexo = random.choice(['M', 'F'])
        if sexo == 'M':
            nombre = random.choice(nombres_m)
        else:
            nombre = random.choice(nombres_f)
        
        writer.writerow({
            'carnet': 1000 + i,
            'nombres': nombre,
            'apellidos': f"{random.choice(apellidos)} {random.choice(apellidos)}",
            'sexo': sexo,
            'fecha_nac': random_date(start_date, end_date).strftime('%Y-%m-%d'),
            'profesion': random.choice(profesiones),
            'celular': f"555{1000 + i}",
            'direccion': f"Calle {random.randint(1, 50)} #{random.randint(100, 999)}"
        })

print("Archivo datos_registro.csv generado con 500 registros")
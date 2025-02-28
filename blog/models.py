from django.db import models

class Profesor(models.Model): 
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=100) 
    email = models.EmailField() 
    materia = models.CharField(max_length=100) 
    
    def __str__(self): return f"{self.nombre} {self.apellido} - {self.materia}" 
    

class Curso(models.Model): 
    nombre = models.CharField(max_length=100) 
    comision = models.IntegerField() 
    
    def __str__(self): return self.nombre 
    
    
class Estudiante(models.Model): 
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=100) 
    email = models.EmailField() 
    carrera = models.CharField(max_length=100, default='Sistemas')
    
    def __str__(self): return f"{self.nombre} {self.apellido} {self.carrera}" 
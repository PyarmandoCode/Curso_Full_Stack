from django.db import models


class peliculas(models.Model):
    reseña = models.CharField(max_length=50)
    puntuacion = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    descripcion = models.TextField(blank=True)
    contenido = models.CharField(max_length=40,blank=True)
    imagen= models.ImageField(upload_to="tapas",blank=True)
    estado = models.BooleanField(default=True)
    sipnosis = models.TextField(blank=True)
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.reseña 
    

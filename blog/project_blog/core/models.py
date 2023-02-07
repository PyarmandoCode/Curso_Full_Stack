from django.db import models


class post(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    tapa = models.ImageField(upload_to="images/", blank=True, null=True)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)  # Nombre del proyecto
    link_github = models.URLField(max_length=200, blank=True, null=True)  # Enlace al repositorio de GitHub
    link_online = models.URLField(max_length=200, blank=True, null=True)  # Enlace al proyecto en línea
    fecha_creacion = models.DateField()  # Fecha de creación del proyecto
    fecha_actualizacion = models.DateField()  # Fecha de la última actualización del proyecto
    imagen_proyecto = models.ImageField(
        upload_to='imgprojects/', 
        null=True, 
        blank=True, 
        verbose_name="Imagen de proyecto"
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-fecha_creacion']

from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    #multiopcs
    CATEGORIES=[
        ('tech', 'Technology'),
        ('lifestyle', 'Lifestyle'),
        ('education', 'Education'),
        ('news', 'News'),
    ]


    # Título del post
    titulo = models.CharField(max_length=200, verbose_name="Título")

    # Contenido del post
    contenido = models.TextField(verbose_name="Contenido")

    #categoria
    categoria = models.CharField(max_length=30, choices=CATEGORIES, default='tech')

    # Imagen de banner
    imagen_banner = models.ImageField(
        upload_to='banners/', 
        null=True, 
        blank=True, 
        verbose_name="Imagen de Banner"
    )

    # Contenido embebido (permitido HTML)
    contenido_embebido = models.TextField(
        null=True, 
        blank=True, 
        verbose_name="Contenido Embebido (HTML)"
    )

    # Fecha de creación
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    # Fecha de última actualización
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Última Actualización")

    # Método para representar el modelo en el administrador de Django
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-fecha_creacion']

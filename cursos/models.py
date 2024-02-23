from django.db import models

class Curso(models.Model):
    niveis_de_curso = (
        ('Iniciante', 'Iniciante'),
        ('Intermediário', 'Intermediário'),
        ('Avançado', 'Avançado'),
    )
    titulo = models.CharField(max_length=50)
    nivel = models.CharField(max_length=15, choices=niveis_de_curso)
    carga_horaria = models.IntegerField()
    data = models.DateField(help_text='aaaa/mm/dd')
    descricao = models.TextField()
    verbose_name = 'Cadastro de curso'
    verbose_name_plural = 'Cadastros de cursos'
    ordering = ['-data']
    
    def __str__(self):
        return f'{self.titulo}: {self.data} - {self.carga_horaria} horas'
from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, related_name='alunos')
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"

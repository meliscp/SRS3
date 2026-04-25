from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория атауы")

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects', verbose_name="Категория")
    title = models.CharField(max_length=200, verbose_name="Жоба атауы")
    description = models.TextField(verbose_name="Сипаттамасы")
    location = models.CharField(max_length=100, verbose_name="Өтетін орны")
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name="Жарияланған күні")

    def __str__(self):
        return self.title


class Application(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='applications', verbose_name="Жоба")
    volunteer_name = models.CharField(max_length=100, verbose_name="Еріктінің аты")
    phone = models.CharField(max_length=20, verbose_name="Телефон нөмірі")
    message = models.TextField(verbose_name="Неліктен қатысқыңыз келеді?")

    def __str__(self):
        return f"{self.volunteer_name} - {self.project.title}"

from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"

class Grade(models.Model):
    name = models.CharField(max_length=5)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    subjects = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.name}, {self.class_teacher}"

class Student(models.Model):
    name = models.CharField(max_length=255)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Name: {self.name}, Grade: {Grade.objects.get(id=self.grade_id).name}"
from django.db import models
from django.contrib.auth.models import User

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/')
    description = models.TextField()

    def __str__(self):
        return self.name


# Lesson Model
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Enrollment Model
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Question Model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


# Choice Model
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


# Submission Model
class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return str(self.enrollment)

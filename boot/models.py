from django.db import models

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name


class Students(models.Model):
    # ENGLISH = 'EN'
    # GERMAN = 'GER'
    #
    # COURSE_CHOICES = [
    #     (ENGLISH, 'English Language Course'),
    #     (GERMAN, 'German Language Course'),
    # ]
    # course = models.CharField(
    #     max_length=20,
    #     choices=COURSE_CHOICES,
    #     default=GERMAN,
    # )
    course_name = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

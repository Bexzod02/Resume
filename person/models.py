from django.db import models
from main.models import Category

# TYPE = (
#     (0, 'Education'),
#     (1, 'Experience'),
#     (2, 'Skills'),
#     (3, 'Awards'),
# )


class Partner(models.Model):
    image = models.ImageField(upload_to='icon')

    def __str__(self):
        return self.image.name


class About(models.Model):
    name = models.CharField(max_length=202)
    image = models.ImageField(upload_to='person')
    birth = models.DateField()
    live = models.CharField(max_length=202)
    zip_code = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=202)

    def __str__(self):
        return self.name


class Resume(models.Model):
    #start_finish = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=202)
   # profession = models.CharField(max_length=255, null=True, blank=True)
   # academy = models.CharField(max_length=255, null=True, blank=True)
    #icon = models.ImageField(upload_to='icon', null=True, blank=True)
    is_skill = models.BooleanField(default=False)
    #content = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.type:
            return self.type
        return 'Skill'

class AdditionalInfo(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    # experience
    start_finish = models.CharField(max_length=255, null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    academy = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(upload_to='icon', null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    # is_skill
    title = models.CharField(max_length=202, null=True)
    percent = models.IntegerField(null=True, blank=True)
    last_month = models.IntegerField(null=True, blank=True)
    last_week = models.IntegerField(null=True, blank=True)
    is_main = models.BooleanField(default=False)

class Projects(models.Model):
    image = models.ImageField(upload_to='projects')
    category = models.ManyToManyField(Category, blank=True)
    link = models.URLField()
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.profession
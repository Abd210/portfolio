# portfolio/portfolio_app/models.py

from django.db import models

class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name

class AboutMe(models.Model):
    title = models.CharField(max_length=100, default="About Me")
    content = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    expected_graduation = models.DateField()
    relevant_subjects = models.TextField()

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="Bucharest, Romania")  # Added default
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100, default="Bucharest, Romania")  # Added default
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(max_length=300, default="")  # Added default

    def __str__(self):
        return self.title

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Percentage of proficiency (0-100)")

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email

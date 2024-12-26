# portfolio/portfolio_app/admin.py

from django.contrib import admin
from .models import (
    SocialLink, AboutMe, Education, Experience,
    Project, Certification, Skill, ContactInfo
)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'location', 'expected_graduation')
    search_fields = ('institution', 'degree', 'field_of_study')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'location', 'start_date', 'end_date')
    list_filter = ('company', 'position')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'link')
    search_fields = ('title', 'description', 'technologies')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'issue_date')
    search_fields = ('title', 'issuer')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address')

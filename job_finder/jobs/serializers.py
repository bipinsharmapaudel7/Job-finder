from rest_framework import serializers
from .models import Profile, Job, JobApplication

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'skills', 'experience']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'location', 'salary', 'description', 'created_by']

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['job', 'applicant', 'applied_on']

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework import filters  # Import filters for search functionality
from .models import Profile, Job, JobApplication
from .serializers import JobSerializer, ProfileSerializer, JobApplicationSerializer

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)
    user = User.objects.create_user(username=username, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

@api_view(['GET', 'POST'])
def manage_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile.name = request.data.get('name', profile.name)
        profile.skills = request.data.get('skills', profile.skills)
        profile.experience = request.data.get('experience', profile.experience)
        profile.save()
        return Response({'message': 'Profile updated!'})
    return Response({
        'name': profile.name,
        'skills': profile.skills,
        'experience': profile.experience
    })

class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [filters.SearchFilter]  # Search filter
    search_fields = ['title', 'location', 'salary']  # Fields you can search on

@api_view(['POST'])
def apply_for_job(request, job_id):
    job = Job.objects.get(id=job_id)
    application, created = JobApplication.objects.get_or_create(job=job, applicant=request.user)
    if created:
        return Response({'message': 'Application successful!'})
    return Response({'message': 'You have already applied for this job.'}, status=400)

class JobCreateView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]

class JobUpdateView(UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]

class JobDeleteView(DestroyAPIView):
    queryset = Job.objects.all()
    permission_classes = [IsAdminUser]

@api_view(['GET'])
def view_applications(request, job_id):
    if not request.user.is_staff:
        return Response({'error': 'Permission denied.'}, status=403)
    
    job = Job.objects.get(id=job_id)
    applications = JobApplication.objects.filter(job=job)
    serializer = JobApplicationSerializer(applications, many=True)
    return Response(serializer.data)

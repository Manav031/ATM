from django.forms import ModelForm
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TeacherForm(ModelForm):
    class Meta:
        model = models.Instructor
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1']

class AddBatch(ModelForm):
    class Meta:
        model = models.Section
        fields = ['section_id', 'department', 'num_class_in_week']

class AddSubject(ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'

class AddClassroom(ModelForm):
    class Meta:
        model = models.Room
        fields = '__all__'

class AddDepartment(ModelForm):
    class Meta:
        model = models.Department
        fields = '__all__'

class AddTimeslots(ModelForm):
    class Meta:
        model = models.MeetingTime
        fields = '__all__'
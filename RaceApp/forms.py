from django import forms
from . models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TeacherProfile,StudentProfile,AssignmentT,Results

class UsForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["username","eid"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		"eid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Unique Id",
			}),
		}

class TprofileForm(forms.ModelForm):
	class Meta:
		model = TeacherProfile
		fields = ["tage","tgr",'tsubject','texpr','tdesg']
		widgets = {
		"tage":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your age",
			}),
		"tgr":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"tsubject":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your Subject",
			}),
		"texpr":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your Experience",
			}),
		"tdesg":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your Designation",
			}),
		}


class SprofileForm(forms.ModelForm):
	class Meta:
		model = StudentProfile
		fields = ["stage","sgr","sclass","semail"]
		widgets = {
		"stage":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your age",
			}),
		"sgr":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"sclass":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"semail":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter  parent Email",
			}),
		}


class AstForm(forms.ModelForm):
	class Meta:
		model = AssignmentT
		fields = ["anm","aname","aclass","asubject","astartdate","aenddate","amarks","adesc"]
		widgets = {
		"anm":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Assgn number",
			}),
		"aname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Assgn Name",
			}),
		"aclass":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"asubject":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"astartdate":forms.TextInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			}),
		"aenddate":forms.TextInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			}),
		"amarks":forms.NumberInput(attrs={
			"class":"form-control my-2",
			}),
		"adesc":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Assgn Desc",
			"rows":3,
			}),
		}

class ResultForm(forms.ModelForm):
	class Meta:
		model = Results
		fields = ["maths","hindi","eng","phy","biology","social"]
		widgets = {
		"maths":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"maths",
			}),
		"hindi":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Hindi",
			}),
		"eng":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"English",
			}),
		"phy":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Physics",
			}),
		"biology":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Biology",
			}),
		"social":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Social",
			}),
		}
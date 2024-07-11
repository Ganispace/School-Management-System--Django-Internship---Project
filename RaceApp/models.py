from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
	rt=[
	   (0,'Guest'),
	   (1,'student'),
	   (2,'Teacher'),
	]
	eid = models.CharField(max_length=20)
	role_type = models.IntegerField(default=0)

class TeacherProfile(models.Model):
	g = [
		("k","Select Your Gender"),
		('M',"Male"),
		("F","Female")
		]
	b = [
		("L","---select the subject---"),
        ('MATHS','mathamatics'),
        ('PHY','physics'),
        ('BIO','Biology'),
        ('SC','Social'),
        ('ENG','English'),
        ('HND','Hindi'),
	]
      
	tage = models.IntegerField()
	tgr = models.CharField(max_length=5,default='k',choices=g)
	tsubject = models.CharField(max_length=6,default='L',choices=b)
	
	texpr = models.IntegerField()
	tdesg = models.CharField(max_length=50)
	tstatus = models.BooleanField(default=0)
	tch = models.OneToOneField(User,on_delete=models.CASCADE)

class StudentProfile(models.Model):
	sg = [
		("h","Select Your Gender"),
		('M',"Male"),
		("F","Female")
	]
	
	y = [
		('0','----- Select class -----'),
		('1','1st class'),
		('2','2nd class'),
		('3','3rd class'),
		('4','4th class'),
		('5','5th class'),
		('6','6th class'),
		('7','7th class'),
		('8','8th class'),
		('9','9th class'),
		('10','10th class')
	]
	stage = models.IntegerField()
	sgr = models.CharField(max_length=5,default='h',choices=sg)
	sclass = models.CharField(max_length=12,default="0",choices=y)
	sstatus = models.BooleanField(default=0)
	semail = models.CharField(max_length=30)
	std = models.OneToOneField(User,on_delete=models.CASCADE)



class AssignmentT(models.Model):
	y = [
		('0','----- Select class -----'),
		('1','1st class'),
		('2','2nd class'),
		('3','3rd class'),
		('4','4th class'),
		('5','5th class'),
		('6','6th class'),
		('7','7th class'),
		('8','8th class'),
		('9','9th class'),
		('10','10th class')
	]
	P = [
		("J","---select the subject---"),
        ('MATHS','mathamatics'),
        ('PHY','physics'),
        ('BIO','Biology'),
        ('SC','Social'),
        ('ENG','English'),
        ('HND','Hindi'),
	]
	
	anm = models.IntegerField()
	aname = models.CharField(max_length=50)
	aclass = models.CharField(default="0",max_length=12,choices=y)
	asubject = models.CharField(max_length=10,default="j",choices=P)
	adesc = models.CharField(max_length=250)
	astartdate = models.DateField()
	aenddate = models.DateField()
	amarks = models.IntegerField(default=10)
	astatus = models.BooleanField(default=0)
	atch = models.ForeignKey(User,on_delete=models.CASCADE)


class Marks(models.Model):
	maths = models.IntegerField(default=50)
	hindi = models.IntegerField(default=50)
	eng = models.IntegerField(default=50)
	phy = models.IntegerField(default=50)
	biology = models.IntegerField(default=50)
	social = models.IntegerField(default=50)

	def total_marks(self):
		return self.maths+self.hindi+self.eng+self.phy+self.biology+self.social

	def percentage(self):
		total = self.total_marks()
		return (total / 600) * 100

class Results(models.Model):
	st_class = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
	st_eid = models.ForeignKey(User,on_delete=models.CASCADE)
	maths = models.IntegerField()
	hindi = models.IntegerField()
	eng = models.IntegerField()
	phy = models.IntegerField()
	biology = models.IntegerField()
	social = models.IntegerField()

	def total_marks(self):
		return self.maths+self.hindi+self.eng+self.phy+self.biology+self.social

	def percentage(self):
		total = self.total_marks()
		return (total / 600) * 100
		
			
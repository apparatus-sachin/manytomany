from django.db import models

class student(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class course(models.Model):
	name =models.CharField(max_length=50)
	students = models.ManyToManyField(student, through='Enrollment')
	def __str__(self):
		return self.name

class Enrollment(models.Model):
	student = models.ForeignKey(student,on_delete=models.CASCADE)
	course =models.ForeignKey(course,on_delete=models.CASCADE)
	date_enrolled = models.DateField()
	final_grade = models.CharField(max_length=1,blank=True,null=True)

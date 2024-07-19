from django.db import models

# Create your models here.
class Student(models.Model):
    Stu_name=models.CharField(max_length=50)
    Stu_email=models.EmailField()
    Stu_add=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Stu_name
    
class Course(models.Model):
    C_name=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.C_name

class Teacher(models.Model):
    T_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.T_name 
    
class School(models.Model):
    Scl_name=models.CharField(max_length=50) 
    Stu_name=models.OneToOneField(Student,on_delete=models.CASCADE)
    C_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    T_name=models.ManyToManyField(Teacher)
    
    
    def __str__(self):
        return self.Scl_name+' '+str(self.Stu_name)+' '+str(self.C_name)#+' '+str(self.T_name)
                                # yese kr ke persion ki puri detail show kra skte hai


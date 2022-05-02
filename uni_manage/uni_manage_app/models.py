from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class Staff(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class Course(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class Subject(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class Student(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255)
    profile_pic = models.FileField()
    address = models.TextField()
    course_id=models.ForeignKey(Course, on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class Attendance(models.Model):
    id = models.AutoField(primary_key = True)
    subject_id = models.ForeignKey(Subject, on_delete = models.DO_NOTHING)
    Attendance_date = models.DateField(auto_now_add= True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class AttendanceReport(models.Model):
    id = models.AutoField(primary_key = True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendace_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class LeaveReportStudent(models.Model):
    id = models.AutoField(primary_key = True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    leave_date = models.DateField()
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key = True)
    staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    leave_date = models.DateField()
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class FeedbackStudent(models.Model):
    id = models.AutoField(primary_key = True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    feedback_message = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class FeedbackStaff(models.Model):
    id = models.AutoField(primary_key = True)
    staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    feedback_message = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class NotificationStudent(models.Model):
    id = models.AutoField(primary_key = True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    notification_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class NotificationStaff(models.Model):
    id = models.AutoField(primary_key = True)
    staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    notification_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()



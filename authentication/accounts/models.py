# custom user model(email)
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

User = settings.AUTH_USER_MODEL


class MyAccountManager(BaseUserManager):
    def create_user(self, email, fullname, department, designation, employee_id=None, student_id=None, image=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            fullname=fullname,
            department=department,
            designation=designation,
            employee_id=employee_id,
            student_id=student_id,
            image=image,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, fullname=None, department=None, designation=None, employee_id=None, student_id=None, image=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            fullname=fullname,
            department=department,
            designation=designation,
            employee_id=employee_id,
            student_id=student_id,
            image=image,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    fullname = models.CharField(max_length=255, null=True)
    department = models.CharField(max_length=255, null=True)
    designation = models.CharField(max_length=255, null=True)
    employee_id = models.CharField(max_length=30, null=True, unique=True)
    student_id = models.CharField(max_length=30, null=True, unique=True)
    image = models.FileField(upload_to='images/%Y/%m/%d/', null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permission
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return self.is_admin


# class StudentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=60, null=True)
#     address = models.CharField(max_length=255, null=True)
#     date_of_birth = models.CharField(max_length=60, null=True)
#     blood_group = models.CharField(max_length=60, null=True)
#     gender = models.CharField(max_length=60, null=True)
#     department = models.CharField(max_length=60, null=True)
#     religion = models.CharField(max_length=60, null=True)
#     image = models.FileField(upload_to='images/%Y/%m/%d/', null=True)
#     update_on = models.DateTimeField(auto_now_add=True, null=True)
#
#     def __str__(self):
#         return self.user.email
#
#
# class TeacherProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=60, null=True, default='')
#     phone = models.CharField(max_length=60, null=True, default='')
#     address = models.CharField(max_length=255, null=True, default='')
#     date_of_birth = models.CharField(max_length=60, null=True, default='')
#     blood_group = models.CharField(max_length=60, null=True, default='')
#     gender = models.CharField(max_length=60, null=True, default='')
#     religion = models.CharField(max_length=60, null=True, default='')
#     initial = models.CharField(max_length=60, null=True, default='')
#     image = models.ImageField(upload_to='images/%Y/%m/%d/', null=True, default='')
#
#     def __str__(self):
#         return self.user.email








# custom user model(username)
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.conf import settings
#
# User = settings.AUTH_USER_MODEL
#
#
# class MyAccountManager(BaseUserManager):
#     def create_user(self, fullname, department, designation, email=None, employee_id=None, student_id=None, image=None,
#                     password=None):
#         # if not email:
#         #     raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             fullname=fullname,
#             department=department,
#             designation=designation,
#             employee_id=employee_id,
#             student_id=student_id,
#             image=image,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     # customizing authentication
#     def create_superuser(self, fullname, password, email, department=None, designation=None, employee_id=None,
#                          student_id=None, image=None):
#         user = self.create_user(
#             email=email,
#             password=password,
#             fullname=fullname,
#             department=department,
#             designation=designation,
#             employee_id=employee_id,
#             student_id=student_id,
#             image=image,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
#
# class Account(AbstractBaseUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     fullname = models.CharField(max_length=255, null=True, unique=True)
#     username = models.CharField(max_length=255, null=True)
#     department = models.CharField(max_length=255, null=True)
#     designation = models.CharField(max_length=255, null=True)
#     employee_id = models.CharField(max_length=30, null=True, unique=True)
#     student_id = models.CharField(max_length=30, null=True, unique=True)
#     image = models.FileField(upload_to='images/%Y/%m/%d/', null=True)
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'fullname'
#     REQUIRED_FIELDS = ['email']
#
#     objects = MyAccountManager()
#
#     def __str__(self):
#         return self.fullname
#
#     # For checking permissions. to keep it simple all admin have ALL permission
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#
#     # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
#     def has_module_perms(self, app_label):
#         return self.is_admin

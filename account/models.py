from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
    

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, username, phone, first_name, last_name, location, password):
        if not email:
            raise ValueError('Email must not be blank')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            phone = phone,
            first_name = first_name,
            last_name = last_name,
            location = location,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, phone, first_name, last_name, location, password):
        user = self.create_user(
            email=email, 
            username=username,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            location=location,
            password=password
        )
        user.is_superuser = True


class CustomUser (AbstractBaseUser):
    email = models.EmailField(max_length = 60, unique = True)
    username = models.CharField(max_length = 30, unique = True)
    phone = models.CharField(max_length = 17)
    first_name = models.CharField(verbose_name='first name' ,max_length = 20)
    last_name = models.CharField(verbose_name='last name' ,max_length = 20)
    profile_image = models.ImageField(verbose_name='profile image', upload_to = "uploads/users/profile_images", null=True, blank=True)
    location = models.CharField(max_length = 20)
    is_superuser = models.BooleanField(verbose_name='is superuser' ,default = False)
    is_staff = models.BooleanField(verbose_name='is staff', default=True)
    is_admin = models.BooleanField(verbose_name='is admin', default=True)
    is_active = models.BooleanField(verbose_name= 'is active', default=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name', 'location']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name + self.last_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True




from django.db import models
# from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
from django.utils import timezone
from django.core.validators import RegexValidator

# class UserManage(BaseUserManager):
#     use_in_migrations = True
#     def _create_user(self, username , phone_number  , **extrafields):
#
#             # creates and saves users with the given username , phone_number
#             now = timezone.now()
#             if not phone_number:
#                 raise ValueError('The given phone_number must be se')
#             if not username:
#                 raise ValueError('The given username must be se')
#             user = self.model(phone_number=phone_number , username=username ,
#             date_joined=now , **extrafields)
#
#             user.save(using=self.db)
#             return user
#     # def create_superuser(self,username , phone_number , false , **extrafields):
#     #     return self._create_user(username , phone_number , True , **extrafields)


class MyUser(models.Model):

    username = models.CharField(verbose_name='nickname',max_length=35 , unique=True ,
    help_text='Required , 35 characters or fewer , starting with Letter , digit or number' ,
    validators=[RegexValidator(r'^[a-z A-Z][a-z A-Z 0-9 _\.]+$)' , 'Enter a valid username starting with a-z , this value may contain letters , numbers and under score character',)],
    error_messages={'unique': ' a user with this username '})
    phone_number = models.BigIntegerField(verbose_name='mobile number' , unique=True , null=True , blank=True
    , validators=[RegexValidator(r'^989[0-3 , 9/\d{8}$','enter a valid number')] , error_messages={'unique':'a user with tis mobile number exist'})
    verified = models.BooleanField(default=False)

    # is_staff = models.BooleanField(verbose_name='admin', default=False,help_text='for diagnose user can log in admin site')
    date_joined = models.DateTimeField(default=timezone.now)

    # last_seen =
    # objects = UserManage()




    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'




from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """A custom user manager for creating my user class where
    email is the unique identifier instead of usernames"""

    # creating user
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given mobile_num and password.
        """
        # if not mobile_num:
        #     raise ValueError(('The email must be set'))
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # creting super user
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

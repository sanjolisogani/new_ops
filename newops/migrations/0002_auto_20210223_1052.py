# Generated by Django 3.0.5 on 2021-02-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newops', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='city',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='gender',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_agency',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_dealer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_driver',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_pictures',
        ),
        migrations.RemoveField(
            model_name='user',
            name='reset_password',
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(choices=[('IN', 'India'), ('US', 'USA'), ('CA', 'CANADA'), ('BE', 'Belguim'), ('CZ', 'Czechia'), ('DK', 'Denmark'), ('DE', 'Germany'), ('EE', 'Estonia'), ('IE', 'Ireland'), ('EL', 'Greece'), ('ES', 'Spain'), ('FR', 'France'), ('HR', 'Crotia'), ('IT', 'Italy'), ('CY', 'Cyprus'), ('LV', 'Latvia'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('HU', 'Hungary'), ('MT', 'Malta'), ('NL', 'Netherlands'), ('AT', 'Austria'), ('PL', 'Poland'), ('PT', 'Portugal'), ('RO', 'Romania'), ('SL', 'Slovenia'), ('SK', 'Slovakia'), ('FI', 'Finland'), ('SW', 'Sweden'), ('TH', 'Thailand')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_password_change',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='next_password_change',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_timezone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]

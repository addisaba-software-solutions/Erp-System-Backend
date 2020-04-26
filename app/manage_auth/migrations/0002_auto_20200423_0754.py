# Generated by Django 3.0.5 on 2020-04-23 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20200423_0754'),
        ('manage_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='claim',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_claim', to='hr.claimModel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_department', to='hr.DepartmentModel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='employe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='hr.EmployeModel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_role', to='hr.RoleModel'),
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-02 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects_api', '0002_rename_comments_comment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Projet'},
        ),
        migrations.AddField(
            model_name='contributor',
            name='permission',
            field=models.CharField(choices=[(1, 'Contributeur ou Contributrice'), (9, 'Auteur ou Autrice')], default=1, max_length=1),
        ),
        migrations.AddField(
            model_name='contributor',
            name='role',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors', to='projects_api.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=2048, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=128, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('BE', 'Back-End'), ('FE', 'Front-End'), ('IO', 'iOS'), ('AN', 'Android')], max_length=2, verbose_name='Type (plateforme)'),
        ),
        migrations.AlterUniqueTogether(
            name='contributor',
            unique_together={('user', 'project')},
        ),
    ]

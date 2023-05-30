# Generated by Django 4.2.1 on 2023-05-30 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=2048)),
                ('type', models.CharField(choices=[('BE', 'Back-End'), ('FE', 'Front-End'), ('IO', 'iOS'), ('AN', 'Android')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=2048)),
                ('tag', models.CharField(choices=[('BUG', 'Bug'), ('IMPROVE', 'Amélioration'), ('TASK', 'Tâche')], max_length=10)),
                ('priority', models.CharField(choices=[('LOW', 'Faible'), ('MODERATE', 'Moyenne'), ('HIGH', 'Élevée')], default='MODERATE', max_length=10)),
                ('status', models.CharField(choices=[('TODO', 'À faire'), ('PROGRESS', 'En cours'), ('COMPLETED', 'Terminé')], default='TODO', max_length=10)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_projects', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_projects', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_api.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_api.projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2048)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_comments', to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_api.issues')),
            ],
        ),
    ]

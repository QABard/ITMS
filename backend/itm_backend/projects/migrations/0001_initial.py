# Generated by Django 3.2.20 on 2023-08-04 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Название Проекта')),
                ('description', models.TextField(verbose_name='Описание Проекта')),
                ('deadline', models.DateField(verbose_name='Дата окончания проекта')),
                ('status', models.CharField(choices=[('Onboarding', 'Онбординг'), ('In progress', 'В работе'), ('Production', 'Проект взлетел'), ('Tests', 'Тестирование')], default='Onboarding', max_length=20, verbose_name='Статус проекта')),
                ('priority', models.CharField(choices=[('maximum', 'Максимальный'), ('average', 'Средний'), ('minimum', 'Минимальный'), ('urgent', 'Срочно')], max_length=20, verbose_name='Приоритет проекта')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации проекта')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления проекта')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Участник Проекта',
                'verbose_name_plural': 'Участники Проекта',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Backlog', 'Бэклог'), ('Todo', 'Необходимо сделать'), ('In progress', 'В работе'), ('In review', 'На рассмотрении'), ('Done', 'Завершено')], default='Backlog', max_length=20, verbose_name='Статус задачи')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания задачи')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления задачи')),
                ('deadline', models.DateField(verbose_name='Срок исполнения задачи')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Название задачи')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='TaskUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='projects.task', verbose_name='Задача')),
            ],
            options={
                'verbose_name': 'Задача пользователя',
                'verbose_name_plural': 'Задача пользователя',
                'ordering': ['id'],
            },
        ),
    ]

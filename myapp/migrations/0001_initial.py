# Generated by Django 3.0.5 on 2024-01-23 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('city', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(upload_to='author_profiles/')),
                ('author_id', models.CharField(editable=False, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pages', models.PositiveIntegerField()),
                ('cover_image', models.ImageField(upload_to='book_covers/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Genre')),
            ],
        ),
    ]
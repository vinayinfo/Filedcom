# Generated by Django 3.1.2 on 2021-04-29 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_time', models.DateTimeField()),
                ('duration_time', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AudioBook',
            fields=[
                ('audiobase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='audio.audiobase')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
            ],
            bases=('audio.audiobase',),
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('audiobase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='audio.audiobase')),
                ('name', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=100)),
                ('participents', models.CharField(max_length=100)),
            ],
            bases=('audio.audiobase',),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('audiobase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='audio.audiobase')),
                ('name', models.CharField(max_length=100)),
            ],
            bases=('audio.audiobase',),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-22 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageTitle', models.CharField(max_length=255)),
                ('messageTopic', models.CharField(max_length=255)),
                ('messageSubTopic', models.CharField(max_length=255)),
                ('messageDescription', models.TextField()),
                ('messageLength', models.IntegerField()),
                ('messageType', models.CharField(choices=[('video', 'Video'), ('audio', 'Audio')], max_length=10)),
                ('messagefile', models.FileField(upload_to='')),
                ('dateuploaded', models.DateTimeField(auto_now_add=True)),
                ('languageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.language')),
                ('projectCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projectcategory')),
                ('projectId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('projectSubcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projectsubcategory')),
            ],
        ),
        migrations.CreateModel(
            name='UsageLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('messageLength', models.IntegerField()),
                ('messageCompleted', models.BooleanField(default=False)),
                ('dateloged', models.DateTimeField(auto_now_add=True)),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.member')),
                ('messageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.message')),
            ],
        ),
    ]

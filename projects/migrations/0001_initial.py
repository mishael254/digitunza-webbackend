# Generated by Django 4.2.4 on 2023-09-22 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryName', models.CharField(default='Kenya', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countyName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languageName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizationName', models.CharField(max_length=255)),
                ('userID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=255)),
                ('projectZone', models.CharField(max_length=255)),
                ('projectStartDate', models.DateField()),
                ('projectEndDate', models.DateField()),
                ('projectGroupNo', models.IntegerField()),
                ('projectAnthem', models.FileField(blank=True, null=True, upload_to='')),
                ('projectTheme', models.FileField(blank=True, null=True, upload_to='')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.partner')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectcategoryName', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectSubcategoryName', models.CharField(max_length=80)),
                ('projectCategoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projectcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectOfficer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='projectCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projectcategory'),
        ),
        migrations.AddField(
            model_name='project',
            name='projectCountry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.country'),
        ),
        migrations.AddField(
            model_name='project',
            name='projectCounty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.county'),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membersFirstName', models.CharField(max_length=255)),
                ('membersLastName', models.CharField(max_length=255)),
                ('membersEmail', models.EmailField(max_length=254)),
                ('membersPhone', models.CharField(max_length=20)),
                ('memberGender', models.CharField(max_length=10)),
                ('memberAge', models.IntegerField()),
                ('memberOccupation', models.CharField(max_length=255)),
                ('memberCategory', models.CharField(blank=True, max_length=255, null=True)),
                ('groupId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.group')),
            ],
        ),
        migrations.CreateModel(
            name='GroupLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
                ('groupId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.group')),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.member')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='languageId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.language'),
        ),
        migrations.AddField(
            model_name='group',
            name='projectId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]

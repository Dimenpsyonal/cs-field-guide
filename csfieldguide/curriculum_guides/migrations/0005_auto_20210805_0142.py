# Generated by Django 2.2.22 on 2021-08-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum_guides', '0004_auto_20191008_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculumguide',
            name='introduction_xx_lr',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='curriculumguide',
            name='introduction_yy_rl',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='curriculumguide',
            name='name_xx_lr',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='curriculumguide',
            name='name_yy_rl',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='curriculumguidesection',
            name='content_xx_lr',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='curriculumguidesection',
            name='content_yy_rl',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='curriculumguidesection',
            name='name_xx_lr',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='curriculumguidesection',
            name='name_yy_rl',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]

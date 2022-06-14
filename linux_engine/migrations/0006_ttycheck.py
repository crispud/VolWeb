# Generated by Django 3.2.13 on 2022-06-13 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investigations', '0001_initial'),
        ('linux_engine', '0005_lsof'),
    ]

    operations = [
        migrations.CreateModel(
            name='TtyCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.BigIntegerField(null=True)),
                ('Module', models.CharField(max_length=255, null=True)),
                ('Name', models.CharField(max_length=255, null=True)),
                ('Symbol', models.CharField(max_length=255, null=True)),
                ('investigation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linux_ttycheck_investigation', to='investigations.uploadinvestigation')),
            ],
        ),
    ]

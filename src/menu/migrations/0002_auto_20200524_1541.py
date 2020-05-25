# Generated by Django 2.1.2 on 2020-05-24 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customization', models.CharField(max_length=250)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='published_date',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='order',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.Menu'),
        ),
    ]

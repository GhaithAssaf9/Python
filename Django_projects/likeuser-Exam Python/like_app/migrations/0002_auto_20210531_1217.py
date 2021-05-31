# Generated by Django 3.2.3 on 2021-05-31 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('like_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='though',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='though', to='like_app.users')),
            ],
        ),
        migrations.RemoveField(
            model_name='messages',
            name='user',
        ),
        migrations.DeleteModel(
            name='comments',
        ),
        migrations.DeleteModel(
            name='messages',
        ),
    ]
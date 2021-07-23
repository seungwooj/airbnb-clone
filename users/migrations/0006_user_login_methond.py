# Generated by Django 3.1 on 2021-07-23 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210722_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_methond',
            field=models.CharField(choices=[('email', 'Email'), ('github', 'Github'), ('kakao', 'KakaoTalk')], default='email', max_length=50),
        ),
    ]
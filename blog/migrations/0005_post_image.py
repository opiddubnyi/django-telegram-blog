# Generated by Django 4.0.4 on 2022-04-22 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_tag_alter_posttag_post_alter_posttag_tag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Image'),
        ),
    ]

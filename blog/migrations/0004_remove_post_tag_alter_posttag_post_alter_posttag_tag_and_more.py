# Generated by Django 4.0.4 on 2022-04-20 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AlterField(
            model_name='posttag',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tag', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(default=None, max_length=20, verbose_name='Title'),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-15 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Authored',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example2.author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.ManyToManyField(through='example2.Authored', to='example2.Author')),
            ],
        ),
        migrations.AddField(
            model_name='authored',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example2.book'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(through='example2.Authored', to='example2.Book'),
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-13 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_id', models.IntegerField(verbose_name='Номер регистрации')),
                ('date_of_submission', models.DateField(auto_now_add=True, verbose_name='Дата подвчи')),
                ('img', models.ImageField(upload_to='media', verbose_name='Картинка')),
                ('num', models.IntegerField(verbose_name='Номер Марки')),
            ],
            options={
                'verbose_name': 'Марка',
                'verbose_name_plural': 'Марки',
            },
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('adress', models.CharField(max_length=255, verbose_name='Адрес')),
                ('tel', models.CharField(max_length=255, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mark', verbose_name='Номер Марки')),
            ],
            options={
                'verbose_name': 'Патент',
                'verbose_name_plural': 'Патенты',
            },
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Код')),
                ('description', models.TextField(max_length=1500, verbose_name='Описание')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mark', verbose_name='Номер Марки')),
            ],
            options={
                'verbose_name': 'Код',
                'verbose_name_plural': 'Коды',
            },
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='ФИО')),
                ('adress', models.CharField(max_length=255, verbose_name='Адрес')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mark', verbose_name='Номер Марки')),
            ],
            options={
                'verbose_name': 'Заявитель',
                'verbose_name_plural': 'Заявители',
            },
        ),
    ]

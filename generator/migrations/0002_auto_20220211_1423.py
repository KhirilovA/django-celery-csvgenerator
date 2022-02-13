# Generated by Django 3.2.9 on 2022-02-11 12:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheme',
            name='choice1',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='choice10',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='choice2',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='choice3',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='choice4',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='choice5',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='choice6',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='choice7',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='choice8',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='choice9',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='name1',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='name10',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='name2',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='name3',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='name4',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='name5',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='name6',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='name7',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='name8',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='name9',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='order1',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='order10',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='order2',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='order3',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='order4',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='order5',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='order6',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='order7',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='order8',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='order9',
        ),
        migrations.CreateModel(
            name='SchemeColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_type', models.PositiveSmallIntegerField(choices=[(1, 'Name'), (2, 'Job'), (3, 'Email'), (4, 'Domain'), (5, 'Phone number'), (6, 'Company'), (7, 'Text'), (8, 'Age'), (9, 'Address'), (10, 'Date')], default=1)),
                ('name', models.CharField(default='None', max_length=255)),
                ('order', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.scheme')),
            ],
        ),
    ]

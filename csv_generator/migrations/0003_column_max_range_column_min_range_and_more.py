# Generated by Django 4.0.4 on 2022-05-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_generator', '0002_alter_column_data_type_dataset'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='max_range',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='column',
            name='min_range',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='column',
            name='data_type',
            field=models.CharField(choices=[('Full name', 'Full name'), ('Job', 'Job'), ('Date', 'Date'), ('Integer', 'Integer')], max_length=50),
        ),
    ]

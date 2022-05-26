# Generated by Django 4.0.4 on 2022-05-26 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csv_generator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='data_type',
            field=models.CharField(choices=[('Full name', 'Full name')], max_length=50),
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('csv_file', models.FileField(upload_to='csv')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csv_generator.schema')),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-31 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterField(
            model_name='empleado',
            name='edad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]

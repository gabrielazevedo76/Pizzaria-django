# Generated by Django 4.0.3 on 2022-04-13 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_flavor_cover_alter_pedido_situation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavor',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='App/static/img/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='situation',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done')], default='Pending', max_length=30, null=True),
        ),
    ]

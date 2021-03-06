# Generated by Django 4.0.3 on 2022-04-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_flavor_cover_alter_pedido_situation'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavor',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='App/media/img/%Y/%m/%d/'),
        ),
    ]

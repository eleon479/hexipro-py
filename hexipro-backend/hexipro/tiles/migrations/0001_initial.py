# Generated by Django 3.0.11 on 2021-01-07 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField(default=0)),
                ('column', models.IntegerField(default=0)),
                ('power', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tile_owner', to='players.Player')),
            ],
        ),
    ]

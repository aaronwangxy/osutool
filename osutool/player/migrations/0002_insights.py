# Generated by Django 4.2.6 on 2023-11-05 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_accuracy', models.FloatField()),
                ('avg_map_length', models.FloatField()),
                ('fav_mod', models.CharField(max_length=255)),
                ('farmable_pp', models.FloatField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
            ],
            options={
                'verbose_name_plural': 'Insights',
            },
        ),
    ]
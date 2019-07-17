# Generated by Django 2.1.7 on 2019-07-17 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('odds', models.FloatField()),
                ('home', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='awayteam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awayteam', to='games.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='hometeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hometeam', to='games.Team'),
        ),
    ]

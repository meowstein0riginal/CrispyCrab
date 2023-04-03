# Generated by Django 4.2 on 2023-04-03 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ing_name', models.CharField(max_length=25, unique=True)),
                ('ing_quantity', models.IntegerField(default=0)),
                ('multi_pack_quantity', models.IntegerField(default=1)),
                ('unit', models.CharField(choices=[('PC', 'pcs.'), ('GR', 'gr.'), ('ML', 'ml')], default='PC', max_length=2)),
                ('multi_pack_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('minimal_quantity', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['ing_name'],
            },
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30, unique=True)),
                ('item_description', models.CharField(max_length=150)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['item_name'],
            },
        ),
        migrations.CreateModel(
            name='RecipeRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crispy_crab.ingredients')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crispy_crab.menuitems')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('table', models.IntegerField()),
                ('menu_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crispy_crab.menuitems')),
            ],
        ),
    ]

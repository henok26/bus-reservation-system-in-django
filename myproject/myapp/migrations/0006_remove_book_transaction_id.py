# Generated by Django 4.0 on 2023-06-12 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_book_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='transaction_id',
        ),
    ]

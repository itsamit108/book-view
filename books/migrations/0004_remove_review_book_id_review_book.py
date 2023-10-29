# Generated by Django 4.2.5 on 2023-10-14 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_review_book_id_review_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book_id',
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-21 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course_title", models.CharField(max_length=30)),
                ("course_description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("session_no", models.IntegerField(default=0)),
                ("session_title", models.CharField(max_length=50)),
                ("session_objective", models.CharField(max_length=500)),
                ("session_note", models.CharField(max_length=20)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.course"
                    ),
                ),
            ],
        ),
    ]
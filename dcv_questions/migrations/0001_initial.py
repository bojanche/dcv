# Generated by Django 4.0.6 on 2022-07-11 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionText', models.CharField(max_length=500)),
                ('questionGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcv_questions.questionsgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=500)),
                ('trueAnswer', models.BooleanField(default=False)),
                ('theQuestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcv_questions.questions')),
            ],
        ),
    ]

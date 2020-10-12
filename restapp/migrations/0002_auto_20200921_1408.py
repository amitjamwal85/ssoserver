# Generated by Django 3.1 on 2020-09-21 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkLessonRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, null=True)),
                ('request_by', models.CharField(max_length=100, null=True)),
                ('request_to', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OngoingSupportRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, null=True)),
                ('request_by', models.CharField(max_length=100, null=True)),
                ('request_to', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='billingtransaction',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='ExpenseConnectRequestOngoingSupport',
            fields=[
                ('billingtransaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='restapp.billingtransaction')),
                ('ongoing_support_request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restapp.ongoingsupportrequest')),
            ],
            bases=('restapp.billingtransaction',),
        ),
        migrations.CreateModel(
            name='ExpenseConnectRequestBulkLesson',
            fields=[
                ('billingtransaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='restapp.billingtransaction')),
                ('bulk_lesson_request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restapp.bulklessonrequest')),
            ],
            bases=('restapp.billingtransaction',),
        ),
    ]

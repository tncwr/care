# Generated by Django 2.2.11 on 2022-01-01 18:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0273_auto_20210825_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='UCCBedRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('TypeOfCaller', models.IntegerField(choices=[(1, 'PATIENT'), (2, 'ATTENDER')], default=1)),
                ('TypeOfBedReq', models.CharField(max_length=2000)),
                ('Counseling_Required', models.IntegerField(choices=[(1, 'TRUE'), (0, 'FALSE')], default=None)),
                ('Remarks', models.TextField(default=None, max_length=2000, null=True)),
                ('Name', models.CharField(max_length=2000)),
                ('Age', models.IntegerField(default=None, null=True)),
                ('Gender', models.CharField(max_length=2000)),
                ('Address', models.TextField(default=None, max_length=2000, null=True)),
                ('Mobile', models.IntegerField(default=None, null=True)),
                ('District', models.CharField(max_length=2000)),
                ('Taluk', models.CharField(max_length=2000)),
                ('HomeorHsptl', models.IntegerField(choices=[(1, 'HOME'), (2, 'HOSPITAL'), (3, 'TRIAGE_FACILITY'), (4, 'TRANSIT_AMBULANCE')], default=None)),
                ('HospitalName', models.TextField(default=None, max_length=2000, null=True)),
                ('confustion', models.IntegerField(choices=[(1, 'TRUE'), (0, 'FALSE')], default=None)),
                ('breathlessness', models.IntegerField(choices=[(1, 'TRUE'), (0, 'FALSE')], default=None)),
                ('fever', models.IntegerField(choices=[(1, 'TRUE'), (0, 'FALSE')], default=None)),
                ('DM', models.IntegerField(choices=[(1, 'TRUE'), (0, 'FALSE')], default=None)),
                ('HT', models.IntegerField(choices=[(1, 'TRUE'), (0, 'FALSE')], default=None)),
                ('IHD', models.IntegerField(choices=[(1, 'TRUE'), (0, 'FALSE')], default=None)),
                ('SpO2', models.CharField(max_length=2000)),
                ('O2', models.CharField(max_length=2000)),
                ('RR', models.CharField(max_length=2000)),
                ('PR', models.CharField(max_length=2000)),
                ('BP_Systolic', models.CharField(max_length=2000)),
                ('BP_Diastolic', models.CharField(max_length=2000)),
                ('CT', models.CharField(max_length=2000)),
                ('Bed', models.IntegerField(choices=[(1, 'GOVERMENT_HOSPITAL'), (2, 'PRIVATE_HOSPITAL'), (3, 'ANY_OF_THE_ABOVE')], default=None)),
                ('SourceType', models.IntegerField(choices=[(1, 'ONENOTFOUR'), (2, 'WARROOM')], default=None)),
                ('Asthma', models.IntegerField(choices=[(1, 'TRUE'), (0, 'FALSE')], default=None)),
                ('Chronic_Kidney_Disease', models.IntegerField(choices=[(1, 'TRUE'), (0, 'FALSE')], default=None)),
                ('CT1', models.IntegerField(default=None, null=True)),
                ('InsertDate', models.DateTimeField(blank=True, null=True)),
                ('priority_status', models.IntegerField(choices=[(1, 'LOW'), (2, 'MEDIUM'), (3, 'HIGH')], default=None)),
                ('BedAllotmentStatus', models.IntegerField(choices=[(1, 'ACCEPTED'), (2, 'REJECTED')], default=None)),
                ('TriageID', models.IntegerField(default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

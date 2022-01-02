import enum

from django.db import models

from care.facility.models import FacilityBaseModel
from care.users.models import User
from django.contrib.postgres.fields import JSONField


class UCCBedRequest(FacilityBaseModel):
    class AllotmentStatus(enum.Enum):
        ACCEPTED = 1
        REJECTED = 2

    AllotmentStatusChoices = [(e.value, e.name) for e in AllotmentStatus]


    class SourceType(enum.Enum):
        ONENOTFOUR = 1
        WARROOM = 2

    SourceTypeChoices = [(e.value, e.name) for e in SourceType]

    class CallerType(enum.Enum):
        PATIENT = 1
        ATTENDER = 2

    CallerTypeChoices = [(e.value, e.name) for e in CallerType]

    class BooleanValues(enum.Enum):
        TRUE = 1
        FALSE = 0

    BooleanValuesChoices = [(e.value, e.name) for e in BooleanValues]

    class AdmitType(enum.Enum):
        HOME = 1
        HOSPITAL = 2
        TRIAGE_FACILITY = 3
        TRANSIT_AMBULANCE = 4

    AdmitTypeChoices = [(e.value, e.name) for e in AdmitType]

    class BedType(enum.Enum):
        GOVERMENT_HOSPITAL = 1
        PRIVATE_HOSPITAL = 2
        ANY_OF_THE_ABOVE = 3

    BedTypeChoices = [(e.value, e.name) for e in BedType]

    class PriorityStatus(enum.Enum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    PriorityStatusChoices = [(e.value, e.name) for e in PriorityStatus]

    TypeOfCaller = models.IntegerField(choices=CallerTypeChoices, default=CallerType.PATIENT.value)
    TypeOfBedReq = models.CharField(max_length=2000)
    Counseling_Required = models.IntegerField(choices=BooleanValuesChoices, default=None)
    Remarks = models.TextField(max_length=2000, null=True, default=None)
    Name = models.CharField(max_length=2000)
    Age = models.IntegerField(null=True, default=None)
    Gender = models.CharField(max_length=2000)
    Address = models.TextField(max_length=2000, null=True, default=None)
    Mobile = models.IntegerField(null=True, default=None)
    District = models.CharField(max_length=2000)
    Taluk = models.CharField(max_length=2000)
    HomeorHsptl = models.IntegerField(choices=AdmitTypeChoices, default=None)
    HospitalName = models.TextField(max_length=2000, null=True, default=None)
    confustion = models.IntegerField(choices=BooleanValuesChoices, default=None)
    breathlessness = models.IntegerField(choices=BooleanValuesChoices, default=None)
    fever = models.IntegerField(choices=BooleanValuesChoices, default=None)
    DM = models.IntegerField(choices=BooleanValuesChoices, default=None)
    HT = models.IntegerField(choices=BooleanValuesChoices, default=None)
    IHD = models.IntegerField(choices=BooleanValuesChoices, default=None)
    SpO2 = models.CharField(max_length=2000)
    O2 = models.CharField(max_length=2000)
    RR = models.CharField(max_length=2000)
    PR = models.CharField(max_length=2000)
    BP_Systolic = models.CharField(max_length=2000)
    BP_Diastolic = models.CharField(max_length=2000)
    CT = models.CharField(max_length=2000)
    Bed = models.IntegerField(choices=BedTypeChoices, default=None)
    SourceType = models.IntegerField(choices=SourceTypeChoices, default=None)
    Asthma = models.IntegerField(choices=BooleanValuesChoices, default=None)
    Chronic_Kidney_Disease = models.IntegerField(choices=BooleanValuesChoices, default=None)
    CT1 = models.IntegerField(null=True, default=None)
    InsertDate = models.DateTimeField(null=True, blank=True)
    priority_status = models.IntegerField(choices=PriorityStatusChoices, default=None)
    BedAllotmentStatus = models.IntegerField(choices=AllotmentStatusChoices, default=None)
    TriageID = models.IntegerField(null=True, default=None)




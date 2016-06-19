from django.db import models
from django.core.validators import RegexValidator


class Brother(models.Model):
    # General profile information
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    FIFTH_YEAR = 'FY'
    ALUMNI = 'AL'

    SCHOOL_STATUS_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (FIFTH_YEAR, 'Fifth Year'),
        (ALUMNI, 'Alumni'),
    )
    school_status = models.CharField(
        max_length=2,
        choices=SCHOOL_STATUS_CHOICES,
        default=FRESHMAN,
    )

    BROTHER_STATUS_CHOICES = (
        ('0', 'Candidate'),
        ('1', 'Brother'),
        ('2', 'Alumni'),
    )

    brother_status = models.CharField(
        max_length=1,
        choices=BROTHER_STATUS_CHOICES,
        default=0,
    )

    # Secretary Information
    case_ID = models.CharField(max_length=200)
    birthday = models.DateField()
    hometown = models.CharField(max_length=200, default="Cleveland, OH")

    # regex for proper phone number entry
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)  # validators should be a list

    # Vice President Information
    room_number = models.CharField(max_length=3, default="NA")
    current_residence = models.CharField(max_length=200, default="Theta Chi House")
    standing_committee = models.CharField(max_length=200, default="Not assigned")
    operational_committee = models.CharField(max_length=200, default="Not assigned")

    # Treasurer Information

    # Recruitment Information

    # Scholarship Information
    past_semester_gpa = models.DecimalField(max_digits=5, decimal_places=2, default=4.0)
    cumulative_gpa = models.DecimalField(max_digits=5, decimal_places=2, default=4.0)
    scholarship_plan = models.TextField(default="Scholarship plan has not been setup yet if you past semester GPA "
                                                "or cum GPA are below 3.0 you should "
                                                "setup a meeting to have this corrected")

    # Service Chair Information

    # Philanthropy Chair Information

    # Detail Manager Chair Information

    def __str__(self):
        return self.first_name + " " + self.last_name


class ServiceEvent(models.Model):
    name = models.CharField(max_length=200, default="Service Event")
    description = models.TextField(default="I did the service thing")
    hours = models.IntegerField(default=0)
    submitted = models.BooleanField(default=False)
    date = models.DateField()
    brother = models.ForeignKey(Brother, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ChapterEvent(models.Model):
    name = models.CharField(max_length=200, default="Chapter Event")
    date_time = models.DateTimeField()
    mandatory = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class EventExcuse(models.Model):
    event = models.ForeignKey(ChapterEvent, on_delete=models.CASCADE)
    brother = models.ForeignKey(Brother, on_delete=models.CASCADE)
    description = models.TextField(("I will not be attending %s because", event.name))
    response_message = models.TextField(default="Your excuse was not approved because")

    STATUS_CHOICES = (
        ('0', 'Pending'),
        ('1', 'Approved'),
        ('2', 'Denied'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='0',
    )

    def __str__(self):
        return self.brother.first_name + " " + self.brother.last_name + "- " + self.event.name

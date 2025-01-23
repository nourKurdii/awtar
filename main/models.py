from django.db import models

# Home Page Content
class AboutPageContent(models.Model):
    about = models.TextField()
    message = models.TextField()
    vision = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "Home Page Content"

# Events
def event_media_upload_path(instance, filename):
    event_type = instance.event.event_type
    return f'{event_type}/{filename}'

class Event(models.Model):
    TYPE_CHOICES = [
        ('run', 'Run'),
        ('workshop', 'Workshop'),
        ('exhibition', 'Exhibition'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    event_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Workshop')

    def __str__(self):
        return self.title

class EventMedia(models.Model):
    event = models.ForeignKey(Event, related_name='media', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_media_upload_path', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Media for {self.event.title}"

class ExhibitionParticipant(models.Model):
    exhibition = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    name = models.CharField(max_length=100)
    drawing = models.ImageField(upload_to='exhibition/', blank=True, null=True)

# Courses
class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_course = models.BooleanField(default=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    seasonal = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ActivityMedia(models.Model):
    activity = models.ForeignKey(Activity, related_name='media', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='activities/')
    video_url = models.URLField(blank=True, null=True)
    main_pic = models.BooleanField(default=False)

    def __str__(self):
        return f"Media for {self.activity.title}"

# Registrations
class Registration(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True, null=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.activity:
            return f"{self.full_name} registered for {self.activity.title}"
        return f"{self.full_name} (No Activity)"


# Announcements
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='announcements/',null=True)

    def __str__(self):
        return self.title


class License(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    document = models.FileField(upload_to='licenses/')

    def __str__(self):
        return self.title


# Team Members
class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Sponsors
class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='sponsors/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Tenders
class Tender(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    document = models.FileField(upload_to='tenders/')
    publish_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title

class TenderRegistration(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} registered for {self.tender.title}"

# Blog
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogMedia(models.Model):
    blog = models.ForeignKey(Blog, related_name='media', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blogs/')
    video_url = models.URLField(blank=True, null=True)


# Visits
class Visit(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    visit_date = models.DateField()

    def __str__(self):
        return self.title

class VisitMedia(models.Model):
    visit = models.ForeignKey(Visit, related_name='media', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='visits/')
    main_pic = models.BooleanField(default=False)

    def __str__(self):
        return f"Media for {self.visit.title}"


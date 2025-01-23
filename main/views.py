from django.shortcuts import render
from .models import *

def index(request):
    sponsors = Sponsor.objects.all()
    about_content = AboutPageContent.objects.first()
    course_activities = Activity.objects.filter(is_course=True)
    latest_news = Visit.objects.order_by('-visit_date')[:4]
    remaining_count = 8 - course_activities.count()

    if remaining_count > 0:
        non_course_activities = Activity.objects.filter(is_course=False)[:remaining_count]
    else:
        non_course_activities = Activity.objects.none()

    activities = list(course_activities) + list(non_course_activities)

    activity_data = []

    for activity in activities:
        main_media = ActivityMedia.objects.filter(activity=activity, main_pic=True).first()

        activity_data.append({
            'activity': activity,
            'main_media': main_media
        })

    news_data = []
    for n in latest_news:
        visit_media = VisitMedia.objects.filter(visit=n, main_pic=True).first()

        news_data.append({
            'visit': n,
            'visit_media': visit_media
        })
    context = {
        'about_content': about_content,
        'activity_data': activity_data,
        'sponsors': sponsors,
        'news_data': news_data
    }
    return render(request, 'index.html', context)

def about(request):
    about_content = AboutPageContent.objects.first()  # Get the first (and only) row
    team_members = TeamMember.objects.all()
    context = {
        'page_title': 'About Us',
        'team_members': team_members,
        'about_content': about_content
    }
    return render(request, 'about.html', context)

def tender(request):
    return render(request, 'tender.html')

def activities(request):
    return render(request, 'courses.html')

def activity(request):
    return render(request, 'course.html')

def event(request):
    return render(request, 'event.html')

def events(request):
    return render(request, 'events.html')

def activity_form(request):
    return render(request, 'activity_form.html')

def blog(request):
    return render(request, 'blog.html')

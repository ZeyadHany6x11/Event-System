from django.shortcuts import render, redirect ,get_object_or_404
from .models import Event


def home(request):

    search = request.GET.get('search')

    if search:
        events = Event.objects.filter(
            title__icontains=search
        ).order_by('date')

    else:
        events = Event.objects.all().order_by('date')

    return render(request, 'home.html', {
        'events': events
    })

def event_details(request, id):

    event = get_object_or_404(Event, id=id)

    return render(request, 'details.html', {
        'event': event
    })
def book_event(request, id):

    event = get_object_or_404(Event, id=id)

    if event.seats > 0:
        event.seats -= 1
        event.save()

    return redirect('details', id=event.id)
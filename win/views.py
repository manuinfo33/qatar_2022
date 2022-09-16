from django.shortcuts import render, redirect
from win.models import Participants
from win.forms import Form_participants

def create_participant(request):
    if request.method == 'POST':
        form=Form_participants(request.POST)

        if form.is_valid():
            Participants.objects.create(
                name=form.cleaned_data['name'],
                document=form.cleaned_data['document'],
                age=form.cleaned_data['age'],
                country=form.cleaned_data['country'],
                description=form.cleaned_data['description'],
            )
            return redirect(list_participants)
    
    elif request.method == 'GET':
        form= Form_participants()
        context={'form':form}

        return render(request, 'win/new_participant.html', context=context)


def list_participants(request):
    all_participants= Participants.objects.all()
    context={
        'all_participants':all_participants
    }
    return render(request, 'win/all_participants.html' , context=context)


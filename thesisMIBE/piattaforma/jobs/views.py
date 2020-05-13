from django.shortcuts import render
from .models import post_job
from .forms import post_jobModelForm
from django.http import HttpResponse

# Create your views here.


def creapost(request):
    form = post_jobModelForm(request.POST)
    if form.is_valid():
            form.save()
            return render(request,'jobs/submit.html')

    else:
        form= post_jobModelForm()


        context = {'form' : form}
        return render(request,'jobs/jobs_creation.html',context)





def viz_job(request):
    jobs = post_job.objects.all()
    return render(request,'jobs/jobs.html',{'jobs': jobs})





    # jobs = []
    # descrizioni = []
    # posizione = post_job.objects.all()
    # for pos in posizione:
    #     jobs.append(pos.posizione)
    #     descrizioni.append(pos.descrizione)
    # context = {'posizione': jobs,'descrizione': descrizioni}
    # return render(request, 'jobs/jobs.html', context=context)  # this will return context dictonary to the template

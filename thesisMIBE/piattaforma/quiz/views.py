from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Questions
from jobs.models import *
from .decorators import allowed_user

# Create your views here.
@allowed_user(allowed_roles=['Admin','Students'])
def quiz(request):
    choices = Questions.CAT_CHOICES
    print(choices)
    return render(request,
        'quiz/quiz.html',
        {'choices':choices})

def questions(request , choice):
    print(choice)
    ques = Questions.objects.filter(catagory__exact = choice)
    return render(request,
        'quiz/questions.html',
        {'ques':ques})

def result(request):
    category = ""
    print("result page")
    if request.method == 'POST':
        data = request.POST
        total=int(data.get("count"))
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)


        for i in range(len(ans)):
            if ans[i] == qans[i]:
                quest = Questions.objects.get(id = qid[i])
                category = quest.catagory
                quest.student.add(request.user)
                quest.save()
                score += 1
        jobs = post_job.objects.filter(categoria=category)
        # print(qid)
        # print(qans)
        # print(ans)
        print(score)
        if total==0:
            eff=0
        else:
            eff = (score/total)*100
    return render(request,
        'quiz/result.html',
        {'score':score,
        'eff':eff,
        'total':total,
         'jobs':jobs})






#
#
#
#
#
#
#

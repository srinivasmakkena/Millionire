"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpRequest,JsonResponse
from app.models import Question,UserRule,UserScore

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        name = request.POST.get('name')
        request.session['User_Name']=name
        request.session['Score']=0
        request.session['visited']=[]
        request.session.save()    
    # print(request.session.get('User_Name', None)==None , request.session.get('Score', None)==None)
    # print(request.session.__dict__)
    print(request.session.items)
    if request.session.get('User_Name', None)==None and request.session.get('Score', None)==None:
        return render(request,'app/userdata.html',
        {   'title':'Treasure Trail Adventure',
            'year':datetime.now().year})
    print(request.session.keys())
    print(len(request.session['visited'])==Question.objects.count(),len(request.session['visited']),Question.objects.count())
    if UserRule.objects.count()>0:
        if request.session.get('Score', None)>=UserRule.objects.all()[0].Max_Award or len(request.session['visited'])>=UserRule.objects.all()[0].Max_questions:
            question=None
            score=UserScore()
            score.userName=request.session['User_Name']
            score.score=round(float(request.session.get('Score', 0)), 2)
            score.save()
            return render(
                request,
                'app/gameover.html',
                {
                    'title':'Treasure Trail Adventure',
                    'year':datetime.now().year,
                    'Question':question,
                    'name': request.session['User_Name'],
                    'score':round(float(request.session.get('Score', 0)), 2)
                }
                )
    if len(request.session['visited'])==Question.objects.count():
        question=None
        score=UserScore()
        score.userName=request.session['User_Name']
        score.score=round(float(request.session.get('Score', 0)), 2)
        score.save()
        
        return render(
            request,
            'app/gameover.html',
            {
                'title':'Treasure Trail Adventure',
                'year':datetime.now().year,
                'Question':question,
                'name': request.session['User_Name'],
                'score':round(float(request.session.get('Score', 0)), 2)
            }
            )
    
    for i in Question.objects.all():
        print(i.id, request.session['visited'])
        if i.id not in request.session['visited']:
            question=i
            break    
    print(request.session['visited'])  
    print(question.__dict__)
    question.options=question.options.split("\n")
    question.id=question.id
    # print(question.__dict__)
    return render(
        request,
        'app/index.html',
        {
            'title':'Treasure Trail Adventure',
            'year':datetime.now().year,
            'Question':question,
            'name': request.session['User_Name'],
            'score':round(float(request.session.get('Score', 0)), 2),
            'max_questions':UserRule.objects.all()[0].Max_questions,
            'visited':len(request.session['visited'])
        }
    )

# del request.session['User_Name']
# del request.session['Score']

def end(request):
    request.session['User_Name']=None
    request.session['Score']=None
    request.session['visited']=None
    request.session.save()    
    return redirect('home')

def check_answer(request):
    if request.method=='POST':
        print(request.POST.get('answer'),request.POST.get('id'))
        ans=Question.objects.get(id=request.POST.get('id')).answer
        request.session['visited'].append(int(request.POST.get('id')))
        request.session.save()  
        if(ans.lower().strip()==request.POST.get('answer').lower().strip()):
            request.session['Score']+=float(Question.objects.get(id=request.POST.get('id')).award)
            request.session.save()  
            return JsonResponse({'is_correct':True})
        return JsonResponse({'is_correct':False})


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

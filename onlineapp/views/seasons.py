from django.views import View
from django.urls import resolve
from onlineapp.models import *
from django.shortcuts import  render,redirect
from django.db.models import *
#from onlineapp.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
class Seasonview(View):
    def get(self, request, *args, **kwargs):
        if kwargs:
            matches = Season.objects.filter(season=kwargs.get('id'))
            paginator=Paginator(matches,8)
            page=request.GET.get('page')
            m1=paginator.get_page(page)
            return render(request, 'hello.html', context={'list':m1 , 'pk': kwargs.get('pk')})
        matches = Season.objects.filter(season=2019)
        return render(request, 'hello.html', context={'list': matches})


class Matchview(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        match1=Season.objects.filter(id=kwargs.get('pk'))
        deliveries=Match.objects.filter(match=kwargs.get('pk'))
        top_runs=Match.objects.filter(match=kwargs.get('pk')).values('batsman','batting_team').annotate(the_Score=Sum('batsman_runs')).order_by('-the_Score')[:3]
        top_wickets=Match.objects.filter(match=kwargs.get('pk')).values('fielder','bowling_team').annotate(wic=Count('fielder')).order_by('-wic')[:3]
        return render(request,'hello1.html',context={'list': deliveries,'match':match1,'topruns':top_runs,'topwickets':top_wickets})

class Pointsview(View):
    def get(self,request,*args,**kwargs):
        matches = Season.objects.filter(season=kwargs.get('id')).values('winner').annotate(score=Count('winner')).order_by('-winner')
        return render(request, 'hello2.html', context={'list': matches})

class Homeview(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')


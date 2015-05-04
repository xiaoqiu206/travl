# coding=utf-8
from models import User, Travel
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import time
import utils


def login(request):
    data = request.POST
    username = data['username']
    password = data['password']
    if username and password:
        user = User.objects.filter(username=username)
        if user and user[0].password == password:
            request.session['username'] = username
            return HttpResponseRedirect('travelList/')
        else:
            data = {'display': 'block', 'error': u'用户名或密码错误'}
            return render_to_response('login_register.html', data)
    else:
        data = {'display': 'block', 'error': u'用户名或密码错误'}
        return render_to_response('login_register.html', data)


def register(request):
    data = request.POST
    username = data['username']
    password = data['password']
    if username and password:
        user = User.objects.filter(username=username)
        if user:  # 如果用户名已经被注册
            data = {'display': 'block', 'error': u'该用户名已经被注册'}
            return render_to_response('login_register.html', data)
        else:
            User.objects.create(username=username, password=password).save()
            data = {'display': 'block', 'error': u'注册成功,请登录'}
            return render_to_response('login_register.html', data)
    else:  # 如果用户名和密码没有填写
        data = {'display': 'none'}
        return render_to_response('login_register.html', data)


def travelList(request):
    if 'username' in request.session:  # 已经登陆
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        travels = Travel.objects.filter(travel_date__gte=now_date).order_by('travel_date')
        re_data = {}
        travel_code = ''
        travel_date = ''
        # print request.GET['travel_code']
        # print request.GET['date']
        if 'date' in request.GET and request.GET['date']:
            travels = travels.filter(travel_date=request.GET['date'])
            travel_date = request.GET['date']
        if 'travel_code' in request.GET and request.GET['travel_code']:
            travels = travels.filter(travel_code=request.GET['travel_code'])
            travel_code = request.GET['travel_code']
        if 'page' in request.GET:
            page = request.GET['page']
        else:
            page = '1'
        re_data = utils.page(travels, 20, page)
        re_data['travel_code'] = travel_code
        re_data['date'] = travel_date
        # re_data['now_date'] = now_date
        return render_to_response('travel_list.html', re_data)
    else:
        data = {'display': 'none'}
        return render_to_response('login_register.html', data)


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    data = {'display': 'none'}
    return render_to_response('login_register.html', data)

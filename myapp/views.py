# -*- coding: utf-8 -*-
from django.shortcuts import render
from collections import OrderedDict

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
import json, codecs, sys


# from myapp.forms import LoginForm


# def login(request):
#     lesson = ""
#     date = ""
#     homework = ""
#     submit = "off"
#     deadline = ""
#     valid = "off"
#
#     if request.method == "POST":
#         # Get the posted form
#         MyLoginForm = LoginForm(request.POST)
#
#         if MyLoginForm.is_valid():
#             lesson = MyLoginForm.cleaned_data['lesson']
#             date = MyLoginForm.cleaned_data['date']
#             homework = MyLoginForm.cleaned_data['homework']
#             submit = MyLoginForm.cleaned_data['submit']
#             deadline = MyLoginForm.cleaned_data['deadline']
#             valid = MyLoginForm.cleaned_data['valid']
#
#     else:
#         MyLoginForm = LoginForm()
#
#     return render(request, 'loggedin.html', {
#         "lesson": lesson,
#         "date": date,
#         "homework": homework,
#         "submit": submit,
#         "deadline": deadline,
#         "valid": valid
#     })


def login(request):
    lesson, date, homework, submit, deadline, valid = u"", u"", u"", False, u"", False
    if request.POST:
        lesson = request.POST[u'lesson']
        date = request.POST[u'date']
        homework = request.POST[u'homework'].replace(u'\r\n', '\n')
        deadline = request.POST[u'deadline']
        check = request.POST.getlist(u'check')
        act = int(request.POST[u'act'])
        if u'submit' in check:
            submit = True
        else:
            submit = False
        if u'valid' in check:
            valid = True
        else:
            valid = False
        obj = OrderedDict([
            (u'lesson', lesson),
            (u'date', date),
            (u'homework', homework),
            (u'submit', submit),
            (u'deadline', deadline),
            (u'valid', valid)
        ])
        with codecs.open(sys.path[0] +'/homework.json', 'r', 'utf-16') as f:
            ff = json.loads(f.read(), object_pairs_hook=OrderedDict)
        if act:
            del ff[u'list'][act - 1]
            ff[u'list'].insert(act - 1, obj)
        else:
            ff[u'list'].append(obj)
        with codecs.open(sys.path[0] +'/homework.json', 'w', 'utf-16') as f:
            f.write(json.dumps(ff, indent=2, ensure_ascii=False))
        return HttpResponseRedirect('/')
        #return render(request, 'loggedin.html', {
        #    u"lesson": lesson,
        #    u"date": date,
        #    u"homework": homework,
        #    u"submit": submit,
        #    u"deadline": deadline,
        #    u"valid": valid
        #})


def display(request):
    with codecs.open(sys.path[0] +'/homework.json', 'r', 'utf-16') as f:
        ff = json.loads(f.read(), object_pairs_hook=OrderedDict)
    alias = ff[u'alias']
    ls = ff[u'list']
    ls_index = [unicode(i + 1) for i in range(len(ls))]
    ls_lesson = [unicode(alias[unicode(i[u'lesson'])][0]) for i in ls]
    ls_date = [unicode(i[u'date']) for i in ls]
    ls_homework = [unicode(i[u'homework']) for i in ls]
    ls_submit = [i[u'submit'] for i in ls]
    ls_deadline = [unicode(i[u'deadline']) for i in ls]
    ls_valid = [i[u'valid'] for i in ls]
    ls_POST = zip(ls_index, ls_lesson, ls_date, ls_homework, ls_submit, ls_deadline, ls_valid)
    return render(request, 'display.html', {
        u"ls_POST_len": range(len(ls_POST)),
        u"ls_POST": ls_POST
    })


def Add(request):
    with codecs.open(sys.path[0] +'/homework.json', 'r', 'utf-16') as f:
        ff = json.loads(f.read(), object_pairs_hook=OrderedDict)
    alias = ff[u'alias']
    lesson_list = [i[0] for i in alias.values()]
    lesson_code = [i for i in alias.keys()]
    return render(request, 'login.html', {
        u'lesson_list': zip(lesson_code, lesson_list),
        u'act': 0,
        u'lesson': u'',
        u'date': u'',
        u'homework': u'',
        u'submit': False,
        u'deadline': u'',
        u'valid': True
    })


def manage(request):
    if request.POST:
        if u'delete' in request.POST:  # 删除
            item = int(request.POST[u'delete'])
            with codecs.open(sys.path[0] +'/homework.json', 'r', 'utf-16') as f:  # 读取 json
                ff = json.loads(f.read(), object_pairs_hook=OrderedDict)
            del ff[u'list'][item - 1]  # 删除数据
            with codecs.open(sys.path[0] +'/homework.json', 'w', 'utf-16') as f:  # 写入 json
                f.write(json.dumps(ff, indent=2, ensure_ascii=False))
            return HttpResponseRedirect('/')  # 跳转到主页
        elif u'modify' in request.POST:  # 修改
            item = int(request.POST[u'modify'])
            with codecs.open(sys.path[0] +'/homework.json', 'r', 'utf-16') as f:  # 读取 json
                ff = json.loads(f.read(), object_pairs_hook=OrderedDict)
            alias = ff[u'alias']
            lesson_list = [i[0] for i in alias.values()]
            lesson_code = [i for i in alias.keys()]
            return render(request, 'login.html', {
                u'lesson_list': zip(lesson_code, lesson_list),
                u'act': item,
                u'lesson': ff[u'list'][item - 1][u'lesson'],
                u'date': ff[u'list'][item - 1][u'date'],
                u'homework': ff[u'list'][item - 1][u'homework'],
                u'submit': ff[u'list'][item - 1][u'submit'],
                u'deadline': ff[u'list'][item - 1][u'deadline'],
                u'valid': ff[u'list'][item - 1][u'valid']
            })
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

    #return HttpResponse('Successfully deleted {0}'.format(item))

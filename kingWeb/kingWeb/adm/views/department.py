"""
Definition of views.
"""
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from django.core import serializers

from kingWeb.DynamicRouter import urls
from kingWeb.models import *
from django.contrib.auth.models import User

def index(request,kwargs):
    assert isinstance(request, HttpRequest)
    return render(request,
        'adm/department/index.html',
        {
            'title':'部门管理',
        })

def add(request,kwargs):
    assert isinstance(request, HttpRequest)
    departments = SysDepartment.objects.values('id','name')
    return render(request,
        'adm/department/add.html',
        {
            'title':'添加部门',
            'departments':departments
        })


def edit(request,kwargs):
    assert isinstance(request, HttpRequest)
    id = kwargs.get('id','')
    if id == '':
        return render(request, 'adm/department/index')
    object = SysDepartment.objects.get(id=id)
    departments = SysDepartment.objects.values('id','name')
    return render(request,
        'adm/department/edit.html',
        {
            'title':'编辑部门',
            'id':object.id,
            'name':object.name,
            'leader':object.leader,
            'description':object.description,
            'parentid':object.parentid,
            'departments':departments
        })

@csrf_exempt
def post_add(request,kwargs):
    assert isinstance(request, HttpRequest)
    result = ResultModel()
    parentid = request.POST.get('ParentId','')
    name = request.POST.get('Name','')
    leader = request.POST.get('Leader','')
    description = request.POST.get('Description','')
    object = SysDepartment.objects.create(parentid=parentid,name=name,leader=leader,description=description)
    result.msg = '操作成功'
    return HttpResponse(json.dumps(result.tojson()), content_type="application/json")

@csrf_exempt
def post_edit(request,kwargs):
    assert isinstance(request, HttpRequest)
    result = ResultModel()
    parentid = request.POST.get('ParentId','')
    id = request.POST.get('Id','')
    name = request.POST.get('Name','')
    leader = request.POST.get('Leader','')
    description = request.POST.get('Description','')
    object = SysDepartment.objects.filter(id=id).update(parentid=parentid,name=name,leader=leader,description=description)
    result.msg = '操作成功'
    return HttpResponse(json.dumps(result.tojson()), content_type="application/json")

@csrf_exempt
def post_delete(request,kwargs):
    result = ResultModel()
    assert isinstance(request, HttpRequest)
    ids = request.POST.getlist('ids[]')
    if ids == '':
        result.msg='操作失败'
        return HttpResponse(json.dumps(result.tojson()), content_type="application/json")

    object = SysDepartment.objects.filter(id__in=ids).delete()
    result.msg = '操作成功'
    return HttpResponse(json.dumps(result.tojson()), content_type="application/json")


@csrf_exempt
def get_page_data(request,kwargs):
    assert isinstance(request, HttpRequest)
    start = request.POST.get('start','0')
    length = request.POST.get('length','0')
    searchkey = request.POST.get('searchKey','')
    orderby = request.POST.get('orderBy','')
    orderdir = request.POST.get('orderDir','')
    draw = request.POST.get('draw','')
    value = request.POST.get('value','')
    _orderby = ''
    if orderdir == 'desc':
        _orderby = '-'
    if orderby != '':
        _orderby +=orderby
    else:
        _orderby +='id'

    alldata = None
    if searchkey != '':
        alldata = SysDepartment.objects.filter(description__icontains=searchkey).order_by(_orderby).\
        values('name','parentid','leader','description','id')
    else:
        alldata = SysDepartment.objects.order_by(_orderby).\
        values('name','parentid','leader','description','id')
    pagedata = list(alldata[int(start):int(length)])

    rownum = int(start)
    for row in pagedata:
        rownum = rownum + 1
        row['rownum'] = rownum
        pid = row['parentid']
        if pid != 0 and pid != None:
            row['parentname'] = SysDepartment.objects.get(id=pid).name
        else:
            row['parentname'] = '无'

    datatable = DataTableModel(draw,alldata.count(),alldata.count(),pagedata)

    return HttpResponse(json.dumps(datatable.tojson()), content_type="application/json")

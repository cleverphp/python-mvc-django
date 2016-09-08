from django.http import Http404
from django.shortcuts import render
import os

def index(request):
    
    path = request.path_info
    
    path = path.split('/')
    
    p_len = len(path)
    
    if p_len > 1 and len(path[1]) != 0:
        act = path[1]
    else:
        act = 'index'
        
    if p_len > 2 and len(path[2]) != 0:
        op = path[2]
    else:
        op = 'index'
        
    act_file = os.path.join(os.path.realpath(os.path.dirname('.')),'control')
    
    act_file = os.path.join(act_file,act+'.py')
    
    with open(act_file) as mvc:
        exec(mvc.read())
    '''
    r = {}
    r['ctrl'] = locals()
    return render(request,'index/index.html',r)
    '''
    return getattr(locals()[act+'Ctrl'](),op)(request)
    
    
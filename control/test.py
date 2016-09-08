class testCtrl:
    def index(self,request):
        r = {'name':'test'}
        r['path'] = request.path_info
        return render(request,'test/index.html',r)
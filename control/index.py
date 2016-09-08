class indexCtrl:
    def index(self,request):
        r = {'name':'ok'}
        return render(request,'index/index.html',r)
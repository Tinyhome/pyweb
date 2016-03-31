#coding:utf-8
from django.http.response import HttpResponse
from com.CommonFuncs import loadClass


def index(request,c1,c2):
    
    getClass=loadClass("com."+c1+"."+c2 +"Controller",c2,request)
    if getClass==None:
        return HttpResponse("404")
    
    return getClass.run()
    

def unlogin(request):  #用户注销
    r=HttpResponse()
    r.delete_cookie("userlogin_username")
    r.write("<script>self.location='/index'</script>")
    return r


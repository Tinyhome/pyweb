#coding:utf-8
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from mydb.models import myuser

class userlogin():
    
    input_Request=None
    
    def __init__(self,r):
        self.input_Request=r
    
    def run(self):
        
        if self.input_Request.GET.get("unlogin")!=None:
            return self.unlogin()

        beijing={"id":1,"name":"北京"}
        shanghai={"id":2,"name":"上海"}
        userAreas=[beijing,shanghai]
        dataset={"result":"","areas":userAreas}
        
        if self.input_Request.method=="POST":
            getUserName=self.input_Request.POST.get("txtUserName")
            getUserPass=self.input_Request.POST.get("txtUserPass")
            
            Login_result=self.login(getUserName,getUserPass)
        
            if Login_result:
                myResponse=HttpResponse("<script>self.location='/index/index'</script>")
                myResponse.set_cookie("userlogin_username",getUserName,3600)
                return myResponse
            else:
                dataset["result"]="用户名和密码错误"
            
        myResponse=render_to_response("userlogin.html",dataset)  

        return render_to_response("userlogin.html",dataset)    
    
        
    def login(self,uname,upass):    
        
        result=myuser.objects.filter(user_name=uname)
        if len(result)==1 and result[0].user_pass==upass:
            return True
        return False
   
   
   
    def unlogin(self):
        r=HttpResponse()
        r.delete_cookie("userlogin_username")
        r.write("<script>self.location='/index/index'</script>")
        return r
    
    
    
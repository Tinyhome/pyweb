#coding:utf-8
from django.shortcuts import render_to_response
from mydb.models import myuser
import datetime

class index():
    
    input_Request=None
    
    def __init__(self,r):
        self.input_Request=r
    
    def run(self):
        
        dataset={"result":"","currentuser":u"游客"}
        
        if self.input_Request.COOKIES.get("userlogin_username")!=None:
            dataset["currentuser"]=self.input_Request.COOKIES.get("userlogin_username")
  
                    
        myResponse=render_to_response("index.html",dataset)
            
        return myResponse
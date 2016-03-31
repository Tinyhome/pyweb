#coding:utf-8

def test():
    print "aaa"

class UserLogin:
    UserName=""
    UserPass=""
    
    #构造函数    
    def __init__(self,uname,upass):
        self.UserName=uname
        self.UserPass=upass
    
    def Login(self):
        if self.UserName=="tiny" and self.UserPass=="123":
            return True
        return False
    
    def run(self):
        print "run"

        
        


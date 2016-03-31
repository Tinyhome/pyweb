#coding:utf-8

def loadClass(pkgPath,className,r):
    
    try:
        pkg_main=__import__(pkgPath)
        split_pkg=pkgPath.split(".")
        for p in split_pkg[1:]:
            pkg_main=getattr(pkg_main,p)          #加载文件
        
        pkg_main=getattr(pkg_main, className)     #加载类
        retClass=pkg_main(r)                      #实例化
        
        return retClass
    except Exception,e:
        #print Exception
        #print e
        return None
    
#用字典创建一个平台的用户信息（包含用户名和密码）管理系统，新用户可以用与现有系统帐号不冲突的用户名创建帐号，
#已存在的老用户则可以用用户名和密码登陆重返系统。建议基本框架为(伪代码)：


def newusers():
    enter a name
    if the name is used in the system:
        enter again
    else:
        set the password
… …

def oldusers():
    Enter the  username and password
    if password is right:  
        print(name, 'welcome back ')  
    else:  
        print('login incorrect') 
    … …

def login():
    option = '''
             (N)ew User Login 
             (O)ld User Login
             (E)xit
                    '''
    Enter the option
    … …

if __name__ == '__main__':  
    login() 

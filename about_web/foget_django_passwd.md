# Django如何重设Admin密码

django的admin用户被设了一个随机密码又没有保存好，结果把密码给忘记了，需要重置。从网上搜索了一些方法。

从数据库重置的可能性为0，因为django对于密码有保护策略。考虑从运行程序的地方进行重置：

1. 在程序的文件夹下，执行这样的命令，进行shell窗口：  
    > python manage.py shell


2. 对admin用户进行修改密码：
```python
from django.contrib.auth.models import User  
user =User.objects.get(username='admin')  
user.set_password('new_password')  
user.save()  
```

结果，登录admin成功!

</br>

但是，还有疑问...我连用户名也不是太确定了

## 如果连用户名admin也忘记怎么办？　　　　
```python
from django.contrib.auth.models import User
user1 = User.objects.filter(is_superuser = True)
user2 = User.objects.filter(is_superuser = True, is_staff = True) 
print(user1, user2)
```

上面第二句选择了所有的超级用户，可以选择其中一个进行修改密码。  
第三句选择了是staff并且是superuser的用户。

　　　　　　

__注意：__默认情况下，只有是staff和superuser的双重身份才能进去django自带的admin管理后台并进行修改和管理。

_当只是staff的时候，只能进入后台，但是不能进行任何操作。当只是superuser状态时，则无法进入后台。_
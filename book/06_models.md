
### Django 创建表：

创建数据库表：
```python
from django.db import models


class Project(models.Model):
    """
    项目表
    """
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态：", default=True)
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    """
    模块表
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name
```

数据类型查看 ```C:\Python37\Lib\site-packages\django\db\models\fields\__init__.py```


### 数据库表操作：

* 创建
```python
Project.objects.create()
```

* 查询
```python
Project.objects.all()
Project.objects.get(pk=1)
Project.objects.filter(status=1)
Project.objects.filter(name__contains='项目')
```

* 更新
```python
g = Project.objects.get(name='xxx测试项目')
g.status=0
g.save()

Project.objects.select_for_update().filter(name__contains='项目').update(describe='')
```

* 删除
```python
Project.objects.get(name='xxx测试项目').delete()
```

* django模版日期格式
```
django数据库中的时间格式与页面渲染出来的时间格式不一致的处理。

在数据库中，时间是这样显示的：
create_time:2012-07-21 12:27:22 

在模版中使用：
post.create_time打印出来，时间格式是这样的：
July 21, 2012, 7:27 a.m.

想要得到：2012-07-21 12:27:22 
处理方法：
{{project.create_time|date:"Y-m-d H:i:s"}}
```


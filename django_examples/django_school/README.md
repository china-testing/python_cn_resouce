### 简介

Django的书看了很多，却始终没胆量下手做实际的Web的开发？这里有一些企业应用的实例供学习。本例是一个考试系统。

![](https://upload-images.jianshu.io/upload_images/12713060-209b85544b88e089.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

教师可以创建测验，学生可以注册并参加与他们兴趣相关的测验。

### 安装
```python
$ git clone https://github.com/china-testing/python_cn_resouce
$ cd django_examples/django_school/
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py loaddata datas.json
$ python manage.py runserver
```
### 初始用户
- 学生
  - username: teacher
  - password: teacher

- 教师
  - username: student
  - password: student






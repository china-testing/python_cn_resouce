# Awesome Flask [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

 收集了大量 Flask 相关的优秀应用、项目等资源，方便了 Flask 用户参考查阅。

[Flask 优秀资源大全](https://github.com/china-testing/python_cn_resouce/blob/main/fastapi.md ) 则是翻译而来。也欢迎你帮助推荐和提供建议

赞善或进入python技术群：钉钉或微信 pythontesting、 支付宝xurongzhong#gmail.com, 请将#替换为@。

python测试开发钉钉群：21745728，目前800多人，另有几千人的python测试开发微信群，可联系 钉钉或微信号 pythontesting 加群（备注：python）！

[python八字排盘](https://github.com/china-testing/bazi)  目前市面上功能最强大的八字排盘，科学的尽头是道教，玄学。



* 目录
   * [精品图书](#精品图书)
   * [框架](#框架) 
   * [管理界面](#管理界面)  
   * [验证](#验证)
   * [授权](#授权)
   * [数据库](#数据库)
   * [数据库迁移](#数据库迁移)
   * [缓存](#缓存)
   * [数据验证](#数据验证)
   * [速率限制](#速率限制)
   * [任务队列](#任务队列)
   * [异常跟踪](#异常跟踪)
   * [APM](#apm)
   * [其他SDK](#其他sdk)
   * [前端](#前端)
   * [开发(调试/测试/文档)](#开发调试测试文档)
   * [工具](#工具)
* [资源](#资源)
   * [教程](#教程)
   * [书籍](#书籍)
   * [幻灯片](#幻灯片)
   * [视频](#视频)
   * [项目](#项目)
   * [Boilerplate](#boilerplate)


## 精品图书

访问密码: 2274, 无需注册，点击普通下载即可。如遇失效可加钉钉或微信 pythontesting获取。

- [Web API Development with Python A Beginners Guide using Flask and FastAPI .epub](https://url97.ctfile.com/f/18113597-809569549-740e43?p=2274)

- [Flask Web开发实战：入门、进阶与原理解析 - 2018.pdf](https://itbooks.ctfile.com/fs/18113597-319371801)

- [Flask Web开发：基于Python的Web应用开发实战（第2版）- 2018.pdf](https://itbooks.ctfile.com/fs/18113597-319371799)

- [深入理解Flask - 2016.pdf](https://itbooks.ctfile.com/fs/18113597-319371589)

- [The New And Improved Flask - 2018.pdf](https://itbooks.ctfile.com/fs/18113597-319371576)

- [Python高效开发实战Django、Tornado、Flask、Twisted - 2016.pdf](https://itbooks.ctfile.com/fs/18113597-319371573)

- [head first flask - 2016.pdf](https://itbooks.ctfile.com/fs/18113597-319371558)

- [Flask Web Development 2nd - 2018.pdf](https://itbooks.ctfile.com/fs/18113597-319371546)

- [Flask Building Python Web Services - 2017.pdf](https://itbooks.ctfile.com/fs/18113597-319371544)

- [Flask Blueprints - 2015.pdf](https://itbooks.ctfile.com/fs/18113597-319371537)

- [Building Web Applications with Flask - 2015.pdf](https://itbooks.ctfile.com/fs/18113597-319371534)

## 框架

- [Connexion](https://github.com/zalando/connexion) - Swagger/OpenAPI，支持自动端点验证和OAuth2  ★★
- [Eve](https://github.com/pyeve/eve) - 机遇Flask、MongoDB的REST API框架 ★★★★★
- [Flask-RESTful](https://github.com/flask-restful/flask-restful) - 用于创建REST API的简单框架 ★★★★★
- [Flask-RestPlus](https://github.com/noirbizarre/flask-restplus) - 语法糖、帮助器和自动生成的Swagger文档。 ★★
- [Zappa](https://github.com/Miserlou/Zappa) - 在AWS Lambda和API网关上构建和部署无服务器的Flask应用程序  ★★★★★

## 管理界面

- [Flask-Admin](https://github.com/flask-admin/flask-admin) - Flask的简单和可扩展的管理界面框架  ★★★★


## 验证

- [Flask-Security](https://github.com/mattupstate/flask-security) - 为Flask应用程序提供快速和简单的安全保护。
- [Flask-Login](https://github.com/maxcountryman/flask-login) - Flask用户会话管理  ★★
- [Flask-User](https://github.com/lingthio/Flask-User) - Flask的可定制的用户账户管理
- [Flask-HTTPAuth](https://github.com/miguelgrinberg/Flask-HTTPAuth) - 简单的扩展，为Flask路由提供Basic和Digest HTTP认证。

## 授权

- [Authlib](https://github.com/lepture/authlib) - Authlib是一个雄心勃勃的认证库，用于OAuth 1、OAuth 2、OpenID客户端、服务器等。 ★★
- [Authomatic](https://github.com/authomatic/authomatic) - Authomatic为使用OAuth 1.0a（Twitter、Tumblr等）和OAuth 2.0（Facebook、Foursquare、GitHub、Google、LinkedIn、PayPal等）的一些提供者提供开箱即用的支持。
- [Flask-Dance](https://github.com/singingwolfboy/flask-dance) - Flask的OAuth消费者扩展，预先设置了对Facebook、GitHub、Google等的支持。

## 数据库

- [Flask-MongoEngine](https://github.com/MongoEngine/flask-mongoengine) - MongoEngine的Flask扩展，支持WTF模型形式。
- [Flask-SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy) - 为Flask添加SQLAlchemy支持。 ★★★

## 数据库迁移
 
- [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate) - 使用Alembic为Flask应用程序进行SQLAlchemy数据库迁移。 ★

## 缓存

- [Flask-Caching](https://github.com/sh4nks/flask-caching) - 为Flask添加简单的缓存支持

## 数据验证

- [Flask-WTF](https://github.com/lepture/flask-wtf) - Flask和WTForms的简单集成，包括CSRF、文件上传和Recaptcha的集成。


## 速率限制

- [Flask-Limiter](https://github.com/alisaifee/flask-limiter) - Flask-Limiter为flask路线提供速率限制功能。

## 任务队列
 
- [huey](https://github.com/coleifer/huey) - 一个用于python的小任务队列  ★★★
- [celery](https://github.com/celery/celery/) - 分布式任务队列  ★★★★★

## 异常跟踪

- [sentry-sdk](https://github.com/getsentry/sentry-python) - [Sentry](https://sentry.io/welcome/)的Python客户端。


## APM

- [elastic-apm](https://github.com/elastic/apm-agent-python) - Python的Elastic APM代理。

## 其他SDK

- [Flask-GoogleMaps](https://github.com/rochacbruno/Flask-GoogleMaps) - 在Flask模板中建立和嵌入谷歌地图

## 前端

- [Flask-CORS](https://github.com/corydolphin/flask-cors) - 用于处理跨源资源共享（CORS）的Flask扩展，使跨源AJAX成为可能。

## 开发(调试/测试/文档)

- [flask_profiler](https://github.com/muatik/flask-profiler) - Flask的端点分析器/profiler
- [Flask-DebugToolbar](https://github.com/mgood/flask-debugtoolbar) - 将django的调试工具条移植到flask上。
- [Flask-Testing](https://github.com/jarus/flask-testing) - 用于Flask的Unittest扩展
- [pytest-flask](https://github.com/pytest-dev/pytest-flask) - 一组用于测试Flask应用程序的pytest fixtures 
- [Flask-MonitoringDashboard](https://github.com/flask-dashboard/Flask-MonitoringDashboard) - 自动监测Flask/Python Web服务的性能变化。
- [nplusone](https://github.com/jmcarp/nplusone#flask-sqlalchemy) - 使用Flask和SQLAlchemy自动检测n+1个查询。
- [connexion](https://github.com/zalando/connexion) - Swagger/OpenAPI，支持自动端点验证和OAuth2。

## 工具

- [flask-marshmallow](https://github.com/marshmallow-code/flask-marshmallow) Flask + marshmallow for beautiful APIs
- [Mixer](https://github.com/klen/mixer) - Mixer是用于生成Django或SQLAlchemy模型实例的应用程序。
- [Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO) - 为Flask应用程序整合Socket.IO  ★★★★
- [Flask-Moment](https://github.com/miguelgrinberg/Flask-Moment) - 在Flask模板中使用moment.js对日期和时间进行格式化。
- [Flask-graphql](https://github.com/graphql-python/flask-graphql) - 将GraphQL支持添加到你的Flask应用程序中。

# 资源
## 教程

- [如何建立一个永不停机且几乎不花钱的新闻应用](http://blog.apps.npr.org/2013/02/14/app-template-redux.html) (由NPR提供)
- [用Flask在Python中构建网站](http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/)
- [Flask大型教程](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [用Python和Flask实现一个RESTful Web API](http://blog.luisrei.com/articles/flaskrest.html)
- [发现Flask--用Flask进行全栈网络开发](https://github.com/realpython/discover-flask)
- [Flaskr--Flask、测试驱动开发和jQuery介绍](https://github.com/mjhea0/flaskr-tdd)

## 课程

- [全栈基础](https://www.udacity.com/course/full-stack-foundations--ud088)
- [设计RESTful APIs](https://www.udacity.com/course/designing-restful-apis--ud388)

## 书籍

- [探索Flask](https://exploreflask.com/en/latest/)
- [Flask Web开发](http://shop.oreilly.com/product/0636920031116.do)
- [Real Python](https://realpython.com)
- [Flask Framework Cookbook](https://www.packtpub.com/web-development/flask-framework-cookbook)

## 幻灯片

- [用Flask创建漂亮的REST API](http://pycoder.net/bospy/presentation.html)
- [高级Flask模式](https://speakerdeck.com/mitsuhiko/advanced-flask-patterns)
- [Flasky Goodness](https://speakerdeck.com/kennethreitz/flasky-goodness)
- [领域驱动设计（...用Flask）](https://speakerdeck.com/mikedebo/domain-driven-design-dot-dot-dot-with-flask)
- [In Flask we Trust](https://speakerdeck.com/playpauseandstop/in-flask-we-trust)

## 视频

- [PyVideo](https://pyvideo.org/search.html?q=flask)
- [实用Flask网络开发教程](https://www.youtube.com/playlist?list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB)

## 项目

- [zmusic-ng](https://git.zx2c4.com/zmusic-ng/) - ZX2C4 Music提供了一个使用元数据播放和下载音乐文件的网络接口。
- [redispapa](https://github.com/no13bus/redispapa) - 使用flask、angular、socket.io的另一个redis监视器
- [Frozen-Flask](https://github.com/Frozen-Flask/Frozen-Flask) - 将Flask应用程序冻结为一组静态文件
- [Skylines](https://github.com/skylines-project/skylines) - 实时跟踪、飞行数据库和竞赛框架
- [airflow](https://github.com/apache/incubator-airflow) - Airflow是一个以编程方式编写、安排和监控数据管道的系统。 ★★★★★
- [timesketch](https://github.com/google/timesketch) - 协作取证的时间线分析  ★★
- [security_monkey](https://github.com/Netflix/security_monkey) - 监视政策变化并对AWS账户中的不安全配置发出警报。 ★★★
- [securedrop](https://github.com/freedomofpress/securedrop)--一个开源的举报人提交系统，媒体机构可以用它来安全地接受匿名来源的文件并与之沟通。 ★★
- [sync_engine](https://github.com/nylas/sync-engine) - 具有现代API的IMAP/SMTP同步系统  ★★
- [indico](https://github.com/indico/indico) - 通用的活动管理网络解决方案。它包括一个完整的会议组织工作流程，以及会议管理和房间预订的工具。它还提供与视频会议解决方案的整合。
- [flaskbb](https://github.com/flaskbb/flaskbb) - 使用Flask的经典Python论坛软件。

## Boilerplate

- [fbone](https://github.com/imwilsonxu/fbone) 
- [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask)  ★★★
- [Flask-Foundation](https://github.com/JackStouffer/Flask-Foundation)
- [gae-init](https://gae-init.appspot.com) - 在谷歌应用引擎上运行的Flask锅炉模板
- [Flask-AppBuilder](https://github.com/dpgaspar/Flask-AppBuilder) - 简单快速的应用程序生成器框架，建立在Flask之上。包括详细的安全性、自动生成表单、谷歌图表等内容。 ★★★
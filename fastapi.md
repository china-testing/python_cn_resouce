
[FastAPI](https://fastapi.tiangolo.com/)是一个现代的、高性能的、强大的Python Web框架，非常适合于构建RESTful API。


[Awesome-fastapi](https://github.com/mjhea0/awesome-fastapi) 收集了大量 fastapi 相关的优秀应用、项目等资源，方便了 fastapi 用户参考查阅。

[Django 优秀资源大全](https://github.com/china-testing/python_cn_resouce/blob/main/fastapi.md ) 则是翻译而来。也欢迎你帮助推荐和提供建议

赞善或进入python技术群：钉钉或微信 pythontesting、 支付宝xurongzhong#gmail.com, 请将#替换为@。

python测试开发钉钉群：21745728，目前800多人，另有几千人的python测试开发微信群，可联系 钉钉或微信号 pythontesting 加群（备注：python）！

[python八字排盘](https://github.com/china-testing/bazi)  目前市面上功能最强大的八字排盘，科学的尽头是道教，玄学。

本指南主要收集GitHub星级1k+的库。

## 内容

   * [内容](#内容)
   * [精品图书](#精品图书)
   * [第三方扩展](#第三方扩展)
      * [Admin](#admin)
      * [Auth](#auth)
      * [Databases](#databases)
         * [ORMs](#orms)
         * [查询生成器](#查询生成器)
         * [ODMs](#odms)
         * [其他工具](#其他工具)
      * [Developer-tools](#developer-tools)
      * [Email](#email)
      * [Utils](#utils)
   * [资源](#资源)
      * [官方资源](#官方资源)
      * [外部资源](#外部资源)
      * [播客](#播客)
      * [文章](#文章)
      * [教程](#教程)
      * [讲座](#讲座)
      * [视频](#视频)
      * [课程](#课程)
      * [最佳实践](#最佳实践)
   * [托管](#托管)
      * [PaaS](#paas)
      * [IaaS](#iaas)
   * [项目](#项目)
      * [模板](#模板)
      * [Docker图像](#docker图像)
      * [开源项目](#开源项目)



## 精品图书

访问密码: 2274, 无需注册，点击普通下载即可。如遇失效可加钉钉或微信 pythontesting获取。

- [FastAPI Modern Python Web Development .epub](https://url97.ctfile.com/f/18113597-809569500-c26672?p=2274)
- [Web API Development with Python A Beginners Guide using Flask and FastAPI .epub](https://url97.ctfile.com/f/18113597-809569549-740e43?p=2274)
- [Full Stack FastAPI, React, and MongoDB Build Python web applications with the FARM stack .epub](https://url97.ctfile.com/f/18113597-809569535-538d24?p=2274)
- [Building Data Science Applications with FastAPI Develop, manage, and deploy efficient machine learning applications with... .epub](https://url97.ctfile.com/f/18113597-809569436-b00186?p=2274)
- [Building Python Web APIs with FastAPI .epub](https://url97.ctfile.com/f/18113597-809569462-f4771c?p=2274)


## 第三方扩展

### Admin

- [FastAPI Admin](https://github.com/fastapi-admin/fastapi-admin) - 管理功能面板，为在数据上进行CRUD操作提供了用户接口。目前只适用于Tortoise ORM。
- [SQLAlchemy Admin](https://github.com/aminalaee/sqladmin) - FastAPI/Starlette的管理面板，适用于SQLAlchemy模型。

### Auth

- [FastAPI Users](https://github.com/fastapi-users/fastapi-users) - 账户管理、认证、授权。 ★★

### Databases

#### ORMs

- [GINO](https://github.com/python-gino/gino) - 一个建立在SQLAlchemy核心之上的轻量级异步ORM，用于Python asyncio。 ★★
  - [FastAPI 示例](https://github.com/leosussan/fastapi-gino-arq-uvicorn)
- [ORM](https://github.com/encode/orm) - 异步的ORM。	★
- [ormar](https://github.com/collerek/ormar) - Ormar是一个异步ORM，它使用Pydantic验证，可以直接用于FastAPI请求和响应，因此你只需要维护一套模型。包括Alembic迁移。
  - [FastAPI实例](https://collerek.github.io/ormar/fastapi/) - 使用FastAPI与ormar。
- [Piccolo](https://github.com/piccolo-orm/piccolo) - 一个异步ORM和查询生成器，支持Postgres和SQLite，带有电池（迁移、安全等）。
  - [FastAPI实例](https://github.com/piccolo-orm/piccolo_examples) - 在Piccolo中使用FastAPI。
- [Prisma Client Python](https://github.com/RobertCraigie/prisma-client-py) - 一个由Pydantic提供的自动生成的、完全类型安全的ORM，并为你的模式专门定制 - 支持SQLite、PostgreSQL、MySQL、MongoDB、MariaDB等。
  - [FastAPI实例](https://github.com/RobertCraigie/prisma-client-py/tree/main/examples/fastapi-basic)
- [Tortoise ORM](https://tortoise.github.io) - 易于使用的asyncio ORM（对象关系映射器），灵感来自Django。 ★★★
  - [FastAPI实例](https://tortoise.github.io/examples/fastapi.html) - 一个Tortoise-ORM FastAPI集成的实例。
  - [教程：用FastAPI设置Tortoise ORM](https://web.archive.org/web/20200523174158/https://robwagner.dev/tortoise-fastapi-setup/)
  - [Aerich](https://github.com/tortoise/aerich) - Tortoise ORM的迁移工具。
- [SQLModel](https://sqlmodel.tiangolo.com/) - SQLModel（由Pydantic和SQLAlchemy支持）是一个从Python代码中与SQL数据库交互的库，使用Python对象。 ★★★★★

#### 查询生成器

- [Databases](https://github.com/encode/databases) - 在[SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/core/)表达式语言之上工作的异步SQL查询构建器。 ★★

#### ODMs

- [Beanie](https://github.com/roman-right/beanie) - MongoDB的异步Python ODM，基于[Motor](https://motor.readthedocs.io/en/stable/)和[Pydantic](https://pydantic-docs.helpmanual.io/)，支持开箱即用的数据和模式迁移。
- [MongoEngine](http://mongoengine.org/) - 文档-对象映射器（ORM，但用于文档数据库），用于Python与MongoDB一起工作。
- [Motor](https://motor.readthedocs.io/) - MongoDB的异步Python驱动。 ★★
- [ODMantic](https://art049.github.io/odmantic/) - 与[Pydantic](https://pydantic-docs.helpmanual.io/)集成的AsyncIO MongoDB ODM。

#### 其他工具

- [Pydantic-SQLAlchemy](https://github.com/tiangolo/pydantic-sqlalchemy) - 将SQLAlchemy模型转换成[Pydantic](https://pydantic-docs.helpmanual.io/)模型。

### Developer-tools

- [FastAPI代码生成器](https://github.com/koxudaxi/fastapi-code-generator) - 从OpenAPI文件创建FastAPI应用程序，实现模式驱动的开发。
- [Manage FastAPI](https://github.com/ycd/manage-fastapi) - 用于生成和管理FastAPI项目的CLI工具。

### Email

- [FastAPI Mail](https://github.com/sabuhish/fastapi-mail) - 用于发送电子邮件和附件（单独和批量）的轻量级邮件系统。

### Utils

- [FastAPI Cache](https://github.com/long2ice/fastapi-cache) - 用于缓存FastAPI响应和函数结果的工具，支持Redis、Memcached、DynamoDB和内存后端。
- [FastAPI CRUDRouter](https://github.com/awtkns/fastapi-crudrouter) - FastAPI路由器，为你的模型自动创建和记录CRUD路由。
- [FastAPI Pagination](https://github.com/uriyyo/fastapi-pagination) - FastAPI的分页。
- [FastAPI Utilities](https://github.com/dmontagu/fastapi-utils) - 可重复使用的实用程序：基于类的视图、响应推断路由器、定期任务、定时中间件、SQLAlchemy会话、OpenAPI规范简化。
- [SlowApi](https://github.com/laurents/slowapi) - 速度限制器（基于[Flask-Limiter](https://flask-limiter.readthedocs.io)）。
- [Strawberry GraphQL](https://github.com/strawberry-graphql/strawberry) - 基于数据类的Python GraphQL库。

## 资源

### 官方资源

- [文档](https://fastapi.tiangolo.com/) - 全面的文档。 ★★★★★
- [Tutorial](https://fastapi.tiangolo.com/tutorial/) - 官方教程，一步一步地展示如何使用FastAPI的大部分功能。 ★★★★★
- [源代码](https://github.com/tiangolo/fastapi) ★★★★★  
- [Discord](https://discord.com/invite/VQjSZaeJmf) - 与其他FastAPI用户聊天。

### 外部资源

- [TestDriven.io FastAPI](https://testdriven.io/blog/topics/fastapi/) - 多篇针对FastAPI的文章，侧重于开发和测试生产就绪的RESTful API，提供机器学习模型，以及其他。

### 播客

- [Build The Next Generation Of Python Web Applications With FastAPI](https://www.pythonpodcast.com/fastapi-web-application-framework-episode-259/) - 在[Podcast Init](https://www.pythonpodcast.com/)的这一集中，FastAPI的创建者[Sebastián Ramirez](https://tiangolo.com/)分享了他创建FastAPI的动机以及它是如何在引擎盖下工作的。
- [PythonBytes上的FastAPI](https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855) - 项目的良好概述。

### 文章

- [FastAPI对我来说永远毁了Flask](https://towardsdatascience.com/fastapi-has-ruined-flask-forever-for-me-73916127da)
- [Why we switched from Flask to FastAPI for production machine learning](https://medium.com/@calebkaiser/why-we-switched-from-flask to-fastapi-for-production-machine-learning-765aab9b3679) - 深入探讨为什么要从Flask转移到FastAPI。

### 教程

- [Async SQLAlchemy with FastAPI](https://stribny.name/blog/fastapi-asyncalchemy/) - 学习如何异步地使用SQLAlchemy。
- [Build and Secure an API in Python with FastAPI](https://blog.yezz.me/blog/Build-and-Secure-an-API-in-Python-with-FastAPI) - 保护和维护基于FastAPI和SQLAlchemy的API。
- [将Docker化的FastAPI应用部署到Google云平台](https://towardsdatascience.com/deploy-a-dockerized-fastapi-app-to-google-cloud-platform-24f72266c7ef) - 使用Cloud Run和SQL实例将Docker化的Python应用部署到Google云平台的简短指南。
- [使用Keras、FastAPI、Redis和Docker部署机器学习模型](https://medium.com/analytics-vidhya/deploy-machine-learning-models-with-keras-fastapi-redis-and-docker-4940df614ece)
- [Deploying Iris Classifications with FastAPI and Docker](https://towardsdatascience.com/deploying-iris-classifications-with-fastapi-and-docker-7c9b83fdec3a) - Docker化FastAPI应用程序。
- [使用FastAPI和Pytest开发和测试异步API](https://testdriven.io/blog/fastapi-crud/) - 使用测试驱动开发，用FastAPI、Postgres、Pytest和Docker开发和测试一个异步API。
- [FastAPI for Flask Users](https://amitness.com/2020/06/fastapi-vs-flask/) - 通过与Flask的并列代码比较来学习FastAPI。
- [FastAPI微服务模式](https://florian-kromer.medium.com/fastapi-microservice-patterns-3052c1241019) - 博客文章系列，包括微服务模式的示范性实现。
  - [Local Development Environment](https://florian-kromer.medium.com/fastapi-microservice-patterns-local-development-environment-12182e786f1c) - Skaffold、docker、kubectl和minikube的简述。
  - 容器编排平台中的服务发现](https://florian-kromer.medium.com/fastapi-microservice-patterns-service-discovery-in-container-orchestration-platforms-290c00d1ad8) - 在Kubernetes中启用FastAPI服务通信的解释。
  - [Asynchronous Communication](https://florian-kromer.medium.com/fastapi-microservice-patterns-asynchronous-communication-45a3b68f8bb8) - 通过消息传递实现松散耦合的服务。
  - [应用监控](https://medium.com/swlh/fastapi-microservice-patterns-application-monitoring-49fcb7341d9a) - 使用Prometheus和Grafana进行应用指标监控。
  - [无服务器部署](https://medium.com/swlh/fastapi-microservice-serverless-deployment-41a6d21e5cb3) - 关于FastAPI和Kubernetes原生FaaS平台之间的兼容性现状。
- [GraphQL in Python with FastAPI and Ariadne入门](https://blog.yezz.me/blog/Getting-started-with-GraphQL-in-Python-with-FastAPI-and-Ariadne) - 使用FastAPI、GraphQL和Ariadne生成一个FullStack游乐场。
- [How to monitor your FastAPI service](https://guitton.co/posts/fastapi-monitoring) - 解释如何使用OpenTelemetry和Datadog/Jaeger实现应用性能监控（APM）。
- [Implementing FastAPI Services - Abstraction and Separation of Concerns](https://camillovisini.com/article/abstracting-fastapi-services/) - FastAPI应用程序和服务结构，使代码库更容易维护。
- 介绍FARM栈 - FastAPI、React和MongoDB](https://www.mongodb.com/developer/languages/python/farm-stack-fastapi-react-mongodb/) - 开始使用完整的FastAPI网络应用程序栈。
- [使用FastAPI、SQLAlchemy和PostgreSQL的多租户](https://mergeboard.com/blog/6-multitenancy-fastapi-sqlalchemy-postgresql/) - 了解如何使FastAPI应用程序做好多租户准备。
- [Porting Flask to FastAPI for ML Model Serving](https://www.pluralsight.com/tech-blog/porting-flask-to-fastapi-for-ml-model-serving/) - Flask与FastAPI的比较。
- [使用FastAPI和WebSockets的实时数据流](https://stribny.name/blog/2020/07/real-time-data-streaming-using-fastapi-and-websockets/) - 了解如何将数据从FastAPI直接流到实时图表中。
- [在生产中运行FastAPI应用程序](https://stribny.name/blog/fastapi-production/) - 在生产部署中使用Gunicorn和systemd。
- [用FastAPI在Python中服务机器学习模型](https://medium.com/@8B_EC/tutorial-serving-machine-learning-models-with-fastapi-in-python-c1a27319c459) - 使用FastAPI在Python中以RESTful API方式快速、轻松地部署和服务机器学习模型。
- [使用FastAPI流媒体视频](https://stribny.name/blog/fastapi-video/) - 了解如何为视频流提供服务。
- [Using Hypothesis and Schemathesis to Test FastAPI](https://testdriven.io/blog/fastapi-hypothesis/) - 将基于属性的测试应用于FastAPI。

### 讲座

- [PyConBY 2020: Serve ML models easily with FastAPI](https://www.youtube.com/watch?v=z9K5pwb0rt8) - 从Sebastian Ramirez的演讲中，你将了解到如何用FastAPI为你的ML模型轻松构建一个生产就绪的网络（JSON）API，包括默认的最佳实践。
- [PyCon UK 2019: FastAPI from the ground up](https://www.youtube.com/watch?v=3DLwPcrE5mA) - 本讲座展示了如何使用FastAPI从头开始为数据库构建一个简单的REST API。

### 视频

- 用FastAPI构建股票筛选器](https://www.youtube.com/watch?v=5GorMC2lPpk) - 用FastAPI构建一个基于Web的股票筛选器，你将被介绍到FastAPI的许多功能，包括Pydantic模型、依赖注入、后台任务和SQLAlchemy集成。
- [Building Web APIs Using FastAPI](https://www.youtube.com/watch?v=Pe66M8mn-wA) - 使用FastAPI来构建网络应用程序接口（RESTful API）。
- [FastAPI - A Web Framework for Python](https://www.youtube.com/watch?v=PUhio8CprhI&list=PL5gdMNl42qynpY-o43Jk3evfxEKSts3HS) - 看看如何用FastAPI做数字验证。
- [FastAPI vs. Django vs. Flask](https://www.youtube.com/watch?v=9YBAOYQOzWs) - 2020年哪个框架最适合Python？哪个使用async/await最好？哪一个是最快的？
- [Serving Machine Learning Models As API with FastAPI](https://www.youtube.com/watch?v=mkDxuRvKUL8) - 使用FastAPI构建机器学习API。

### 课程

- [Test-Driven Development with FastAPI and Docker](https://testdriven.io/courses/tdd-fastapi/) - 学习如何使用Python、FastAPI和Docker构建、测试和部署一个文本总结的微服务。
- [Modern APIs with FastAPI and Python](https://training.talkpython.fm/courses/getting-started-with-fastapi) - 本课程旨在让您利用FastAPI快速创建在云中运行的新API。
- [使用FastAPI的完整网络应用程序课程](https://training.talkpython.fm/courses/full-html-web-applications-with-fastapi) - 您将学习如何使用FastAPI构建完整的网络应用程序，相当于使用Flask或Django所能做到的。
- [The Definitive Guide to Celery and FastAPI](https://testdriven.io/courses/fastapi-celery/) - 了解如何将Celery添加到FastAPI应用程序中以提供异步任务处理。

### 最佳实践

- [FastAPI最佳实践](https://github.com/zhanymkanov/fastapi-best-practices) - 在GitHub repo中收集的最佳实践。

## 托管

### PaaS

(Platforms-as-a-Service)

- [Heroku](https://www.heroku.com/) ([Step-by-step tutorial](https://tutlinks.com/create-and-deploy-fastapi-app-to-heroku/), [Heroku上的ML模型教程](https://testdriven.io/blog/fastapi-machine-learning/)
- [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
- [谷歌应用引擎](https://cloud.google.com/appengine/)
- [Microsoft Azure App Service](https://azure.microsoft.com/en-us/products/app-service/)
- [Deta](https://www.deta.sh/) ([例子](https://dev.to/athulcajay/fastapi-deta-ni5))

### IaaS

(基础设施即服务)

- [AWS EC2](https://aws.amazon.com/ec2/)
- [Google Compute Engine](https://cloud.google.com/compute/)
- [数字海洋](https://www.digitalocean.com/)
- [Linode](https://www.linode.com/)

###无服务器

框架。

- [Chalice](https://github.com/aws/chalice)
- [Mangum](https://mangum.io/) - 用AWS Lambda和API网关运行ASGI应用程序的适配器。
- [Vercel](https://vercel.com/) - (以前是Zeit) ([example](https://github.com/paul121/fastapi-zeit-now))。

计算。

- [AWS Lambda](https://aws.amazon.com/lambda/) ([教程](https://iwpnd.pw/articles/2020-01/deploy-fastapi-to-aws-lambda), [代码](https://github.com/iwpnd/fastapi-aws-lambda-example))
- [谷歌云函数](https://cloud.google.com/functions/)
- [Azure Functions](https://azure.microsoft.com/en-us/products/functions/)
- [Google Cloud Run](https://cloud.google.com/run) ([例子](https://github.com/anthonycorletti/cloudrun-fastapi))

## 项目

### 模板

- 全栈FastAPI和PostgreSQL - 基础项目生成器](https://github.com/tiangolo/full-stack-fastapi-postgresql) - 全栈、现代网络应用程序生成器，包括FastAPI、PostgreSQL、Docker、Celery、Vue前端、自动HTTPS等（由FastAPI的创造者[Sebastián Ramírez](https://github.com/tiangolo) 开发）。
- [FastAPI和Tortoise ORM](https://github.com/prostomarkeloff/fastapi-tortoise) - 强大而简单的网络API模板，包括FastAPI（作为网络框架）和Tortoise-ORM（用于通过数据库工作而不需要头痛）。
- [FastAPI Model Server Skeleton](https://github.com/eightBEC/fastapi-ml-skeleton) - 为机器学习模型提供服务的骨架应用，可供生产使用。
- [cookiecutter-spacy-fastapi](https://github.com/microsoft/cookiecutter-spacy-fastapi) - 使用FastAPI快速部署specy模型。
- [cookiecutter-fastapi](https://github.com/arthurhenrique/cookiecutter-fastapi) - 用于FastAPI项目的Cookiecutter模板，使用。机器学习、Poetry、Azure Pipelines和pytest。
- [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) - 从OpenAPI生成现代FastAPI Python客户端（通过FastAPI）。
- [Pywork](https://github.com/vutran1710/YeomanPywork) - [Yeoman](https://yeoman.io/)生成器，用于构建FastAPI应用程序的支架。
- [fastapi-gino-arq-uvicorn](https://github.com/leosussan/fastapi-gino-arq-uvicorn) - 高性能异步REST API的模板，使用Python。FastAPI + GINO + Arq + Uvicorn (w/ Redis and PostgreSQL)。
- [FastAPI and React Template](https://github.com/Buuntu/fastapi-react) - 使用FastAPI、TypeScript、Docker、PostgreSQL和React的全堆栈cookiecutter模板。
- [FastAPI Nano](https://github.com/rednafi/fastapi-nano) - 带有工厂模式架构的简单FastAPI模板。

- [FastAPI模板](https://github.com/s3rius/FastAPI-template) - 灵活、轻便的FastAPI项目生成器。它包括对SQLAlchemy、多个数据库、CI/CD、Docker和Kubernetes的支持。
- [FastAPI on Google Cloud Run](https://github.com/anthonycorletti/cloudrun-fastapi) - 使用FastAPI、SQLModel和Google Cloud Run构建API的模板。
- [FastAPI with Firestore](https://github.com/anthonycorletti/firestore-fastapi) - 使用FastAPI和Google Cloud Firestore构建API的模板。
- [fastapi-alembic-sqlmodel-async](https://github.com/jonra1993/fastapi-alembic-sqlmodel-async) - 这是一个项目模板，使用FastAPI、Alembic和async SQLModel作为ORM。
- [fastapi-starter-project](https://github.com/mirzadelic/fastapi-starter-project) - 一个使用FastAPI、SQLModel、Alembic、Pytest、Docker、GitHub Actions CI的项目模板。

### Docker图像

- [inboard](https://github.com/br3ndonland/inboard) - Docker图像，为你的FastAPI应用程序提供动力，并帮助你更快地出货。
- [uvicorn-gunicorn-fastapi-docker](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) - 由Gunicorn管理的Uvicorn的Docker镜像，用于Python 3.7和3.6中的高性能FastAPI网络应用，具有性能自动调整功能。
- [uvicorn-gunicorn-poetry](https://github.com/max-pfeiffer/uvicorn-gunicorn-poetry) - 这个Docker镜像提供了一个使用Gunicorn与Uvicorn工作者运行FastAPI的平台。它提供了用于管理依赖关系和在容器中设置虚拟环境的诗歌。
- [uvicorn-poetry](https://github.com/max-pfeiffer/uvicorn-poetry) - 这个Docker镜像提供了一个在Kubernetes容器编排系统上使用Uvicorn运行FastAPI的平台。它提供了用于管理依赖关系和在容器中设置虚拟环境的诗歌。

### 开源项目

- [Astrobase](https://github.com/anthonycorletti/astrobase) - 简单、快速、安全地在任何地方进行部署。
- [Awesome FastAPI Projects](https://github.com/Kludex/awesome-fastapi-projects) - 使用FastAPI的项目的组织列表。
- [Bitcart](https://github.com/bitcartcc/bitcart) - 为商家、用户和开发人员提供易于设置和使用的平台。
- [Bali](https://github.com/bali-framework/bali) - 基于FastAPI和gRPC简化云原生微服务开发。
- [Bunnybook](https://github.com/pietrobassi/bunnybook) - 一个用FastAPI、React+RxJs、Neo4j、PostgreSQL和Redis构建的小型社交网络。
- [Coronavirus-tg-api](https://github.com/egbakou/coronavirus-tg-api) - 用于跟踪全球冠状病毒（COVID-19、SARS-CoV-2）爆发的API。
- [Dispatch](https://github.com/Netflix/dispatch) - 管理安全事件。
- FastAPI CRUD实例。
  - [Async风味](https://github.com/testdrivenio/fastapi-crud-async)
  - [同步风味](https://github.com/testdrivenio/fastapi-crud-sync)
- [DogeAPI](https://github.com/yezz123/DogeAPI) - 具有高性能的API，用于创建一个简单的博客和使用OAuth2PasswordBearer的CRUD。
- [FastAPI Websocket Broadcast](https://github.com/kthwaite/fastapi-websocket-broadcast) - Websocket "广播 "演示。
- [FastAPI with Celery, RabbitMQ, and Redis](https://github.com/GregaVrbancic/fastapi-celery) - 利用FastAPI和Celery的最小例子，RabbitMQ用于任务队列，Redis用于Celery后端，Flower用于监控Celery任务。
- [JeffQL](https://github.com/yezz123/JeffQL/) - 使用GraphQL和JWT的简单认证和登录API。
- [JSON-RPC服务器](https://github.com/smagafurov/fastapi-jsonrpc) - 基于FastAPI的JSON-RPC服务器。
- [Mailer](https://github.com/rclement/mailer) - 用于静态网站的非常简单的邮件微服务。
- [Nemo](https://github.com/harshitsinghai77/nemo-backend) - 使用Nemo提高生产力。
- [OPAL（Open Policy Administration Layer）](https://github.com/authorizon/opal) - 在Open-Policy之上的实时授权更新；用FastAPI、Typer和FastAPI WebSocket pub/sub构建。
- [RealWorld Example App - mongo](https://github.com/markqiu/fastapi-mongodb-realworld-example-app)
- [RealWorld Example App - postgres](https://github.com/nsidnev/fastapi-realworld-example-app)
- [redis-streams-fastapi-chat](https://github.com/leonh/redis-streams-fastapi-chat) - 一个使用Websockets、Asyncio和FastAPI/Starlette的简单Redis Streams支持的聊天应用程序。
- [Sprites as a service](https://github.com/ljvmiranda921/sprites-as-a-service) - 使用Cellular Automata生成你个人的8位头像。
- [Slackers](https://github.com/uhavin/slackers) - Slack webhooks API。
- [TermPair](https://github.com/cs01/termpair) - 通过端到端加密从你的浏览器查看和控制终端。
- [Universities](https://github.com/ycd/universities) - 用于获取全球9600所大学信息的API服务。
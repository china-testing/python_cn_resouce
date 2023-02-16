# 真棒的Python测试[！[真棒](https://awesome.re/badge.svg)](https://awesome.re)
用于测试和生成测试数据的真棒Python资源的集合。

[awesome-python-testing](https://github.com/cleder/awesome-python-testing) 收集了python测试相关库。


赞赏或进入python技术群：钉钉或微信 pythontesting、 支付宝xurongzhong#gmail.com, 请将#替换为@。

python测试开发钉钉群：21745728，目前800多人，另有几千人的python测试开发微信群，可联系 钉钉或微信号 pythontesting 加群（备注：python）！

[python八字排盘](https://github.com/china-testing/bazi)  目前市面上功能最强大的八字排盘，科学的尽头是道教，玄学。


## 内容

   * [内容](#内容)
   * [断言](#断言)
   * [行为驱动的开发](#行为驱动的开发)
   * [代码覆盖率](#代码覆盖率)
   * [契约设计](#契约设计)
   * [数据Fake](#数据fake)
   * [负载测试](#负载测试)
   * [内存管理](#内存管理)
   * [Mock和存根](#mock和存根)
   * [突变测试](#突变测试)
   * [对象工厂](#对象工厂)
   * [渗透测试](#渗透测试)
   * [基于属性的测试](#基于属性的测试)
   * [REST API测试](#rest-api测试)
   * [速度](#速度)
   * [静态检查](#静态检查)
   * [测试运行程序](#测试运行程序)
   * [测试框架](#测试框架)
   * [工具](#工具)
   * [UI测试](#ui测试)
   * [资源](#资源)
      * [试题](#试题)
      * [软件测试](#软件测试)


## 断言

- [expects](https://github.com/jaimegildesagredo/expects) - 用于Python的表达式和可扩展的TDD/BDD断言库。
- [expycted](https://github.com/bdsoha/expycted) - 另一个Python期望模式实现。简单、直观、平易近人，能够插入到任何依赖断言的测试框架中。
- [dirty-equals](https://github.com/samuelcolvin/dirty-equals) - 使用了`__eq__`方法，使Python代码（一般是单元测试）更具有声明性，因此更容易阅读和编写。
- [Precisely](https://github.com/mwilliamson/python-precisely) - 允许你编写精确的断言。
- [PyHamcrest](https://github.com/hamcrest/PyHamcrest) - 编写匹配器对象的框架，允许你声明式地定义 "匹配 "规则。
- [sure](https://github.com/gabrielfalcao/sure) - 一个具有人性化的失败信息的成语断言工具包，灵感来自于RSpec Expectations和should.js。

## 行为驱动的开发

- [behave](https://github.com/behave/behave) - 是行为驱动的开发，Python风格。 ★★★
- [lettuce](https://github.com/gabrielfalcao/lettuce) - 用于Python的行为驱动开发工具，灵感来自Cucumber for Ruby。  ★
- [mamba](http://nestorsalceda.github.io/mamba) - Python的权威测试工具。诞生于BDD的旗帜下。 

## 代码覆盖率

- [Coverage.py](https://github.com/nedbat/coveragepy) - 是一个用于测量Python程序代码覆盖率的工具。 ★★★
- [diff_cover](https://github.com/Bachmann1234/diff_cover) - 自动找到需要测试覆盖的diff行。

## 契约设计

- [deal](https://github.com/life4/deal) - 为Python提供静态检查器和测试生成的合同设计。
- [icontract](https://github.com/Parquery/icontract) - 在Python3中通过合同进行设计，具有丰富的违规信息和继承性。

## 数据Fake

- [faker](https://github.com/joke2k/faker) - 可以生成假数据的Python包。 ★★★★★
- [fake2db](https://github.com/emirozer/fake2db) - 假的数据库生成器。 ★★
- [mimesis](https://github.com/lk-geimfari/mimesis) - 帮助你生成假数据的Python库。 ★★★

## 负载测试

- [Locust](https://github.com/locustio/locust) - 用Python编写的可扩展的用户负载测试工具。 ★★★★★  开源性能测试之王。

## 内存管理

- [filprofiler](https://github.com/pythonspeed/filprofiler) - 用于数据处理和科学计算应用的Python内存分析器。
- [Guppy 3](https://github.com/zhuyifei1999/guppy3) - Python编程环境和堆分析工具集。
- [Pympler](https://github.com/pympler/pympler) - 用于测量、监控和分析运行中的Python应用程序中Python对象的内存行为。★★ 
- [tracemalloc](https://docs.python.org/3/library/tracemalloc.html) - 用于跟踪Python分配的内存块。 ★★★

## Mock和存根

- [Aioresponses](https://github.com/pnuckowski/aioresponses) - 是Python aiohttp包中模拟/假网络请求的辅助工具。
- [Cornell](https://github.com/hiredscorelabs/cornell) - 记录和重放模拟服务器。
- [doublex](https://pypi.org/project/doublex) - 用于Python的强大的测试替身框架。
- [freezegun](https://github.com/spulec/freezegun) - 通过模拟日期时间模块来穿越时间。 ★★
- [httmock](https://github.com/patrys/httmock) - 为Python 2.6以上和3.2以上的requests提供的mock库。
- [httpretty](https://github.com/gabrielfalcao/HTTPretty) - Python的HTTP请求模拟工具。 ★★
- [mock](https://docs.python.org/3/library/unittest.mock.html) - (Python标准库)  ★★
- [mocket](https://github.com/mindflayer/python-mocket) - 支持gevent/asyncio/SSL的socket mock框架。
- [Mockintosh](https://github.com/up9inc/mockintosh) - 旨在提供通常的HTTP模拟服务功能，资源占用小，使其对微服务应用友好。
- [moto](https://github.com/spulec/moto) - 允许你轻松地模拟基于AWS基础设施的测试。  ★★★★★
- [Pretend](https://github.com/alex/pretend) - 使Python的stub更容易。
- [response](https://github.com/getsentry/responses) - 一个用于模拟Requests的Python库。
- [time-machine](https://github.com/adamchainz/time-machine) - 在你的测试中穿越时间。
- [VCR.py](https://github.com/kevin1024/vcrpy) - 在你的测试中记录和回放HTTP交互。 ★★

## 突变测试

- [Cosmic Ray](https://github.com/sixty-north/cosmic-ray) - 对你的源代码进行小的修改，对每个修改运行你的测试套件。。
- [Mutmut](https://github.com/boxed/mutmut) - 用于Python的突变测试系统，非常注重使用的方便性。

## 对象工厂

- [factory_boy](https://github.com/FactoryBoy/factory_boy) - 测试夹具替代工具。 ★★
- [mixer](https://github.com/klen/mixer) - 另一个夹具的替代品。支持Django, Flask, SQLAlchemy, Peewee等。
- [Model Bakery](https://github.com/model-bakers/model_bakery) - 为你提供一种聪明的方式来创建Django中的测试夹具。
- [pydantic-factories](https://github.com/Goldziher/pydantic-factories) - 为基于pydantic的模型提供模拟数据生成。

## 渗透测试

- [fsociety](https://github.com/fsociety-team/fsociety) - 一个模块化的渗透测试框架。
- [python-pentest-tools](https://github.com/dloss/python-pentest-tools) - 渗透测试人员的Python工具。

## 基于属性的测试

- [Atheris](https://github.com/google/atheris) - 是一个覆盖引导的Python模糊测试引擎。它支持Python代码的模糊测试，但也支持为CPython编写的本地扩展。
- [Hypothesis](https://github.com/HypothesisWorks/hypothesis) - 是一个高级Quickcheck风格的基于属性的测试库。 ★★★★★

## REST API测试

- [Dredd](https://github.com/apiaryio/dredd) - 语言无关的命令行工具，用于验证API描述文档与API的后端实现。 ★★★
- [HttpRunner](https://github.com/httprunner/httprunner) - 简单、优雅、但功能强大的HTTP(S)测试框架。  ★★★
- [Schemathesis](https://github.com/kiwicom/schemathesis) - 对使用Open API/Swagger规范构建的Web应用进行基于属性的自动测试的工具。
- [SnapshotTest](https://github.com/syrusakbary/snapshottest) - 不写实际测试案例的情况下测试你的API的方法。
- [playback](https://github.com/Optibus/playback) - 一个基于Python装饰器的框架，可以让你 "记录 "和 "回放 "操作（如API请求，工人从队列中消耗作业）。
- [RESTler](https://github.com/microsoft/restler-fuzzer) - 是第一个有状态的REST API模糊工具，用于通过其REST API自动测试云服务，并在这些服务中找到安全和可靠性的缺陷。  ★★
- [Tavern](https://github.com/taverntesting/tavern) - 是一个用于自动测试API的pytest插件、命令行工具和Python库，其语法简单、简洁、灵活，基于YAML。

## 速度

- [Pytest-incremental](https://github.com/pytest-dev/pytest-incremental) - 分析你的项目结构和测试运行之间的文件修改，以修改测试的执行顺序和取消选择测试。
- [pytest-testmon](https://github.com/tarpas/pytest-testmon) - 选择受更改文件影响的测试。当与pytest-watch一起使用时，可以连续测试运行器。
- [Awesome pytest speedup](https://github.com/zupo/awesome-pytest-speedup) - 加快你的pytest套件的最佳做法的清单。

## 静态检查

- [awesome-flake8-extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions) - flake8扩展列表。
- [awesome-python-typing](https://github.com/typeddjango/awesome-python-typing) - 收集了很棒的Python类型、存根、插件和使用它们的工具。
- [Bandit](https://github.com/PyCQA/bandit) - 寻找Python代码中常见安全问题的工具。 ★★★★
- [flake8](https://gitlab.com/pycqa/flake8) -  它将pep8、pyflakes、mccabe和第三方插件粘合在一起，用于检查Python代码的风格和质量。 ★★★★
- [pyanalyze](https://github.com/quora/pyanalyze) - 是一个以编程方式检测Python代码中常见错误的工具，例如对未定义变量的引用和某些类别的类型不匹配。
- [pyflakes](https://github.com/PyCQA/pyflakes) - 用于检查Python源文件的错误。 ★
- [Pylint](https://github.com/PyCQA/pylint) - Python静态代码分析工具，它寻找编程错误，帮助执行编码标准，嗅探代码气味，并提供简单的重构建议。 ★★★★
- [Refurb](https://github.com/dosisod/refurb) - 整修和现代化Python代码库的工具。
- [ruff](https://github.com/charliermarsh/ruff) - 用Rust编写的极快的Python linter。 ★★★★★
- [slotscheck](https://github.com/ariebovenberg/slotscheck) - 在你的"__slots__"定义中查找错误。

## 测试运行程序

- [green](https://github.com/CleanCut/green) - 干净、多彩的测试运行器。
- [Nox](https://github.com/theacodes/nox) - 命令行工具，可以在多个Python环境中自动测试，类似于tox。与 tox 不同，Nox 使用标准的 Python 文件进行配置。
- [tox](https://tox.readthedocs.io/en/latest) - 在多个Python版本中自动构建和测试分布。  ★★

## 测试框架

- [async-asgi-testclient](https://github.com/vinissimus/async-asgi-testclient) - 用于测试ASGI网络应用的框架无关的库。
- [awesome-pytest](https://github.com/augustogoulart/awesome-pytest) - 一个精选的pytest资源列表。
- [awesome-robotframework](https://github.com/fkromer/awesome-robotframework) - 一个精心策划的机器人框架资源和库列表。
- [doctest](https://docs.python.org/3/library/doctest.html) - (Python标准库) doctest模块搜索看起来像交互式Python会话的文本片段，然后执行这些会话以验证它们是否完全按照显示的方式工作。 ★★★★
- [nose2](https://github.com/nose-devs/nose2) - `nose`的后续版本，基于`unittest2`。
- [pytest](https://docs.pytest.org/en/latest) - 成熟的全功能Python测试工具。  ★★★★★
- [Robot Framework](https://github.com/robotframework/robotframework) - 一个通用的测试自动化框架。 ★★★★
- [testbook](https://github.com/nteract/testbook) - 单元测试框架扩展，用于测试Jupyter Notebooks中的代码。
- [unittest](https://docs.python.org/3/library/unittest.html) - （Python标准库）单元测试框架。★★★★
- [Ward](https://github.com/darrenburns/ward) - 现代的Python测试框架，关注于生产力和可读性。
- [xdoctest](https://github.com/Erotemic/xdoctest) - 重写Python的内置doctest模块（与pytest插件集成），用AST代替REGEX。

## 工具

- [ApprovalTests](https://github.com/approvals/ApprovalTests.Python) - 通过将测试结果与黄金母版进行比较来工作。
- [Auger](https://github.com/laffra/auger) - 自动生成单元测试的项目。
- [CrossHair](https://github.com/pschanely/CrossHair) - 用于Python的分析工具，模糊了测试和类型系统之间的界限。
- [ghostwriter](https://hypothesis.readthedocs.io/en/latest/ghostwriter.html) - 用Hypothesis编写测试，把你从决定和写出具体的测试输入的繁琐中解放出来。
- [importlab](https://github.com/google/importlab) - 一个可以自动推断Python文件的依赖关系的库。Importlab 的主要用例是与静态分析工具一起工作，这些工具一次处理一个文件，确保在文件之前对文件的依赖关系进行分析。  ★★★★★
- [Klara](https://github.com/usagitoneko97/klara) - 自动生成测试用例的静态分析工具，基于SMT(z3)求解器，具有强大的 ast 级推理系统。
- [Pifpaf](https://github.com/jd/pifpaf) - 是一套固定装置和一个命令行工具，允许启动和停止守护程序，以便快速使用。当需要这些守护程序来运行集成测试时，这通常很有用。
- [Ponicode](https://www.ponicode.com) - VS Code的AI驱动的单元测试接口。编写、生成、修改和可视化JavaScript、TypeScript和Python的各种单元测试。
- [Pynguin](https://github.com/se2p/pynguin) - 是一个允许开发者自动生成单元测试的工具。  ★

## UI测试

- [Flybirds](https://github.com/ctripcorp/flybirds) - 基于BDD模式的前端UI自动化测试框架，提供一系列开箱即用的工具和完整文档。
- [Golem](https://github.com/golemhq/golem) - 浏览器自动化的完整工具。测试可以用Python的代码编写，也可以用Web IDE的无代码编写，或者两者都可以。
- [helium](https://github.com/mherrmann/selenium-python-helium) - Web自动化,轻量级的Selenium-python。 ★★
- [Lost Pixel](https://github.com/lost-pixel/lost-pixel) - 开源的视觉回归测试工具。在你的Storybook和Ladle故事以及你的应用程序页面上运行可视化回归测试。
- [selene](https://github.com/yashaka/selene) - Python中面向用户的Web UI浏览器测试（Selenide移植）。
- [Selenium](https://pypi.org/project/selenium) - [Selenium](http://www.seleniumhq.org/) WebDriver 的 Python 绑定。 ★★★★★
- [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) - 用于自动化浏览器测试的多合一Python框架。测试用 "pytest "运行，并使用WebDriver的API进行网页交互。 ★★★
- [sixpack](https://github.com/seatgeek/sixpack) - 语言无关的A/B测试框架。 ★★
- [splinter](https://github.com/cobrateam/splinter) - 用于测试wEB应用的开源工具。  ★★

 * appium - 移动端UI自动化测试。 [链接](https://github.com/appium/python-client) --推荐

 * uiautomator- 安卓UI自动化测试。 [链接](https://github.com/xiaocong/uiautomator) 

 * ATX - 智能手机自动化工具。支持iOS，Android，WebApp和游戏。 网易出品 [链接](https://github.com/xiaocong/uiautomator) --推荐

 * uiautomator2- Android Uiautomator2 Python Wrapper。 [链接](https://github.com/openatx/uiautomator2) --推荐

 * facebook-wda Facebook WebDriverAgent Python Client Library (not official) 可用于IOS应用测试。 [链接](https://github.com/openatx/facebook-wda2) --推荐
 
 * Winium.Desktop - 开源测试自动化工具，用于基于WinForms和WPF平台自动测试Windows应用程序，基于Selenium远程WebDriver实现。 [链接](https://github.com/2gis/Winium.Desktop/)

 * pyautogui- 跨平台的UI自动化工具，控制鼠标和键盘。 [链接](https://github.com/asweigart/pyautogui)
 
 * autopy - 简单的跨平台GUI自动化工具包，适用于Python。 [链接](https://github.com/msanders/autopy) 

 * pywinauto - Windows UI自动化。 [链接](https://github.com/pywinauto/pywinauto/) 

 * SikuliX - sikuli的稳定长期更新版本。[链接](https://github.com/RaiMan/SikuliX1) 
 
 * Python-UIAutomation-for-Windows - uiautomation封装了微软UIAutomation API，支持自动化Win32，MFC，WPF，Modern UI(Metro UI), Qt, IE, Firefox等。[链接](https://github.com/yinkaisheng/Python-UIAutomation-for-Windows)  国产
 
 * pyautoacad - AutoCAD自动化。 [链接](https://github.com/reclosedev/pyautocad) 

 * sikuli - 位图自动化。 [链接](http://www.sikuli.org) 

 * monkeyrunner- 安卓自动化。 [链接](https://developer.android.com/studio/test/monkeyrunner/index.html) 

 * ldtp - Linux UI自动化。 [链接](https://pypi.python.org/pypi/ldtp) 

 * dogtail- Linux UI自动化。 [链接](https://pypi.python.org/pypi/dogtail) 

 * pyautoit- autoit python api。 [链接](https://github.com/jacexh/pyautoit) 

## 资源
###文章

- [async test patterns for Pytest](https://tonybaloney.github.io/posts/async-test-patterns-for-pytest-and-unittest.html) - 在Pytest中学习一些方便的async例子和测试模式。
- [Stargirl Flowers: "My Python testing style guide"](https://blog.thea.codes/my-python-testing-style-guide) - 试图围绕测试Python项目的一些做法进行编目。它并不意味着被当作教条来对待。
- [Test & Code: Python Testing](https://testandcode.com/) - Test & Code是由Brian Okken主持的每周播客。该节目涵盖广泛的主题，包括软件工程、开发、测试、Python编程和许多相关主题。
- [用Hypothesis测试你的Python代码](https://www.inspiredpython.com/course/testing-with-hypothesis/testing-your-python-code-with-hypothesis) - 看一下Hypothesis如何帮助你发现代码中的错误。
- [在Jupyter笔记本中对Python代码进行单元测试](https://www.wrighters.io/unit-testing-python-code-in-jupyter-notebooks) - 这篇文章介绍了在Jupyter笔记本中对Python代码进行单元测试的几种方案。
- [软件开发和测试的30个最佳实践](https://opensource.com/article/17/5/30-best-practices-software-development-and-testing) - 这些软件工程规则和测试最佳实践可能有助于节省你的时间和头痛。

###书籍下载


[书籍:ASTQB-BCS移动测试基础指南 Mobile Testing An ASTQB-BCS Foundation Guide - 2018.pdf](https://www.jianshu.com/p/a252732f8f1c)


### 试题
 [软件测试综合面试题(高级测试)-试题.pdf](https://itbooks.pipipan.com/fs/18113597-316083198)

  [软件测试综合面试题(python测试开发).pdf](https://itbooks.pipipan.com/fs/18113597-316083196)

  [自动化_性能_web测试 - 试卷.pdf](https://itbooks.pipipan.com/fs/18113597-316083195)

  [自动化试卷.pdf](https://itbooks.pipipan.com/fs/18113597-316083192)

### 软件测试

- [Doing Agile Right-2020](https://545c.com/f/18113597-492993454-0bc945)
- [Agile Conversation-2020](ttps://545c.com/f/18113597-492993435-7c7cf0)


- [自动化测试点滴 Software Testing Automation Tips-2017.pdf](https://545c.com/f/18113597-493119549-84944e)
- [软件测试简介 A Friendly Introduction to Software Testing-2016 A4.3-38__.pdf](https://545c.com/f/18113597-493119547-c4b508)
- [使用python进行selenium测试 Python Testing with Selenium-2021 A5-2——.pdf](https://545c.com/f/18113597-493951160-f3f156)
- [python HTTP自动化测试： Python Requests Essentials -2015__.pdf](https://545c.com/f/18113597-493934407-38aec6)
- [python自动化菜单 第2版 Python Automation Cookbook -2020 2nd Ae4.3-34__.pdf](https://545c.com/f/18113597-493950719-7b6f40)
- [python测试：pytest Python Testing with pytest-2017 4.5 Ae4.5-92__.pdf](https://545c.com/f/18113597-493950522-3b3724)

  [Pro Apache JMeter Web Application Performance Testing - 2017.pdf](https://www.jianshu.com/p/56125b1c91c0) - [下载](https://itbooks.pipipan.com/fs/18113597-384173739)

  [Performance Testing with JMeter 3 - Third Edition - 2017.pdf](https://www.jianshu.com/p/4c4ce0b8ba45) - [下载](https://itbooks.pipipan.com/fs/18113597-384173741)

  [优质代码：软件测试的原则、实践与模式 \- 2015.pdf](https://itbooks.pipipan.com/fs/18113597-316074102)


  [应用程序性能测试的艺术 \- 2012.pdf](https://itbooks.pipipan.com/fs/18113597-316074076)

  [移动App测试实战：顶级互联网企业软件测试和质量提升最佳实践 - 2015.pdf](https://itbooks.pipipan.com/fs/18113597-316074007)

  [腾讯Android自动化测试实战 - 2016.pdf](https://itbooks.pipipan.com/fs/18113597-316073745)

  [软件性能测试过程详解与案例剖析（第二版）\- 2012.pdf](https://itbooks.pipipan.com/fs/18113597-316073529)

  [软件测试价值提升之路 \- 2016.pdf](https://itbooks.pipipan.com/fs/18113597-316072834)

  [Praxiswissen Softwaretest - Test Analyst und Technical Test Analyst Aus - 2015.pdf](https://itbooks.pipipan.com/fs/18113597-316072683)

  [Google软件测试之道 - 2013.pdf](https://itbooks.pipipan.com/fs/18113597-316072590)

  [Advanced Software Testing - Vol. 2, 2nd Edition Guide to the ISTQB Advanced Certification as an Advanced Test Manager - 2014.pdf](https://itbooks.pipipan.com/fs/18113597-316072495)

  [std1008-1987 IEEE 1008 单元测试国际标准.pdf](https://itbooks.pipipan.com/fs/18113597-314969695)

  [IEEE Std 829-2008 测试计划模板.pdf](https://itbooks.pipipan.com/fs/18113597-314969548)

  [BS ISO IEC 25010-2011 Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models.pdf](https://itbooks.pipipan.com/fs/18113597-314939974)

  [IEEE-Std-829-2008.pdf](https://itbooks.pipipan.com/fs/18113597-314939694)

  [ISO-IEC 25010 系统和软件质量模型.pdf](https://itbooks.pipipan.com/fs/18113597-314939352)

  [Hands-On Continuous Integration and Delivery - 2018.pdf](https://itbooks.pipipan.com/fs/18113597-314170123)

  [Remote Usability Testing - 2018.pdf](https://itbooks.pipipan.com/fs/18113597-314167512)

  [Database Benchmarking and Stress Testing - 2018.pdf](https://itbooks.pipipan.com/fs/18113597-314044807)

  [Python Testing with pytest - 2017.pdf](https://itbooks.pipipan.com/fs/18113597-309198424)

  [\[高级软件测试卷2：高级软件测试经理\].Rex.Black.扫描版.pdf](https://itbooks.pipipan.com/fs/18113597-302728068)

  [Rocky.Nook.Improving.the.Test.Process.Dec.2013.pdf](https://itbooks.pipipan.com/fs/18113597-302727922)

  [Software Testing Foundations 4th - 2014.pdf](https://itbooks.pipipan.com/fs/18113597-302727870)

  [Rocky.Nook Advanced Software Testing .Vol.3.2nd.Edition - 2015.pdf](https://itbooks.pipipan.com/fs/18113597-302727763)

[深入理解Android自动化测试 (移动开发) - 2016.pdf](https://itbooks.pipipan.com/fs/18113597-316090216)

[精通Metasploit渗透测试 (图灵程序设计丛书) - 2016.pdf](https://itbooks.pipipan.com/fs/18113597-316090186)

[测试架构师修炼之道：从测试工程师到测试架构师 \- 2016.pdf](https://itbooks.pipipan.com/fs/18113597-316090161)

[Web渗透测试：使用Kali Linux (图灵程序设计丛书) - 2014.pdf](https://itbooks.pipipan.com/fs/18113597-316090132)

[Kali Linux高级渗透测试（原书第2版） (网络空间安全技术丛书) - 2018.pdf](https://itbooks.pipipan.com/fs/18113597-316090098)

[Kali Linux 无线渗透测试入门指南 - 2016.pdf](https://itbooks.pipipan.com/fs/18113597-316090032)

[Android移动性能实战 - 2017.pdf](https://itbooks.pipipan.com/fs/18113597-316090015)

[有效的单元测试 (华章程序员书库) \- 2014.pdf](https://itbooks.pipipan.com/fs/18113597-316089972)

[Kali Linux渗透测试的艺术 - 2015.pdf](https://itbooks.pipipan.com/fs/18113597-316089945)

[程序之美系列套装（6册）团队之美、项目管理之美、架构之美、数据之美、测试之美、安全之美 - 2015.pdf](https://itbooks.pipipan.com/fs/18113597-316096746)

[Sample Exam Questions- ISTQB Foundation Level-Agile Tester Extension Exam - 2016.pdf](https://itbooks.pipipan.com/fs/18113597-316096725)

[Mobile Test Auto with Appium - 2017.pdf](https://itbooks.pipipan.com/fs/18113597-322413180)

[Appium Recipes - 2016.pdf](https://itbooks.pipipan.com/fs/18113597-322413178)

* [Learning Android Application Testing-2015.pdf](http://file.allitebooks.com/20170415/Learning%20Android%20Application%20Testing.pdf)
* [Effective Python Penetration Testing-2016.pdf](http://file.allitebooks.com/20170710/Effective%20Python%20Penetration%20Testing.pdf)
* [Kali Linux 2 Windows Penetration Testing-2016.pdf](http://file.allitebooks.com/20170608/Kali%20Linux%202%20Windows%20Penetration%20Testing.pdf)
* [Selenium Testing Tools Cookbook, 2nd Edition-2015.pdf](http://file.allitebooks.com/20180107/Selenium%20Testing%20Tools%20Cookbook,%202nd%20Edition.pdf)
* [Performance Testing with Jmeter, Second Edition-2015.pdf](http://file.allitebooks.com/20170418/Performance%20Testing%20with%20Jmeter,%20Second%20Edition.pdf)
* [Advanced Penetration Testing for Highly-Secured Environments, Second Edition-2016.pdf](http://file.allitebooks.com/20170310/Advanced%20Penetration%20Testing%20for%20Highly-Secured%20Environments,%20Second%20Edition.pdf)
* [iOS Code Testing-2017.pdf](http://file.allitebooks.com/20170701/iOS%20Code%20Testing.pdf)
* [Software Testing Automation Tips-2017.pdf](http://file.allitebooks.com/20171029/Software%20Testing%20Automation%20Tips.pdf)
* [iOS Penetration Testing-2016.pdf](http://file.allitebooks.com/20170130/iOS%20Penetration%20Testing.pdf)
* [Penetration Testing Basics-2016.pdf](http://file.allitebooks.com/20160820/Penetration%20Testing%20Basics.pdf)
* [Performance Testing With JMeter 2-2013.9-2013.pdf](http://file.allitebooks.com/20170204/Performance%20Testing%20With%20JMeter%202.9.pdf)
* [Penetration Testing with the Bash shell-2014.pdf](http://file.allitebooks.com/20161127/Penetration%20Testing%20with%20the%20Bash%20shell.pdf)
* [Testing and Securing Android Studio Applications-2014.pdf](http://file.allitebooks.com/20161108/Testing%20and%20Securing%20Android%20Studio%20Applications.pdf)
* [Kali Linux 2 Assuring Security by Penetration Testing, 3rd Edition-2016.pdf](http://file.allitebooks.com/20161005/Kali%20Linux%202%20Assuring%20Security%20by%20Penetration%20Testing,%203rd%20Edition.pdf)
* [Instant Hands-on Testing with PHPUnit How-to-2013.pdf](http://file.allitebooks.com/20160810/Instant%20Hands-on%20Testing%20with%20PHPUnit%20How-to.pdf)
* [Application Testing with Capybara-2013.pdf](http://file.allitebooks.com/20161204/Application%20Testing%20with%20Capybara.pdf)
* [Learning Yii Testing-2015.pdf](http://file.allitebooks.com/20160706/Learning%20Yii%20Testing.pdf)
* [Web App Testing Using Knockout-2014.JS-2014.pdf](http://file.allitebooks.com/20160418/Web%20App%20Testing%20Using%20Knockout.JS.pdf)
* [Intermediate Security Testing with Kali Linux 2-2015.pdf](http://file.allitebooks.com/20160509/Intermediate%20Security%20Testing%20with%20Kali%20Linux%202.pdf)
* [Learning Penetration Testing with Python-2015.pdf](http://file.allitebooks.com/20160613/Learning%20Penetration%20Testing%20with%20Python.pdf)
* [Kali Linux Wireless Penetration Testing Essentials-2015.pdf](http://file.allitebooks.com/20160615/Kali%20Linux%20Wireless%20Penetration%20Testing%20Essentials.pdf)
* [Testing with Junit-2015.pdf](http://file.allitebooks.com/20160421/Testing%20with%20Junit.pdf)
* [Software Testing using Visual Studio 2012-2013.pdf](http://file.allitebooks.com/20160701/Software%20Testing%20using%20Visual%20Studio%202012.pdf)
* [Kali Linux Web Penetration Testing Cookbook-2016.pdf](http://file.allitebooks.com/20160611/Kali%20Linux%20Web%20Penetration%20Testing%20Cookbook.pdf)
* [Mastering Kali Linux Wireless Pentesting-2016.pdf](http://file.allitebooks.com/20160419/Mastering%20Kali%20Linux%20Wireless%20Pentesting.pdf)
* [Jasmine JavaScript Testing-2015.pdf](http://file.allitebooks.com/20160324/Jasmine%20JavaScript%20Testing.pdf)
* [Metasploit Penetration Testing Cookbook, Second Edition-2013.pdf](http://file.allitebooks.com/20160101/Metasploit%20Penetration%20Testing%20Cookbook,%20Second%20Edition.pdf)
* [Mastering Kali Linux for Advanced Penetration Testing-2014.pdf](http://file.allitebooks.com/20160405/Mastering%20Kali%20Linux%20for%20Advanced%20Penetration%20Testing.pdf)
* [Java Testing with Spock-2016.pdf](http://file.allitebooks.com/20160329/Java%20Testing%20with%20Spock.pdf)
* [Selenium Testing Tools Cookbook-2015.pdf](http://file.allitebooks.com/20160103/Selenium%20Testing%20Tools%20Cookbook.pdf)
* [Learning Selenium Testing Tools with Python-2014.pdf](http://file.allitebooks.com/20160412/Learning%20Selenium%20Testing%20Tools%20with%20Python.pdf)
* [Robotium Automated Testing for Android-2013.pdf](http://file.allitebooks.com/20160304/Robotium%20Automated%20Testing%20for%20Android.pdf)
* [The Hacker Playbook 2- Practical Guide To Penetration Testing-2015.pdf](http://file.allitebooks.com/20150922/The%20Hacker%20Playbook%202-%20Practical%20Guide%20To%20Penetration%20Testing.pdf)
* [Hacking Basic Security, Penetration Testing and How to Hack-2015.pdf](http://file.allitebooks.com/20151105/Hacking%20Basic%20Security,%20Penetration%20Testing%20and%20How%20to%20Hack.pdf)
* [Web Penetration Testing with Kali Linux, Second Edition-2015.pdf](http://file.allitebooks.com/20151212/Web%20Penetration%20Testing%20with%20Kali%20Linux,%20Second%20Edition.pdf)
* [Testing and Validation of Computer Simulation Models-2015.pdf](http://file.allitebooks.com/20151010/Testing%20and%20Validation%20of%20Computer%20Simulation%20Models.pdf)
* [Mastering Wireless Penetration Testing for Highly-Secured Environments-2015.pdf](http://file.allitebooks.com/20150909/Mastering%20Wireless%20Penetration%20Testing%20for%20Highly-Secured%20Environments.pdf)
* [Instant Penetration Testing-2013.pdf](http://file.allitebooks.com/20151222/Instant%20Penetration%20Testing.pdf)
* [Software Testing- Concepts and Operations-2015.pdf](http://file.allitebooks.com/20151017/Software%20Testing-%20Concepts%20and%20Operations.pdf)
* [Mastering Unit Testing Using Mockito and JUnit-2014.pdf](http://file.allitebooks.com/20150912/Mastering%20Unit%20Testing%20Using%20Mockito%20and%20JUnit.pdf)
* [Computer Vision for X-Ray Testing-2015.pdf](http://file.allitebooks.com/20151202/Computer%20Vision%20for%20X-Ray%20Testing.pdf)
* [Penetration Testing with Raspberry Pi-2015.pdf](http://file.allitebooks.com/20150909/Penetration%20Testing%20with%20Raspberry%20Pi.pdf)
* [Leveraging the Wisdom of the Crowd in Software Testing-2014.pdf](http://file.allitebooks.com/20150709/Leveraging%20the%20Wisdom%20of%20the%20Crowd%20in%20Software%20Testing.pdf)
* [Python Penetration Testing Essentials-2015.pdf](http://file.allitebooks.com/20150909/Python%20Penetration%20Testing%20Essentials.pdf)
* [Kali Linux Wireless Penetration Testing Beginner-s Guide-2015.pdf](http://file.allitebooks.com/20150904/Kali%20Linux%20Wireless%20Penetration%20Testing%20Beginner-s%20Guide.pdf)
* [Learning Python Testing-2014.pdf](http://file.allitebooks.com/20150731/Learning%20Python%20Testing.pdf)
* [Backbone-2013.js Testing-2013.pdf](http://file.allitebooks.com/20150626/Backbone.js%20Testing.pdf)
* [Testing in Scala-2013.pdf](http://file.allitebooks.com/20150627/Testing%20in%20Scala.pdf)
* [Python Web Penetration Testing Cookbook-2015.pdf](http://file.allitebooks.com/20150805/Python%20Web%20Penetration%20Testing%20Cookbook.pdf)
* [The Hacker Playbook Practical Guide To Penetration Testing-2014.pdf](http://file.allitebooks.com/20150521/The%20Hacker%20Playbook%20Practical%20Guide%20To%20Penetration%20Testing.pdf)
* [Building Virtual Pentesting Labs for Advanced Penetration Testing-2014.pdf](http://file.allitebooks.com/20150521/Building%20Virtual%20Pentesting%20Labs%20for%20Advanced%20Penetration%20Testing.pdf)
* [Penetration Testing with the Bash shell-2014.pdf](http://file.allitebooks.com/20150521/Penetration%20Testing%20with%20the%20Bash%20shell.pdf)
* [Penetration Testing-2014.pdf](http://file.allitebooks.com/20150521/Penetration%20Testing.pdf)
* [Penetration Testing with BackBox-2014.pdf](http://file.allitebooks.com/20150521/Penetration%20Testing%20with%20BackBox.pdf)
* [Web Penetration Testing with Kali Linux-2013.pdf](http://file.allitebooks.com/20150521/Web%20Penetration%20Testing%20with%20Kali%20Linux.pdf)
* [Learning Pentesting for Android Devices-2014.pdf](http://file.allitebooks.com/20150521/Learning%20Pentesting%20for%20Android%20Devices.pdf)
* [AngularJS Testing Cookbook-2015.pdf](http://file.allitebooks.com/20150626/AngularJS%20Testing%20Cookbook.pdf)
* [Learning Nessus for Penetration Testing-2014.pdf](http://file.allitebooks.com/20150521/Learning%20Nessus%20for%20Penetration%20Testing.pdf)
* [Instant Mock Testing with PowerMock-2013.pdf](http://file.allitebooks.com/20150509/Instant%20Mock%20Testing%20with%20PowerMock.pdf)
* [JavaScript Unit Testing-2013.pdf](http://file.allitebooks.com/20150513/JavaScript%20Unit%20Testing.pdf)
* [Testing Python-2014.pdf](http://file.allitebooks.com/20150514/Testing%20Python.pdf)
* [JavaScript Testing with Jasmine-2013.pdf](http://file.allitebooks.com/20150513/JavaScript%20Testing%20with%20Jasmine.pdf)
* [python自动化测试圣经 -2018 Python Automation Cookbook - 2018 英文版](https://itbooks.pipipan.com/fs/18113597-313910541)
* 数据库基准和压力测试 2018版本 [Database Benchmarking and Stress Testing - 2018.pdf](https://itbooks.pipipan.com/fs/18113597-314044807)
* [Remote Usability Testing - 2018.pdf](https://itbooks.ctfile.com/fs/18113597-314167512) 
* [Selenium自动化测试 基于 Python 语言 - 2018.pdf](https://itbooks.pipipan.com/fs/18113597-315206043)


###相关

- [Awesome Python](https://github.com/vinta/awesome-python/blob/master/README.md#testing) - 一个精心策划的超强Python框架、库、软件和资源的列表。
- [Python测试自动化](https://github.com/atinfo/awesome-test-automation/blob/master/python-test-automation.md) - 一个全面的Python测试自动化框架、工具、库和软件的策划列表，以帮助软件工程师在Python上轻松启动测试自动化。

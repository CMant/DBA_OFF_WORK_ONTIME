之前我发在了码云那边，直接在那边编辑的。结果下载下来图片没跟带着。要看的话也可以移步码云
其实也没啥看的，就是代码说明 和 UI
https://gitee.com/cotxtan/DBA_OFF_WORK_ONTIME


# DBA下班就跑远程执行sql工具
是的，我暂时起不到什么比较高大上的名字。
这个项目库的名字叫做  DBA_OFF_WORK_ONTIME 原谅我的工地英语水平，就是 DBA下班就走 的英文叫法。

#### 介绍

在我工作的过程中发现，开发和我下班的时间不一致，他们指不定几点走，而我到了5点半就想跑那种。
关键是他们还总是要让我执行一些sql。
有的还挺紧急，最初我是用teamviewer解决这个问题的。但是有一天我坐火车回老家的时候要过几十个山洞，手机信号断断续续。teamviewer连接痛苦的要命。
当时我就想了一个办法。能不能取消远程桌面的过程，仅仅通过字符传输来解决这个问题？
数据库的地址是不对公网开放的，搞什么vpn啊之类的，说白了，一过山洞肯定又不行了。我想把这个过程简化，再简化。
那么有没有什么能打通公司内网到外网，保持信号稳定而又不需要使用VPN的方法呢


邮箱！

是的，开发人员如果想执行什么sql语句，就通过这个软件提交，然后这个软件会给我发送一封邮件，包含了，｛谁，哪个库，执行什么sql｝的详细内容。以及一个四位的随机验证码。

然后我把这四位随机验证码发回给开发，他自己填写验证码就可以执行成功了。

NICE！

![输入图片说明](https://images.gitee.com/uploads/images/2019/0906/135711_98b95bff_1832805.png "屏幕截图.png")
填写上述如内容之后会跳转下面的页面

![输入图片说明](https://images.gitee.com/uploads/images/2019/0906/134510_d24fd7f9_1832805.jpeg "QQ截图20190906134444.jpg")
同时你的手机邮箱会收到下面的内容

![输入图片说明](https://images.gitee.com/uploads/images/2019/0906/134605_90e68971_1832805.jpeg "QQ截图20190906134554.jpg")


#### 软件架构

我不是软件开发人员，代码水平很一般。只把代码大概含义解释一下吧
![输入图片说明](https://images.gitee.com/uploads/images/2019/0906/141204_3547b212_1832805.jpeg "1567748944(1).jpg")
conf 文件是数据库的列表清单，大家可以根据手头的数据库逐一填写。里面我保留了一个示例



![输入图片说明](https://images.gitee.com/uploads/images/2019/0906/135237_b880bbe5_1832805.jpeg "QQ截图20190906135227.jpg")

这部分之前是写死的，新增一个数据库我能累屁了。抱歉我对前端技术一窍不通。都是现学现卖。迫不得已了才学。
后来改成了从配置文件直接读取，就可以在页面打开的时候动态的加载数据库的清单了。

![输入图片说明](https://images.gitee.com/uploads/images/2019/0906/135432_2ad0c27c_1832805.png "屏幕截图.png")

这是启动命令，大家根据自己的IP地址进行修改即可

![输入图片说明](https://images.gitee.com/uploads/images/2019/0906/135543_202a79e0_1832805.png "屏幕截图.png")

在sqldmlcheckexec.py 文件中，这个函数负责在数据库执行sql的任务。 大家根据自己所管理的数据库自行修改即可。如果想支持多种不同的数据库，代码改动还是挺大的，需要在上面的conf 数据库清单文件中再加一个 类型标记 用以判断才可以。当然部分函数的参数也需要更改了。


#### 安装教程
本软件使用到包如下，大家从pip 上安装即可
psycopg2    flask    wtforms（我好像没有用到这里面的功能也可以不装吧）    configparser

其余的如果启动报错缺少什么包，大家直接pip就好。

有一些垃圾代码我没有删除，也不影响，之前的注释我也保留着。。

听说大作家的手稿就是这样，涂涂改改的痕迹非常有价值。 


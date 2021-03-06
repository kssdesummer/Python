2019-11-01
### Python语言的有点和缺点
#### 图灵完备
定义：一切可计算的问题都能计算，这样的虚拟机或编程语言叫图灵完备
拿php与Python做比较了解图灵完备，php的所有功能都能拿Python实现，两者可以进行互换，我们就称这是图灵完备的语言
#### 定位：
优雅、明确、简单，所以Python程序看上去简单易懂，新手容易入门，深入下去可以编写非常复杂的程序。
#### 必知概念
1. C语言编译完就是机器码。机器码可以直接在处理器上执行
2. CPU可以直接读取机器码
3. Python使用C写的
4. Python解释器会把代码内容读到内存，通过Python解释器翻译成字节码
5. CPU不能直接读取字节码，需要把字节码转换成机器码
总的来说：Python相对多了一个字节码转换成机器码的过程，所以会相对慢，实际测试、无法感知
#### 应用领域
1. 云计算: 云计算最火的语言， 典型应用OpenStack
2. WEB开发: 众多优秀的WEB框架，众多大型网站均为Python开发，Youtube, Dropbox, 豆瓣。。。， 典型WEB框架有Django
3. 科学运算、人工智能: 典型库NumPy, SciPy, Matplotlib, Enthought librarys,pandas
4. 系统运维: 运维人员必备语言
5. 金融：量化交易，金融分析，在金融工程领域，Python不但在用，且用的最多，而且重要性逐年提高。原因：作为动态语言的Python，语言结构清晰简单，库丰富，成熟稳定，科学计算和统计分析都很牛逼，生产效率远远高于c,c++,java,尤其擅长策略回测
6. 图形GUI: PyQT, WxPython,TkInter
#### 公司应用
1. 谷歌：Google App Engine 、code.google.com 、Google earth 、谷歌爬虫、Google广告等项目都在大量使用Python开发
2. CIA: 美国中情局网站就是用Python开发的
3. NASA: 美国航天局(NASA)大量使用Python进行数据分析和运算
4. YouTube:世界上最大的视频网站YouTube就是用Python开发的
5. Dropbox:美国最大的在线云存储网站，全部用Python实现，每天网站处理10亿个文件的上传和下载
6. Instagram:美国最大的图片分享社交网站，每天超过3千万张照片被分享，全部用python开发
7. Facebook:大量的基础库均通过Python实现的
8. Redhat: 世界上最流行的Linux发行版本中的yum包管理工具就是用python开发的
9. 豆瓣: 公司几乎所有的业务均是通过Python开发的
10. 知乎: 国内最大的问答社区，通过Python开发(国外Quora)
11. 春雨医生：国内知名的在线医疗网站是用Python开发的
除上面之外，还有搜狐、金山、腾讯、盛大、网易、百度、阿里、淘宝 、土豆、新浪、果壳等公司都在使用Python完成各种各样的任务。
#### 语言优点
1. Python的定位
    - 是“优雅”、“明确”、“简单”，所以Python程序看上去总是简单易懂，初学者学Python，不但入门容易，而且将来深入下去，可以编写那些非常非常复杂的程序。
2. 开发效率非常高
    - Python有非常强大的第三方库，基本上你想通过计算机实现任何功能，Python官方库里都有相应的模块进行支持，直接下载调用后，在基础库的基础上再进行开发，大大降低开发周期，避免重复造轮子。
3. 高级语言
    - 当你用Python语言编写程序的时候，你无需考虑诸如如何管理你的程序使用的内存一类的底层细节
4. 可移植性
    - 由于它的开源本质，Python已经被移植在许多平台上（经过改动使它能够工 作在不同平台上）。如果你小心地避免使用依赖于系统的特性，那么你的所有Python程序无需修改就几乎可以在市场上所有的系统平台上运行
5. 可扩展性
    - 如果你需要你的一段关键代码运行得更快或者希望某些算法不公开，你可以把你的部分程序用C或C++编写，然后在你的Python程序中使用它们。
6. 可嵌入性
    - 你可以把Python嵌入你的C/C++程序，从而向你的程序用户提供脚本功能。
#### 语言缺点
1. 速度慢
    - Python 的运行速度相比C语言确实慢很多，跟JAVA相比也要慢一些，因此这也是很多所谓的大牛不屑于使用Python的主要原因，但其实这里所指的运行速度慢在大多数情况下用户是无法直接感知到的，必须借助测试工具才能体现出来，比如你用C运一个程序花了0.1s,用Python是0.01s,这样C语言直接比Python快了10s,算是非常夸张了，但是你是无法直接通过肉眼感知的，因为一个正常人所能感知的时间最小单位是0.15-0.4s左右，哈哈。其实在大多数情况下Python已经完全可以满足你对程序速度的要求，除非你要写对速度要求极高的搜索引擎等，这种情况下，当然还是建议你用C去实现的。
2. 代码不能加密
    - 因为PYTHON是解释性语言，它的源码都是以名文形式存放的，不过我不认为这算是一个缺点，如果你的项目要求源代码必须是加密的，那你一开始就不应该用Python来去实现。
3. 线程不能利用多CPU问题
    - 这是Python被人诟病最多的一个缺点，GIL即全局解释器锁（Global Interpreter Lock），是计算机程序设计语言解释器用于同步线程的工具，使得任何时刻仅有一个线程在执行，Python的线程是操作系统的原生线程。在Linux上为pthread，在Windows上为Win thread，完全由操作系统调度线程的执行。一个python解释器进程内有一条主线程，以及多条用户程序的执行线程。即使在多核CPU平台上，由于GIL的存在，所以禁止多线程的并行执行。
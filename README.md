# [Github实践——“理想之光“APP自动答题辅助](https://github.com/fjwCode/auto-answer-hznu/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows-4BC51D.svg)](https://pypi.org/project/auto-answer-hznu/)


> 今天（2018.04.14）看到班级群发了《关于组织阿里巴巴商学院学生参加浙江省“卡尔马克思杯”浙江省大学生理论知识竞赛（初赛）的通知》，附带题库，于是心里。。。没错，写这个项目就仅是为了娱乐，顺便完成作业。上午误入歧途，浪费时间在解析题库和写入数据库中了，最后发现，题目和正确答案在答题一开始就已经全部储存于本地了，不算意外，这就非常简单了。后来为了实现全程自动化，用了PIL图像处理，精确定位选项位置，折腾一天，挺开心的。顺道实践了一下Github，啊啊啊，相当不太顺手。

## 项目源起
**学院强制每位在校学生参加浙江省“卡尔马克思杯”浙江省大学生理论知识竞赛！**

基本规则如下：由平台随机生成竞赛试卷，出题范围限于题库（题库文件另附）。每份试卷 80 道题目，包括单选题和多选题，答题时间为25分钟。所有题目均在“理想之光”APP内完成。

基于寒假的经验和知识积累，浏览了一遍文件，这个项目的构思基本就已经成型了。

## 运行环境

### Python 版本

> Python 3.6.4 | Anaconda | Windows 10

### 第三方图片处理库 —— PIL

Anaconda 发行版自带Pillow。否则，需要通过命令行安装：
```
pip install pillow
```

### 我开发的安卓自动化测试框架——Cerium

需要通过命令行安装：
```
pip install cerium
```

### Charles

Charles是一个HTTP代理服务器，当客户端连接Charles的代理访问互联网时，Charles可以监控其发送和接收的所有数据。这里我用来抓取“理想之光”APP从服务器接收到的数据包，将其保存为json文件。


## 实现过程

* 因为觉得抓包好玩，一开始我就尝试抓取数据包，常规操作，几分钟就找到了关键路径，是明文，而且是一次性请求，而非一题一题地请求，愉快地将响应文件保存为find-exam.json。可惜没仔细看，开始绕原路。
* 然后我开始解析附带的题库，是Excel表格，我的想法是全部解析写入sqlite数据库，折腾半天，中间遇到的困难有：表格填写规范不一致、数据库写入操作等。等我搞定回头看find-exam.json文件，答案果然和题目一起发出来了，其实早有想到这种情况，只是解析Excel表格，也挺好玩的。
* 接下来就简单了，答案是现成的，唯一的障碍只剩自动化答题。最开始只是模糊估计选项位置，发现实在是太不精确了，后来就用PIL处理图像，精确识别选项位置。
* 多次调试后，终于大功告成。第一次全程自动答题100分，用时4分22秒，为了防止被检测出作弊，我设置了每题之间停顿3秒多。
* 完成那一刻，超开心！！！


## 训练截图
![训练](https://raw.githubusercontent.com/fjwCode/auto-answer-hznu/master/001.png)

## 正式截图
![正式](https://raw.githubusercontent.com/fjwCode/auto-answer-hznu/master/002.png)

## 关于作者——微信公众号
![微信公众号](https://raw.githubusercontent.com/fjwCode/auto-answer-hznu/master/wx.jpg)
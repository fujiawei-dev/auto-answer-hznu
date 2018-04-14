# [Github实践——“理想之光“APP答题辅助](https://github.com/fjwCode/answer_helper) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> 今天（2018.04.14）看到班级群发了《关于组织阿里巴巴商学院学生参加浙江省“卡尔马克思杯”浙江省大学生理论知识竞赛（初赛）的通知》，附带题库，于是心里。。。没错，写这个项目就仅是为了娱乐，顺便完成作业。上午误入歧途，浪费时间在解析题库和写入数据库中了，最后发现，题目和正确答案在答题一开始就已经全部储存于本地了，不算意外，这就非常简单了。后来为了实现全程自动化，用了PIL图像处理，精确定位选项位置，折腾一天，挺开心的。顺道实践了一下Github，啊啊啊，不太顺手。

## 源起
**学院强制每位在校学生参加浙江省“卡尔马克思杯”浙江省大学生理论知识竞赛！**

基本规则如下：由平台随机生成竞赛试卷，出题范围限于题库（题库文件另附）。每份试卷 80 道题目，包括单选题和多选题，答题时间为25分钟。所有题目均在“理想之光”APP内完成。


## 运行环境

### Python 版本

> Python 3.6.4 | Anaconda | Windows 10

### 第三方图片处理库 —— PIL

Anaconda 发行版自带Pillow。否则，需要通过命令行安装：
```
pip install pillow
```


## 作者

[![fjwCode](https://avatars2.githubusercontent.com/u/29617572?s=40&v=4)](https://github.com/fjwCode)

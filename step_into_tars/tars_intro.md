## Tars Intro

### Tars是什么

Tars是腾讯MIG开源出来的一套完整的应用开发&运营解决方案（An Application DevOps Solution），包括以下几个重要部分：

- Tars含有一套自己的IDL，即tars协议描述语言；
- Tars含有一套应用开发框架，也就是常被提及的RPC开发框架。当前官方版本分别使用C++/Java实现独立的两套RPC（这里说的主要是Server侧的实现）；
- Tars含有配套的运营支撑系统，涉及发布、配置、监控、灰度等模块，级代码中的framework部分，由C++实现。
- 有一个Web运营系统，支持机器节点管理、服务配置、发布更新等。

什么叫Solution？说白了就是一条龙服务，把整个开发和运营环境都给你准备好了。基于这个方案，用者仅需关注业务逻辑开发。

初次接触Tars千万别片面理解为Tars仅仅是一个RPC开发框架。整体来说，不管是代码组织还是整体服务器结构，相对来说是比较清晰、简洁，get到以上三点那基本可以知道Tars大概是什么、并能做什么了，还是非常好理解的。

[官方介绍文档](https://github.com/zergl/Tars/blob/master/Introduction.md)写的不好，想表达的东西很多但却没说清楚。有兴趣请看后边内容。



##### 备注

	[1] MIG,Mobile Internet Group,腾讯移动互联网事业群
 
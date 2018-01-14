bitcoin源码编译
---
标签：比特币源码编译 v0.15.1

[TOC]

# 0. 环境准备
操作系统环境：

    hodor src # lsb_release -a
    No LSB modules are available.
    Distributor ID:	LinuxMint
    Description:	Linux Mint 18.1 Serena
    Release:	18.1
    Codename:	serena

    gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.5)
    
# 1. 下载代码  
当前（截止2018-01-15）最新版本为v0.15.1

1）载代码（含git logs）：
    
    git clone -b v0.15.1  https://github.com/bitcoin/bitcoin.git

2）若仅下载该TAG（不含git logs）：
    
    git clone -b 0.15.1 --depth 1 https://github.com/bitcoin/bitcoin.git

复制出一个自己的分支，方便标注和笔记等，

    hodor bitcoin # git checkout -b dev_v0.15.1  v0.15.1
    Switched to a new branch 'dev_v0.15.1'

# 2. 编译源码

    $ cd bitcoin
    $ ./autogen.sh
    $ ./configure  //其中出错参考问题1、2
    $ make -j4

# 3. 看代码
如何快速找到main函数，简单搜索如下：

    hodor src # grep -r "main(" *|grep bitcoin|grep "main("
    bench/bench_bitcoin.cpp:main(int argc, char** argv)
    bitcoin-cli.cpp:int main(int argc, char* argv[])
    bitcoind.cpp:    // If Qt is used, parameters/bitcoin.conf are parsed in qt/bitcoin.cpp's main()
    bitcoind.cpp:int main(int argc, char* argv[])
    bitcoin-tx.cpp:int main(int argc, char* argv[])
    qt/bitcoin.cpp:int main(int argc, char *argv[])
    qt/bitcoin.cpp:    QApplication::setOrganizationDomain(QAPP_ORG_DOMAIN);
    secp256k1/src/java/org/bitcoin/NativeSecp256k1Test.java:    public static void main(String[] args) throws AssertFailException{
    test/test_bitcoin_fuzzy.cpp:int main(int argc, char **argv)


# 4.附录

### 1. 问题：执行./configure报错：Berkeley DB版本兼容问题

    checking for Berkeley DB C++ headers... default
    configure: error: Found Berkeley DB other than 4.8, required for portable wallets (--with-incompatible-bdb to ignore or --disable-wallet to disable wallet functionality)

解决方式：./configure --with-incompatible-bdb

### 2.问题：执行./configure报错：找不到libevent

    checking for EVENT... no
    configure: error: libevent not found.

解决方式：安装libevent：apt-get install libevent-dev

### 3. 步骤./configure顺利的话输出如下：

    Options used to compile and link:
    with wallet   = yes
    with gui / qt = no
    with zmq      = no
    with test     = yes
    with bench    = yes
    with upnp     = auto
    debug enabled = no
    werror        = no

    target os     = linux
    build os      = 

    CC            = gcc
    CFLAGS        = -g -O2
    CPPFLAGS      =  -DHAVE_BUILD_INFO -D__STDC_FORMAT_MACROS
    CXX           = g++ -std=c++11
    CXXFLAGS      = -g -O2 -Wall -Wextra -Wformat -Wvla -Wformat-security -Wno-unused-parameter
    LDFLAGS       = 
    ARFLAGS       = cr
    
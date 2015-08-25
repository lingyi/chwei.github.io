## 一个非著名C++程序员的自我修炼

@木哈哈 [zergl.github.io](http://zergl.github.io)

-------------------------------

### 1. epoll相关及其内部原理

可能的问题：
> (1) epoll相比select的优点有哪些？

1.支持一个进程打开大数目的socket描述符(FD)

select最不能忍受的是一个进程所打开的FD是有一定限制的，由FD_SETSIZE设置，默认值是2048。对于那些需要支持的上万连接数目的IM服务器来说显 然太少了。这时候你一是可以选择修改这个宏然后重新编译内核，不过资料也同时指出这样会带来网络效率的下降，二是可以选择多进程的解决方案(传统的 Apache方案)，不过虽然linux上面创建进程的代价比较小，但仍旧是不可忽视的，加上进程间数据同步远比不上线程间同步的高效，所以也不是一种完 美的方案。不过 epoll则没有这个限制，它所支持的FD上限是最大可以打开文件的数目，这个数字一般远大于2048,举个例子,在1GB内存的机器上大约是10万左 右，具体数目可以cat /proc/sys/fs/file-max察看,一般来说这个数目和系统内存关系很大。

2.IO效率不随FD数目增加而线性下降

传统的select/poll另一个致命弱点就是当你拥有一个很大的socket集合，不过由于网络延时，任一时间只有部分的socket是"活跃"的，但 是select/poll每次调用都会线性扫描全部的集合，导致效率呈现线性下降。但是epoll不存在这个问题，它只会对"活跃"的socket进行操 作---这是因为在内核实现中epoll是根据每个fd上面的callback函数实现的。那么，只有"活跃"的socket才会主动的去调用 callback函数，其他idle状态socket则不会，在这点上，epoll实现了一个"伪"AIO，因为这时候推动力在os内核。在一些 benchmark中，如果所有的socket基本上都是活跃的---比如一个高速LAN环境，epoll并不比select/poll有什么效率，相 反，如果过多使用epoll_ctl,效率相比还有稍微的下降。但是一旦使用idle connections模拟WAN环境,epoll的效率就远在select/poll之上了。

3.使用mmap加速内核与用户空间的消息传递。

这 点实际上涉及到epoll的具体实现了。无论是select,poll还是epoll都需要内核把FD消息通知给用户空间，如何避免不必要的内存拷贝就很 重要，在这点上，epoll是通过内核于用户空间mmap同一块内存实现的。而如果你想我一样从2.5内核就关注epoll的话，一定不会忘记手工 mmap这一步的。

4.内核微调

这一点其实不算epoll的优点了，而是整个linux平台的优点。也许 你可以怀疑linux平台，但是你无法回避linux平台赋予你微调内核的能力。比如，内核TCP/IP协议栈使用内存池管理sk_buff结构，那么可 以在运行时期动态调整这个内存pool(skb_head_pool)的大小--- 通过echo XXXX>/proc/sys/net/core/hot_list_length完成。再比如listen函数的第2个参数(TCP完成3次握手 的数据包队列长度)，也可以根据你平台内存大小动态调整。更甚至在一个数据包面数目巨大但同时每个数据包本身大小却很小的特殊系统上尝试最新的NAPI网 卡驱动架构。

> (2) epoll LT与ET两种模式区别

> (3)

epoll只有epoll_create,epoll_ctl,epoll_wait 3个系统调用:
> <pre><code>
int epoll_create(int size);
int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event);
int epoll_wait(int epfd, struct epoll_event * events, int maxevents, int timeout);
</code></pre>

#### 引申问题：
> 红黑树

> mmap

>

参考：

[epoll详解]http://blog.csdn.net/xiajun07061225/article/details/9250579

### 2. daemon原理及其过程

### 3. Broken Pipe问题原因及其解决方式
如果尝试向一个已关闭的socket写，则会报Broken Pipe错误，对应抛出SIGPIPE信号，该信号默认处理方式是中止进程。

分两种情况：（1）是不是另一端还没收完就关闭了套接字？如果是则另一端，读时可改为循环；若为写，则可以忽略SIGPIPE信息(signal(SIGPIPE, SIG_IGN);)，以防进程退出。（2）是不是真的不应该写？是的话就别写了，是真的被关闭了，可以尝试重连。

Broken Pipe产生原因：

> 对一个已经收到FIN包的socket调用read方法, 如果接收缓冲已空, 则返回0, 
这就是常说的表示连接关闭。但第一次对其调用write方法时, 如果发送缓冲没问题, 
会返回正确写入(发送). 但发送的报文会导致对端发送RST报文, 
因为对端的socket已经调用了close, 完全关闭, 既不发送, 也不接收数据. 所以, 
第二次调用write方法(假设在收到RST之后), 会生成SIGPIPE信号, 导致进程退出.

> 具体的分析可以结合TCP的"四次握手"关闭. TCP是全双工的信道, 可以看作两条单工信道, TCP连接两端的两个端点各负责一条. 当对端调用close时, 虽然本意是关闭整个两条信道, 但本端只是收到FIN包. 按照TCP协议的语义, 表示对端只是关闭了其所负责的那一条单工信道, 仍然可以继续接收数据. 也就是说, 因为TCP协议的限制, 一个端点无法获知对端的socket是调用了close还是shutdown.


很多种原因：

> 1、网络通讯中，连接意外中断，比如被人拔了网线；

> 2、进程间通讯中管道断裂，譬如管道某一端进程僵死；

> 3、文件描述符终端，多见于*Nix，当退出登录时，虚拟终端断开，导致文件描述符1和2消失；

> 4、客户端向服务器发包后，服务器未返回前主动断开连接，此时若服务器调用write接口时即出现Broken pipe错误。若程序未对SIGPIPE信号做处理 ，系统对SIGPIPE的处理方式中止进程。

> 5、如果是 ssh 会话终止时提示这个消息，可能是网络连接不稳定导致这个会话断了


这里还有一种特殊的case，命令行使用管道的时候也会出现，http://blog.csdn.net/sunxinhere/article/details/7931190

知乎相关提问：http://www.zhihu.com/question/20473231

ssh远程登录失败"Write failed:Broken pipe" http://blog.csdn.net/bbirdsky/article/details/21703555

遭遇SIGPIPE[转] http://blog.chinaunix.net/uid-23849526-id-142808.html

http://stackoverflow.com/questions/108183/how-to-prevent-sigpipes-or-handle-them-properly http://stackoverflow.com/questions/108183/how-to-prevent-sigpipes-or-handle-them-properly

SIGPIPE, Broken pipe http://stackoverflow.com/nocaptcha?s=1fcb92ba-4628-416d-bdad-dd190c0023b5

### 4.socket close和shutdown的区别

> int close(int sockfd);     //返回成功为0，出错为-1.

close 一个套接字的默认行为是把套接字标记为已关闭，然后立即返回到调用进程，该套接字描述符不能再由调用进程使用，也就是说它不能再作为read或write的第一个参数，然而TCP将尝试发送已排队等待发送到对端的任何数据，发送完毕后发生的是正常的TCP连接终止序列。
在多进程并发服务器中，父子进程共享着套接字，套接字描述符引用计数记录着共享着的进程个数，当父进程或某一子进程close掉套接字时，描述符引用计数会相应的减一，当引用计数仍大于零时，这个close调用就不会引发TCP的四路握手断连过程。

> int shutdown(int sockfd,int howto);  //返回成功为0，出错为-1.

> 该函数的行为依赖于howto的值

>    1.SHUT_RD：值为0，关闭连接的读这一半。

>    2.SHUT_WR：值为1，关闭连接的写这一半。

>    3.SHUT_RDWR：值为2，连接的读和写都关闭。

>    终止网络连接的通用方法是调用close函数。但使用shutdown能更好的控制断连过程（使用第二个参数）。
  
区别

>    close函数会关闭套接字ID，如果有其他的进程共享着这个套接字，那么它仍然是打开的，这个连接仍然可以用来读和写，并且有时候这是非常重要的 ，特别是对于多进程并发服务器来说。只要套接字描述符引用计数不为0，则该套接字实际就不会被关闭。

>   而shutdown会切断进程共享的套接字的所有连接，<b>不管这个套接字的引用计数是否为零</b>，那些试图读得进程将会接收到EOF标识，那些试图写的进程将会检测到SIGPIPE信号，同时可利用shutdown的第二个参数选择断连的方式。
     
[linux网络编程之shutdown() 与 close()函数详解] http://blog.csdn.net/lgp88/article/details/7176509

### 5. TCP握手过程
http://robinjie.iteye.com/blog/289843

### 6. TCP断开连接过程

### 7. C++如何调用C代码

### 8. C如何调用C++代码

### 9. C++多态实现原理、虚表

### 10. 同步和阻塞的理解


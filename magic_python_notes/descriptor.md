### Python黑魔法系列之描述符（Descriptor）

	* 阅读难度：中
	* 读者对象：初/中级Python程序员；其他语言爱好者

Descriptor字面译“描述符”，官方说明在[这里](https://docs.python.org/3/howto/descriptor.html)。


- 1. 描述符是什么？官网定义如下：
> In general, a descriptor is an object attribute with “binding behavior”, one whose attribute access has been overridden by methods in the descriptor protocol. Those methods are __get__(), __set__(), and __delete__(). If any of those methods are defined for an object, it is said to be a descriptor.

读起来有些拗口，关键是要理解什么是“binding behavior”（绑定行为），关于描述符关键几个点：

（1）描述符是具有“绑定行为”属性的对象。对于对象属性，一般操作有读、写、删三个操作，因此

（2）只要对象实现了\_\_get\_\_()/\_\_set\_\_()/\_\_delete\_\_()三个方法中任意一个或多个，则该对象即拥有描述符属性。说白了，这个规则也就是描述符协议（Descriptor Protocol）。

（3）同时实现了\_\_get\_\_()和\_\_set\_\_()两个方法的对象，则称为**数据描述符（Data Descriptor）**，仅实现了__get__()方法的描述符成为**非数据描述符**。

 （4）定义\_\_get\_\_()和\_\_set\_\_()，并将\_\_set\_\_()直接抛出异常AttributeError，则可定义一个只读数据描述符。

（5）访问“属性”时，搜索（lookup）优先顺序为：对象实例\_\_dict\_\_字典、对象类型（class）\_\_dict\_\_字典，对象类型父类的\_\_dict\_\_字典（不含元类）。

（6）aaa

```python
class C(object):
	def __init__(self, name=""):
		self._name = name

	def __get__(self):
		return self._name

	def __set__(self, name):
		self._name = name

```

其他：

>	- Python对象是如何访问属性的，比如类（对象）变量或方法。通过__getattribute__()接口，然后依次从实例对象、类、类的父类的__dict__字典中查找是否有对应的属性名称。这里有个优先级问题，也就是所谓的lookup chain。
>	- Python MRO (Method Resolution Order)
>	- \_\_getattribute\_\_()
>	- supper()


- 2. 描述符有什么用？

> Properties, bound and unbound methods, static methods, and class methods are all based on the descriptor protocol.


- 3. 参考附录

	- 1. [Descriptor HowTo Guide](https://docs.python.org/3/howto/descriptor.html)
	- 2. [Python描述器引导(翻译)](http://pyzh.readthedocs.io/en/latest/Descriptor-HOW-TO-Guide.html)

### Python黑魔法系列之"属性"（property）

字面上翻译这个feature就是“属性”，但不是一般理解的属性概念。通常说的属性是Attribute，比如C++里的类变量。

（1）通常说的属性（attribute）是类似someObj.name这样的，等价于someObj.__dict__['name']。也就是，对象变量（instance variable）是对象\_\_dict\_\_字典里的一个子项。

（2）Python

- 参考附录
	- 1.[Attributes, Properties and Descriptors](http://itmaybeahack.com/book/python-2.6/html/p03/p03c05_properties.html)
	- 2. xxx
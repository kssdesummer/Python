## Xpath

### 安装

安装解析包: lxml

导入包: from lxml import etree

### 使用规则

| 表达式   | 描述                                                      |
| -------- | --------------------------------------------------------- |
| nodename | 选取此节点的所有子节点                                    |
| /        | 从根节点选取                                              |
| //       | 从匹配选择的当前节点选择文档中的节点,从未不考虑他们的位置 |
| .        | 选取当前的节点                                            |
| ..       | 选取当前节点的父节点                                      |
| @        | 选取属性                                                  |

### 路径表达式

| 路径表达式                         | 结果                                                   |
| ---------------------------------- | ------------------------------------------------------ |
| /bookstore/book[1]                 | 选取bookstore子元素的第一个子元素                      |
| /bookstore/book[last()]            | 选取bookstore子元素的最后一个子元素                    |
| /bookstore/book[last()-1]          | 选取bookstore子元素的倒数第二个子元素                  |
| /bookstore/book[position()-3]      | 选取bookstore子元素的前两个子元素                      |
| //title[@lang]                     | 选取所有拥有属性lang的title元素                        |
| //title[@lang='eng]                | 选取lang属性值为eng的title属性                         |
| /bookstore/book[price>35.00]       | 选取bookstore子元素的book子元素,price元素的值大于35.00 |
| /bookstore/book[price>35.00]/title | book元素的标题                                         |
|                                    |                                                        |

### 取值规则

使用索引确定,然后使用   `.text()`取出值,`@属性名`取出属性值


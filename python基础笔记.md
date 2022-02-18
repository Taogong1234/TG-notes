# 1. python 
* 面向对象
* 90后
* 交互式命令行 或 IDLE
  
# 2.print
* print（520）数值
* print（'hello'）字符串
* print（3+1） 表达式
* fp=open（'路径'，'a+'）
  print（'hello',file=fp）
  fp.close()
* print('hello','hello','hello') 同一行输出 

# 3. 转义字符
* \n 换行
* \t 制表符（4空格）
* \r 回车
* \b 退一格
* \\ 指单一 \
* \'   '
* \"   "
* 原字符 ：字符串前加r或R使得 转义字符不起作用
* 8bit位=1byte字节 对应 ASCll  Unicode  UTF-8（二进制与字符编码）
* 保留字与标识符
# 4.变量(id type value)
+ type :int folat bool(真、假) str（字符串）
+ 转换为十进制：ob+二进制
+ ‘’ “”不可以换行显示 ‘‘‘’’’可以
+ 数据类型转换 str（） float（） int（） 
+ 多行注释‘‘‘’’’  单行注释 #  编码声明注释
+ 加号 连接符和运算符 
# 5.input输入函数
+ present=input（‘提 示’）
# 6.运算符
+ // 整除  一正一副向下取整
+ % 取余   余数=被除数-除数*商
+ ** 幂运算
+  支持链式赋值 
+  支持参数赋值
  += -= *=  /=  //= %=
+ 支持解包赋值
  a,b,c=20,30,40(位置个数对应)
  a,b=b,a (数值交换)
+ == 等于 ！= 不等于 比较运算比较value
+ is 同 比较id标识  is not 异 
+ id（）查看id
+ bool运算符 and  or  not（非）  in（在）  not in（不在）
+ 位运算 & 与  | 或   << 左移乘2    >> 右移 除以2
  高位溢出，低位补0/ 高位补0，低位截断 （乘除2）
+ 优先级：括号 算数 位  比较 布尔 赋值

# 7.程序结构
+ 顺序 循环 选择结构
+ 布尔值：一切皆对象 bool（）查看布尔值
+ 选择（单分支 双分支 多分支结构）
  
  if 条件：
     （1）
  else:
     （2）
  
  if  条件1：
        （1）
  elif 条件2：
        （2）
  elif 条件3：
        （3）
  else：
        （4）
注意：允许连续判断: 1 < a <= 3
+ 嵌套 if
   if 条件：
      if 条件：
        （1）
      elif条件：
        （2）
      else：
         (3)
   else :
    if 条件：
        （1）
      else：
         (2)
+ 条件表达式简化 （1） if 条件  （2）
  判断为真执行左边，判断为假执行右边
+ pass 占位符号，什么也不做，占用语句位置
+ 
+ r=range（10） 默认从0开始到9，步长为1
+ r=range（1，10，2）从1到9，步长2
# 8.循环语句
+ while a<3:
+ for-in 
   for i in 'hello'
   for i in range(10)
   for _ in range(5)  不需要使用自定义变量，则使用_代替，用于控制循环次数
+ break 非正常结束循环 （结束循环）
+ continue 进入下一次循环（结束本次循环）
+ else  与if while for 搭配
+ end=‘/t’  打制表符   print（）换行
+ 二重循环中，break与continue只影响一层循环

# 9.列表
+ 创建 a=[1,2,3] 或者 a=list([1,2,3])
+ 索引从0开始，若逆序最后为-1
+ 包容性强
+ 查询列表中元素索引号： index（‘hello’，1，4），返回第一个被查到的，可指定查找范围
+ print（a[2]） 应用列表元素 即 列表名[1:6:1],不包括6，默认步长为1，默认从0，默认end
+ append（5） append（lst2）把列表2当做一个元素
+ extend（lst2）
+ insert（1，90）插入
+ 切片并添加
+ lst.remove(value)
+ lst.pop(index),pop()默认移除最后一个
+ lst【1，3】=【】清除
+ lst.clear() 全清除
+ del lst 删除列表 
+ lst.sort()升序
+ lst.sort(reverse=true)降序
+ lst.sorted() 生产新的列表，并升序
+ 列表生产式 lst=[i*i for i in range(1:10)]
  
# 10.字典(成对)
+ scores={‘张三’：100}
+ scores=dict()
+ scores[‘键’]
+ scores.get('键',默认值)
+ del scores[‘键’]
+ scores.clear
+ scores[‘键’]=100 增加或者修改
+ keys=scores.key()  list(keys)
+ valuess=scores.values()
+ itemss=scores.items()
+ 键不可重复，值可以重复，键重复会覆盖
+ 字典生成式

# 11.元组与集合
+ 不可变序列与可变序列
+ 无序与有序
+ 元组不可变
+ t=('hello','world',98)  括号可省略，一个只有一个元素，元素后加逗号，
+ t=tuple(('hello','world',98))
+ 元组中元素引用同数组，但是是不可变序列，但可以对数组元素修改。
+ 集合s={1,2,8,6} 只有键没有value，同样不允许重复，否则覆盖
+ s=set(range(6)) .ect很多方式创建
+ s.add()一次加一个   s.update()一次加多个 
+ s.remove()   s.discard()删一个并不报错
  s.pop()随机删一个不能指定  s.clear 清空
+ issubset 子集
+ issuperset 
+ isdisjiont 有交集为假
+ intersection（）、 &  取交际
+ union（）、| 取并集
+ difference（）、 - 取差集
+ symmetric_difference 、^ 取对称差集
+ 集合生成式 把列表生成式[]改为{}即可

# 12 字符串
+ 字符串的驻留机制（提高性能）
+ 字符串查询 find、rfind
+ 字符串大小写转换命令
+ 字符串对齐方法
+ 字符串的分劈
+ 字符串的判断
+ 字符串的替换与合并  replace  join
+ 字符串比较 ord（）算ascll码  chr（）算值  ==比内容   is比内存地址
+ 字符串切片
+ 格式字符串 % 或 {}
+ 编码与解码
  
# 13 函数
+ def定义 return返回值
+ 位置传递 关键字传递  
+ 不可变对象经过函数修改后不变，可变对象会受到函数修改影响
+ 不需要给调用出返回值return可以不写，返回多个值时会返回一个元组
+ 形参的默认值
+ 可变参数 *位置形参   **关键字形参  （两者都有时，可变位置形参在可变关键字形参之前）
+ 列表转为位置形参用*，字典转为关键之形参用**
+ 一部分采用关键字传递用*
+ 变量的作用域 局部变量（函数内部，可用globle转换） 全局变量（函数外定义）
+ 递归函数 调用条件与终止条件

# 14 常见bug
+ 数据类型
+ 中文输入法
+ if 语句漏：
+ 缩进错误
+ 将字符串与数字拼接
+ 没有定义变量如while循环次数
+ ==与=混淆
+ 索引越界 0开始
+ append不熟练 每次添加一个
+ debug方法 1、print  2、#注释一部分
+ 练练练
+ 异常处理机制1  try 可能异常的代码   except  提示
+ 异常处理机制2  
   try  
 可能异常的代码  
 except   BaseException as e 
 print（e）  
 else  
 未异常则执行  
 finally  
 都会执行的  
+ zerodivisionerror 取零  indexerror索引 keyerror 没有这个键 namerror 未申明 syntaxerror 语法错误 valueerror 传入无效参数
  
# 15 traceback模块 打印错误信息

# 16 程序调试
+ 插入断点

# 17 编程思想
+ 面向过程 （微观）
+ 面向对象 （宏观）
+ 两者相辅相成
+ 类(如数据类型) 对象（具体数据个体）
+ python 一切皆对象
+ 定义类（也是一种类对象）：class Student（约定首字母大写）
+ 类属性 实例方法（有self） 静态方法@staticmethod 类方法@classmethod （有cls）  实例属性 如self.name
+ 类方法 调用 对象.方法 或 类.方法（对象）
+ 动态绑定方法  为实例对象添加新的属性 stu1.gender='girl'

# 18 object类
+ 面向对象的三大特征：封装（黑匣子但可使用），继承，多态
+ 继承 、 多继承
+ 多态 动态语言
+ 特殊方法与特殊属性

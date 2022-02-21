# vs code 与jupyter notebook
## vs code
+ 自动换行 : alt + z
+ 字体放大/缩小: ctrl + ( + 或 - )
+ 多行注释：[alt+shift+A]
+ 控制台终端显示与隐藏：ctrl + ~
+ 全局查找文件：ctrl + shift + f
+ 快速回到顶部 ： ctrl + home
+ 快速回到底部 : ctrl + end
+ 全局替换：ctrl + shift + h
+ 打开新的命令窗：ctrl + shift + c

## jupyper
+ m command模式  Y edit模式
+ ctrl ENETR 运行并下一行
+ shift ENETR  运行
+ l 显示行号

# numpy 与 matplotlib库 数据分析学习
+ np.array([[,,],[,,]],dtype=np.int)
+ np.size
+ np.shape
+ np.ndim
+ np.zeros((3,4))
+ np.ones()
+ np.empty()
+ np.arange(10,20,2),
+ np.arange(12).reshape((3,4))
+ np.linspace(1,10,20).reshape((4,5))
+ 数组运算：+，-,*,/,**,np.sin(),np.cos()  ,数组元素分别对应运算
+ np.dot（a,b）或者 a.dot(b)
+ np.random.random((2,4)) 随机
+ np.sum(a,axis=1) 在行求和，axis=0 对列求和
+ np.min() 
+ np.max()
+ np.argmin 求最小值的索引
+ np.argmax 
+ np.mean(A) A.mean() np.average(A)平均值
+ np.median(A) 中位数
+ np.cumsum(A) 累加
+ np.diff(A) 相邻差值
+ np.nonzero(A) 所在行列索引
+ np.sort(A) 逐行排序
+ np.transpose(A) A.T 转置
+ np.clip(A,5,9) 将所有值
+ 可以针对行列，加上axis=0或1
+ 索引 A[2,1] 第三行第二列  A[:,1] 第二列所有 A[1,1:2] 只有一个数和matlab不同
+ for row in A  #估计和矩阵存储顺序有关
+ for column in A.T
+ A.flatten() 返回以为数组
+ A.flat 迭代器使用
+ np.vstack(A,B) 上下合并
+ np.hstack(A,B) 左右合并
+ np.concatenate((A,B,A,B),axis=1) 指定方向的多个数值合并
+ np.slip(A,2,1) 均等分割  np.vslip np.hslip
+ np.array_slip 不等分割
+ 赋值=  为指针，复制的话要用b=a.copy()
+ numpy pandas 运算更快
+ np.array(data1) 转换为矩阵或数组，且为深拷贝即.copy
+ np.asarray(data1) 转换为矩阵或数组，且为浅拷贝即 =
+ column 列axis=0   row 行 axis=1

+ s=pd.Series(np.one  columns  index)
+ pd.DataFrame()
+ df.dtypes
+ df.index
+ df.columns
+ df.values
+ df.describe()
+ df.T
+ df.sort_index(axis=1,ascending=False)
+ df.sort_value()
+ df['A'] ,df.A  索引
+ df[0:3],df['A':'B']  索引
+ df.loc[:,['A','B']] 按标签索引
+ df.iloc[[2:3],[3:5]] 按位置索引
+ df.ix[] 标签和数值结合索引
+ 通过布尔值索引 如加个df.A<8判断  或如df.B[df.A>4]=222
+ np.nan  即  none
+ df.dropna(axis=0或1，how=‘any’或‘all’) 丢弃行或列，全为none时或一个none
+ df.fillna(value=0) 替换为0
+ np.any(df.isnuff())==true 是否有缺失
+  读取文件
+  pd.read_csv('student.csv')
+  导出
+  data.to_pickle('student.pickle')
+  pd.concat([df1,df2,df3],axis=0,ignore_index=True) 合并
+  pd.concat([],join='inner'或‘outer’)
+  join_axes=df1.index 指定合并基准
+  df.1append([df2,df3])
+  pd.merge(left,right,on=['key1',''key2],how='inner'或‘outer‘’right’‘left’)
+  data.head(5) 前五个数据
+  plt.show()
+  plt.scatter()
+  plot方法 bar，hist，hist，box，kde，area，scatter，pie，hexbin
+  data.plot.scatter(x=‘A’,y='B',color='DarkBlue',lable='Class1')

+  conda install matplotlib(或者pip install matplotlib)  如果缺失库需要安装
+  plt.plot(x,y，label=“我的线”，color="orange",linestyle=':',linewidth=5) 画图
+  plt.show() 显示
+  plt.figure(figsize=(20.8),dpi=80) 图片大小
+  plt.savefig('./tupian.png') 保存图片
+  plt，xticks(x[::3]) 设置刻度,去步长
+  plt，yticks(range(min(y),max(y)+10)) 设置刻度,去步长
+  xtick_lable=[’10点{}分.format(i) for i in range(60)]
+  plt.xticks(list(x)[::3],xtick_lable[::3],rotation=90)
+  fc -list 查看系统字体
+  fc -list ：lang=zh
+  ctrl b 看源码，查注释
+  显示中文 使用font_mannager
+  plt.xlabel('时间')
+  plt.ylable('路程')
+  plt.title('图表')
+  pip list 查看库（?）
+  pip -version 查看版本(？)
+  plt.grid(alpha=0.1) 透明度与网格
+  plt.legend() 图例
+  ipython魔法函数 %matplotlib inline  嵌入式显示，就不需要plt.show()了，否则需要加上后者
+  shift + l 显示行号
+  np.linspace(2,10,5) 与np.ones(5)  都是所见即所得
+  range(25) 0到24
+  plt.xlim(0,10) 限定轴范围
+  import sympy   符号包
+  from sympy import init_printing  输出模块  
+  init_printing(use_latex=true)  支持latex输出
+  sympy.symbol()
+  from sympy.utilities.lambdify import lambdify  转化为可用函数
+  矩阵运算速度快与for循环，成指数增长。

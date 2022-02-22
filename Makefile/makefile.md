# makefile注意事项  
1.  make所看到的第一项规则会被当做默认规则使用。    
2.  命令前必须使用有一个制表符 **Tab**  ，有的代码编辑器会默认用**空格**替换**Tab**，从而报错。如下：  
```
Makefile-5:2: *** missing separator.  Stop.  
```
3.  makefile中清理命令clean最好声明为伪目标，以防存在同名文件。  
4.  makefile中用clean删除不存在文件时候会报错从而停止运行。解决办法有（1）`-f`强制删除  (2)`-`rm 跳过继续执行  
5.  makefile编译时会比较**目标文件**与**依赖文件**的产生时间，所以尽量编译前将前期不满意的过程文件删除  
```
.PHONY:clean
clean: 
	rm -f *.o
	rm -f *.mod
	rm -f *.exe
```
6.  直接make会自动寻找名为makefile的文件，用指定makefile文件需要用`make -f 文件名`  
7.  gfortran -c 依赖文件 （-o 目标文件）  
8.  gfortran -o 执行文件 依赖文件  
9.  `@` 不显示编译过程  `#`注释  `\`换行符、转义符  
10. 自动变量
    \$@    目标文件的文件名；  
    \$%     仅当目标文件为归档成员文件（.lib 或者 .a）时，显示文件名，否则为空；  
    \$<      依赖（prerequisite）列表里面的第一个文件名；  
    \$?      所有在prerequisite列表里面比当前目标新的文件名，用空格隔开；  
    \$^      所有在prerequisite列表中的文件，用空格隔开； 如果有重复的文件名（包含扩展名），会自动去除重复；  
    \$+      与$^相似，也是prerequisite列表中的文件名用空格隔开，不同的是这里包含了所有重复的文件名；  
    \$*       显示目标文件的主干文件名，不包含后缀部分。  
    \%.c %.o  任意一个.c或.o文件   
    \*.c *.o  所有.c .o文件 
	?=    覆盖并赋值
	=   赋值

# 编译cip代码经验（与vs有区别）
1. gfortran对代码长度有要求，不能太长，否则后部直接截断，不识别
2. OUT文件夹与代码中严格一致，大小写敏感
3. 输出**结果文件.dat**需要在OUT文件夹中手动创建好空文件，gfortran不会自动创建
4. 输出结果文件格式不支持**Binary**（二进制），代码中替换为**unformatted**才解决报错问题。
5. 变量声明严格，如声明为real(8) 则赋值为`20`会报错,最好为`20.0`
6. .mod 文件类似于头文件，在代码有引用其他模块时则会需要所依赖的模块的.mod文件（存在嵌套的代码编译需要依赖文件.mod和源文件.f90）
7. 由于过程中.mod文件的存在，所以代码的编译要有顺序要求，先编译不存在依赖.mod的文件
8. -0[0、1、2、3] 代码优化，默认2级优化，**级别越高，不一定代码效率越高**
9. 预定义变量  （1）cpp c预编译器名称  （2）cppflags c预编译器选项，无默认值 （3）cflags c编译器选项，无默认值 (4)fflags fortran编译器选项，无默认值  
10. 显式makefile
```
run:
	gfortran -c PARAMETERS.f90 -o PARAMETERS.o   #代码编译有顺序要求
	gfortran -c BOUNDARY_CONDITIONS.f90 -o BOUNDARY_CONDITIONS.o
	gfortran -c VOF_2D.f90 -o VOF_2D.o
	gfortran -c LS_2D.f90 -o LS_2D.o
	gfortran -c FIELD_FILES.f90 -o FIELD_FILES.o
	gfortran -c solid.f90 -o solid.o   #会有警告
	gfortran -c GAUGE.f90 -o GAUGE.o
	gfortran -c WAVE_MAKER.f90 -o WAVE_MAKER.o
	gfortran -c GLOBAL.f90 -o GLOBAL.o
	gfortran -c Source_wavemake.f90 -o Source_wavemake.o
	gfortran -c NS_SOLVER.f90 -o NS_SOLVER.o
	gfortran -c INTIAL_CONDITION.f90 -o INTIAL_CONDITION.o
	gfortran -c MAIN.f90 -o MAIN.o
	gfortran -o cip.exe *.o   #gfortran *.o -o cip.exe
.PHONY:clean
clean: 
	rm -f *.o
	rm -f *.mod
	rm -f *.exe
```
11. 隐式makefile(使用变量)
```
tar=cip.exe
obj=PARAMETERS.o BOUNDARY_CONDITIONS.o VOF_2D.o LS_2D.o FIELD_FILES.o solid.o GAUGE.o  WAVE_MAKER.o\
GLOBAL.o  Source_wavemake.o NS_SOLVER.o  INTIAL_CONDITION.o   MAIN.o    #obj的定义有顺序要求
gf=gfortran
$(tar):$(obj)
	$(gf) $^  -o $@
#	$(gf) $(obj)  -o $(tar)
%.o:%.f90
	$(gf) -c $^  -o $@
.PHONY:clean
clean: 
	rm -f *.o
	rm -f *.mod
	rm -f *.exe
```
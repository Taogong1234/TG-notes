# 并行计算
+ MPI是一个标准，而非一门语言
+ API 应用程序接口
+ 进程、消息传输、发送与接受、同步与异步、通讯域
+ MPI_Init 初始化
+ MPI_Comm_world 默认通行域
+ MPI_Comm_rank  获得进程序号
+ MPI_Comm_size  通行域中的总进程数
+ MPI_Finalize 清除MPI环境
+ 编译
  mpif90 （gun）
  mpiifort   （intel）
+ 运行
  mpirun -np 进程数
+ 阻塞与非阻塞
+ 点对点 多对多通讯
+ scatter 分发 gather 集合  reduce 规约
+ Allgather 多对多
+ wtime 
+ 并发 单个cpu处理多个线程 ，并行 多个cpu，同一时刻在多个cpu上并发
+ mpi 粗粒度级别 openmp 细粒度级别
+ 

  
高性能计算工具和资源，专为工程师和管理员设计。

高性能计算（[High Performance Computing (HPC)](https://en.wikipedia.org/wiki/Supercomputer)） 通常指通过聚合计算资源以实现远高于普通台式机或工作站的性能，从而解决科学、工程或商业领域中大型问题的实践。


Table of Contents
=================

   * [资源配置](#资源配置)
   * [工作负载管理器](#工作负载管理器)
   * [流水线](#流水线)
   * [应用程序](#应用程序)
   * [编译器](#编译器)
   * [MPI](#mpi)
   * [并行计算](#并行计算)
   * [基准测试](#基准测试)
   * [其他](#其他)
   * [性能](#性能)
   * [并行 shell](#并行-shell)
   * [容器](#容器)
   * [环境管理](#环境管理)
   * [可视化](#可视化)
   * [并行文件系统](#并行文件系统)
   * [编程语言](#编程语言)
   * [监控](#监控)
      * [基于 Prometheus](#基于-prometheus)
   * [期刊](#期刊)
   * [播客](#播客)
   * [博客](#博客)
   * [会议](#会议)
   * [网站](#网站)
   * [用户组](#用户组)

## 资源配置

- [Grendel](https://grendel.readthedocs.io/) - 用于HPC Linux集群的裸资源配置系统（[源代码](https://github.com/ubccr/grendel)）GPL-3。
- [XCat](https://xcat.org/) - xCAT是一个用于部署和管理各种规模集群的工具包 [Source Code](https://github.com/xcat2/xcat-core) EPL-1.0。
- [Warewulf](https://warewulf.hpcng.org/) - Warewulf 是一个用于大型裸机和/或虚拟系统集群的无状态、无盘容器操作系统部署系统[Source Code](https://github.com/hpcng/warewulf) BSD-3.
- [Rocks](http://www.rocksclusters.org/) - 用于开发 Linux 集群的 Linux 发行版。
- [Cobbler](https://cobbler.github.io/) - Cobbler 是一个 Linux 安装服务器，可快速设置网络安装环境 [Source Code](https://github.com/cobbler/cobbler) GPL-2.0。 -- 推荐
- [Base Command Manager](https://docs.nvidia.com/base-command-manager/index.html) - Base Command Manager 允许管理员快速构建和管理异构集群（专有 英伟达）。
- [Scyld](https://www.penguinsolutions.com/computing/products/software/scyld-clusterware/) - Scyld ClusterWare 基于 NASA 于 20 世纪 90 年代开发的 Beowulf 集群的持续演进而开发（专有）。
- [BlueBanquise](https://bluebanquise.com) - BlueBanquise 是一个基于 Python 和 Ansible 的开源集群部署和管理堆栈[Source Code](https://github.com/bluebanquise/bluebanquise) MIT。

## 工作负载管理器

- [Slurm](https://slurm.schedmd.com/documentation.html) - 免费且开源的作业调度程序 [Source Code](https://github.com/SchedMD/slurm) OSS -- 推荐。
- [LSF](https://www.ibm.com/products/hpc-workload-management) - 由 IBM 开发的作业调度程序和工作负载管理软件（专有软件）。
- [Moab](https://adaptivecomputing.com/moab-hpc-suite/) - Moab 是一个工作负载管理和作业调度程序（其他）。
- [Torque](https://en.wikipedia.org/wiki/TORQUE) - Torque 是一个工作负载管理和作业调度程序 （其他）。
- [OpenLava](https://en.wikipedia.org/wiki/OpenLava) - OpenLava 是一个工作负载管理和作业调度程序 （其他）。
- [UGE/SGE](https://en.wikipedia.org/wiki/Univa_Grid_Engine) - Univa Grid Engine 是一个用于高性能计算（HPC）的工作负载管理引擎（专有软件）。
- [Volcano](https://volcano.sh/) - Volcano 是一个基于 Kubernetes 的批处理系统（Apache-2.0 许可证） [Source Code](https://github.com/volcano-sh/volcano) 。
- [Maui](https://www.mhpcc.hpc.mil/) - Maui 是一个工作负载管理和作业调度器 （其他）。
- [Kube Batch](https://github.com/kubernetes-sigs/kube-batch) - Kubernetes 的批处理调度器，适用于高性能工作负载，例如 AI/ML、大数据、HPC Apache-2.0。
- [OpenPBS](https://www.openpbs.org/) - OpenPBS® 软件优化了高性能计算（HPC）环境中的作业调度和工作负载管理 [Source Code](https://github.com/openpbs/openpbs) 其他 -- 推荐。 附：[pbs-professional](https://altair.com/pbs-professional) -- 推荐

## 流水线
- [Nextflow](https://nextflow.io) - 数据驱动的计算管道 Apache-2.0。
- [Cromwell](https://cromwell.readthedocs.io/en/stable/) - 专为简单性和可扩展性设计的科学工作流引擎 [Source Code](https://github.com/broadinstitute/cromwell) BSD-3 -- 推荐。
- [Pegasus](https://pegasus.isi.edu/) - 用于在广泛的计算基础设施上映射和执行科学工作流的可配置系统 [Source Code](https://github.com/pegasus-isi/pegasus) Apache-2.0。

## 应用程序

- [Spack](https://spack.io) - 支持多版本、配置、平台和编译器的灵活包管理器 [Source Code](https://github.com/spack/spack) 其他 -- 推荐。
- [EasyBuild](https://easybuild.io/) - EasyBuild - 轻松构建软件 [Source Code](https://github.com/easybuilders/easybuild) GPL-2。

## 编译器

- [Nvidia](https://developer.nvidia.com/hpc-compilers) - NVIDIA 高性能计算（HPC）编译器套件，支持 Fortran、C/C++ 及 OpenACC（专有）。
- [Portland Group](https://www.pgroup.com/index.htm) - Portland Group 编译器（原 Fortran、C/C++ 编译器）现已整合至 NVIDIA HPC SDK（专有）。
- [Intel](https://software.intel.com/content/www/us/en/develop/tools/oneapi/all-toolkits.html#hpc-kit) - Intel 编译器套件提供多种语言编译器，专为 HPC 领域设计（专有）。
- [Cray](https://bluewaters.ncsa.illinois.edu/cray-compiler) - 专为 AMD Interlagos 指令集设计和优化的编译器套件（专有软件）。
- [GNU](https://gcc.gnu.org/) - GNU 编译器集合（GCC）是针对多种语言的编译器套件 [Source Code](https://gcc.gnu.org/git.html) GPL-3 -- 推荐。
- [LLVM](https://llvm.org/) - LLVM 项目是一组模块化编译器和工具链 [Source Code](https://github.com/llvm/llvm-project) 开源软件（OSS） -- 推荐。。

## MPI
- [OpenMPI](https://www.open-mpi.org/) - OpenMPI 是 MPI-3.1 标准的开源实现（源代码）BSD [Source Code](https://github.com/open-mpi/ompi) -- 推荐。
- [MPICH](https://www.mpich.org/) - MPICH 是 MPI-3.1 标准的高性能且广泛可移植的实现 [Source Code](https://github.com/pmodels/mpich) 其他。
- [MVAPICH](https://mvapich.cse.ohio-state.edu/) - MVAPICH 是俄亥俄州立大学开发的 MPI-3.1 标准的开源实现 BSD。
- [Intel-MPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/mpi-library.html) - Intel-MPI 是 Intel 编译器套件中包含的 MPI-3.1 实现，采用其他许可协议。

## 并行计算
- [ArrayFire](https://arrayfire.org/docs/index.htm) - 这是一个通用张量库，简化了并行架构上的软件开发过程，采用其他许可协议。 [Source Code](https://github.com/arrayfire/arrayfire) BSD-3-Clause license  -- 推荐
- [OpenMP](https://www.openmp.org/)  - OpenMP 是一个支持多平台共享内存多处理编程的应用程序接口，采用其他许可协议。

## 基准测试

- [OSU Benchmarks](https://mvapich.cse.ohio-state.edu/benchmarks/) - 由俄亥俄州立大学开发的 MPI 基准测试工具集合 [Source Code](https://github.com/forresti/osu-micro-benchmarks) 。
- [Intel MPI Benchmarks](https://software.intel.com/content/www/us/en/develop/articles/intel-mpi-benchmarks.html) - 英特尔为其 Intel MPI 开发的基准测试集。
- [HPCC Systems](https://hpccsystems.com/) - HPCC 系统（高性能计算集群）是一个开源的大规模并行处理计算平台，用于大数据处理和分析 [Source Code](https://github.com/hpcc-systems/HPCC-Platform) 。
- [LINPACK](https://www.netlib.org/linpack/) - LINPACK 是一组用于求解线性系统的有效 Fortran 子程序，其基准测试对 HPC 很有用。
- [IOzone](https://www.iozone.org/) - IOzone 是一个文件系统基准测试工具 OSS。
- [IOR](https://www.vi4io.org/tools/benchmarks/ior) - 交错或随机是一种用于测试其他并行文件系统的有用基准测试工具。
- [MDtest](https://www.vi4io.org/tools/benchmarks/mdtest) - MDtest 是一个基于 MPI 的应用程序，用于评估文件系统的元数据性能。
- [FIO](https://fio.readthedocs.io/en/latest/fio_doc.html) - 灵活 I/O 是一个高级磁盘基准测试工具，依赖于内核的 AIO 访问库 [Source Code](https://git.kernel.dk/cgit/fio/) GPL-2。
- [elbencho](https://github.com/breuner/elbencho) - 用于文件、对象和块的分布式存储基准测试工具，支持 GPU，采用 GPL-3 许可证。

## 其他

- [OpenOnDemand](https://openondemand.org/)  - Open OnDemand 帮助计算研究人员和学生高效利用远程计算资源，使其能够从任何设备轻松访问 [Source Code](https://github.com/OSC/ondemand) MIT 许可证。
- [Open XDMod](https://open.xdmod.org) - Open XDMoD 是一个开源工具，用于简化高性能计算资源的管理 [Source Code](https://github.com/ubccr/xdmod/) LGPL-3。
- [Coldfront](https://coldfront.readthedocs.io/en/latest/) - ColdFront 是一个开源资源分配系统，旨在为高性能计算资源的管理、报告和衡量科学影响提供一个中央门户 [Source Code](https://github.com/ubccr/coldfront) GPL-3。
- [Pavilion2](https://pavilion2.readthedocs.io/) - Pavilion 是一个基于 Python 3（3.6+）的框架，用于在高性能计算系统上运行和分析测试 [Source Code](https://github.com/hpc/pavilion2) 其他。
- [Reframe](https://reframe-hpc.readthedocs.io/en/stable/) - 一个强大的 Python 框架，用于编写和运行适用于高性能计算系统的可移植回归测试和基准测试。（[Source Code](https://github.com/reframe-hpc/reframe) BSD-3。
- [OLCF Test Harness](https://olcf.github.io/olcf-test-harness/) - OLCF 测试框架（OTH）有助于自动化测试应用程序、工具和其他系统软件 [Source Code](https://github.com/olcf/olcf-test-harness) 其他。
- GoSlmailer](https://github.com/CLIP-HPC/goslmailer) - GoSlmailer 是一个用于 Slurm 的即插即用通知交付解决方案，支持 Slack、Mattermost、Teams 等。

## 性能

- [TotalView](https://totalview.io/products/totalview) - TotalView 是一款用于 HPC 应用程序的调试工具（专有）。
- [Tau](https://www.cs.uoregon.edu/research/tau/home.php) - TAU Performance System® 是一款用于分析用 Fortran、C、C++、UPC、Java、Python 等语言编写的并行程序性能的可移植剖析和跟踪工具包（其他）。
- [Valgrind](https://www.valgrind.org/) - Valgrind 是一款用于剖析程序以确定内存泄漏的工具 [Source Code](https://sourceware.org/git/?p=valgrind.git) GPL-2。
- [Paraver](https://tools.bsc.es/paraver) - Paraver 是一个非常灵活的数据浏览器，是 CEPBA-Tools 工具包的一部分。
- [PAPI](http://icl.cs.utk.edu/papi) - 性能应用程序编程接口 (PAPI) 是一个性能分析工具（源代码）等。

## 并行 shell

- pdsh](https://linux.die.net/man/1/pdsh) - pdsh 在多个主机上并行运行终端命令 [Source Code](https://github.com/chaos/pdsh) GPL-2。
- [ClusterShell](https://clustershell.readthedocs.io/en/latest/intro.html) - 可扩展的集群管理 Python 框架 [Source Code](https://github.com/cea-hpc/clustershell) LGPL-2.1。

## 容器

- [Apptainer](https://apptainer.org) - Apptainer 是一个开源容器系统 [Source Code](https://github.com/apptainer/apptainer) BSD。
- [Charliecloud](https://hpc.github.io/charliecloud/)  - Charliecloud 为高性能计算（HPC）中心提供用户定义的软件堆栈（UDSS）[Source Code](https://github.com/hpc/charliecloud) Apache-2.0。
- [Docker](https://www.docker.com/ - Docker 是一组基于操作系统级虚拟化的平台即服务产品，用于以称为容器的包形式交付软件。 -- 推荐
- [uDocker](https://indigo-dc.github.io/udocker/) - 用于在批处理或交互式系统中以非 root 权限执行简单 Docker 容器的基本用户工具 [Source Code](https://github.com/indigo-dc/udocker) Apache-2.0。
- [Shifter](https://www.nersc.gov/research-and-development/user-defined-images/) - Shifter 是用于 HPC 的 Linux 容器 [Source Code](https://github.com/NERSC/shifter) 其他。
- [HPC Container Maker](https://github.com/NVIDIA/hpc-container-maker)  - HPC 容器生成器是英伟达的开源工具，用于更轻松地生成容器规范文件。 Apache-2.0.
- [Scarus](https://github.com/eth-cscs/sarus) - 适用于 HPC 的 OCI 兼容容器引擎（BSD）。
- [Singularity HPC](https://singularity-hpc.readthedocs.io) - Singularity 注册表 HPC（shpc）允许您将容器作为模块进行安装。 [Source Code](https://github.com/singularityhub/singularity-hpc) MPL 2.0。

## 环境管理

- [Lmod](https://lmod.readthedocs.io/en/latest/) - Lmod：基于 Lua 的环境模块系统，支持读取 TCL 模块，并支持软件层次结构（源代码）其他。
- 环境模块 - 环境模块：提供对用户环境的动态修改 [Source Code](https://github.com/TACC/Lmod) GPL-2。
- [Anaconda](https://www.anaconda.com/) - Anaconda 是用于计算科学的 Python 和 R 发行版。 -- 推荐
- [Mamba](https://mamba.readthedocs.io/en/latest/) - Mamba 是用 C++ 重新实现的 conda 包管理器（源代码）BSD。 -- 推荐

## 可视化

- [Visit](https://visit-dav.github.io/visit-website/) - VisIt - 基于网格的科学数据可视化和数据分析  [Source Code](https://github.com/visit-dav/visit) BSD-3。
- [Paraview](https://www.paraview.org/) - ParaView 是一个基于可视化工具包（VTK）的开源、多平台数据分析和可视化应用程序 [Source Code](https://github.com/Kitware/ParaView) BSD-3 -- 推荐。

## 并行文件系统

- [GPFS](https://www.ibm.com/docs/en/gpfs/4.1.0.4?topic=guide-introducing-general-parallel-file-system) - GPFS 是由 IBM 开发的专有高性能集群文件系统软件。
- [Quobyte](https://www.quobyte.com/storage-for/high-performance-computing-hpc?gclid=EAIaIQobChMI-fv1pfKG8wIV5x6tBh367Q5CEAAYASABEgJTgPD_BwE) - 高性能文件系统（专有）。
- [Ceph](https://ceph.io/en/) - Ceph 是一个分布式对象、块和文件存储平台 [Source Code](https://github.com/ceph/ceph) 其他。 -- 推荐
- [Weka](https://www.weka.io/) - 专为 HPC 设计的文件系统（专有）。
- [Lustre/Exascaler](https://www.lustre.org/) - Lustre 是一个开源的分布式并行文件系统软件平台，设计用于可扩展性、高性能和高可用性 [Source Code](https://git.whamcloud.com/fs/lustre-release.git) 其他。
- [BeeGFS](https://www.beegfs.io/c/) - BeeGFS 是一个硬件独立的 POSIX 并行文件系统，专注于性能，设计用于易于使用、简单安装和管理专有。
- [OrangeFS](http://www.orangefs.org/) - OrangeFS 是一款专为 Linux 集群设计的下一代并行文件系统  [Source Code](https://github.com/waltligon/orangefs) 其他。
- [MooseFS](https://moosefs.com/) - Moose 文件系统是一个开源的、符合 POSIX 标准的分布式文件系统，由 Core Technology 开发 [Source Code](https://github.com/moosefs/moosefs) GPL-2.0。

## 编程语言

- [Julia](https://julialang.org/ - Julia 是一种用于技术计算的高级、高性能动态语言，由 MIT 开发。
- [Futhark](https://futhark-lang.org/) - Futhark 是一种纯函数式数据并行编程语言，属于 ML 语言家族 isc。
- [Chapel](https://chapel-lang.org/) - Chapel 是一种专为大规模高效并行计算设计的编程语言，采用 Apache-2.0 许可证。

## 监控

### 基于 Prometheus

- [Slurm Exporter](https://github.com/treydock/prometheus-slurm-exporter) - 用于从 Slurm 收集性能指标的 Prometheus 导出器，采用 GPL-3.0 许可证。
- [Slurm Exporter](https://github.com/ubccr/slurm-exporter) - 通过 Rest API 实现的 Prometheus 导出器，采用 GPL-3.0 许可证。
- [Infiniband Exporter](https://github.com/treydock/infiniband_exporter) - InfiniBand 导出器从 InfiniBand 交换机和 HCA 收集计数器 Apache-2.0。
- [Cgroup Exporter](https://github.com/treydock/cgroup_exporter) - Produces metrics from cgroups `Apache-2.0`.
- [Cgroup Exporter](https://github.com/phpHavok/cgroups_exporter) - 从 cgroups 生成指标 Apache-2.0。
- [GPFS Exporter](https://github.com/treydock/gpfs_exporter) - GPFS 导出器从 GPFS 文件系统收集指标 Apache-2.0。
- [Lustre Exporter](https://github.com/GSI-HPC/lustre_exporter) - 用于 Lustre 并行文件系统的 Prometheus 导出器 GPL-3.0。
- [DCGM Exporter](https://github.com/NVIDIA/dcgm-exporter) - 基于 DCGM 的 NVIDIA GPU 指标 Prometheus 导出器 Apache-2.0。  -- 推荐

## 期刊

- [Journal of Super Computing](https://www.springer.com/journal/11227) - 一本关于高性能计算机设计、分析和应用的国际期刊。

## 播客

- [This week in HPC](https://www.intersect360.com/media/podcasts/) - 每周，Intersect360 Research 首席执行官 Addison Snell 和 HPCwire 编辑 Tiffany Trader 解析当周最重要的 HPC 新闻。
- [Exascaler Project](https://www.exascaleproject.org/podcast/) - ECP 的《Let's Talk Exascale》播客深入幕后，与推动能力强且可持续的 exascale 计算生态系统落地的人士对话。
- [@HPCpodcast](https://insidehpc.com/category/resources/hpc-podcast/) - 跟随Shahin Khan和Doug Black，探讨超级计算技术及其塑造的应用、市场和政策。

## 博客

- [HPCWire](https://www.hpcwire.com/) - 自1987年以来，一直报道世界上最快的计算机及其运营者。
- [InsideHPC](https://insidehpc.com/) - InsideHPC 是一份全球性出版物，以全面且富有洞见的报道著称，专注于 HPC-AI 社区，连接供应商、终端用户和 HPC 战略家。
- [The Next Platform](https://www.nextplatform.com/category/hpc/) - 提供对大型企业、超级计算中心、超大规模数据中心和公共云中高端计算的深度报道。
- [The Register HPC](http://www.theregister.co.uk/data_centre/hpc/) - The Register 是全球领先且值得信赖的在线企业技术新闻出版物，全球读者约4000万。
- [HPC at Dell](http://hpcatdell.com) - Dell 提供的高性能计算知识库文章。

## 会议

- [Pearc](https://pearc.acm.org/) - 先进研究计算的实践与经验。
- [Supercomputing (SC)](https://supercomputing.org/) - 国际高性能计算、网络、存储与分析大会。
- [Supercomputing International (ISC)](https://www.isc-hpc.com/)——国际高性能计算、网络、存储与分析会议。
- [CCGrid](https://dl.acm.org/conference/ccgrid)——IEEE/ACM国际集群、云与互联网计算研讨会。
- [IEEE-HPEC](https://ieee-hpec.org/)——IEEE高性能嵌入式计算会议。
- [Hot Chips](https://hotchips.org——半导体行业领先的高性能微处理器及相关电路会议。
- [Hot Interconnects](https://hoti.org) - IEEE关于所有规模互联网络的软件架构与实现的会议。
- [ESSA](https://sites.google.com/view/essa-2024/) - 极端规模存储与分析研讨会。
- [IEEE-IPDPS](https://www.ipdps.org/) - IEEE国际并行与分布式处理研讨会。
- [ESPM2 Workshop](http://nowlab.cse.ohio-state.edu/espm2/) - 极端规模编程模型与中间件国际研讨会。
- [LCI Workshops](https://linuxclustersinstitute.org/workshops/) - Linux集群研究所（LCI）为全球高性能计算社区提供集群部署与应用的教育及高级技术培训。
- [HPC Carpentry](https://www.hpc-carpentry.org/) - 教授高性能计算基础技能。

## 网站

- [Top500](https://top500.org) - TOP500项目对全球500台最强大的非分布式计算机系统进行排名并详细介绍。

## 用户组

- [MVAPICH](https://mug.mvapich.cse.ohio-state.edu/) - MUG会议为所有与会者（用户、系统管理员、研究人员、工程师和学生）提供一个开放论坛，讨论并分享使用MVAPICH库的知识。
- [Slurm](https://slurm.schedmd.com/slurm_ug_agenda.html) - 年度Slurm用户组会议。


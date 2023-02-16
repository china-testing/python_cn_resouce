精心策划的平台、工具、实践和资源清单，用于创建、改善组织中的DevOps文化和SRE团队。

DevOps是文化理念、实践和工具的结合，它提高了组织高速交付应用程序和服务的能力：与使用传统软件开发和基础设施管理流程的组织相比，以更快的速度发展和改进产品。这种速度使组织能够更好地服务于他们的客户并在市场上更有效地竞争。

## ＃＃内容

- [云平台](#cloud-platforms)
- 开源云平台](#open-source-cloud-platforms)
- [操作系统](#operating-systems)
- 分布式文件系统](#distributed-filesystems)
- [应用平台](#应用平台)
- 容器镜像注册](#container-image-registry)
- 自动化和协调](#自动化--协调)(#automation--orchestration)
- [持续集成与交付](#持续集成--交付)
- 源代码管理](#源代码管理)
- [网络服务器](#web-servers)
- [SSL](#ssl)
- [数据库](#databases)
- [可观察性和监控](#可观察性--监控)
- [服务发现和服务网](#服务发现--服务网)
- 混沌工程](#chaos-engineering)
- [API网关](#api-gateway)
- [代码审查](#code-review)
- [分布式信息传递](#distributed-messaging)
- [编程语言](#programming-languages)
- [聊天和ChatOps](#聊天和Chatops)
- [秘密管理](#secret-management)
- [共享](#sharing)
- [VPN](#vpn)
- [资源](#resources)
  - [书籍](#书籍)
  - [会议](#会议)
  - [DevOps 路线图](#devops-roadmap)

---

##云平台

*公有云和私有云平台*。

- [亚马逊网络服务（AWS）](https://aws.amazon.com/) - 云计算服务。
- [Google Cloud Platform (GCP)](https://cloud.google.com/) - 云计算服务。
- [Azure](https://azure.microsoft.com/) - 云计算平台和服务。
- [Alibaba Cloud](https://us.alibabacloud.com/) - 云产品和服务的综合套件。
- [Oracle Cloud](https://www.oracle.com/cloud/) - 全面和完全集成的云应用和平台服务堆栈。
- [DigitalOcean](https://www.digitalocean.com/) - 帮助开发人员轻松构建、测试、管理和扩展任何规模的应用程序。
- [Scaleway](https://www.scaleway.com/) - 在云中创建、部署和扩展基础设施的单一方式。
- [Vultr](https://www.vultr.com/) - 在全球范围内轻松地部署云服务器、裸机和存储。
- [VMware Cloud](https://cloud.vmware.com/) - 在任何云上运行、管理、连接和保护您的所有应用程序。
- [IBM Cloud](https://www.ibm.com/cloud) - 工具、数据和API，使人工智能成为现实。
- [Stackpath](https://www.stackpath.com/) - 在云的边缘建立的计算基础设施和服务平台。
- [Linode](https://www.linode.com/) - 加快云计算的创新，虚拟计算必须更容易获得，更实惠，更简单。
- [Kinsta](https://kinsta.com/application-hosting/) - 在几分钟内创建和部署网络应用和数据库。

## 开源云平台

*私人、公共和混合开源云平台。

- [Openstack](https://www.openstack.org/) - 用于创建私有云和公共云的开源软件。
- [Apache CloudStack](https://cloudstack.apache.org/) - 设计用于部署和管理大型虚拟机网络。
- [OpenNebula](https://opennebula.org/) - 基于KVM、LXD和VMware建立私有云并管理数据中心的虚拟化。
- [Eucalyptus](https://www.eucalyptus.cloud/) - 建立兼容AWS的私有云和混合云。
- [DC/OS](https://dcos.io/) - 基于Apache Mesos分布式系统内核的分布式操作系统。
- [Apache Mesos](http://mesos.apache.org/) - 针对你的数据中心编程，就像它是单一的资源池。
- [Localstack](https://github.com/localstack/localstack) - 全功能的本地AWS云堆栈。在离线状态下开发和测试你的云和无服务器应用程序。

##操作系统

*操作系统--服务器平台。

- [Ubuntu](https://ubuntu.com/) - 企业开源和Linux。
- [Rocky Linux](https://rockylinux.org/) - 开源企业操作系统，旨在与Red Hat Enterprise Linux实现100%的错误兼容。
- [CoreOS](http://coreos.com/) - 首创的轻型容器主机。
- [OSv](http://osv.io/) - 多功能的模块化单内核，设计用于在云中的微型虚拟机上安全地运行未经修改的Linux应用程序。
- [Atomic](http://www.projectatomic.io/) - 使用不可变的基础设施来部署和扩展你的容器化应用。
- [Photon](https://github.com/vmware/photon) - 为云原生应用、云平台和VMware基础设施优化的Linux容器主机。

##分布式文件系统

*网络分布式文件系统。

- [Ceph](https://ceph.io/en/) - 在完整的系统下，高度可扩展的基于对象、块和文件的存储。
- [Gluster](https://www.gluster.org/) - 免费和开放源码软件的可扩展网络文件系统。
- [LINBIT](https://www.linbit.com/en/) - 为数据中心规模的环境创建、删除和复制块存储设备。
- [XtreemFS](http://www.xtreemfs.org/) - 容错的分布式文件系统，满足所有存储需求。
- [min.io](https://min.io/) - 高性能、分布式对象存储系统。

##应用平台

*应用管理平台、容器平台和容器管理。

- [Openshift](https://www.openshift.com/) - 大创意的Kubernetes平台。
- [Dokku](https://dokku.com/) - 帮助你建立和管理应用程序的生命周期。
- [Flynn](https://flynn.io/) - 用于在生产中运行应用程序的开源平台（PaaS）。
- [Docker](https://www.docker.com/) - 通过使用容器创建、部署和运行应用程序。
- [Docker Compose](https://github.com/docker/compose) - 用Docker定义和运行多容器应用程序。
- [Docker Swarm](https://github.com/docker/swarm) - Docker原生集群系统。
- [Kubernetes](https://kubernetes.io/) - 容器化应用的自动部署、扩展和管理。
- [LXC](https://linuxcontainers.org/) - 让Linux用户轻松创建和管理系统或应用容器。
- [Rancher](https://rancher.com/) - 让你提供Kubernetes-as-a-Service。
- [OpenVz](https://openvz.org/) - 基于容器的Linux虚拟化。
- [Singularity](https://sylabs.io/singularity/) - 从本地环境到云端运行应用程序。
- [AppScale](https://github.com/AppScale/appscale) - 易于管理的无服务器平台，用于构建和运行可扩展的Web和移动应用程序。
- [Kata Containers](https://katacontainers.io/) - 构建可无缝插入容器生态系统的轻量级虚拟机。
- [K3S](https://k3s.io/) - 为物联网和边缘计算构建的认证Kubernetes发行版。
- [Podman](https://github.com/containers/podman) - 用于管理OCI容器和pod的工具。
- [Linx](https://linx.software) - 用于构建和托管后端解决方案的通用低代码平台。

## 容器镜像注册表

*Container Image registry.*

- [Quay](https://www.projectquay.io/) - 容器镜像注册表，使你能够建立、组织、分发和部署容器。
- [Dockyard](https://github.com/Huawei/dockyard) - 容器和构件库。
- [Harbor](https://goharbor.io/) - 开源的可信的云原生注册表项目，可以存储、签署和扫描内容。

## 自动化和协调

*用于自动化、协调、部署、供应和配置管理的工具*。

- [Ansible](https://www.ansible.com/) - 简单的IT自动化平台，使你的应用程序和系统更容易部署。
- [Salt](https://www.saltstack.com/) - 自动管理和配置任何规模的基础设施或应用程序。
- [Puppet](https://puppet.com/) - 无与伦比的基础设施自动化和交付。
- [Chef](https://www.chef.io/) - 基础设施和应用程序的自动化。
- [Juju](https://jaas.ai/) - 简化您配置、扩展和操作当今复杂软件的方式。
- [Rundeck](https://www.rundeck.com/) - 现代化运营的运行手册自动化。
- [StackStorm](https://stackstorm.com/) - 连接你所有的应用程序、服务和工作流程。以你的方式实现DevOps自动化。
- [Bosh](https://www.cloudfoundry.org/bosh/) - 复杂分布式系统的发布工程、部署和生命周期管理。
- [Cloudify](https://cloudify.co/) - 从核心到边缘的连接、控制和自动化：无限的地点、云和设备。
- [Tsuru](https://tsuru.io/) - 一个可扩展的、开源的平台即服务软件。
- [Fabric](http://www.fabfile.org/) - 高级别的Python库，旨在通过SSH远程执行shell命令。
- [Capistrano](https://capistranorb.com/) - 远程服务器自动化和部署工具。
- [Mina](http://nadarei.co/mina/) - 真正快速的部署器和服务器自动化工具。
- [Terraform](https://www.terraform.io/) - 使用基础设施即代码来配置和管理任何云、基础设施或服务。
- [Pulumi](https://www.pulumi.com/) - 现代基础设施即代码平台，允许你使用熟悉的编程语言和工具来构建、部署和管理云基础设施。
- [Packer](https://www.packer.io/) - 建立自动化的机器映像。
- [Vagrant](https://www.vagrantup.com/) - 开发环境变得简单。
- [Foreman](https://theforeman.org/) - 物理和虚拟服务器的完整生命周期管理工具。
- [Nomad](https://learn.hashicorp.com/nomad) - 部署和管理任何容器化、传统或批量应用程序。
- [Marathon](https://mesosphere.github.io/marathon/) - 用于DC/OS和Apache Mesos的生产级容器编排平台。
- [OctoDNS](https://github.com/github/octodns) - 跨多个供应商管理DNS。DNS作为代码。
- [ManageIQ](https://www.manageiq.org/) - 从单一平台管理容器、虚拟机、网络和存储。
- [Ignite](https://github.com/weaveworks/ignite) - 具有容器用户体验和内置GitOps管理的开源虚拟机（VM）管理器。
- [Spacelift](https://spacelift.io/) - 用于IaC开发的灵活协调解决方案。
- [Atlantis](https://www.runatlantis.io/) - Terraform Pull Request Automation
- [KubeVela](https://kubevela.io/) - 现代应用交付平台，使在当今的混合、多云环境中部署和运行应用更容易、更快、更可靠。
- [Stacktape](https://stacktape.com) - 建立在AWS之上的开发者友好型基础设施即代码框架。
- [Score](https://score.dev) - 以开发人员为中心、与平台无关的开源工作负载规范。

## 持续集成与交付

*持续集成、持续交付和持续交付。GitOps.*

- 在场所
  - [Buildbot](http://buildbot.net/) - 自动化软件开发周期的所有方面。
  - [Gitlab CI](https://about.gitlab.com/product/continuous-integration/) - 管道构建、测试、部署和监控你的代码，作为单一、集成工作流程的一部分。
  - [Jenkins](http://jenkins-ci.org/) - 用于构建、部署和自动化任何项目的自动化服务器。
  - [Drone](https://github.com/drone/drone) - 容器-原生的持续交付平台。
  - [Concourse](https://concourse-ci.org/) - 基于管道的持续做事器。
  - [Spinnaker](https://www.spinnaker.io/) - 为每个企业提供快速、安全、可重复的部署。
  - [goCD](https://www.gocd.org/) - 交付和发布自动化服务器。
  - [Teamcity](https://www.jetbrains.com/teamcity/) - 企业级CI和CD。
  - [Bamboo](https://www.atlassian.com/software/bamboo) - 将自动构建、测试和发布结合在一个工作流程中。
  - [Integrity](http://integrity.github.io/) - 持续集成服务器。
  - [Zuul](https://zuul-ci.org/) - 驱动持续集成、交付和部署系统，专注于项目门控。
  - [Argo](https://argoproj.github.io/) - 开源Kubernetes原生工作流、事件、CI和CD。
  - [Strider](https://strider-cd.github.io/) - 持续部署/持续集成平台。
  - [Evergreen](https://github.com/evergreen-ci/evergreen) - 来自MongoDB的分布式持续集成系统。
  - [werf](https://werf.io/) - 开源CI/CD工具，用于构建Docker镜像并使用GitOps方法将其部署到Kubernetes。
  - [Flux](https://github.com/fluxcd/flux) - 自动确保你的Kubernetes集群的状态与你在Git中提供的配置一致。
  - [Flagger](https://github.com/weaveworks/flagger) - 逐步交付的Kubernetes运营商（金丝雀、A/B测试和蓝色/绿色部署）。
  - [Tekton](https://tekton.dev/) - 用于创建CI/CD系统的强大而灵活的开源框架。
  - [PipeCD](https://pipecd.dev/) - 用于声明式Kubernetes、无服务器和基础设施应用的持续交付。
  - [Gitploy](https://www.gitploy.io/) - 在几分钟内围绕GitHub建立部署系统。
- 公共服务
  - [Travis CI](https://travis-ci.org/) - 轻松同步你的项目，你将在几分钟内测试你的代码。
  - [Circle CI](https://circleci.com/) - 强大的CI/CD管线，让代码不断前进。
  - [Bitrise](https://www.bitrise.io/) - 用于移动应用程序的CI/CD。
  - [Buildkite](https://buildkite.com/) - 在你自己的基础设施上运行快速、安全和可扩展的持续集成管道。
  - [Cirrus CI](https://cirrus-ci.org/) - 为云计算时代建立的持续集成系统。
  - [Codefresh](https://codefresh.io/) - Kubernetes应用程序的GitOps自动化平台。
  - [Github actions](https://github.com/features/actions) - GitHub Actions使你的所有软件工作流程轻松实现自动化，现在又有了世界级的CI/CD。
  - [Kraken CI](https://kraken.ci/) - 现代CI/CD，开源，内部系统，高度可扩展，专注于测试。
  - [Earthly](https://earthly.dev/) - 在本地开发CI/CD管道，并在任何地方运行它们。

## 源代码管理

*源代码管理，Git-repository管理器，版本控制。其中一些包含在代码审查部分*。

- [GitHub](https://github.com/) - 帮助开发人员存储和管理他们的代码，以及跟踪和控制对他们的代码的修改。
- [Gitlab](https://gitlab.com/) - 整个DevOps生命周期在一个应用程序中。
- [Bitbucket](https://bitbucket.org/product/) - 为团队提供了一个规划项目、协作编写代码、测试和部署的地方。
- [Phabricator](https://github.com/phacility/phabricator/) - 一个帮助软件公司建立更好的软件的网络应用程序集合。
- [Gogs](https://gogs.io/) - 无痛的自我托管的Git服务。
- [Gitea](https://gitea.io/) - 无痛的自我托管的Git服务。
- [Gitblit](https://github.com/gitblit/gitblit) - 用于管理、查看和服务Git存储库的纯Java Git解决方案。

## 网络服务器

*网络服务器和反向代理*。

- [Nginx](http://nginx.org/) - 高性能的负载平衡器、网络服务器和反向代理。
- [Apache](http://httpd.apache.org/) - 网络服务器和反向代理。
- [Caddy](https://caddyserver.com/) - 带有自动HTTPS的Web服务器。
- [Cherokee](http://cherokee-project.com/) - 高并发的安全网络应用。
- [Lighttpd](http://www.lighttpd.net/) - 为速度关键型环境进行了优化，同时保持符合标准、安全和灵活。
- [Uwsgi](https://github.com/unbit/uwsgi/) - 应用服务器容器。

## SSL

*用于自动管理SSL证书的工具。

- [Certbot](https://github.com/certbot/certbot) - 在人工管理的网站上自动使用Let's Encrypt证书以启用HTTPS。
- [Let's Encrypt](https://letsencrypt.org/) - 免费、自动、开放的证书颁发机构。
- [Cert Manager](https://github.com/jetstack/cert-manager) - K8S插件，可自动管理和签发来自不同签发源的TLS证书。

## 数据库

*关系型（SQL）和非关系型（NoSQL）数据库*。

- 关系型(SQL)
  - [PostgreSQL](https://www.postgresql.org/) - 强大的、开放源码的对象关系型数据库系统。
  - [MySQL](https://www.mysql.com/) - 开源的关系型数据库管理系统。
  - [MariaDB](https://mariadb.org/) - 快速、可扩展和强大，拥有丰富的存储引擎、插件和许多其他工具的生态系统。
  - [SQLite](https://sqlite.org/) - 小型、快速、独立、高可靠性、功能齐全的SQL数据库引擎。
- 非关系型(NoSQL)
  - [Cassandra](http://cassandra.apache.org/) - 管理海量数据，速度快。
  - [Apache HBase](http://hbase.apache.org/) - 分布式、版本化、非关系型数据库。
  - [Couchdb](https://couchdb.apache.org/) - 完全拥抱网络的数据库。
  - [Elasticsearch](https://www.elastic.co/products/elasticsearch) - 分布式、RESTful搜索和分析引擎，能够解决越来越多的用例。
  - [MongoDB](https://www.mongodb.com/) - 通用的、基于文档的、为现代应用而建立的分布式数据库。
  - [Rethinkdb](https://github.com/rethinkdb/rethinkdb) - 用于实时网络的开源数据库。
  - 关键值
    - [Couchbase](https://www.couchbase.com/) - 分布式多模型NoSQL面向文档的数据库，为交互式应用而优化。
    - [Leveldb](https://github.com/google/leveldb) - 快速键值存储库。
    - [Redis](https://redis.io/) - 内存数据结构存储，作为数据库、缓存和消息代理使用。
    - [RocksDB](https://rocksdb.org/) - 提供可嵌入的、持久的键值存储的库，用于快速存储。
    - [Etcd](https://github.com/etcd-io/etcd) - 分布式可靠的键值存储，用于分布式系统的最关键数据。

## 可观察性和监控

*可观察性、监控、指标/度量衡收集和警报工具。

- [Sensu](https://sensu.io/) - 简单。可扩展的。多云监控。
- [Alerta](https://github.com/alerta/alerta) - 可扩展、最低配置和可视化的监控系统。
- [Cabot](https://github.com/arachnys/cabot) - 自我托管的、易于部署的监控和警报服务。
- [Amon](https://github.com/amonapp/amon) - 现代服务器监控平台。
- [Flapjack](https://flapjack.io/) - 监控通知路由+事件处理系统。
- [Icinga](https://icinga.com/) - 监视可用性和性能，让你简单地访问相关数据并提出警报。
- [Monit](https://mmonit.com/monit/#home) - 管理和监控Unix系统。
- [Naemon](http://www.naemon.org/) - 快速、稳定和创新，同时让你清楚地看到你的网络和应用程序的状态。
- [Nagios](https://www.nagios.org/) - 监控系统、网络和基础设施的计算机软件应用。
- [Sentry](https://sentry.io/welcome/) - 错误监控，帮助所有软件团队实时发现、分流和优先处理错误。
- [Shinken](http://www.shinken-monitoring.org/) - 监控框架。
- [Zabbix](https://www.zabbix.com/) - 用于网络监控和应用监控的成熟和毫不费力的监控解决方案。
- [Glances](https://github.com/nicolargo/glances) - 通过curses或基于Web的界面监测信息。
- [Healthchecks](https://github.com/healthchecks/healthchecks) - Cron监控工具。
- [Bolo](http://bolo.niftylogic.com/) - 建立分布式、可扩展的监控系统。
- [cAdvisor](https://github.com/google/cadvisor) - 分析运行中的容器的资源使用和性能特征。
- [ElastiFlow](https://github.com/robcowart/elastiflow) - 使用Elastic Stack进行网络流量监控（Netflow、sFlow和IPFIX）。
- [Co-Pilot](https://pcp.io/) - 系统性能分析工具包。
- 衡量标准/指标收集
  - [Thundra Foresight](https://www.thundra.io/foresight) - 通过迅速发现测试失败来了解CI管道。
  - [Prometheus](https://prometheus.io/) - 利用领先的开源监控解决方案为您的指标和警报提供动力。
  - [Collectd](https://github.com/collectd/collectd) - 系统统计收集守护程序。
  - [Facette](https://github.com/facette/facette) - 时间序列数据可视化软件。
  - [Grafana](https://grafana.com/) - 每个数据库的分析和监控解决方案。
  - [Graphite](https://graphite.readthedocs.io/en/latest/) - 存储数字时间序列数据，并根据需要呈现这些数据的图形。
  - [Influxdata](https://www.influxdata.com/) - 时间序列数据库。
  - [Netdata](https://www.netdata.cloud/) - 即时诊断你的基础设施中的减速和异常情况。
  - [Freeboard](https://github.com/Freeboard/freeboard) - 用于物联网和其他网络混搭的实时仪表板构建器。
- 日志管理
  - [Anthracite](https://github.com/Dieterbe/anthracite) - 一个事件/变化记录/管理应用程序。
  - [Graylog](https://github.com/Graylog2/graylog2-server) - 免费和开源的日志管理。
  - [Logstash](https://www.elastic.co/products/logstash#) - 收集、解析、转换日志。
  - [Fluentd](https://www.fluentd.org/) - 统一日志层的数据收集器。
  - [Flume](https://flume.apache.org/) - 分布式的、可靠的、可用的服务，用于有效收集、聚合和移动日志。
  - [Heka](https://hekad.readthedocs.io/en/latest/#) - 流处理软件系统。
  - [Kibana](https://www.elastic.co/products/kibana) - 探索、可视化、发现数据。
  - [Loki](https://github.com/grafana/loki) - 横向可扩展、高可用、多租户的日志聚合系统，灵感来自Prometheus。
- 状态
  - [Cachet](https://github.com/CachetHQ/Cachet) - 美丽而强大的开源状态页面系统。
  - [StatusPal](https://statuspal.io/?utm_source=github.com&utm_medium=referral&utm_campaign=awesome-devops) - 通过一个漂亮的托管状态页面有效地沟通事件和维护。

##服务发现与服务网

*服务发现、服务网和故障检测工具。

- [Consul](https://www.hashicorp.com/products/consul/) - 连接和保护任何服务。
- [Serf](https://www.serf.io/) - 分散的集群成员、故障检测和协调。
- [Doozerd](https://github.com/ha/doozerd) - 一致的分布式数据存储。
- [Zookeeper](http://zookeeper.apache.org/) - 用于配置、命名、提供分布式同步等的集中式服务。
- [Etcd](https://etcd.io/) - 分布式的、可靠的键值存储，用于分布式系统中最关键的数据。
- [Istio](https://istio.io/) - 连接、安全、控制和观察服务。
- [Kong](https://konghq.com/) - 为微服务、服务网和云本地部署提供所需的性能。
- [Linkerd](https://github.com/linkerd/linkerd2) - 用于Kubernetes及更多的服务网状结构。

## 混沌工程

*在分布式系统上进行实验的学科，以便对系统在生产中承受动荡条件的能力建立信心。

- [Chaos Toolkit](https://github.com/chaostoolkit) - 混沌工程的开源平台。
- [Chaos Monkey](https://github.com/Netflix/chaosmonkey) - 帮助应用程序容忍随机实例故障的弹性工具。
- [Toxiproxy](https://github.com/Shopify/toxiproxy) - 模拟网络和系统条件，进行混沌和弹性测试。
- [Pumba](https://github.com/alexei-led/pumba) - 容器的混沌测试、网络仿真和压力测试工具。
- [Chaos Mesh](https://github.com/chaos-mesh/chaos-mesh) - Kubernetes的混沌工程平台。
- [Litmus](https://github.com/litmuschaos/litmus) - Litmus使团队能够识别基础设施的弱点。

## API网关

*API网关、服务代理和服务管理工具。

- [API Umbrella](https://github.com/NREL/api-umbrella) - 坐落在你的API前面的代理，API管理平台。
- [Ambassador](https://www.getambassador.io/) - 建立在Envoy代理上的Kubernetes-Native API网关。
- [Kong](https://konghq.com/) - 用业界最高效、可扩展和灵活的API平台连接你的所有微服务和API。
- [Tyk](https://tyk.io/) - API和服务管理平台。
- [Cilium](https://github.com/cilium/cilium) - 使用BPF和XDP的API感知网络和安全。
- [Gloo](https://github.com/solo-io/gloo) - 功能丰富的Kubernetes原生入口控制器，以及下一代API网关。
- [Envoy](https://www.envoyproxy.io/) - 云原生高性能边缘/中间/服务代理。
- [Traefik](https://traefik.io/) - 面向HTTP和基于TCP的应用的反向代理和负载平衡器。

##代码审查

*代码审查。一些源代码管理工具有内置的代码审查功能*。

- [Gerrit](https://www.gerritcodereview.com/) - 基于网络的团队代码协作工具。
- [Review Board](https://www.reviewboard.org/) - 基于网络的协作式代码审查工具。

## 分布式消息传递

*分布式消息传递平台和队列软件。

- [Rabbitmq](https://www.rabbitmq.com/) - 消息代理。
- [Kafka](http://kafka.apache.org/) - 建立实时数据管道和流媒体应用程序。
- [Activemq](http://activemq.apache.org/) - 多协议消息传递。
- [Beanstalkd](https://beanstalkd.github.io/) - 简单、快速的工作队列。
- [NSQ](https://nsq.io/) - 实时分布式消息传递平台。
- [Celery](http://www.celeryproject.org/) - 基于分布式消息传递的异步任务队列/工作队列。
- [Faktory](https://github.com/contribsys/faktory) - 应用程序中后台工作的存储库。
- [Nats](https://nats.io/) - 简单、安全、高性能的开源消息传递系统。
- [RestMQ](http://restmq.com/) - 使用HTTP作为传输的消息队列。
- [Dkron](https://github.com/distribworks/dkron) - 分布式、容错的工作调度系统。
- [KubeMQ](https://kubemq.io/) - Kubernetes原生的消息传递平台。

## 编程语言

*编程语言。

- [Python](https://www.python.org/) - 编程语言，让你快速工作，更有效地整合系统。运维首选语言。
- [Go](https://golang.org/) - 开放源码的编程语言，可以轻松构建简单、可靠、高效的软件。
- shell

## 聊天和ChatOps

*Chat and ChatOps.*

- [Rocket](https://rocket.chat/) - 开源的团队交流。
- [Mattermost](https://mattermost.com/) - 实现安全团队协作的消息平台。
- [Zulip](https://zulipchat.com/) - 具有电子邮件线程模型的实时聊天。
- [Riot](https://about.riot.im/) - 一个完全由你控制的通用安全聊天应用程序。
- ChatOps。
  - [CloudBot](https://github.com/CloudBotIRC/CloudBot) - 简单、快速、可扩展、开源的Python IRC Bot。
  - [Hubot](https://hubot.github.com/) - 可定制的机器人。

## 秘密管理

*安全即代码，敏感的凭证和秘密需要使用自动化来管理、安全、维护和轮换。

- [Sops](https://github.com/mozilla/sops) - 用于管理秘密的简单而灵活的工具。
- [Vault](https://www.hashicorp.com/products/vault/) - 管理秘密和保护敏感数据。
- [Keybase](https://keybase.io/) - 端到端加密聊天和云存储系统。
- [Vault Secrets Operator](https://github.com/ricoberger/vault-secrets-operator) - 从Vault创建Kubernetes秘密，以实现基于GitOps的安全工作流程。
- [Git Secret](https://github.com/sobolevn/git-secret) - 在git仓库内存储你的私人数据的bash工具。

##分享

*一个帮助分享知识和讲述故事的工具集*。

- [Gitbook](https://github.com/GitbookIO/gitbook) - 使用Git和Markdown的现代文档格式和工具链。
- [Docusaurus](https://github.com/facebook/docusaurus) - 易于维护的开源文档网站。
- [Docsify](https://github.com/docsifyjs/docsify/) - 一个神奇的文档网站生成器。
- [MkDocs](https://github.com/mkdocs/mkdocs/) - 使用Markdown的项目文档。

## VPN

*VPN，路由和防火墙。

- [OpenVPN](https://openvpn.net/) - 灵活的VPN解决方案，以确保你的数据通信，无论是互联网隐私。
- [Pritunl](https://pritunl.com/) - 企业分布式OpenVPN和IPsec服务器。
- [VyOS](https://vyos.io/) - 开源网络操作系统，可在各种硬件、虚拟机和云供应商上运行。
- [Algo](https://github.com/trailofbits/algo) - 在云中设置个人VPN。
- [Streisand](https://github.com/StreisandEffect/streisand) - 几乎自动设置新的VPN服务。
- [Freelan](https://github.com/freelan-developers/freelan) - 一个点对点的、安全的、易于设置的、多平台的、开源的、高度可配置的VPN软件。
- [Sshuttle](https://github.com/sshuttle/sshuttle) - 透明的代理服务器，可作为穷人的VPN使用。
- [SoftEther](https://www.softether.org/) - 一个开源的免费跨平台多协议VPN程序。
作为筑波大学的一个学术项目，采用Apache许可证2.0。
- [Firezone](https://www.firezone.dev/) - 使用WireGuard的自我托管的VPN服务器。支持MFA、SSO，并有简单的部署选项。

## 资源

### 书籍

*专注于DevOps、DevSecOps和网站可靠性工程的书籍*。

- [Effective DevOps: Building a Culture of Collaboration, Affinity, and Tooling at Scale](http://shop.oreilly.com/product/0636920039846.do)
- [Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation](https://www.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/)
- [Hands-On Security in DevOps](https://www.packtpub.com/networking-and-servers/hands-security-devops)
- [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/)
- [The Site Reliability Workbook](https://sre.google/workbook/table-of-contents/)
- [Building Secure & Reliable Systems](https://static.googleusercontent.com/media/sre.google/ro//static/pdf/building_secure_and_reliable_systems.pdf)
- [Infrastructure as Code: Managing Servers in the Cloud](http://shop.oreilly.com/product/0636920039297.do)
- [The DevOps Handbook](https://www.oreilly.com/library/view/the-devops-handbook/9781457191381/)

###会议

- [DevOpsCon](https://devopscon.io/)
- [AWS re:Invent](https://reinvent.awsevents.com/)
- [DevSecOps](https://www.devseccon.com/)
- [ADDO](https://www.alldaydevops.com/)
- [DevOpsConnect](https://www.devopsconnect.com/)
- [@Scale](https://atscaleconference.com/)
- [devopsdays](https://devopsdays.org/)
- [DevOps企业峰会](https://events.itrevolution.com/)

### DevOps 路线图

基本了解和成为*DevOps*工程师应该知道的内容，请查看路线图[这里](https://roadmap.sh/devops)。

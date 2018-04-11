## Viking

系统自动化运维平台    

![image](http://on7nqcxcq.bkt.clouddn.com/viking_v0.3_snapshot.png)

#### Pre Install
1. Python>=3.6
2. Mysql(mariaDB)>=5.6
3. Virturalenv==15
4. [Lib Dependencies](./docs/Dependencies.md) 

#### How To Run 

1. Bin Tools
```bash
## Run Local
bin/start_dev_server.sh

## Run Pro
bin/start_pro_server.sh
```

2. [Setup and Run on CentOS 7](docs/CentOS7_INSTALL.md)

#### Milestones 
1. [Milestone...](https://github.com/liujiaqiid/viking/milestone/2)

#### TODO
0. V0.3待优化点    
    + [x] storm python + vikings + ansible
    + [x] 屏蔽dnat配置，网站服务迁移至内网
    + [x] storm.juliye.net 配置
    + [x] viking.juliye.net 配置
    + [x] 服务器部署文档更新
    + [ ] cms python + vikings + ansible
    + [ ] 功能&优化
        + [ ] 部署任务 数据结构设计 | 持久化
        + [ ] 部署任务 动态设置功能
        + [ ] 部署记录 ＋ 部署历史日志 持久化
        + [ ] 版本回退功能
        + [ ] 部署日志 输出文本 格式化
        + [ ] 部署日志 控制隐藏控件
        + [ ] 部署操作过程中 提示 等待 || 实时输出日志    
    + 调研
        + [ ] 调研Ansible Python API
        + [ ] 调研[django_web_ansible](https://github.com/yianjiajia/django_web_ansible)
        + [ ] 调研[AnsibleUI2](https://github.com/alaxli/AnsibleUI2) 
        + [ ] 调研[ansibleUI](https://github.com/stanleylst/ansibleUI)
1. 工程优化
    1. [ ] Reusable App Package (pip)
    2. [ ] (Build Aliyun API)(docs/AliyunOpenAPI.md)    
    3. [ ] View Templates
        - bootstrap 
        - 确定模版UX方案
        - 4xx + 5xx
    4. [ ] Document Gen
        - 文档生成
    5. [ ] Cache Framwork (redis) 
    6. [ ] Authentication
    7. [ ] Logging
    8. [ ] Test | Coverage
    9. [ ] Pagination
    10. [ ] Security
    11. [ ] Performance and Optimize
    12. Internationalization and localization
2. 基于云服务的工作流 workflow
3. 自动化
4. 虚拟化

![image](http://on7nqcxcq.bkt.clouddn.com/vikings_1200_630.png?imageView2/2/w/100/h/100)

#### 相关文档
- [阿里云Open API](docs/AliyunOpenAPI.md)
- [自动化运维平台RoadMap_201712](https://www.processon.com/view/link/5a4dc1f7e4b0c4ee141986b0)
- [自动化运维平台RoadMap_201707](https://www.processon.com/view/link/5959c260e4b0c2773f83e423)
- [平台快照v0.1](http://on7nqcxcq.bkt.clouddn.com/vikings_v0.1_snapshot.png)

#### 模块功能

##### 分包优化
- 可以参考jumpserver的分包结构
- 顶层模块: 主入口,提供其他功能切入口
- 单个功能模块单独放入对应文件夹

#####  bin 
- 提供启动和停止脚本 

##### cmdb 
- 资产管理

#####  docs
- 文档

#####  locale 
- 国际化

#####  manage 
- web层

##### static
- 静态文件

#####  viking 
- 工程基本配置

##### wiki
- wiki 功能


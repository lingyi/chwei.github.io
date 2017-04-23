# Tars学习笔记(非官方文档)

	作者：ZR/859077290@qq.com
	创建：2017.04.23
	更新：2017.04.24
	特别说明：
		1. Server部分仅涉及C++部分。
		2. 仅个人学习笔记，并非官方文档。

- 介绍
	- [Tars方案介绍](tars_intro.md)
	- Tars源码组织和工程管理
	
- 编译
	- Tars编译规则（及缺点）
	- 第三方依赖准备
	- 基础服务编译
	- RPC框架编译
	- 应用模块Makefile调整（不依赖按照到系统目录）
	- 编译Web组件（tars.war）
	
- 部署
	- 初始化数据库（不含MySQL/MariaDB部署）
	- 基础服务模块
		- 优化：启停脚本统一为tars_svc.sh
		- 部署tars_RegistryServer
		- 部署tars_AdminRegistryServer
		- 部署tars_ConfigServer
		- 部署tars_PropertyServer
		- 部署tars_PatchServer
	- Web系统部署（启动resin服务）

- 深入：扩展
	- 扩展：Python支持（Client侧）
	- 扩展：Go支持（Client侧）

- 深入：源码走读
	- pendding


````
1135604098@qq.com
Jssvc@183311
````


https://www.universal-robots.com/articles/ur/interface-communication/overview-of-client-interfaces/



https://docs.universal-robots.com/tutorials/communication-protocol-tutorials/rtde-guide.html

https://gitlab.com/sdurobotics/ur_rtde

https://docs.universal-robots.com/Universal_Robots_ROS_Documentation/doc/ur_client_library/doc/installation.html


https://sdurobotics.gitlab.io/ur_rtde/api/api.html#rtde-control-interface-api



https://gitlab.com/sdurobotics/ur_rtde

[优傲机器人 RTDE C++ 接口](https://sdurobotics.gitlab.io/ur_rtde/index.html#)
[RTDE客户端库和示例](https://github.com/UniversalRobots/RTDE_Python_Client_Library)
[实时数据交换 （RTDE） 指南](https://docs.universal-robots.com/tutorials/communication-protocol-tutorials/rtde-guide.html)











### 一、UR机器人核心端口定义

| 端口号  | 官方名称                           | 核心功能                                                                 | 典型用途                                  |
|---------|------------------------------------|----------------------------------------------------------------------------------|-------------------------------------------|
| 22  | SSH                            | 远程登录机器人Linux系统，支持执行系统命令、查看运行日志、修改系统配置、故障排查等操作 | 机器人系统维护、日志分析、远程脚本执行    |
| 80  | HTTP                           | 提供机器人Web控制台入口，通过浏览器可访问并配置网络参数、更新固件、监控设备状态       | 可视化配置机器人、远程查看运行状态        |
| 102 | Profinet                       | 基于Profinet工业以太网协议，实现与PLC、传感器、驱动器等工业设备的实时数据交互       | 工业自动化系统集成（如PLC控制机器人运动）|
| 123 | NTP                            | 通过网络时间协议，同步机器人系统时钟与网络时间服务器，确保多设备时间一致性           | 多设备协同作业、日志时间对齐              |
| 502 | Modbus TCP                     | 支持读取机器人全面状态数据（关节角度、速度、电流、工具坐标等），可发送简单控制指令（如设置IO） | PLC读取机器人状态、外部系统控制基础IO      |
| **30001**| **Real-Time Data Output**          | 单向数据流端口，主动、实时发送机器人状态数据（关节位置、TCP位置、IO状态等），不接收任何指令 | 实时监控机器人关节角度、TCP坐标            |
| **30002**| **Primary Client Interface**       | 接收URScript控制指令并执行（如运动控制、IO操作），无指令执行结果返回，仅负责“执行”   | 下发纯控制指令（如控制机器人moveL运动、设置DO高电平）|
| **30003**| **Secondary Client Interface**     | 接收URScript指令并返回执行结果，支持指令验证（如查询IO状态、读取当前位置）           | 下发指令+结果验证（如检查DO端口状态、确认关节角度）|
| **30004**| **RTDE**                           | 高频率（通常>100Hz）实时数据交换接口，可预配置数据项（机器人状态+外部输入），适用于高精度实时控制场景 | 视觉引导定位、力控装配、高响应速度协同控制|
| 30005| FTP                            | 基于文件传输协议，支持将.urp机器人程序文件上传至机器人，或从机器人下载程序文件       | 批量部署机器人程序、备份关键运行程序      |
| 50001| Dashboard Server               | 远程管理机器人程序（启动/停止/加载/暂停/恢复），支持解锁保护停止，保障操作灵活性与安全性 | 自动化流程中远程控制程序运行、解除急停状态|








### 二、端口功能差异
- **30001与30004（实时数据类）**：两者均涉及实时数据输出，但30001是**单向数据发送**（仅机器人输出状态数据，不接收指令），频率约10Hz，专注于基础状态监控；30004则是**高频双向交互**（>100Hz），支持预配置数据项，可同时传输机器人状态与外部输入，适用于高精度实时控制场景。
  
- **30002与30003（指令控制类）**：两者均接收并执行URScript指令，但30002是**无反馈执行**（仅执行指令，不返回结果），适合简单直接的控制需求；30003是**带反馈交互**（执行指令后返回结果），支持指令验证，满足需要确认执行状态的场景。


### 三、场景化选择指南
- **仅需获取实时状态数据**（如监控关节角度、工具坐标）：选30001，其专注单向数据输出，满足基础监控需求。  
- **需控制机器人执行动作**（如运动、IO操作）且无需确认结果：选30002，适用于简单直接的指令执行场景。  
- **需控制机器人并验证执行结果**（如确认动作完成、查询IO状态）：选30003，支持指令反馈，确保操作准确性。  
- **需高频双向数据交换**（如视觉引导、力控装配）：选30004，凭借毫秒级响应速度，满足高精度实时控制需求。















### 1. 安装Miniconda




```bash
# 1. 下载Miniconda3
# x86_64架构（PC）：
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# rm64架构（RK3588/Jetson）：
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
```



```bash
# 3. 赋予安装脚本执行权限
chmod +x Miniconda3-latest-Linux-*.sh

# 4. 运行安装脚本
./Miniconda3-latest-Linux-*.sh
```

- **安装选项指引**：  
  1. 按 `Enter` 阅读协议 → 输入 `yes` 同意协议；  
  2. 默认安装路径 ` /home/ur/miniconda3`（直接按 `Enter` 确认，不建议修改）；  
  3. 最后输入 `yes` 初始化conda（关键！否则conda命令无法生效）。


### 2. 激活 conda 环境并接受服务条款

```bash
# 1. 刷新环境变量（使conda命令生效，必执行）
source ~/.bashrc

# 2. 验证conda安装（需输出conda版本号，如conda 24.5.0）
conda --version

# 3. 接受conda官方频道条款（创建环境前必做，否则报错）
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r


# 4. 创建名为「py310」的虚拟环境
conda create -n py310 python=3.10 -y

# 5. 激活环境
conda activate py310


```









### **步骤3：安装RTDE_Python_Client_Library最新版本**

```bash
# 安装最新版本（确保在激活的conda环境中执行）
pip install --upgrade pip
pip --version # 检查当前 pip 是否对应 py310
pip install ur_rtde==1.5.4 # 安装 ur_rtde 库
pip install git+https://github.com/UniversalRobots/RTDE_Python_Client_Library.git@main
git clone https://github.com/UniversalRobots/RTDE_Python_Client_Library
cd RTDE_Python_Client_Library/examples
```














#### **启动机器人模拟器（可选，无实体机器人时使用）**

```bash
# 在examples目录下运行数据记录脚本（连接本地模拟器）
python record.py --host localhost --frequency 10
```
若成功运行，会生成`robot_data.csv`文件，包含机器人实时数据，说明安装正常。







# UR机器人端口操作命令（按执行逻辑排序）

## 一、查看端口监听与进程信息（从整体到具体）
1. **查看所有监听的TCP/UDP端口**（无需root，快速了解端口开放情况）  
   `ss -tuln`

2. **查看所有端口及对应进程**（需root，获取进程级关联信息）  
   `sudo ss -tulnp`

3. **查看URControl进程占用的端口**（定位机器人核心进程端口）  
   `sudo ss -tulnp | grep URControl`

4. **查看特定端口（如30002）的进程信息**（针对性排查目标端口）  
   `sudo ss -tulnp | grep 30002`


## 二、测试目标端口连通性（验证端口可用性）
**用nc（netcat）测试关键端口**（以30001为例，可替换为需测试的端口）  
`nc -zv 0.0.0.0 30001`  
- 成功提示：`Connection to 0.0.0.0 30001 port [tcp/*] succeeded!`  
- 失败提示：`nc: connect to 0.0.0.0 port 30001 (tcp) failed: Connection refused`


## 三、防火墙配置（按需开放端口）
1. **查看ufw防火墙当前状态**（先确认防火墙是否启用，避免无效配置）  
   `sudo ufw status`

2. **放行目标端口**（以29999/Dashboard、30001/Real-Time Data Output为例）  
   `sudo ufw allow 29999/tcp`  
   `sudo ufw allow 30001/tcp`
[优傲机器人 RTDE C++ 接口](https://sdurobotics.gitlab.io/ur_rtde/index.html#)
[RTDE客户端库和示例](https://github.com/UniversalRobots/RTDE_Python_Client_Library)
[实时数据交换 （RTDE） 指南](https://docs.universal-robots.com/tutorials/communication-protocol-tutorials/rtde-guide.html)







# pip install ur-rtde

# 配置canda

### 1. 安装Miniconda

```bash
# 1. 查看系统架构
uname -m
# 输出说明：x86_64→英特尔/AMD架构；aarch64→ARM架构（如RK3588/Jetson）

# 2. 下载对应架构的Miniconda
# x86_64架构（PC）：
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# rm64架构（RK3588/Jetson）：
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh

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
```


### 3. 创建并激活 Python 3.12 虚拟环境

```bash
# 1. 创建名为「py312」的虚拟环境
conda create -n py312 python=3.12 -y

# 2. 激活环境
conda activate py312
# 激活成功后，终端前缀会显示 「(py312)」
```

放行 30001（RTDE）和 29999（Dashboard）端口
sudo ufw allow 29999/tcp
sudo ufw allow 30001/tcp



## UR5e 机器人 DO 端口控制方案

方案 1：Python 远程控制（30002 端口）

```python
import socket
import time

# -------------------------- 需修改的参数 --------------------------
ROBOT_IP = "192.168.1.103"  # 机器人实际IP
DO_PORT = 0                  # 目标DO端口（0-7）
HIGH_DELAY = 5               # 高电平持续时间（秒）
# -------------------------------------------------------------------

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((ROBOT_IP, 30002))  
        # 高电平指令
        s.send(f"set_digital_out({DO_PORT}, True)\n".encode())
        print(f"DO{DO_PORT} → 高电平（持续{HIGH_DELAY}s）")
        time.sleep(HIGH_DELAY)
        # 低电平指令
        s.send(f"set_digital_out({DO_PORT}, False)\n".encode())
        print(f"DO{DO_PORT} → 低电平")
    except ConnectionError:
        print("连接失败！检查：1.机器人IP 2.网络连通性 3.30002端口开放")
    except Exception as e:
        print(f"错误：{e}")
```

方案 2：UR5e 本地 URScript 控制
 
```URScript
DO_PORT = 0
HIGH_DELAY = 5.0

set_digital_out(DO_PORT, True)  # 高电平
sleep(HIGH_DELAY)               # 延时（URScript需小数，如5.0）
set_digital_out(DO_PORT, False) # 低电平
```



# (py312) ur@ur:~/UR$ python RTDE.py 
# [-0.14396865671123069, -0.43562006072665155, 0.3630723594532053, -0.0012213596815780676, 3.1162765284819702, 0.03889191563689282]
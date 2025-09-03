# ViTai-SDK 安装指南


## 一、下载SDK源码

1. 访问仓库：[ViTai-SDK-Release](https://github.com/ViTai-Tech/ViTai-SDK-Release)
2. 下载源码包：点击页面中的「Code」→「Download ZIP」，获取[ViTai-SDK-Release-main.zip](https://codeload.github.com/ViTai-Tech/ViTai-SDK-Release/zip/refs/heads/main)
3. 解压源码包（以解压到`/home/ur/vitai`目录为例）


### 二、基础依赖安装

```bash
# 1. 更新系统包列表
sudo apt update

# 2. 安装SDK核心依赖（视频设备控制工具v4l-utils）
sudo apt-get -y install v4l-utils

# 3. 安装Python 3.12（SDK指定版本）
sudo apt install python3.12 -y

# 4. 验证Python安装（需输出：Python 3.12.x）
python3.12 --version
```


## 三、Miniconda与虚拟环境配置

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


### 四、安装ViTai SDK

```bash
# 1. 进入SDK的wheel目录
cd /home/ur/vitai/ViTai-SDK-Release-main/wheel

# 2. 确保虚拟环境已激活
conda activate py312

# 3. 若系统是x86_64架构：
pip install pyvitaisdk-1.0.7-cp312-cp312-linux_x86_64.whl

# 若系统是arm64架构（RK3588/Jetson）：
# pip install pyvitaisdk-1.0.7-cp312-cp312-linux_aarch64.whl

```


### 五、基础功能测试

```bash
# 1. 进入SDK的examples目录
cd /home/ur/vitai/ViTai-SDK-Release-main/examples

# 2. 确保虚拟环境已激活
conda activate py312

# 测试设备查找（验证传感器连接）
python gf225_find_sensor.py

# 测试获取图像（自动校正模式）
python gf225_read_image.py

# 测试3D点云可视化
python gf225_xyz_vector.py

# 测试滑动检测
python gf225_slip_detect.py

# 测试Marker追踪
python gf225_tracking.py
```

- **测试失败提示**：若提示“找不到传感器”，需检查传感器接线是否正常、设备是否被系统识别（可通过 `v4l2-ctl --list-devices` 查看视频设备）。


## 六、基于 ViTai-SDK 开发 WASD 操作（模拟键盘控制）

### 1. 安装依赖库

```bash
# 1. 确保在py312环境中
conda activate py312

# 2. 安装键盘鼠标模拟库
pip install pyautogui
```


### 2. 配置图形界面权限（解决X11授权问题）

```bash
# 生成X授权文件（若不存在）
xauth generate :0 . trusted

# 验证文件生成（应显示-rw-------权限的文件）
ls -la ~/.Xauthority

# 允许本地程序访问图形界面
xhost +local:
```


### 3. 运行WASD操作示例

```bash
# 根据传感器数据，通过WASD键模拟操作
python /home/ur/vitai/ViTai-SDK-Release-main/examples/wasd.py
```
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
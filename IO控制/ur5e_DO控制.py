"""
方案1：
机器人远程控制，python通过30002端口控制DO
"""

import socket
import time

# 机器人IP和端口（30002为脚本接收端口）
ROBOT_IP = "192.168.1.103"
PORT = 30002

# 连接机器人
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ROBOT_IP, PORT))

try:
    # 控制DO端口0：高电平（True）
    do_port = 0
    cmd = f"set_digital_out({do_port}, True)\n"  # URScript指令
    s.send(cmd.encode('utf-8'))
    print(f"已将DO{do_port}设置为高电平")
    
    # 延时5秒
    time.sleep(5)
    
    # 控制DO端口0：低电平（False）
    cmd = f"set_digital_out({do_port}, False)\n"
    s.send(cmd.encode('utf-8'))
    print(f"已将DO{do_port}设置为低电平")

finally:
    # 关闭连接
    s.close()


"""
方案2：
UR5e 机器人本地控制，使用脚本代码
```
set_digital_out(0, True)
sleep(5.0)
set_digital_out(0, False)
```
"""
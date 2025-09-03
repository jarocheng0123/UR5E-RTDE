# pip install ur-rtde

# https://github.com/jarocheng0123/ViTaiSDK

# https://github.com/jarocheng0123/UR5e 
# 配置canda




# UR机器人RTDE接口（用于通信和控制）
import rtde_receive
import rtde_control


# 机器人的IP地址
ROBOT_HOST = '0.0.0.0'
# 与RTDE使用的端口号
ROBOT_PORT = 30004



# 连接UR机器人并获取当前位姿
rtde_r = rtde_receive.RTDEReceiveInterface("0.0.0.0")
pose = rtde_r.getActualTCPPose()
print(pose)

# 控制UR机器人移动（修改Z轴高度后移动）
pose[2] += 1  # Z轴增加5cm
rtde_c = rtde_control.RTDEControlInterface("0.0.0.0")
rtde_c.moveL(pose, 0.5, 0.3)  # 线性移动


# (py312) ur@ur:~/UR$ python RTDE.py 
# [-0.14396865671123069, -0.43562006072665155, 0.3630723594532053, -0.0012213596815780676, 3.1162765284819702, 0.03889191563689282]
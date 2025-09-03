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


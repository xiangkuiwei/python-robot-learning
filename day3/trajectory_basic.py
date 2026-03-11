def linear_trajectory(start_angle,end_angle,steps):
    trajectory = []
    delta = (end_angle-start_angle)/(steps-1)
    for i in range(steps):
        angle = start_angle + i * delta
        trajectory.append(angle)
    return trajectory
start = 0
end = 1.57
steps = 10
traj = linear_trajectory(start,end,steps)
print(f"线性轨迹: 从 {start} rad 到 {end} rad, {steps} 步")
print("-" * 40)
for i, angle in enumerate(traj):     # enumerate() 可以同时获得索引和值
    print(f"步骤{i:2d}: {angle:.3f} rad = {angle*180/3.14159:.1f}度 ")


# enumerate() 可以同时获得索引和值
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 输出：
# 0 apple
# 1 banana
# 2 orange


# 多关节版本
def multi_joint_trajectory(joint_starts, joint_ends, steps):
    num_joints = len(joint_starts)   # 获取关节数量
    trajectory = []                  # 存储所有轨迹点
    for step in range(steps):        # 遍历每一步
        step_angles = []             # 存储当前步各关节的角度
        for j in range(num_joints):  # 遍历每个关节
            delta = (joint_ends[j]-joint_starts[j])/(steps - 1)
            angle = joint_starts[j] + step*delta
            step_angles.append(angle)
        trajectory.append([step,step_angles])
    return trajectory

starts = [0, 0.5, -0.3]
ends = [1.57, 1.0, 0.8]
steps = 8

multi_traj = multi_joint_trajectory(starts, ends, steps)
print("\n" + "="*40)
print("多关节轨迹")
print("="*40)
print(f"起始角度: {starts}")
print(f"目标角度: {ends}")
print(f"步数: {steps}")
print("-"*40)

for step, angles in multi_traj:
    angles_str = [f"{a:.3f}" for a in angles]    # 格式化角度到3位小数
    print(f"步骤{step:2d}:{angles_str}")
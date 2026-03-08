import numpy as np
import matplotlib.pyplot as plt

print("🎉 环境配置成功！")
print(f"NumPy 版本: {np.__version__}")

# 生成数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 画图
plt.plot(x, y)
plt.title("Hello, Robot!")
plt.show()
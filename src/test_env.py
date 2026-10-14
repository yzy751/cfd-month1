import numpy as np
import matplotlib.pyplot as plt
import scipy

print("numpy:", np.__version__)
print("matplotlib:", plt.matplotlib.__version__)
print("scipy:", scipy.__version__)

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label="sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Environment Test")
plt.legend()
plt.tight_layout()
plt.savefig("figures/test_env.png", dpi=150)
print("figure saved to figures/test_env.png")
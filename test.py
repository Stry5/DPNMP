import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("log_2026-05-09_15-47-33.csv")
print(df)
df.plot(kind="line", x="time_ms", y="ecvt_bus_voltage")
print(df.columns.tolist())
plt.show()

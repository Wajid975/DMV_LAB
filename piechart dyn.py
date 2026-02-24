import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Initial data
labels = ['A', 'B', 'C', 'D']
data = np.random.randint(10, 50, size=4)

# Create figure and axis
fig, ax = plt.subplots()
ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle

# Function to update pie chart
def update(frame):
    ax.clear()
    ax.axis('equal')
    # Generate new random data for each frame
    data = np.random.randint(10, 50, size=4)
    wedges, texts, autotexts = ax.pie(
        data, labels=labels, autopct='%1.1f%%', startangle=90
    )
    ax.set_title(f"Dynamic Pie Chart - Frame {frame}")

# Animate
ani = FuncAnimation(fig, update, frames=20, interval=1000, repeat=False)

plt.show()

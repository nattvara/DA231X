import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

matplotlib.rcParams['font.family'] = 'Arial'
matplotlib.rcParams['font.size'] = 14

categories = {
    'Animals': ['Dog', 'Cat', 'Elephant', 'Lion', 'Tiger', 'Eurasian lynx'],
    'Foods': ['Pizza', 'Burger', 'Salad', 'Sushi', 'Pasta', 'Meatballs'],
    'Sports': ['Football', 'Soccer', 'Alpine skiing', 'Basketball', 'Baseball', 'Tennis', 'Cricket']
}

figure_width = 16
figure_height = figure_width / 16 * 9
dpi = 300

fig = plt.figure(figsize=(figure_width, figure_height), dpi=dpi)
ax = fig.add_subplot(111, projection='3d')

colors = {'Animals': '#ac0a10', 'Foods': '#bd6500', 'Sports': '#bba600'}

for category_index, (category, items) in enumerate(categories.items()):
    x = np.full(len(items), category_index / (len(categories) - 1))
    y = np.random.rand(len(items)) * 0.8 + 0.1
    z = np.random.rand(len(items)) * 0.8 + 0.1
    ax.scatter(x, y, z, color=colors[category], s=100, label=category)

    for i, item in enumerate(items):
        ax.text(x[i], y[i], z[i], item, color='black')

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

ax.set_xlabel('Dimension 1')
ax.set_ylabel('Dimension 2')
ax.set_zlabel('Dimension 3')

plt.tight_layout()

file_path = os.path.realpath(f"{os.path.dirname(__file__)}/../content/figures/assets/04-background-word-plot.png")
os.makedirs(os.path.dirname(file_path), exist_ok=True)
plt.savefig(file_path, bbox_inches='tight', pad_inches=0)

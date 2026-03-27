import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

steps = [
    "Start",
    "Generate Traffic Dataset",
    "Initialize GOA Population",
    "Calculate Fitness",
    "Update Positions",
    "Stop Condition?",
    "Best Solution",
    "Run GA",
    "Compare Results",
    "Plot Graph",
    "End",
]

box_x, box_w, box_h = 1, 2, 0.5
gap = 1.0


def _draw_box(ax, label, y, diamond=False):
    color = ("orange", "#fff3cd") if diamond else ("steelblue", "#dce9f7")
    patch = mpatches.FancyBboxPatch(
        (box_x, y), box_w, box_h,
        boxstyle="round,pad=0.05",
        edgecolor=color[0], facecolor=color[1], linewidth=1.5
    )
    ax.add_patch(patch)
    ax.text(box_x + box_w / 2, y + box_h / 2, label,
            ha="center", va="center", fontsize=9, fontweight="bold")


def draw_flowchart():
    fig, ax = plt.subplots(figsize=(5, 14))
    ax.set_xlim(0, 4)
    ax.set_ylim(0, len(steps) + 1)
    ax.axis("off")

    positions = {}
    for idx, step in enumerate(steps):
        y = (len(steps) - idx) * gap
        positions[step] = y
        _draw_box(ax, step, y, diamond=(step == "Stop Condition?"))

    # Arrows between steps
    cx = box_x + box_w / 2
    for i in range(len(steps) - 1):
        ax.annotate("", xy=(cx, positions[steps[i + 1]] + box_h),
                    xytext=(cx, positions[steps[i]]),
                    arrowprops=dict(arrowstyle="->", color="gray", lw=1.5))

    # "No" loop back from Stop Condition? to Calculate Fitness
    stop_y   = positions["Stop Condition?"]
    target_y = positions["Calculate Fitness"]
    loop_x   = box_x + box_w + 0.6

    ax.annotate("No", xy=(box_x + box_w, stop_y + box_h / 2),
                xytext=(loop_x, stop_y + box_h / 2),
                fontsize=8, color="red",
                arrowprops=dict(arrowstyle="->", color="red", lw=1.2))
    ax.plot([loop_x, loop_x], [stop_y + box_h / 2, target_y + box_h / 2], color="red", lw=1.2)
    ax.annotate("", xy=(box_x + box_w, target_y + box_h / 2),
                xytext=(loop_x, target_y + box_h / 2),
                arrowprops=dict(arrowstyle="->", color="red", lw=1.2))

    plt.title("Traffic Flow Optimization Flowchart", fontsize=11, fontweight="bold", pad=10)
    plt.tight_layout()

import matplotlib.pyplot as plt


def plot_waiting_time_comparison(classical, vision_driven):
    labels = ['Classical Queue', 'Vision-Driven Queue']
    values = [classical, vision_driven]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.ylabel('Average Waiting Time')
    plt.title('Experiment 1: Waiting Time Comparison')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

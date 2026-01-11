from experiments import run_simulation
from plots import plot_waiting_time_comparison

classical_wait = run_simulation(dynamic=False)
vision_driven_wait = run_simulation(dynamic=True)

print("Classical average waiting time:", classical_wait)
print("Vision-driven average waiting time:", vision_driven_wait)

plot_waiting_time_comparison(classical_wait, vision_driven_wait)

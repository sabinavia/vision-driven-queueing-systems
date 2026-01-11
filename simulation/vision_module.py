import numpy as np

def estimate_arrival_rate(t):
    """
    Vision-driven arrival rate estimator (proxy).
    Simulates real-time CV-based fluctuations.
    """
    base_rate = 0.8
    noise = 0.3 * np.sin(0.1 * t) + np.random.normal(0, 0.05)
    lambda_t = base_rate + noise

    return max(lambda_t, 0.05)

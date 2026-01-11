import simpy
import numpy as np
import random
from vision_module import estimate_arrival_rate


def service_process(env, server, service_rate, waiting_times):
    arrival_time = env.now
    with server.request() as request:
        yield request
        waiting_times.append(env.now - arrival_time)
        service_time = random.expovariate(service_rate)
        yield env.timeout(service_time)


def arrival_process(env, server, service_rate, arrival_rate_func, waiting_times):
    i = 0
    while True:
        lambda_t = arrival_rate_func(env.now)
        interarrival_time = random.expovariate(lambda_t)
        yield env.timeout(interarrival_time)
        env.process(service_process(env, server, service_rate, waiting_times))
        i += 1


def run_simulation(sim_time=120, servers=3, mu=1.0, dynamic=True):
    env = simpy.Environment()
    server = simpy.Resource(env, capacity=servers)
    waiting_times = []

    if dynamic:
        arrival_rate_func = lambda t: estimate_arrival_rate(t)
    else:
        arrival_rate_func = lambda t: 0.8  # classical fixed arrival rate

    env.process(
        arrival_process(
            env,
            server,
            mu,
            arrival_rate_func,
            waiting_times
        )
    )

    env.run(until=sim_time)

    return np.mean(waiting_times)

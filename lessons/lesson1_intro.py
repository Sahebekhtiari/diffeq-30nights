#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Newton's Cooling Law - Euler vs. Exact
--------------------------------------
This script demonstrates Newton's Law of Cooling.
It compares:
    1. The numerical solution using the explicit Euler method
    2. The exact analytical solution

Both results are plotted on the same graph, and the final error is printed.

Run:
    python lesson1_cooling.py
"""

import math
import matplotlib.pyplot as plt


def euler_cooling(T0, T_env, k, dt, t_end):
    """
    Euler method for solving the ODE:
        dT/dt = -k * (T - T_env)

    Parameters:
        T0     - initial temperature
        T_env  - ambient temperature
        k      - cooling constant (> 0)
        dt     - time step
        t_end  - total simulation time

    Returns:
        times (list of floats) - time values
        temps (list of floats) - temperature values by Euler's method
    """
    n_steps = int(round(t_end / dt))  # number of steps
    t = 0.0                           # start time
    T = float(T0)                     # start temperature

    times = [t]
    temps = [T]

    for _ in range(n_steps):
        # derivative of temperature at current state
        dTdt = -k * (T - T_env)

        # Euler update
        T = T + dTdt * dt
        t = t + dt

        times.append(t)
        temps.append(T)

    return times, temps


def exact_cooling(T0, T_env, k, times):
    """
    Exact solution of Newton's Cooling Law:
        T(t) = T_env + (T0 - T_env) * exp(-k * t)

    Parameters:
        T0     - initial temperature
        T_env  - ambient temperature
        k      - cooling constant
        times  - list of time values

    Returns:
        list of floats - exact temperature values
    """
    return [T_env + (T0 - T_env) * math.exp(-k * t) for t in times]


def run_cooling_demo():
    """
    Runs the cooling demo:
      - defines parameters
      - computes Euler and exact solutions
      - plots results
      - prints final error
    """
    # ---- Parameters (editable) ----
    T_env = 25.0     # ambient temperature (°C)
    T0 = 90.0        # initial object temperature (°C)
    k = 0.18         # cooling coefficient (per second)
    dt = 0.5         # time step (seconds)
    t_end = 20.0     # total simulation time (seconds)

    # ---- Euler solution ----
    t_euler, T_euler = euler_cooling(T0, T_env, k, dt, t_end)

    # ---- Exact solution ----
    T_exact = exact_cooling(T0, T_env, k, t_euler)

    # ---- Error at the last time ----
    abs_err_final = abs(T_euler[-1] - T_exact[-1])

    # ---- Plot results ----
    plt.figure(figsize=(8, 5), dpi=120)
    plt.plot(t_euler, T_euler, marker="o", linewidth=1.8, label="Euler (numerical)")
    plt.plot(t_euler, T_exact, linestyle="--", linewidth=2.0, label="Exact (analytical)")
    plt.axhline(T_env, color="gray", linewidth=1.2, linestyle=":", label="T_env")

    plt.title("Newton's Cooling: Euler vs. Exact")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.grid(True, alpha=0.25)
    plt.legend()

    plt.tight_layout()
    plt.savefig("newton_cooling_euler_vs_exact.png", dpi=150)
    plt.show()

    # ---- Console output ----
    print(f"[Summary] dt={dt:.3f}s, k={k:.3f}/s, T0={T0}°C, T_env={T_env}°C")
    print(f"[Summary] Final-time absolute error (|Euler - Exact|): {abs_err_final:.4f} °C")


# Run the demo
run_cooling_demo()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Newton's Cooling Law - Euler vs. Exact
--------------------------------------
This script compares the explicit Euler numerical solution
to the analytical solution of Newton's cooling law, and plots both curves.

Run:
    python lesson1_cooling.py
"""

import math
import matplotlib.pyplot as plt


def euler_cooling(T0, T_env, k, dt, t_end):
    """
    Explicit Euler method for dT/dt = -k * (T - T_env)
    """
    n_steps = int(round(t_end / dt))
    t = 0.0
    T = float(T0)

    times = [t]
    temps = [T]

    for _ in range(n_steps):
        # derivative at current time
        dTdt = -k * (T - T_env)

        # Euler step
        T = T + dTdt * dt
        t = t + dt

        times.append(t)
        temps.append(T)

    return times, temps


def exact_cooling(T0, T_env, k, times):
    """
    Analytical solution:
        T(t) = T_env + (T0 - T_env) * exp(-k t)
    """
    return [T_env + (T0 - T_env) * math.exp(-k * t) for t in times]


def run_cooling_demo():
    # ---- Parameters (editable) ----
    T_env = 25.0     # ambient temperature (°C)
    T0 = 90.0        # initial object temperature (°C)
    k = 0.18         # cooling coefficient (> 0)
    dt = 0.5         # time step (s)
    t_end = 20.0     # total simulation time (s)

    # ---- Euler method ----
    t_euler, T_euler = euler_cooling(T0, T_env, k, dt, t_end)

    # ---- Exact solution ----
    T_exact = exact_cooling(T0, T_env, k, t_euler)

    # ---- Error at final time ----
    abs_err_final = abs(T_euler[-1] - T_exact[-1])

    # ---- Plot ----
    plt.figure(figsize=(8, 5), dpi=120)
    plt.plot(t_euler, T_euler, marker="o", linewidth=1.8, label="Euler")
    plt.plot(t_euler, T_exact, linestyle="--", linewidth=2.0, label="Exact")
    plt.axhline(T_env, color="gray", linewidth=1.2, linestyle=":", label="T_env")

    plt.title("Newton's Cooling: Euler vs. Exact")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.grid(True, alpha=0.25)
    plt.legend()

    plt.tight_layout()
    plt.savefig("newton_cooling_euler_vs_exact.png", dpi=150)
    plt.show()

    # Console output
    print(f"[Summary] dt={dt:.3f}s, k={k:.3f}/s, T0={T0}°C, T_env={T_env}°C")
    print(f"[Summary] Final-time absolute error (|Euler-Exact|): {abs_err_final:.4f} °C")


# Run the demo
run_cooling_demo()

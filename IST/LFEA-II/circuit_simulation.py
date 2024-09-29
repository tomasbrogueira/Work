import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the RLD circuit parameters (these can be tweaked)
R = 4.8  # Resistance in ohms
L = 221e-6  # Inductance in Henry
C_0 = 1e-12  # Zero-bias capacitance of the varicap in Farads
V_bi = 0.7  # Built-in potential of the varicap in volts
n = 0.5  # Doping constant for the varicap diode
f = 376e3  # Frequency of the function generator in Hz
V_in_amp = 1.5  # Amplitude of the input voltage in volts

# Define the input driving voltage (sinusoidal function)
def V_in(t):
    return V_in_amp * np.sin(2 * np.pi * f * t)

# Define the diode capacitance model (Varicap behavior)
def varicap_capacitance(V_d):
    if V_d < V_bi:
        return C_0 / ((1 - V_d / V_bi) ** n)
    else:
        return C_0  # Capacitance remains at C_0 for forward bias

# Define the diode current model (for simplicity, we assume a basic linear current-voltage relation)
def diode_current(V):
    if V < V_bi:
        return 0  # No current if below built-in potential (reverse biased)
    else:
        return (V - V_bi) / R  # Forward current approximation

# Define the system of differential equations for the RLD circuit with a varicap diode
def circuit_dynamics(t, y):
    I_L, V_d = y  # Current through the inductor (I_L) and voltage across the diode (V_d)
    
    # Calculate capacitance at this diode voltage
    C_j = varicap_capacitance(V_d)
    
    # Differential equations
    dI_L_dt = (V_in(t) - R * I_L - V_d) / L  # Kirchhoff's voltage law
    dV_d_dt = (I_L - diode_current(V_d)) / C_j  # Diode's variable capacitance
    
    return [dI_L_dt, dV_d_dt]

# Time range for simulation - reduced to avoid long runs
t_start = 0
t_end = 1e-4  # Simulate for 0.1 ms to avoid long run times initially
time = np.linspace(t_start, t_end, 1000)

# Initial conditions: zero current through the inductor, and zero voltage across the diode
y0 = [0, 0]

# Set up solver tolerances to prevent excessive computation
tolerances = {'rtol': 1e-6, 'atol': 1e-9}

# Solve the differential equations
solution = solve_ivp(circuit_dynamics, [t_start, t_end], y0, t_eval=time, method='RK45', **tolerances)

# Check if solution was successful
if not solution.success:
    print("Warning: Integration failed.")
else:
    # Extract the results
    I_L_sol = solution.y[0]  # Current through the inductor
    V_d_sol = solution.y[1]  # Voltage across the diode

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(time, V_in(time), label="Input Voltage (V_in)")
    plt.plot(time, V_d_sol, label="Voltage across Diode (V_d)", linestyle='--')
    plt.title('Voltage vs. Time with Varicap Diode')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(time, I_L_sol, label="Current through Inductor (I_L)")
    plt.title('Current vs. Time with Varicap Diode')
    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')
    plt.legend()

    plt.tight_layout()
    plt.show()
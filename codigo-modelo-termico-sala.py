import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

V       = 203.57
P       = 17580.0
Tc      = 20.0
T0      = 35.0
N       = 40.0
q_occ   = 70.0
C       = 50.6e6
UA      = 158.88
Kp      = 8790.0

a = UA / C
b = Kp / C
c = q_occ / C

omega = np.pi / 18000.0

def Te_func(t):
    return 32.5 - 2.5 * np.cos(omega * t)

def modelo_termico(T, t):
    Te = Te_func(t)
    return a * (Te - T) - b * (T - Tc) + c * N

t = np.linspace(0, 10800, 10801)
T_interna = odeint(modelo_termico, T0, t).flatten()

print("--- VALIDAÇÃO NUMÉRICA ---")
print(f"T(0 min):   {T_interna[0]:.2f} °C")
print(f"T(30 min):  {T_interna[1800]:.2f} °C")
print(f"T(60 min):  {T_interna[3600]:.2f} °C")
print(f"T(120 min): {T_interna[7200]:.2f} °C")
print(f"T(180 min): {T_interna[10800]:.2f} °C")

plt.plot(t/60, T_interna, label="Solução Numérica (odeint)")
plt.xlabel("Tempo (minutos)")
plt.ylabel("Temperatura (°C)")
plt.title("Dinâmica Térmica da Sala Climatizada")
plt.legend()
plt.grid(True)
plt.show()
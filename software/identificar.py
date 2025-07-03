import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction
from scipy.optimize import minimize
from scipy.interpolate import interp1d

# --- Leitura do CSV ---
with open('teste.csv', 'r') as f:
    linha = f.readline().strip()

grupos = [list(map(float, g.split(','))) for g in linha.split(';') if g]
u_raw = np.array([g[0] for g in grupos])  # entrada (ex: PWM)
y_raw = np.array([g[1] for g in grupos])  # saída (ex: tensão)
t_raw = np.array([g[2] for g in grupos])  # tempo

# --- Interpola para tempo uniforme ---
t_uniforme = np.linspace(t_raw[0], t_raw[-1], len(t_raw))
u = interp1d(t_raw, u_raw, kind='linear')(t_uniforme)
y = interp1d(t_raw, y_raw, kind='linear')(t_uniforme)

# --- Modelo de 1ª ordem ---
def simulate_tf_first_order(params, u, t):
    K, tau = params
    num = [K]
    den = [tau, 1]
    system = TransferFunction(num, den)
    tout, yout, _ = system.output(U=u, T=t)
    return yout

# --- Função de custo ---
def cost_function_first_order(params, u, y, t):
    y_sim = simulate_tf_first_order(params, u, t)
    return np.mean((y - y_sim)**2)

# --- Ajuste dos parâmetros ---
initial_params = [1.0, 1.0]
result = minimize(cost_function_first_order, initial_params, args=(u, y, t_uniforme), method='Nelder-Mead')
K, tau = result.x

# --- Impressão da função de transferência ---
print(f"Parâmetros ótimos (1ª ordem): K = {K:.10f}, tau = {tau:.10f}")
print(f"\nFunção de Transferência estimada:")
print(f"G(s) = {K:.4f} / ({tau:.4f}s + 1)")

# --- Simulação com modelo ajustado ---
y_simulado = simulate_tf_first_order([K, tau], u, t_uniforme)

# --- Gráfico da resposta ---
plt.figure(figsize=(10, 5))
plt.plot(t_uniforme, y, label='Saída Real', color='blue')
plt.plot(t_uniforme, y_simulado, label='Saída Simulada (1ª ordem)', linestyle='--', color='green')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.title('Identificação de Função de Transferência - 1ª Ordem')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
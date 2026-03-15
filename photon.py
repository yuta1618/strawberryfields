import strawberryfields as sf
from strawberryfields.ops import *
import numpy as np
from numpy import pi, sqrt

# 1. 4モードのプログラム作成
prog = sf.Program(4)

# パラメータ設定
r_sq = 2       # スクイーズレベル
x_ini = 1.0    # 送信したい状態のx
p_ini = 0.5    # 送信したい状態のp

# コヒーレント状態の「半径」と「位相」を計算
alpha = x_ini + 1j*p_ini
r_coh = np.abs(alpha)
phi_coh = np.angle(alpha)

# 2. 回路図の作成
with prog.context as q:
    # --- 状態準備 ---
    # Coherent(半径, 位相) の形式で入力
    Coherent(r_coh, phi_coh) | q[0]
    
    # リソース作成
    Sgate(-r_sq) | q[1] 
    Sgate(r_sq) | q[2]
    
    # 比較用
    Coherent(r_coh, phi_coh) | q[3]
    
    # --- 量子操作 ---
    BSgate(pi/4, 0) | (q[1], q[2])
    BSgate(pi/4, 0) | (q[0], q[1])
    
    # ホモダイン測定
    MeasureX | q[0]
    MeasureP | q[1]    
    
    # 古典フィードバック（.par を使って計算）
    Xgate(q[0].par * sqrt(2)) | q[2]
    Zgate(q[1].par * sqrt(2)) | q[2]

# 3. 実行
eng = sf.Engine(backend='gaussian')
result = eng.run(prog)
state = result.state

# --- 結果の表示 ---
print("--- Quantum Teleportation Result ---")
means = state.means()
print(f"Teleported state (q[2]) mean x: {means[2]:.4f}, p: {means[6]:.4f}")
print(f"Original state   (q[3]) mean x: {means[3]:.4f}, p: {means[7]:.4f}")

# 4. 可視化
import matplotlib.pyplot as plt
x_range = np.arange(-5, 5, 0.1)
p_range = np.arange(-5, 5, 0.1)
W = state.wigner(2, x_range, p_range)

X, P = np.meshgrid(x_range, p_range)
plt.figure(figsize=(8, 6))
plt.contourf(X, P, W, levels=50, cmap='RdBu_r')
plt.title("Wigner Function of the Teleported State (q[2])")
plt.xlabel("x")
plt.ylabel("p")
plt.colorbar()
plt.show()
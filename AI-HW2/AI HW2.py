
# 1. 展示网络结构
print()
print("Bayesian Network Structure")
print()
print("Nodes: Cloudy (C), Sprinkler (S), Rain (R), Wet Grass (W)")
print("Edges (Directed):")
print("  Cloudy → Sprinkler")
print("  Cloudy → Rain")
print("  Sprinkler → Wet Grass")
print("  Rain → Wet Grass")
print()


# 2. 定义并展示条件概率表
print()
print("Conditional Probability Tables")
print()

# 2.1 P(Cloudy)
P_C = {'T': 0.5, 'F': 0.5}
print("\nP(Cloudy):")
print(f"  Cloudy = T : {P_C['T']}")
print(f"  Cloudy = F : {P_C['F']}")

# 2.2 P(Sprinkler | Cloudy)
P_S_given_C = {
    ('T', 'T'): 0.1,   # P(S=T | C=T)
    ('T', 'F'): 0.5,   # P(S=T | C=F)
    ('F', 'T'): 0.9,   # P(S=F | C=T)
    ('F', 'F'): 0.5    # P(S=F | C=F)
}
print("\nP(Sprinkler | Cloudy):")
print("  Cloudy\tSprinkler=T\tSprinkler=F")
print(f"  T\t\t{P_S_given_C[('T','T')]}\t\t{P_S_given_C[('F','T')]}")
print(f"  F\t\t{P_S_given_C[('T','F')]}\t\t{P_S_given_C[('F','F')]}")

# 2.3 P(Rain | Cloudy)
P_R_given_C = {
    ('T', 'T'): 0.8,   # P(R=T | C=T)
    ('T', 'F'): 0.2,   # P(R=T | C=F)
    ('F', 'T'): 0.2,   # P(R=F | C=T)
    ('F', 'F'): 0.8    # P(R=F | C=F)
}
print("\nP(Rain | Cloudy):")
print("  Cloudy\tRain=T\t\tRain=F")
print(f"  T\t\t{P_R_given_C[('T','T')]}\t\t{P_R_given_C[('F','T')]}")
print(f"  F\t\t{P_R_given_C[('T','F')]}\t\t{P_R_given_C[('F','F')]}")

# 2.4 P(Wet Grass | Sprinkler, Rain)
P_W_given_S_R = {
    ('T', 'T'): 0.99,  # P(W=T | S=T, R=T)
    ('T', 'F'): 0.9,   # P(W=T | S=T, R=F)
    ('F', 'T'): 0.9,   # P(W=T | S=F, R=T)
    ('F', 'F'): 0.0    # P(W=T | S=F, R=F)
}
print("\nP(Wet Grass = T | Sprinkler, Rain):")
print("  Sprinkler\tRain\tProbability")
print(f"  T\t\tT\t{P_W_given_S_R[('T','T')]}")
print(f"  T\t\tF\t{P_W_given_S_R[('T','F')]}")
print(f"  F\t\tT\t{P_W_given_S_R[('F','T')]}")
print(f"  F\t\tF\t{P_W_given_S_R[('F','F')]}")
print("\n")


# 3. 计算 P(Wet Grass = T)
P_W_T = 0.0
for c in ['T', 'F']:
    for s in ['T', 'F']:
        for r in ['T', 'F']:
            prob = P_C[c] * P_S_given_C[(s, c)] * P_R_given_C[(r, c)] * P_W_given_S_R[(s, r)]
            P_W_T += prob

print(f"\nP(Wet Grass = T) = {P_W_T:.4f}")

# 4. 计算 P(Rain = T | Wet Grass = T)
P_R_T_W_T = 0.0
for c in ['T', 'F']:
    for s in ['T', 'F']:
        prob = P_C[c] * P_S_given_C[(s, c)] * P_R_given_C[('T', c)] * P_W_given_S_R[(s, 'T')]
        P_R_T_W_T += prob

P_R_given_W_T = P_R_T_W_T / P_W_T
print(f"P(Rain = T | Wet Grass = T) = {P_R_given_W_T:.4f}")
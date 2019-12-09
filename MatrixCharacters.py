A = [252, 18, 18, 18, 252]
B = [254, 146, 146, 146, 108]
C = [124, 130, 130, 130, 68] 
D = [254, 130, 130, 130, 124]
E = [254, 146, 146, 146, 130]
F = [254, 18, 18, 18, 2]
G = [124, 130, 130, 162, 100] 
H = [254, 16, 16, 16, 254]
I = [130, 254, 130]
J = [64, 128, 130, 126, 2]
K = [254, 16, 40, 68, 130]
L = [254, 128, 128, 128, 128]
M = [254, 4, 24, 4, 254]
N = [254, 8, 16, 32, 254]
O = [124, 130, 130, 130, 124]
P = [254, 18, 18, 18, 12]
Q = [124, 130, 162, 66, 188]
R = [254, 18, 50, 82, 140]
S = [140, 146, 146, 146, 98]
T = [2, 2, 254, 2, 2]
U = [126, 128, 128, 128, 126]
V = [30, 96, 128, 96, 30]
W = [126, 128, 112, 128, 126]
X = [198, 40, 16, 40, 198]
Y = [6, 8, 240, 8, 6]
Z = [194, 162, 146, 138, 134]

Space = [0, 0, 0, 0]

Characters = {}
Characters['A'] = A
Characters['B'] = B
Characters['C'] = C
Characters['D'] = D
Characters['E'] = E
Characters['F'] = F
Characters['G'] = G
Characters['H'] = H
Characters['I'] = I
Characters['J'] = J
Characters['K'] = K
Characters['L'] = L
Characters['M'] = M
Characters['N'] = N
Characters['O'] = O
Characters['P'] = P
Characters['Q'] = Q
Characters['R'] = R
Characters['S'] = S
Characters['T'] = T
Characters['U'] = U
Characters['V'] = V
Characters['W'] = W
Characters['X'] = X
Characters['Y'] = Y
Characters['Z'] = Z
Characters[' '] = Space

def Parse(message):
        charSpacer = [0]
        return [Characters[c] + charSpacer for c in message.upper()]






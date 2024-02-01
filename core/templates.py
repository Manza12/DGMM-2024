import numpy as np

# Thinning templates
C = np.array([[1]])

C_W = np.array([
    [0, 0, 0],
    [0, 1, 1],
    [0, 0, 0]
])

D_W = np.array([
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]
])

C_E = np.array([
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
])

D_E = np.array([
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1]
])

C_N = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 1, 0]
])

D_N = np.array([
    [1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]
])

C_S = np.array([
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
])

D_S = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 1]
])

# Restoring
C_WE = np.array([
    [0, 1, 1, 0],
])

D_WE = np.array([
    [1, 0, 0, 1],
])

ORIGIN_WE = (0, 1)
ORIGIN_WE_DIL = (0, 2)

C_NS = np.array([
    [0],
    [1],
    [1],
    [0],
])

D_NS = np.array([
    [1],
    [0],
    [0],
    [1],
])

ORIGIN_NS = (1, 0)
ORIGIN_NS_DIL = (2, 0)

# Trimming
C_NE = np.array([
    [0, 0, 0],
    [1, 1, 0],
    [0, 1, 0]
])

D_NE = np.array([
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
])

C_NW = np.array([
    [0, 0, 0],
    [0, 1, 1],
    [0, 1, 0]
])

D_NW = np.array([
    [1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]
])

C_SW = np.array([
    [0, 1, 0],
    [0, 1, 1],
    [0, 0, 0]
])

D_SW = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0]
])

C_SE = np.array([
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]
])

D_SE = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 1]
])

C_WT = np.array([
    [0, 0, 0],
    [0, 1, 1],
    [0, 0, 0]
])

D_WT = np.array([
    [1, 1, 0],
    [1, 0, 0],
    [1, 1, 0]
])

D_ET = np.array([
    [0, 1, 1],
    [0, 0, 1],
    [0, 1, 1]
])

C_NT = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 1, 0]
])

D_NT = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1]
])

B_O = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

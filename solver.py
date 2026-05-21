import cupy as cp

class PhaseFieldSolver:
    def __init__(self, grid_size, num_grains, mobility, kappa):
        self.grid_size = grid_size
        self.num_grains = num_grains
        self.mobility = mobility
        self.kappa = kappa
        self.eta = cp.zeros((num_grains, grid_size, grid_size))
        self.dx = 1.0
        self.dt = 0.1

    def calculate_laplacian(self, field):
        lap = cp.roll(field, 1, axis=1) + cp.roll(field, -1, axis=1) + \
              cp.roll(field, 1, axis=2) + cp.roll(field, -1, axis=2) - 4 * field
        return lap / (self.dx ** 2)

    def step(self):
        for i in range(self.num_grains):
            laplacian = self.calculate_laplacian(self.eta[i])
            df_deta = self.eta[i] ** 3 - self.eta[i]
            
            for j in range(self.num_grains):
                if i != j:
                    df_deta += 2 * self.eta[i] * (self.eta[j] ** 2)
                    
            d_eta = self.mobility * (self.kappa * laplacian - df_deta)
            self.eta[i] += d_eta * self.dt
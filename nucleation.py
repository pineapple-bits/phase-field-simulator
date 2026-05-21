import cupy as cp

class NucleationEngine:
    def __init__(self, nucleation_rate, driving_force_threshold):
        self.rate = nucleation_rate
        self.threshold = driving_force_threshold

    def seed_grains(self, eta_tensor, current_timestep):
        if current_timestep % 10 == 0:
            num_grains, h, w = eta_tensor.shape
            empty_spots = cp.sum(eta_tensor, axis=0) < 0.1
            
            if cp.any(empty_spots):
                y, x = cp.where(empty_spots)
                if len(y) > 0:
                    idx = int(cp.random.choice(len(y)))
                    grain_idx = int(cp.random.choice(num_grains))
                    eta_tensor[grain_idx, y[idx], x[idx]] = 1.0
                    
        return eta_tensor
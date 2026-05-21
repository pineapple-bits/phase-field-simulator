import sys
from PyQt6.QtWidgets import QApplication
from matplotlib.animation import FuncAnimation
from solver import PhaseFieldSolver
from nucleation import NucleationEngine
from ui import SimulationWindow

def main():
    GRID_SIZE = 128
    NUM_GRAINS = 20
    
    solver = PhaseFieldSolver(grid_size=GRID_SIZE, num_grains=NUM_GRAINS, mobility=1.0, kappa=0.5)
    nucleator = NucleationEngine(nucleation_rate=0.01, driving_force_threshold=0.8)
    
    app = QApplication(sys.argv)
    window = SimulationWindow(solver, nucleator)
    
    ani = FuncAnimation(window.figure, window.update_frame, interval=50, cache_frame_data=False)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
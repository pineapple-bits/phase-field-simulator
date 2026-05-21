import cupy as cp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class SimulationWindow(QMainWindow):
    def __init__(self, solver, nucleation_engine):
        super().__init__()
        self.solver = solver
        self.nucleator = nucleation_engine
        
        self.setWindowTitle("Phase-Field Grain Growth")
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasQTAgg(self.figure)
        
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        initial_data = cp.asnumpy(cp.argmax(self.solver.eta, axis=0))
        self.im = self.ax.imshow(initial_data, cmap='tab20', vmin=0, vmax=self.solver.num_grains)
        self.ax.axis('off')

    def update_frame(self, frame):
        self.solver.step()
        self.nucleator.seed_grains(self.solver.eta, frame)
        
        if frame % 5 == 0:
            display_data = cp.asnumpy(cp.argmax(self.solver.eta, axis=0))
            self.im.set_data(display_data)
            self.canvas.draw()
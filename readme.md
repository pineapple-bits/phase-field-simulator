# GPU-Accelerated Phase-Field Grain Growth

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![CuPy](https://img.shields.io/badge/CuPy-CUDA_Accelerated-green)
![PyQt6](https://img.shields.io/badge/PyQt6-Live_Rendering-red)

A modular, high-performance computational materials science simulator tracking microstructural evolution and continuous nucleation via the Allen-Cahn equations. 

## 📂 Project Architecture
This repository features both an exploratory notebook and a production-ready modular backend:
* `project.ipynb`: Interactive sandbox showing the mathematical derivation and progression of the model.
* `main.py`: The application entry point.
* `solver.py`: CuPy-accelerated tensor mathematics (9-point isotropic 3D Laplacian).
* `nucleation.py`: Thermodynamic continuous grain seeding logic.
* `ui.py`: Real-time PyQt6/Matplotlib streaming interface from GPU to System RAM.

## 🚀 Quick Start
Ensure you have an NVIDIA GPU and CUDA installed.

```bash
git clone [https://github.com/pineapple-bits/phase-field-simulator.git](https://github.com/pineapple-bits/phase-field-simulator.git)
cd phase-field-simulator
pip install -r requirements.txt

# Run the live simulation
python main.py

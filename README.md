# Circuit_Simulation
## Overview:
- This is a program to simulate a simple DC circuit where **RL** is a fixed resistor, **VS** is a DC voltage source (VS=10V), **R1** and **R2** are variable resistors, **V** is a voltmeter, and **A** is an ammeter. The project was built using python==3.10.5.
- At the beginning (t1=0s) the resistances are R1=0Ω and R2=100kΩ. These two resistances change linearly so that after 10 seconds (t2=10s) they are R1=100kΩ and R2 = 0Ω.
- RL=30kΩ.

![alt text](https://github.com/mhdsulaimantan/Circuit_Simulation/blob/main/circuit.png)

## How it works:
When the user run the program, it will give the following values:
- **Voltmeter (VL)**: 100ms timestamp.
- **Ammeter (IL)**: 300ms timestamp.
- **Ohmmeter (RL)**: 1000ms or 1 ms timestamp.
- **Rolling Average (Avg)**: 2000ms or 2s timestamp.

 ## Run and installation:
 - Clone the repository: `git clone repo`
 - Navigate to the project path and run: `python main.py`

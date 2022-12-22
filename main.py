from circuit import Circuit
from devices import *

if __name__ == '__main__':
    circuit = Circuit()
    voltmeter = Voltmeter(circuit)
    ammeter = Ammeter(circuit)
    ohmmeter = Ohmmeter(voltmeter, ammeter)
    rolling_avg = RollingAverage(voltmeter, ammeter)

    # start the simulation
    circuit.start(voltmeter, ammeter, ohmmeter, rolling_avg)

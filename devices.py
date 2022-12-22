class Voltmeter:
    def __init__(self, circuit):
        self.__circuit = circuit

    def get_voltmeter_value(self):
        return self.__circuit.voltmeter_value()

    def print_voltmeter_value(self, time):
        print('VL = ', self.get_voltmeter_value(), 'V at t =', time / 10, 'S')
        print('==============================================')


class Ammeter:
    def __init__(self, circuit):
        self.__circuit = circuit

    def get_ammeter_value(self):
        return self.__circuit.ammeter_value()

    def print_ammeter_value(self, time):
        print('IL = ', self.get_ammeter_value(), 'mA at t =', time/10, 'S')
        print('==============================================')


class Ohmmeter:
    def __init__(self, voltmeter, ammeter):
        self.__voltmeter = voltmeter
        self.__ammeter = ammeter

    def calculate_resistance_value(self):
        if self.__ammeter.get_ammeter_value() == 0:
            return float('inf')
        else:
            return self.__voltmeter.get_voltmeter_value() / self.__ammeter.get_ammeter_value()

    def print_RL_value(self, time):
        print('RL =', self.calculate_resistance_value(),
              'kΩ at t =', time / 10, 'S')
        print('==============================================')


class RollingAverage(Ohmmeter):
    def __init__(self, voltmeter, ammeter):
        super().__init__(voltmeter, ammeter)
        self.RL_values_list = []

    def calculate_avg(self):
        return sum(self.RL_values_list) / len(self.RL_values_list)

    def print_RL_avg(self, time):
        print('The Average value for RL =', self.calculate_avg(),
              'kΩ in the last 2 seconds from t =', (time/10) - 2, 'S to t =', time/10, 'S')
        print('==============================================')

    def reset_RL_list(self):
        self.RL_values_list = []

    def add_RL_value(self):
        self.RL_values_list.append(self.calculate_resistance_value())

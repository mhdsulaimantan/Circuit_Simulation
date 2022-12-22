'''
Resistance unit in kΩ (Kilo ohm)
Voltage unit in V (volt)
Current unit in mA (milliampere)
Time unit is in mS (millisecond)
'''

RL = 30
VS = 10

class Circuit:
    def __init__(self):
        self.__r1 = 0
        self.__r2 = 100

    def start(self, voltmeter, ammeter, ohmmeter, rolling_avg):
        print('***********************************************************************')
        print('* VL -> Voltmeter value will be print for every 100ms timestamp       *')
        print('* IL -> ammeter value will be print for every 300ms timestamp         *')
        print('* RL -> ohmmeter value will be print for every 1s or 1000ms timestamp *')
        print('* inf -> ∞                                                            *')
        print('***********************************************************************')

        print('The circuit simulation has started:\n')
        print('==============================================')

        # each loop represent 100ms
        for t in range(0, 101):
            self.update_resistances_value(t)

            # collect RL values
            rolling_avg.add_RL_value()

            # timestamp 100ms
            voltmeter.print_voltmeter_value(t)

            # timestamp 300ms
            if t % 3 == 0:
                ammeter.print_ammeter_value(t)

            # timestamp 1s or 1000ms
            if t % 10 == 0:
                ohmmeter.print_RL_value(t)

            # timestamp 2s or 2000ms
            if t != 0 and t % 20 == 0:
                rolling_avg.print_RL_avg(t)
                rolling_avg.reset_RL_list()

        self.restart(voltmeter, ammeter, ohmmeter, rolling_avg)

    def restart(self, voltmeter, ammeter, ohmmeter, rolling_avg):
        ans = input('Do you want to restart the simulation?\n1)Yes 2)No\n')
        if ans in ('1', 'Yes', 'yes'):
            return self.start(voltmeter, ammeter, ohmmeter, rolling_avg)
        elif ans in ('2', 'No', 'no'):
            print('The circuit simulation will stop now!')
        else:
            print('Please enter correct option!')
            self.restart(voltmeter, ammeter, ohmmeter, rolling_avg)

    def voltmeter_value(self):
        if self.__r1 == 0:
            return VS

        elif self.__r2 == 0:
            return 0

        else:
            return VS - (self.total_current() * self.__r1)

    def ammeter_value(self):
        if self.__r2 == 0:
            return 0
        else:
            # IL = I_total - I2
            # V2 = VL
            # IL = I_total - (VL / R2)
            return self.total_current() - (self.voltmeter_value() / self.__r2)

    def total_current(self):
        return VS / self.total_resistance()

    def total_resistance(self):
        if self.__r2 == 0:
            return self.__r1
        else:
            return self.__r1 + pow(1 / self.__r2 + 1 / RL, -1)

    def update_resistances_value(self, time):
        # each step change 1kΩ
        self.__r1 = time * 1
        self.__r2 = 100 - time * 1

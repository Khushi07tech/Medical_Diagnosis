from models.disease import Disease
class Infectious (Disease):

    def __init__(self, name, common_symptoms, severity, treatment, transmission_method, incubation_period):
        super().__init__(name, "Infectious", common_symptoms, severity, treatment)
        self.transmission_method = transmission_method
        self.incubation_period = incubation_period

    def display_info(self):
        super().display_info()
        print (f"Transmission method: {self.transmission_method}")
        print (f"Incubation Period: {self.incubation_period}")

    def is_contagious(self):
        return f"Yes, {self.name} is contagious via {self.transmission_method}"
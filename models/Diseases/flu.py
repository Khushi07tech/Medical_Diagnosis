from models.infectious import Infectious
class Flu (Infectious):
    def __init__(self):
        super().__init__(name= "Influenza",
                         common_symptoms= ["fever", "cough", "sore throat", "body aches", "fatigue", "headache"],
                         severity= "Moderate",
                         treatment = "Rest, fluids, antiviral medication if needed",
                         transmission_method= "Airborne droplets",
                         incubation_period= "1-4 days")
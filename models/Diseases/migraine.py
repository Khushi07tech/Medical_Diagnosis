from models.acute import Acute
class Migraine (Acute):
    def __init__(self):
        super().__init__(name= "Migraine",
                        common_symptoms= ["severe headache", "nausea", "sensitivity to light", "sensitivity to sound", "visual disturbances"],
                        severity= "Moderate",
                        treatment= "Pain relievers, rest in dark quiet room, preventive medication",
                        onset_speed= "Gradual (hours)",
                        typical_duration= "4-72 hours")
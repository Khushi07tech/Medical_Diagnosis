from models.disease import Disease
class Acute (Disease):

    def __init__(self, name, common_symptoms, severity, treatment, onset_speed, typical_duration):
        super().__init__(name, "Acute", common_symptoms, severity, treatment)
        self.onset_speed = onset_speed
        self.typical_duration = typical_duration

    def display_info(self):
        super().display_info()
        print (f"Onset Speed: {self.onset_speed}")
        print (f"Typical Duration: {self.typical_duration}")

    def is_emergency(self):
        if self.severity == "Severe":
            return "Urgent medical attention required"
        else:
            return "No urgent medical attention required"
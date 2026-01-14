class Disease:
    def __init__(self, name, category, common_symptoms, severity, treatment):
        self.name = name
        self.category = category
        self.common_symptoms = common_symptoms
        self.severity = severity
        self.treatment = treatment

    def __str__(self):
        return f"{self.name} ({self.category}) - severity: {self.severity}"

    def display_info(self):
        print ("-" * 25)
        print (f"Disease: {self.name}")
        print (f"Category: {self.category}")
        print (f"Common Symptoms: {self.common_symptoms}")
        print (f"Severity: {self.severity}")
        print (f"Treatment: {self.treatment}")
        print("-" * 25)

    def check_symptoms(self, user_symptoms):
        disease_symptoms = [s.strip().lower() for s in self.common_symptoms]
        user_symptoms = [s.strip().lower() for s in user_symptoms]

        symptoms_match = sum(1 for s in user_symptoms if s in disease_symptoms)

        if not disease_symptoms:
            return 0

        return symptoms_match/len(disease_symptoms) * 100

    def get_recommendation(self):
        if self.severity == "Mild":
            return "Rest at home and monitor symptoms."
        elif self.severity == "Moderate":
            return "Consider consulting a doctor."
        elif self.severity == "Severe":
            return "Seek immediate medical attention."

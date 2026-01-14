from models.chronic import Chronic
class Diabetes (Chronic):
    def __init__(self):
        super().__init__(name= "Type 2 Diabetes",
                        common_symptoms= ["increased thirst", "frequent urination", "fatigue", "blurred vision", "slow healing wounds"],
                        severity= "Mild",
                        treatment= "Lifestyle changes, medication, insulin therapy",
                        management_plan= "Regular blood sugar monitoring, healthy diet, exercise, medication compliance",
                        requires_monitoring= True)

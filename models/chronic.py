from models.disease import Disease
class Chronic (Disease):

    def __init__(self, name, common_symptoms, severity, treatment, management_plan, requires_monitoring):
        super().__init__(name, "Chronic", common_symptoms, severity, treatment)
        self.management_plan = management_plan
        self.requires_monitoring = requires_monitoring

    def display_info(self):
        super().display_info()
        print (f"Management Plan: {self.management_plan}")
        print (f"Monitoring: {'Required' if self.requires_monitoring else 'Not Required'}")

    def get_management_tips(self):
        return self.management_plan
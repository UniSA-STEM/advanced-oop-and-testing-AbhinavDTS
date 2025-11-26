'''
File: animal.py
Author: Abhinav Sharma
ID: 110376072
Username: shaay186
This is my own work as defined by the University's Academic Integrity Policy.
'''
# Represents a health issue for an animal, including its details, severity, and treatment status.


from datetime import date

from datetime import date

class HealthRecord:
    def __init__(self, description, record_date, severity, treatment):
        self.description = description
        self.date = record_date
        self.severity = severity
        self.treatment = treatment
        self.status = "Active"  # Active or Resolved

    def resolve(self):
        self.status = "Resolved"

    def __repr__(self):
        return f"HealthRecord(date={self.date}, severity={self.severity}, status={self.status}, desc='{self.description}')"



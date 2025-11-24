'''
File: animal.py
Author: Abhinav Sharma
ID: 110376072
Username: shaay186
This is my own work as defined by the University's Academic Integrity Policy.
'''
# Represents a health issue for an animal, including its details, severity, and treatment status.

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

#This class serves as the foundation for all animals in the zoo, handling their basic details, behaviours, and any health issues they may develop.

class Animal:
    def __init__(self, name, species, age, category, diet="Omnivore"):
        self.name = name
        self.species = species
        self.age = age
        self.category = category
        self.diet = diet
        self.health_records = []

    def eat(self):
        return f"{self.name} is eating {self.diet}"

    def sleep(self):
        return f"{self.name} is sleeping"

    def make_sound(self):
        return f"{self.name} makes a generic animal sound"

    def add_health_issue(self, description, record_date=None, severity="Low", treatment="None"):
        if record_date is None:
            record_date = date.today().isoformat()
        record = HealthRecord(description, record_date, severity, treatment)
        self.health_records.append(record)

    def get_health_report(self):
        return [
            {
                "description": rec.description,
                "date": rec.date,
                "severity": rec.severity,
                "status": rec.status,
                "treatment": rec.treatment,
            }
            for rec in self.health_records
        ]

    def is_healthy(self):
        # Cannot move if any active health records exist
        for rec in self.health_records:
            if rec.status == "Active":
                return False
        return True





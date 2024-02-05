import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class User:
    def __init__(self, name, level, matric_number, department):
        self.name = name
        self.level = level
        self.matric_number = matric_number
        self.department = department

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nMatric Number: {self.matric_number}\nDepartment: {self.department}"

class AccessPoint:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name} - {self.location}"

class Route:
    def __init__(self, start_point, end_point, distance, vehicle_type, cost):
        self.start_point = start_point
        self.end_point = end_point
        self.distance = distance
        self.vehicle_type = vehicle_type
        self.cost = cost

    def __str__(self):
        return f"{self.start_point.name} to {self.end_point.name} ({self.distance} km) - {self.vehicle_type} - ${self.cost:.2f}"
class TransportationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BingDrive")

        self.current_user = None
        self.access_points = {}
        self.routes = []

        self.selected_start_point = tk.StringVar()
        self.destination_entry = tk.StringVar()

        self.create_login_page()
def create_main_app(self):
    ttk.Label(self.root, text="BingDrive", font=('Helvetica', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(self.root, text=f"Welcome, {self.current_user.name}!", font=('Helvetica', 12)).grid(row=1, column=0,
                                                                                                  columnspan=2, pady=5)

    # Adding access points
    self.add_access_point("ICT", "A")
    self.add_access_point("Clinic", "B")
    self.add_access_point("Portfolio", "C")
    self.add_access_point("Chapel", "D")
    self.add_access_point("Green Plaza", "E")
    self.add_access_point("Clinic Road", "F")
    self.add_access_point("Class", "G")

    # Adding routes
    self.add_route("ICT", "Clinic", 1.5, "Bus", 1.00)
    self.add_route("Clinic", "Portfolio", 0.8, "Walking", 0.00)
    self.add_route("Portfolio", "Chapel", 2.0, "Bicycle", 0.50)
    self.add_route("Chapel", "Green Plaza", 1.0, "Bus", 0.75)
    self.add_route("Green Plaza", "Clinic Road", 1.2, "Walking", 0.00)
    self.add_route("Clinic Road", "Class", 1.5, "Bicycle", 0.50)

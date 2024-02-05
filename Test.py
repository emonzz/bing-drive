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

    def create_login_page(self):
        self.login_frame = ttk.Frame(self.root)
        self.login_frame.grid(row=0, column=0, padx=20, pady=20)
        # center the login frame
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        ttk.Label(self.login_frame, text="Login to BingDrive", font=('Helvetica', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.login_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(self.login_frame)
        self.name_entry.grid(row=1, column=1, pady=5)

        ttk.Label(self.login_frame, text="Level:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.level_entry = ttk.Entry(self.login_frame)
        self.level_entry.grid(row=2, column=1, pady=5)

        ttk.Label(self.login_frame, text="Matric Number:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.matric_number_entry = ttk.Entry(self.login_frame)
        self.matric_number_entry.grid(row=3, column=1, pady=5)

        ttk.Label(self.login_frame, text="Department:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.department_entry = ttk.Entry(self.login_frame)
        self.department_entry.grid(row=4, column=1, pady=5)

        ttk.Button(self.login_frame, text="Login", command=self.login).grid(row=5, column=0, columnspan=2, pady=10)

    def login(self):
        name = self.name_entry.get()
        level = self.level_entry.get()
        matric_number = self.matric_number_entry.get()
        department = self.department_entry.get()

        self.current_user = User(name, level, matric_number, department)

        # Destroy the login frame and create the main app window
        self.login_frame.destroy()
        self.create_main_app()

    def create_main_app(self):
        ttk.Label(self.root, text="BingDrive", font=('Helvetica', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.root, text=f"Welcome, {self.current_user.name}!", font=('Helvetica', 12)).grid(row=1, column=0, columnspan=2, pady=5)

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

        # Dropdown menu for selecting start point
        ttk.Label(self.root, text="Select Start Point:").grid(row=2, column=0, sticky=tk.W, pady=5)
        start_point_menu = ttk.Combobox(self.root, textvariable=self.selected_start_point)
        start_point_menu['values'] = list(self.access_points.keys())
        start_point_menu.grid(row=2, column=1, pady=5)
        start_point_menu.set("ICT")

        # Input form for entering destination
        ttk.Label(self.root, text="Enter Destination (End Point):").grid(row=3, column=0, sticky=tk.W, pady=5)
        destination_entry = ttk.Entry(self.root, textvariable=self.destination_entry)
        destination_entry.grid(row=3, column=1, pady=5)

        ttk.Button(self.root, text="Calculate Cost and Time", command=self.calculate_cost_and_time).grid(row=4, column=0, columnspan=2, pady=10)

        # Profile section
        ttk.Label(self.root, text="User Profile", font=('Helvetica', 12, 'bold')).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Label(self.root, text=str(self.current_user)).grid(row=6, column=0, columnspan=2, pady=5)

        # Logout button
        ttk.Button(self.root, text="Logout", command=self.logout).grid(row=7, column=0, columnspan=2, pady=10)

    def calculate_cost_and_time(self):
        start_point = self.selected_start_point.get()
        destination = self.destination_entry.get()

        route = self.find_route(start_point, destination)

        if route:
            cost_label = ttk.Label(self.root, text=f"Cost: ${route.cost:.2f}")
            cost_label.grid(row=8, column=0, columnspan=2, pady=5)

            distance_label = ttk.Label(self.root, text=f"Distance: {route.distance} km")
            distance_label.grid(row=9, column=0, columnspan=2, pady=5)

            estimated_time_label = ttk.Label(self.root, text=f"Estimated Time: {self.calculate_estimated_time(route.distance)} minutes")
            estimated_time_label.grid(row=10, column=0, columnspan=2, pady=5)
        else:
            ttk.Label(self.root, text="Route not found. Please check your input.").grid(row=8, column=0, columnspan=2, pady=5)

    def find_route(self, start_point, end_point):
        for route in self.routes:
            if route.start_point.name == start_point and route.end_point.name == end_point:
                return route
        return None

    def calculate_estimated_time(self, distance):
        # Assuming an average speed of 30 km/h for simplicity
        average_speed = 30
        time_in_hours = distance / average_speed
        time_in_minutes = time_in_hours * 60
        return int(time_in_minutes)

    def add_access_point(self, name, location):
        access_point = AccessPoint(name, location)
        self.access_points[name] = access_point

    def add_route(self, start_point, end_point, distance, vehicle_type, cost):
        route = Route(
            self.access_points[start_point],
            self.access_points[end_point],
            distance,
            vehicle_type,
            cost
        )
        self.routes.append(route)

    def logout(self):
        # Destroy the current window and recreate the login page
        self.root.destroy()
        root = tk.Tk()
        app = TransportationApp(root)
        root.mainloop()

def main():
    root = tk.Tk()
    app = TransportationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import os
import psutil
import matplotlib.pyplot as plt

# function to get active services
def get_active_services():
    services = {}
    for proc in psutil.process_iter():
        try:
            service_name = proc.name()
            cpu_usage = proc.cpu_percent()
            services[service_name] = cpu_usage
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return services

# function to display service usage
def display_service_usage(services):
    plt.pie(services.values(), labels=services.keys(), autopct='%1.1f%%')
    plt.title('CPU Usage by Services')
    plt.axis('equal')
    plt.show()


# call the function
if __name__ == "__main__":
    active_services = get_active_services()
    display_service_usage(active_services)

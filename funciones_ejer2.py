def mission_report(pre_launch_time, flight_time, destination, external_tank, main_tank):
    return f"""
    Mission to {destination}
    Total travel time: {pre_launch_time + flight_time} minutes
    Total fuel left: {external_tank + main_tank} gallons
    """
print("Impresión del 1er resultado:::::::::\n")
print(mission_report(14, 51, "Moon", 200000, 300000))

def mission_report(destination, *minutes, **fuel_reservoirs):
    return f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
print("Impresión del 2do resultado:::::::::\n")
print(mission_report("Moon", 10, 15, 51, main=300000, external=200000))

def mission_report(destination, *minutes, **fuel_reservoirs):
    main_report = f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
    for tank_name, gallons in fuel_reservoirs.items():
        main_report += f"{tank_name} tank --> {gallons} gallons left\n"
    return main_report

print("Impresión del 3er resultado:::::::::\n")
print(mission_report("Moon", 8, 11, 55, main=300000, external=200000))
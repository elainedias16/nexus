def get_component_by_id(component_id: int):
    return {"id": 1, "well_name": "CPU", "component_type": "Processor", "install_timestamp": "2023-10-01", "manufacterer": "Intel", "phase_num": "INCONEL 718"},


def get_all_components():
    return [
        {"id": 1, "well_name": "CPU", "component_type": "Processor", "install_timestamp": "2023-10-01", "manufacterer": "Intel", "phase_num": "INCONEL 718"},
        {"id": 2, "well_name": "Memória", "component_type": "Memory", "install_timestamp": "2023-10-02", "manufacterer": "Kingston", "phase_num": "VT HC"},
        {"id": 3, "well_name": "Disco", "component_type": "Storage", "install_timestamp": "2023-10-03", "manufacterer": "Samsung", "phase_num": "CR13"},
       
    ]


def get_components_by_criteria(component_type: str = None, install_timestamp: str = None, manufacterer: str = None):
    all_components = get_all_components()

    filtered_components = [
        component for component in all_components
        if (install_timestamp is None or component["install_timestamp"] == install_timestamp) and
           (manufacterer is None or component["manufacterer"] == manufacterer) and
           (component_type is None or component["component_type"] == component_type)
    ]
    return filtered_components


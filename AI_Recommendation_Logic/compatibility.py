def cpu_motherboard_compatible(cpu, motherboard):

    if cpu["CPU_Socket"] == motherboard["CPU_Socket"]:
        return True

    return False
def motherboard_ram_compatible(motherboard, ram):

    if motherboard["RAM_Type"] == ram["RAM_Type"]:
        return True

    return False

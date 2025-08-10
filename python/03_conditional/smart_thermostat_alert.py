device_status = "active"
temperature = 40

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Normal temperature")
else:
    print("Device is offline")
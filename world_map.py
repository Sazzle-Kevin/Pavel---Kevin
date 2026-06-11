import location

world_map = [location.dorf, location.sollum, location.monda]

current_location = location.dorf


def open_map():
    print("Karte: ")
    for location in world_map:
        if location.name == current_location.name:
            print(">>", location.name, "<<")
            continue
        print(location.name)

    while True:
        world_map_input = input("Wohin möchtest du reisen?").lower()
        if world_map_input in world_map or world_map_input == "exit":
            current_location = location.world_map_input.lower()
            return

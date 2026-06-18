################################################################################
#                                 WORLD MAP                                    #
################################################################################

import location

################################################################################
#                              KLASSE: WORLDMAP                                #
################################################################################


class WorldMap:

    def __init__(self):
        self.locations = [location.dorf, location.monda, location.sollum]

    def append(self, location):
        if location not in self.locations:
            self.locations.append(location)

    def print(self):
        for location in self.locations:
            if location == player.location:
                print(">>", location.name, "<<")
            else:
                print(location.name)

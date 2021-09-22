from model import *


class MyStrategy:
    def __init__(self):
        pass
    def get_action(self, game: Game) -> Action:
        moves = []
        builds = []
        start_planet = game.planets[0]
        start_planet_coords = (start_planet.x, start_planet.y)
        quarry_properties = game.building_properties[BuildingType.QUARRY]
        index_distance_list = []
        for index, planet in enumerate(game.planets):
            index_distance = {index:self.calc_distance(start_planet.x,
            start_planet.y, planet.x, planet.y)}
            print("INDEX",index)
            print("PLANET", planet)
            index_distance_list.append(index_distance)
        print(index_distance_list)

        # for planet in game.planets:
        #     print(self.calc_distance(start_planet.x, start_planet.y,
        #                         planet.x, planet.y))

        # current_planet_resource_type = planet.harvestable_resource
        # print(start_planet_coords)
        # print(game.planets)
        return Action([], [])

    def calc_distance(self, start_x, start_y, finish_x, finish_y):
        x = abs(finish_x - start_x)
        y = abs(finish_y - start_y)
        return x + y
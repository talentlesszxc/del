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
        list_of_indexes = []
        list_of_values = []
        for index, planet in enumerate(game.planets):
            list_of_indexes.append(index) # получить список индексов планет
            list_of_values.append(self.calc_distance(start_planet.x,
            start_planet.y, planet.x, planet.y)) # получить список расстояния до каждой планеты 
            dictionary = dict(zip(list_of_indexes, list_of_values))
            sorted_keys = sorted(dictionary, key = dictionary.get)
            new_dict = {}
            for x in sorted_keys:
                new_dict[x] = dictionary[x]
                    # готовый словарь, отсортированный в порядке дальности планет от ближайшей к самой дальней
                    # дальше отправлять челов на эти планеты + чекать что там можно построить и строить
           # index_distance = {};
           # index_distance.update({index:self.calc_distance(start_planet.x,
           # start_planet.y, planet.x, planet.y)})
           # print("INDEX",index)
           # print("PLANET", planet)
           # index_distance_list.append(index_distance)            
        #prin#t(index_distance_list)
        print#(index_distance)
        print(new_dict)

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

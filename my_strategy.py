from model import *


class MyStrategy:
    def __init__(self):
        pass
    def get_action(self, game: Game) -> Action:
        moves = []
        builds = []
        start_planet = game.planets[0]
        # start_planet_coords = (start_planet.x, start_planet.y)
        # quarry_properties = game.building_properties[BuildingType.QUARRY]
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
        planets_list = list(new_dict.keys());
        print(planets_list)
        print("QUarry prop: ", game.building_properties[BuildingType.QUARRY])
        stone_planets = []

        print(sum(x.player_index for x in game.planets[0].worker_groups))

        for i in range(len(planets_list)-1):
            # print(sum(x.number for x in game.planets[0].worker_groups))
            print(f"Planet {planets_list[i]} has {sum(x.number for x in game.planets[i].worker_groups)} workers")
            print(f"Planet {planets_list[i]} has {game.planets[i].harvestable_resource} resource type")
            owner = sum(x.player_index for x in game.planets[planets_list[i]].worker_groups)
            if game.planets[planets_list[i]].harvestable_resource == Resource.STONE and owner != 1:
                stone_planets.append(planets_list[i])
            print("Stone planets: ", stone_planets)

            for i in range(len(stone_planets)-1):
                my_workers = sum(x.number for x in game.planets[stone_planets[i]].worker_groups)
                # owner = sum(x.player_index for x in game.planets[stone_planets[i+1]].worker_groups)
                print(f"On planet {stone_planets[i]} owner is {owner}")
                if my_workers > 100:
                    print(f"Отправляем челиков с планеты {stone_planets[i]} на планету {stone_planets[i+1]}")
                    moves.append(MoveAction(stone_planets[i], stone_planets[i+1], 100, Resource.STONE))
                    builds.append(BuildingAction(stone_planets[i+1], BuildingType.QUARRY))
                # if (sum(x.number for x in game.planets[stone_planets[i]].worker_groups) > 100) and
                #     (sum(x.player_index for x in game.planets[stone_planets[i]].worker_groups) != 1):
                #     moves.append(MoveAction(stone_planets[i], stone_planets[i+1], 100, Resource.STONE))
                #     builds.append(BuildingAction(stone_planets[i+1], BuildingType.QUARRY))



        # for i in range(len(stone_planets)-1):
        #     if sum(x.number for x in game.planets[0].worker_groups) > 100:
        #         builds.append(BuildingAction(stone_planets[i+1], BuildingType.QUARRY))
        #         moves.append(MoveAction(stone_planets[i], stone_planets[i+1], 100, Resource.STONE))
        # if sum(x.number for x in game.planets[0].worker_groups) > 100:
        #
        #     # moves.append(MoveAction(0, stone_planets[1], 100, Resource.STONE))
        #     # builds.append(BuildingAction(stone_planets[1], BuildingType.QUARRY))
        #     # moves.append(MoveAction(0, stone_planets[2], 100, Resource.STONE))
        #     # builds.append(BuildingAction(stone_planets[2], BuildingType.QUARRY))
        #     moves.append(MoveAction(0, stone_planets[1], 100, Resource.STONE))
        #     builds.append(BuildingAction(stone_planets[1], BuildingType.QUARRY))
        # if sum(x.number for x in game.planets[stone_planets[1]].worker_groups) > 100:
        #     moves.append(MoveAction(stone_planets[1], stone_planets[2], 100, Resource.STONE))
        #     builds.append(BuildingAction(stone_planets[2], BuildingType.QUARRY))


            # if game.planets[i].harvestable_resource == Resource.STONE:
            #     moves.append(MoveAction(0, i, 20, Resource.STONE))

        # for i in range(len(planets_list)):
        #     next_planet = game.planets[i]
        #
        #     if next_planet.harvestable_resource == Resource.STONE:
        #         moves.append(MoveAction(i, i+1, 20, Resource.STONE))

        # print(sum(x.number for x in start_planet.worker_groups))
        # print(game.building_properties[BuildingType.QUARRY])
        #
        # for key in new_dict.keys():
        #     not_busy_workers = sum(x.number for x in start_planet.worker_groups) - 20
        #     list_of_keys = list(new_dict.keys())
        #     print(list_of_keys)
        #     if game.planets[key].harvestable_resource == 0:
        #         moves.append(MoveAction(0, key, 10, Resource.STONE))


        # print(new_dict)
        # for key in new_dict.keys():
        #     resource = game.planets[key].harvestable_resource
        #     if resource == 0:
        #         moves.append(MoveAction(0, key, 10, Resource.STONE))
        #         builds.append(BuildingAction(key, BuildingType.QUARRY))

        return Action(moves, builds)

    def calc_distance(self, start_x, start_y, finish_x, finish_y):
        x = abs(finish_x - start_x)
        y = abs(finish_y - start_y)
        return x + y

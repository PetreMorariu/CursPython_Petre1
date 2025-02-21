import copy

l_add = lambda x, y: x +y

numbers = [4, 345, 6546, 3 ,100, -3]
letters = ['x', 'a', 'f', 'b', 'd']

players = [{
    "first_name":"John",
    "last_name":"Doe",
    "rank":3,
    "league":"beginner"
}, {
    "first_name":"Alex",
    "last_name":"Smith",
    "rank":1,
    "league":"beginner"
},{
    "first_name":"Dan",
    "last_name":"Black",
    "rank":5,
    "league":"beginner"
}]

def extract_rank_from_obj(player):
    return player["rank"]

def update_player(player):
    temp_player = copy.deepcopy(player)
    if player["rank"] > 3:
        temp_player["league"] = "Advanced"
    return temp_player

def choose_rank_player(player):
    return player["rank"] > 3

number_list = [2, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100, 500, 1000, 20000]
number_list_sq = list(map(lambda x: x ** 2, number_list))



def main():
     sorted_numbers = sorted(numbers)
     print(sorted_numbers)
     sorted_leters = sorted(letters)
     print(sorted_leters)
     print(sorted(players, key= extract_rank_from_obj))
     upd_players = list(map(update_player, players))
     print(upd_players)

     filtered_players = list(filter(choose_rank_player, players))
     print(filtered_players)

     zipped_nr= list(zip(number_list,number_list_sq))
     print(zipped_nr)



if __name__ == '__main__':
    main()
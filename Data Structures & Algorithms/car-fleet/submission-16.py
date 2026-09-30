class Solution:
    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #     # # maintain a stack of the car index of the leading
    #     # # car for every 'destination fleet' in increasing
    #     # # order of arrival time.
    #     # # then loop through the stack to find where this
    #     # # car belongs

    #     # fleet_leaders = [0]
    #     # for car_index, car_position in enumerate(position[1:],1):
    #     #     soonest_arrival_time = (target - car_position) / speed[car_index]

    #     #     # move all fleet_leaders that arrive before the
    #     #     # current car to temp:
    #     #     # the current car can't arrive with any of them
    #     #     temp = []
    #     #     while fleet_leaders:
    #     #         i = fleet_leaders[-1]
    #     #         i_arrival = (target - position[i]) / speed[i]
    #     #         if position[i] > car_position:
    #     #             # car_i started ahead
    #     #             if i_arrival < soonest_arrival_time:
    #     #                 # car_i started ahead and arrived before the current car
    #     #                 # could have, so the current car never caught up, and
    #     #                 # can't be in car_i's fleet.
    #     #                 # Check the next fleet leader.
    #     #                 temp.append(fleet_leaders.pop())
    #     #             else:
    #     #                 # car_i started ahead, but the current car caught up,
    #     #                 # so the current car is in this, or a later, fleet.
    #     #                 # in particular it is not a new fleet leader.
    #     #                 # so break.
    #     #                 break
    #     #         else:  # car_i started behind
    #     #             if i_arrival <= soonest_arrival_time:
    #     #                 # car_i started behind the current car, but caught up to it.
    #     #                 # car_i is in the same fleet, but current car is the leader.
    #     #                 # so replace car_i by the current car in the leader stack.
                        
    #     #                 # remove this leader and all leaders after this down the 
    #     #                 # stack that would have finished with or before the 
    #     #                 # current car
    #     #                 fleet_leaders.pop()
    #     #                 while fleet_leaders:
    #     #                     i = fleet_leaders[-1]
    #     #                     i_arrival = (target - position[i]) / speed[i]
    #     #                     if i_arrival <= soonest_arrival_time:
    #     #                         fleet_leaders.pop()
    #     #                     else:
    #     #                         break
    #     #                 fleet_leaders.append(car_index)
    #     #             else:
    #     #                 # car_i never caught up to the current car
    #     #                 # so the current car is the leader of a new fleet.
    #     #                 # add it to the top of the fleet leader stack
    #     #                 fleet_leaders.append(car_index)
    #     #             break
    #     #     if not fleet_leaders:
    #     #     # if there are no more fleet leaders
    #     #     # then the current car started behind all of the fleet leaders
    #     #     # and never caught up to any of them, so it is a new fleet leader
    #     #     # at the back of the pack.
    #     #         fleet_leaders.append(car_index)

    #     #     # move all the leaders in temp, that started ahead and finished
    #     #     # earlier back onto the top of fleet_leaders
    #     #     while temp:
    #     #         fleet_leaders.append(temp.pop())
    #     # return len(fleet_leaders)

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrival_time = [-1] * target
        for i, pos in enumerate(position):
            arrival_time[pos] = (target - pos) / speed[i]

        count = 0
        current_arrival_time = 0
        for p in reversed(sorted(position)):
            if arrival_time[p] > current_arrival_time:
                current_arrival_time = arrival_time[p]
                count += 1
        return count
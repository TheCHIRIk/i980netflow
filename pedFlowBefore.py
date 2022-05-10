"""From Bradley, Hax and Maganti, 'Applied Mathematical Programming', figure 8.1."""
from ortools.graph import pywrapgraph


def main():
    """MinCostFlow simple interface example."""
    # Instantiate a SimpleMinCostFlow solver.
    min_cost_flow = pywrapgraph.SimpleMinCostFlow()

    # Define four parallel arrays: sources, destinations, capacities,
    # and unit costs between each pair. For instance, the arc from node 0
    # to node 1 has a capacity of 15.
    start_nodes = [0,  0, 1,  1, 2,  2, 3,  3,  4,  4, 5,  5, 6,  6, 7, 7,  8, 9,  10, 11, 13, 13, 14, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 21, 21, 22, 23, 26, 27]
    end_nodes =   [1,  7, 2,  8, 3,  9, 4,  10, 5,  3, 19, 4, 13, 7, 8, 14, 9, 10, 17, 4,  14, 20, 15, 21, 16, 15, 17, 16, 18, 22, 17, 23, 19, 24, 18, 27, 21, 25, 22, 26, 26, 27, 26]
    capacities =  [80 for x in range(len(start_nodes))]
    unit_costs =  [2,  3, 1,  2, 1,  4, 2,  1,  1,  2, 7,  1, 5,  1, 1, 5,  1, 1,  5,  4,  1,  3,  1,  4,  1,  1,  1,  1,  2,  6,  2,  4,  3,  4,  3,  7,  2,  6,  5,  1,  3,  1,  1]

    # Define an array of supplies at each node.     10     12       15     16          20                              27
    supplies = [20, 15, 0, 25, 0, 15, 0, 50, 0, 50, 0, 50, 0, 0, 0, -10, -40, 0, 0, 0, 0, -30, 0, -30, -15, -20, -50, -30]
    print(len(supplies))
    #            supply: total of 180
    # Add each arc.
    for arc in zip(start_nodes, end_nodes, capacities, unit_costs):
        min_cost_flow.AddArcWithCapacityAndUnitCost(arc[0], arc[1], arc[2],
                                                    arc[3])

    # Add node supply.
    for count, supply in enumerate(supplies):
        min_cost_flow.SetNodeSupply(count, supply)

    # Find the min cost flow.
    status = min_cost_flow.Solve()

    if status != min_cost_flow.OPTIMAL:
        print('There was an issue with the min cost flow input.')
        print(f'Status: {status}')
        exit(1)
    print('Time travelled across all pedestrians: ', min_cost_flow.OptimalCost())
    print('')
    print('Time travelled per pedestrian:  ', min_cost_flow.OptimalCost()/205.0)
    print('')
    print(' Arc   Flow / Capacity  Cost')
    for i in range(min_cost_flow.NumArcs()):
        cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
        print('%1s -> %1s    %3s   / %3s   %3s' %
              (min_cost_flow.Tail(i), min_cost_flow.Head(i),
               min_cost_flow.Flow(i), min_cost_flow.Capacity(i), cost))


if __name__ == '__main__':
    main()
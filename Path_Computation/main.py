from nodes import *
import argparse
import sys

situations = [
    'video',
    'audio',
    'large_file',
    'financial',
    'gaming',
]

'''
OBJECTIVE

1.) Given a topology of 9 nodes, and one of the above situations, create a function that calculates the relative weight
of the edge between each of the nodes in the topology. This function must be dynamic, in the sense that it has to 
adapt the calculation of the weights according to the situation. You must take account of each factor of the two nodes
when you are calculating the edge weight.

2.) Create a shortest path function once the weights have been computed given the start node A (accessible by topo['A'])
to the end node H (accessible by topo['H'])

NOTES (See the nodes file for the code):
- The connect_topo function returns a dictionary of all the Nodes in the topology, where the keys are the labels of the
nodes, and the paired value is the corresponding Node. Each Node has an 'edges' attribute which is a dictionary of all
the neighbours to that node - keys are the labels of the neighbour, and the value is the weight of the edge between 
those two nodes. The weights are defaulted to 0. 
'''


# Takes in parsed arg
def start(args):
    create_topo(args=args)
    topo = connect_topo()

    '''-+-+-+-+-+-+-+DO NOT CHANGE ABOVE-+-+-+-+-+-+-+'''

    # Insert your code here...
    # Feel free to use as many auxiliary and helper functions as you want.

    '''-+-+-+-+-+-+-+DO NOT CHANGE BELOW-+-+-+-+-+-+-+'''

    # This prints all nodes + their attributes in the network
    for label, node in topo.items():
        print(node)


def parse_input():
    parser = argparse.ArgumentParser(description='Argument parser for Cisco@McGill Python challenge')
    parser.add_argument(
        '-s', '--situation', help='Situation in question for node traversal', type=str, required=True
    )
    parser.add_argument(
        '-f', '--fix', help='Assign seed to network topology for debugging', type=int, default=0, required=False
    )
    return parser.parse_known_args()


if __name__ == '__main__':
    args, unknown = parse_input()
    if args.situation not in situations:
        print('Unrecognized argument for situation, try again...')
        sys.exit(0)
    else:
        start(args)

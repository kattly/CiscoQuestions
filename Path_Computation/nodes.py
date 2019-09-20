import sys
import random

# Global Variables

ALL_NODES = {}     # Aggregate of nodes that make the graph ; keys are labels, and values are corresponding NetworkNodes

LABELS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
]


def create_topo(args):
    if args.fix != 0:
        random.seed(args.fix)

    global LABELS
    for label in LABELS:
        ALL_NODES[label] = NetworkNode(
            label=label,
            bandwidth=random.randint(500, 5000),
            congestion=random.randint(1, 10),
            latency=random.randint(1, 10),
            hop_count=random.randint(1, 64),
            reliability=random.randint(1, 10),
            security=random.randint(1, 5),
            edges=None      # connecting the graph together handled in separate function
        )

    return ALL_NODES               # all nodes created are returned to connect


def reset_topo():                  # returns deep copy of all nodes for error handling
    global ALL_NODES
    return ALL_NODES.copy()


def connect_topo():         # static connection of all nodes - takes in ALL_NODES copy as arg, and inits 'edges'
    global ALL_NODES
    ALL_NODES['A'].edges = {'B': 0, 'C': 0, 'I': 0}
    ALL_NODES['B'].edges = {'A': 0, 'C': 0, 'D': 0}
    ALL_NODES['C'].edges = {'A': 0, 'B': 0, 'I': 0, 'E': 0}
    ALL_NODES['D'].edges = {'B': 0, 'E': 0}
    ALL_NODES['E'].edges = {'D': 0, 'C': 0, 'F': 0}
    ALL_NODES['F'].edges = {'E': 0, 'G': 0, 'H': 0}
    ALL_NODES['G'].edges = {'F': 0, 'H': 0}
    ALL_NODES['H'].edges = {'F': 0, 'G': 0}
    ALL_NODES['I'].edges = {'A': 0, 'C': 0}
    return ALL_NODES.copy()


def add_weight(a: str, b: str, weight):
    global ALL_NODES
    try:
        node_a = ALL_NODES[a]
        node_b = ALL_NODES[b]
    except KeyError as e:
        print('Node label passed into add_weight function could not be found...\n{}'.format(e))
        sys.exit(0)

    try:
        node_a.edges[b] = weight
        node_b.edges[a] = weight
    except KeyError as e:
        print('Node labels passed into add_weight function are not neighbours...\n{}'.format(e))

    return ALL_NODES.copy()


class NetworkNode():

    def __init__(self, label=None, bandwidth=None, congestion=None, latency=None, hop_count=None,
                 reliability=None, security=None, load=None, edges: dict = None):
        self.label = label
        self.bandwidth = bandwidth
        self.congestion = congestion
        self.latency = latency
        self.hop_count = hop_count
        self.reliability = reliability
        self.security = security
        self.load = load
        # Dict where keys are the labels of the neighbouring nodes, and the values are weights (of the factors above)
        self.edges = edges

    def __str__(self):
        print('\nNode {}'.format(self.label))
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+')
        for attr, value in self.__dict__.items():
            print('{} - {}'.format(attr, value))
        return ""

    def get_bandwidth(self):
        x = self.bandwidth
        return x

    def get_congestion(self):
        x = self.congestion
        return x

    def get_latency(self):
        x = self.latency
        return x

    def get_hops(self):
        x = self.hop_count
        return x

    def get_reliability(self):
        x = self.reliability
        return x

    def get_security(self):
        x = self.security
        return x

    def get_load(self):
        x = self.load
        return x

    def get_edges(self):
        return self.edges.copy()    # return deep copy of all neighbouring nodes for that node

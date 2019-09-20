# Cisco @ McGill :canada: - Python Challenge :snake:

**Author** - Gaurav Karna (_gkarna@cisco.com_ | _gaurav.karna@mail.mcgill.ca_)

A network topology is at essence a structured organization of nodes. These nodes in the real world can be anything, from routers and switches, to servers and hosts. 

In this challenge, you are given a sample network topology shown below, with nodes A-H. These nodes are simply instances of the ```NetworkNode``` class in ```nodes.py```. See [NetworkNode](https://wwwin-github.cisco.com/gkarna/Cisco-McGill-Python-Challenge/blob/186ed0b7031b4a443e1bca5f7895ae33f9d29b2f/nodes.py#L53) for more information.

![graph screenshot](https://i.ibb.co/HHCLYwy/Screen-Shot-2019-08-14-at-9-46-31-AM.png)

## Objectives

You have two objectives to complete. We encourage you to think about the decisions carefully you make throughout the challenge, as we will not only be assessing the functionality of your code, but also why you chose to do the objective the way you did.

In this challenge, you are presented with the above network topology, and the following 5 situations:
  - video
  - audio
  - large file transfer
  - financial transactions
  - gaming

For a minimum of 2 of the situations, your objectives are:
  1. Given a topology of 9 nodes, and one of the above situations, create a function that calculates the relative weight
of the edge between each of the nodes in the topology. This function must be dynamic, in the sense that it has to 
adapt the calculation of the weights according to the situation. You must take account of each factor of the two nodes
when you are calculating the edge weight.

  2. Create a shortest path function once the weights have been computed given the start node A (accessible by ```topo['A']```) to the end node H (accessible by ```topo['H']```)
  
You are welcome to use helper functions and establish your own control flow.

## Notes
The ```connect_topo``` [function](https://wwwin-github.cisco.com/gkarna/Cisco-McGill-Python-Challenge/blob/186ed0b7031b4a443e1bca5f7895ae33f9d29b2f/nodes.py#L39) returns a deep copy of the network topology, known as [ALL_NODES](https://wwwin-github.cisco.com/gkarna/Cisco-McGill-Python-Challenge/blob/186ed0b7031b4a443e1bca5f7895ae33f9d29b2f/nodes.py#L6) in ```nodes.py```. 

The ```topo``` variable is a dictionary, where the keys are the **labels of the nodes**, and the paired value is the **corresponding ```NetworkNode``` object**. 

### NetworkNode Class
Each ```NetworkNode``` is an object with the following attributes:
  - ```label``` - a ```str``` denoting the node's label (A - H)
  
  - ```bandwidth``` - a ```int``` representing the capacity of data throughput through the node. A higher bandwidth value means that the node can handle more traffic at a higher frequency
  
  - ```congestion``` - a ```int``` representing the current congestion in the node. A higher congestion value means that the node's bandwidth is being approached and any traffic going through it is likely going to suffer delays. 
  
  - ```latency``` - a ```int``` representing the node's latency, which is a measure of the amount of time it takes to send information from one node to the next. Higher latency values indicate worse connections in the network and can cause delays in traffic.
  
  - ```hop_count``` - a ```int``` representing the number of intermediate points that traffic must go through between two nodes. A higher hop count signifies more delay between two nodes in the network. For example, if node A has a hop count of 5, then assume that between moving from A to any other node that A is connected to - the traffic must go through 5 intermediate devices. 
  
  - ```reliability``` - a ```int``` representing the reliability of the node itself. In the real network, devices are almost never homogeneous. There are devices from several vendors in a variety of different configurations. A higher reliability value means that node is less likely to fail.
  
  - ```security``` - a ```int``` representing the security level of the node. Although all devices on the network are held to a high standard of security, some traffic is more privileged than others. A higher security value represents a higher security threshold for that node, at the compromise of suffering more delays in traffic.
  
  - ```edges``` - a ```dict``` representing all neighbouring nodes to the current code. In this dictionary, the keys are the **labels of the neighbouring nodes**, and the values are the **corresponding weight of the edge between those two ```NetworkNode``` objects**. For example, to iterate through node A's neighbours:
  
  ```python
        for label, neighbour in topo['A'].edges.items():
            print('Neighbour {} to node A, with security value {}'.format(label, topo[label].security))
  ```

### Seeding and Randomization
We have randomized the attribute values for each of the nodes with each run of the program to put the emphasis of the challenge on your weight calculation algorithm.

However, you are welcome to add the ```-f``` or ```-fix``` flag when you run your code to attach a seed to the randomization, so that it is easier to write and debug the code.

Run your program like this: ```python main.py -s gaming```. Feel free to change gaming to any of the situations listed above as you desire, and attach a ```-f``` for fixed randomization.

### Weight Calculation
After you have made your weight calculation algorithm and want to move on to adding the weights to the graph, you are expected to use the ```add_weight``` function provided to you in the ```nodes.py``` file.

For example, to add a weight of 6 between A and B, simply do ```topo = add_weight('A', 'B', 6)```. The function will return the new network topology in the form of a dictionary again, and the old one will be garbage collected.

If you want to add a single weight of 6 between A and all of its neighbours:
```python
    for label, neighbour in topo['A'].edges.items():
        add_weight('A', label, 6)
``` 


### Helpful Tip :bulb:
We wanted to make this more of a cognitive challenge rather than a programming one. Thus, we would like to mention that we are more interested in how you design your weight calculation algorithm in relation to the situation at hand. We are looking forward to observe how and why you prioritized certain node factors over others in your weight calculation in the context of one of the situations we provided.

**Good luck! Best or most successful attempt is guaranteed a _first-round interview_ for a position at Cisco!**

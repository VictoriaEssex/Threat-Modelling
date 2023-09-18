#import the following libraries to create and visualise the graph/ attack tree
import networkx as nx
import matplotlib.pyplot as plt

#create an empty attack tree graph
Graph = nx.DiGraph()

#Define variables and assign them numberical values
spoofingDamage = 10
spoofingReproducibility = 5
spoofingExploitability = 5
spoofingAffectedUsers = 10
spoofingDiscoverability = 8
spoofingProbability = spoofingDamage + spoofingReproducibility + spoofingExploitability + spoofingAffectedUsers + spoofingDiscoverability

tamperingDamage = 10
tamperingReproducibility = 7.5
tamperingExploitability = 2.5
tamperingAffectedUsers = 10
tamperingDiscoverability = 5
tamperingProbability = tamperingDamage + tamperingReproducibility + tamperingExploitability + tamperingAffectedUsers + tamperingDiscoverability

repudiationDamage = 10
repudiationReproducibility = 10
repudiationExploitability = 5
repudiationAffectedUsers = 6
repudiationDiscoverability = 0
repudiationProbability = repudiationDamage + repudiationReproducibility + repudiationExploitability + repudiationAffectedUsers + repudiationDiscoverability

InformationClosureDamage = 10
InformationClosureReproducibility = 10
InformationClosureExploitability = 5
InformationClosureAffectedUsers = 6
InformationClosureDiscoverability = 0
InformationClosureProbability = InformationClosureDamage + InformationClosureReproducibility + InformationClosureExploitability + InformationClosureAffectedUsers + InformationClosureDiscoverability

DenialOfServiceDamage = 10
DenialOfServiceReproducibility = 5
DenialOfServiceExploitability = 2.5
DenialOfServiceAffectedUsers = 10
DenialOfServiceDiscoverability = 8
DenialOfServiceProbability = DenialOfServiceDamage + DenialOfServiceReproducibility + DenialOfServiceExploitability + DenialOfServiceAffectedUsers + DenialOfServiceDiscoverability

ElevationOfPriviledgeDamage = 10
ElevationOfPriviledgeReproducibility = 5
ElevationOfPriviledgeExploitability = 2.5
ElevationOfPriviledgeAffectedUsers = 10
ElevationOfPriviledgeDiscoverability = 8
ElevationOfPriviledgeProbability = ElevationOfPriviledgeDamage + ElevationOfPriviledgeReproducibility + ElevationOfPriviledgeExploitability + ElevationOfPriviledgeAffectedUsers + ElevationOfPriviledgeDiscoverability

#creating/ adding different nodes using the NetworkX library
# The different nodes represent the STRIDE model, along with making use of the DREAD rating system
Graph.add_node('Threat')
#Create the node name and assign different attributes to the node
Graph.add_node('Spoofing', 
            damage=spoofingDamage, 
            reproducibility=spoofingReproducibility, 
            exploitability=spoofingExploitability, 
            AffectedUsers=spoofingAffectedUsers, 
            discoverability=spoofingDiscoverability, 
            probability=spoofingProbability)

Graph.add_node('Tampering', 
            damage=tamperingDamage, 
            reproducibility=tamperingReproducibility, 
            exploitability=tamperingExploitability, 
            AffectedUsers=tamperingAffectedUsers, 
            discoverability=tamperingDiscoverability, 
            probability=tamperingProbability)

Graph.add_node('Repudiation', 
            damage=repudiationDamage, 
            reproducibility=repudiationReproducibility, 
            exploitability=repudiationExploitability, 
            AffectedUsers=repudiationAffectedUsers, 
            discoverability=repudiationDiscoverability, 
            probability=repudiationProbability)

Graph.add_node('Information Closure', 
            damage=InformationClosureDamage, 
            reproducibility=InformationClosureReproducibility, 
            exploitability=InformationClosureExploitability, 
            AffectedUsers=InformationClosureAffectedUsers, 
            discoverability=InformationClosureDiscoverability, 
            probability=InformationClosureProbability)

Graph.add_node('Denial of Service', 
            damage=DenialOfServiceDamage, 
            reproducibility=DenialOfServiceReproducibility, 
            exploitability=DenialOfServiceExploitability, 
            AffectedUsers=DenialOfServiceAffectedUsers, 
            discoverability=DenialOfServiceDiscoverability, 
            probability=DenialOfServiceProbability)

Graph.add_node('Elevation of priviledge', 
            damage=ElevationOfPriviledgeDamage, 
            reproducibility=ElevationOfPriviledgeReproducibility, 
            exploitability=ElevationOfPriviledgeExploitability, 
            AffectedUsers=ElevationOfPriviledgeAffectedUsers, 
            discoverability=ElevationOfPriviledgeDiscoverability, 
            probability=ElevationOfPriviledgeProbability)

#create a connection/ link between different nodes, this is known as a directed edge
Graph.add_edge("Threat", "Spoofing")
Graph.add_edge('Threat', 'Tampering')
Graph.add_edge('Threat', 'Repudiation')
Graph.add_edge('Threat', 'Information Closure')
Graph.add_edge('Threat', 'Denial of Service')
Graph.add_edge('Threat', 'Elevation of priviledge')

#Define a function, where the node name will be displayed in the graph, along with node attributes 
def format_node_label(node_name): #python function to define the nodel label, which takes node name as the argument
    node_attrs = Graph.nodes[node_name] #collects the attributes associated with the node name
    label = f'{node_name}\n' #f-string (formatted string literal) to create a label for the node name, along with a line break
    
 #Create a condition, where if an attribute exists, then it displays both the attribute and its value 
    if 'damage' in node_attrs: #looks for attribute in the dictionary
        label += f'Damage: {node_attrs["damage"]}\n' #if the attribute is found, then the value associated with that attribute is inserted into the string 
    if 'reproducibility' in node_attrs:
        label += f'Reproducibility: {node_attrs["reproducibility"]}\n'
    if 'exploitability' in node_attrs:
        label += f'Exploitability: {node_attrs["exploitability"]}\n'
    if 'AffectedUsers' in node_attrs:
        label += f'Affected Users: {node_attrs["AffectedUsers"]}\n'
    if 'discoverability' in node_attrs:
        label += f'Discoverability: {node_attrs["discoverability"]}\n'

  #create conditions using an if statement, where if the attribute exists in the node dictionary, a probability outcome is assigned
    if 'probability' in node_attrs: #looks for probability in the dictionary
        if node_attrs["probability"] <= 10:
            label += f'Probability: Low\n'
        elif 10 < node_attrs["probability"] <= 24:
            label += f'Probability: Medium\n'
        elif 25 <= node_attrs["probability"] <= 39:
            label += f'Probability: High\n'
        elif 40 <= node_attrs["probability"] <= 50:
            label += f'Probability: Critical\n'
        else:
            label += f'Probability: Error\n'

    return label #output of this function


pos = nx.spring_layout(Graph)   #spring layout algorithm to visualise the graph, where it is assigned to position variable
labels = {node: format_node_label(node) for node in Graph.nodes()} #Each node in the graph is paired with a label
nx.draw(Graph, pos, with_labels=False, node_size=10000, node_color='lightgreen', font_size=10, node_shape='s')
nx.draw_networkx_labels(Graph, pos, labels, font_size=8, font_color='black', verticalalignment='center') #add node labels to the graph


plt.axis('off')  #turn off the axis 
plt.show() #display the graph frontend

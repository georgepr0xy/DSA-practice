import pygraphviz as pgv

# Create a new graph
dfd = pgv.AGraph(strict=True, directed=True)

# Add nodes to the graph
dfd.add_node("User Interface", shape="box")
dfd.add_node("Backend Processing", shape="box")
dfd.add_node("Model Training and Prediction", shape="box")
dfd.add_node("Output Interface", shape="box")

# Add edges to represent data flow
dfd.add_edge("User Interface", "Backend Processing")
dfd.add_edge("Backend Processing", "Model Training and Prediction")
dfd.add_edge("Model Training and Prediction", "Output Interface")

# Set graph attributes
dfd.graph_attr['label'] = "1st Level Data Flow Diagram (DFD) for Price Prediction Project"

# Write the graph to a file
dfd.draw("1st_level_dfd.png", prog="dot", format="png")

print("1st Level DFD generated successfully!")

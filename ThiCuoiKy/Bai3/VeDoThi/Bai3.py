import networkx as nx
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file
with open("data.txt", "r") as f:
    data = f.readlines()

# Tạo đồ thị
G = nx.DiGraph()

# Thêm cạnh từ fromNodeId đến toNodeId với trọng số weight
for line in data:
    line = line.strip().split("\t")
    fromNodeId = int(line[0])
    toNodeId = int(line[1])
    G.add_edge(fromNodeId, toNodeId)

# Vẽ đồ thị
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=10)
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.axis('off')
plt.show()

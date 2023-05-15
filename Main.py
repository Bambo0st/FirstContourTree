import matplotlib.pyplot as plt
from shapely.geometry import Polygon, LineString
import networkx as nx

print("Enter the resolution of tree ")
k = int(input())

vertices = [1, 2, 3, 4]
d = (vertices[3] - vertices[0]) / k

labels = []
for i in range(k + 1):
    labels.append(1 + i * d)
print(labels)

corners = {1: [1, 5], 2: [5, 1], 3: [1, 1], 4: [5, 5]}


# Define the coordinates of the square vertices
x = [1, 5, 5, 1, 1]
y = [1, 1, 5, 5, 1]

# Create the figure with two subplots side by side
# fig, ax2 = plt.subplots(ncols=2, figsize=(16, 8))
fig1, ax2 = plt.subplots()
edge14 = {}
edges14 = []

for i in labels:
    if i >= 1 and i <= 4:  # and i != 2:
        edge14[i] = [1 + (i - 1) / (vertices[3] - vertices[0]) * 4, 5]
        edges14.append(i)
edges14.sort()
print("The edge14 is ", edge14)
print("The edges14 is", edges14)
print()
edge23 = {}
edges23 = []
for i in labels:
    if i > 2 and i < 3:
        edge23[i] = [5 - (i - 2) / (vertices[2] - vertices[1]) * 4, 1]
        edges23.append(i)
edges23.sort()
print("The edge23 is ", edge23)
print("The edges23 is", edges23)
print()
edge13 = {}
edges13 = []
for i in labels:
    if i >= 1 and i < 3:  # and i != 2:
        edge13[i] = [1, 5 - (i - 1) / (vertices[2] - vertices[0]) * 4]
        edges13.append(i)
edges13.sort()
print("The edge13 is ", edge13)
print("The edges13 is", edges13)
print()
edge24 = {}
edges24 = []
for i in labels:
    if i > 2 and i <= 4:
        edge24[i] = [5, 1 + (i - 2) / (vertices[3] - vertices[1]) * 4]
        edges24.append(i)
edges24.sort()
print("The edge24 is ", edge24)
print("The edges24 is", edges24)
print()

edge12 = {}
edges12 = []
for i in labels:
    if i > 1 and i < 2:
        edge12[i] = [
            1 + ((i - 1) / (vertices[1] - vertices[0]) * 4 * pow(2, 0.5)) / pow(2, 0.5),
            5 - ((i - 1) / (vertices[1] - vertices[0]) * 4 * pow(2, 0.5)) / pow(2, 0.5),
        ]
        print(" how is it ", edge12[i])
        edges12.append(i)
print("The edge12 is ", edge12)
print("The edges12 is", edges12)
print()

e12 = len(edges12)
e13 = len(edges13)
e14 = len(edges14)
e23 = len(edges23)
e24 = len(edges24)

print("e12 size is ", e12)
print("e23 size is ", e23)
print("e13 size is ", e14)
print("e24 size is ", e24)
print("e14 size is ", e14)

count = k

rightTriangleVertices = []
rightTriangleVertices.append(edge14[vertices[3]])  # This is label 4
rightTriangleVertices.append(edge24[edges24[e24 - 2]])
rightTriangleVertices.append(edge14[edges14[e14 - 2]])

print(rightTriangleVertices)
triangle_right = Polygon(rightTriangleVertices)

triangle1_patch = plt.Polygon(
    rightTriangleVertices, facecolor="gray", edgecolor="black"
)

ax2.add_patch(triangle1_patch)
ax2.text(
    triangle_right.centroid.x,
    triangle_right.centroid.y,
    count,
    ha="center",
    va="center",
)

count = count - 1

for i in range(e24 - 2):
    trapezium = []
    trapezium.append(edge24[edges24[e24 - i - 3]])  # 2.5
    trapezium.append(edge14[edges14[e14 - i - 3]])
    trapezium.append(edge14[edges14[e14 - i - 2]])
    trapezium.append(edge24[edges24[e24 - i - 2]])
    trapeziumPolygon = Polygon(trapezium)

    trap_patch = plt.Polygon(trapezium, facecolor="gray", edgecolor="black")

    ax2.add_patch(trap_patch)
    ax2.text(
        trapeziumPolygon.centroid.x,
        trapeziumPolygon.centroid.y,
        count,
        ha="center",
        va="center",
    )
    count = count - 1


# For just beside quadrilateral
if k != 6:
    poly = []
    poly.append(corners[vertices[1]])  # label 2
    poly.append(edge24[edges24[0]])  # label 2.
    poly.append(edge14[edges24[0]])  # label 2.
    poly.append(edge14[edges14[e12]])  # label 1.
    poly.append(edge12[edges14[e12]])  # labl 1.
    polyPolygon = Polygon(poly)
    print(poly)
    trap_patch = plt.Polygon(poly, facecolor="gray", edgecolor="black")

    ax2.add_patch(trap_patch)
    ax2.text(
        polyPolygon.centroid.x,
        polyPolygon.centroid.y,
        count,
        ha="center",
        va="center",
    )

    count = count - 1

    for i in range(e12 - 1):
        trapezium = []
        trapezium.append(edge12[edges12[e12 - i - 1]])
        trapezium.append(edge12[edges12[e12 - i - 2]])
        trapezium.append(edge14[edges12[e12 - i - 2]])
        trapezium.append(edge14[edges12[e12 - i - 1]])  # 2.5
        trapeziumPolygon = Polygon(trapezium)

        trap_patch = plt.Polygon(trapezium, facecolor="gray", edgecolor="black")

        ax2.add_patch(trap_patch)
        ax2.text(
            trapeziumPolygon.centroid.x,
            trapeziumPolygon.centroid.y,
            count,
            ha="center",
            va="center",
        )
        count = count - 1

else:
    trapezium = []
    trapezium.append(corners[vertices[1]])  # 2.5
    trapezium.append(edge14[edges14[2]])
    trapezium.append(edge14[edges14[3]])
    trapezium.append(edge24[edges24[0]])
    trapeziumPolygon = Polygon(trapezium)

    trap_patch = plt.Polygon(trapezium, facecolor="gray", edgecolor="black")

    ax2.add_patch(trap_patch)
    ax2.text(
        trapeziumPolygon.centroid.x,
        trapeziumPolygon.centroid.y,
        count,
        ha="center",
        va="center",
    )
    count = count - 1

    trapezium = []
    trapezium.append(corners[vertices[1]])  # 2.5
    trapezium.append(edge12[edges12[0]])
    trapezium.append(edge14[edges14[1]])
    trapezium.append(edge14[edges14[2]])
    trapeziumPolygon = Polygon(trapezium)

    trap_patch = plt.Polygon(trapezium, facecolor="gray", edgecolor="black")

    ax2.add_patch(trap_patch)
    ax2.text(
        trapeziumPolygon.centroid.x,
        trapeziumPolygon.centroid.y,
        count,
        ha="center",
        va="center",
    )
    count = count - 1


#


# # For  triangle near diagonal

diagTriangle = []
diagTriangle.append(corners[vertices[0]])  # This is label 1
diagTriangle.append(edge12[edges12[0]])
diagTriangle.append(edge14[edges14[1]])

print(diagTriangle)
DiagPoly = Polygon(diagTriangle)

triangle21_patch = plt.Polygon(diagTriangle, facecolor="gray", edgecolor="black")

ax2.add_patch(triangle21_patch)
ax2.text(
    DiagPoly.centroid.x,
    DiagPoly.centroid.y,
    1,
    ha="center",
    va="center",
)

# #
# #
# # Left side

count = 2

diagTriangle = []
diagTriangle.append(corners[vertices[0]])  # This is label 1
diagTriangle.append(edge12[edges12[0]])
diagTriangle.append(edge13[edges13[1]])

print(diagTriangle)
DiagPoly = Polygon(diagTriangle)

triangle21_patch = plt.Polygon(diagTriangle, facecolor="gray", edgecolor="black")

ax2.add_patch(triangle21_patch)
ax2.text(
    DiagPoly.centroid.x,
    DiagPoly.centroid.y,
    1,
    ha="center",
    va="center",
)
c2 = count + e12 - 2

for i in range(e12 - 1):
    trapezium = []
    trapezium.append(edge12[edges12[e12 - i - 1]])
    trapezium.append(edge12[edges12[e12 - i - 2]])
    trapezium.append(edge13[edges12[e12 - i - 2]])
    trapezium.append(edge13[edges12[e12 - i - 1]])  # 2.5
    trapeziumPolygon = Polygon(trapezium)

    trap_patch = plt.Polygon(trapezium, facecolor="gray", edgecolor="black")

    ax2.add_patch(trap_patch)
    ax2.text(
        trapeziumPolygon.centroid.x,
        trapeziumPolygon.centroid.y,
        c2,
        ha="center",
        va="center",
    )
    c2 -= 1
# # For just beside quadrilateral
last_count = count
if k != 6:
    count += e12 - 1
    poly = []
    poly.append(corners[vertices[1]])  # label 2
    poly.append(edge23[edges23[0]])  # label 2.
    poly.append(edge13[edges23[0]])  # label 2.
    poly.append(edge13[edges13[e12]])  # label 1.
    poly.append(edge12[edges13[e12]])  # labl 1.
    polyPolygon = Polygon(poly)
    print(poly)
    trap_patch = plt.Polygon(poly, facecolor="gray", edgecolor="black")

    ax2.add_patch(trap_patch)
    ax2.text(
        polyPolygon.centroid.x,
        polyPolygon.centroid.y,
        count,
        ha="center",
        va="center",
    )
    count += 1
    print("The count here is ", count)
    count = count + e23 - 2
    last_count = count

    for i in range(e23 - 1):
        trapezium = []
        trapezium.append(edge23[edges23[e23 - i - 1]])
        trapezium.append(edge23[edges23[e23 - i - 2]])  # 2.5
        trapezium.append(edge13[edges23[e23 - i - 2]])
        trapezium.append(edge13[edges23[e23 - i - 1]])
        trapeziumPolygon = Polygon(trapezium)

        trap_patch = plt.Polygon(trapezium, facecolor="gray", edgecolor="black")

        ax2.add_patch(trap_patch)
        ax2.text(
            trapeziumPolygon.centroid.x,
            trapeziumPolygon.centroid.y,
            count,
            ha="center",
            va="center",
        )
        count -= 1

else:
    trapezium = []
    trapezium.append(corners[vertices[1]])  # 2.5
    trapezium.append(edge13[edges13[2]])
    trapezium.append(edge13[edges13[1]])
    trapezium.append(edge12[edges12[0]])
    trapeziumPolygon = Polygon(trapezium)

    trap_patch = plt.Polygon(trapezium, facecolor="gray", edgecolor="black")

    ax2.add_patch(trap_patch)
    ax2.text(
        trapeziumPolygon.centroid.x,
        trapeziumPolygon.centroid.y,
        count,
        ha="center",
        va="center",
    )
    count = count - 1

    trapezium = []
    trapezium.append(corners[vertices[1]])  # 2.5
    trapezium.append(edge23[edges23[0]])
    trapezium.append(edge13[edges13[3]])
    trapezium.append(edge13[edges13[2]])
    trapeziumPolygon = Polygon(trapezium)

    trap_patch = plt.Polygon(trapezium, facecolor="gray", edgecolor="black")

    ax2.add_patch(trap_patch)
    ax2.text(
        trapeziumPolygon.centroid.x,
        trapeziumPolygon.centroid.y,
        3,
        ha="center",
        va="center",
    )
    count = count - 1


if k == 6:
    last_count = 3

leftTriangleVertices = []
leftTriangleVertices.append(corners[vertices[2]])  # This is label 4
leftTriangleVertices.append(edge23[edges23[e23 - 1]])
leftTriangleVertices.append(edge13[edges13[e13 - 1]])

print(leftTriangleVertices)
triangle_left = Polygon(leftTriangleVertices)

triangle11_patch = plt.Polygon(
    leftTriangleVertices, facecolor="gray", edgecolor="black"
)
print(last_count)
ax2.add_patch(triangle11_patch)
ax2.text(
    triangle_left.centroid.x,
    triangle_left.centroid.y,
    last_count + 1,
    ha="center",
    va="center",
)

ax2.plot(x, y)
ax2.text(x[0], y[0], str(3), ha="left", va="top")
ax2.text(x[1], y[1], str(2), ha="left", va="top")
ax2.text(x[2], y[2], str(4), ha="left", va="top")
ax2.text(x[3], y[3], str(1), ha="right", va="top")


ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("OUTPUT Graph")


# For 2nd graph

fig1, ax1 = plt.subplots()

G = nx.Graph()

# Add nodes and edges

nodes = []
pos = {}
label = {}
for i in range(1, k + 1):
    nodes.append(i)
    pos[i] = (0, i)
    label[i] = i

for i in range(k + 1, k + 1 + e12 + 1 + e23):
    nodes.append(i)
    pos[i] = (0.15, i - k)
    label[i] = i - k


edges = []
for i in range(1, k):
    edges.append((i, i + 1))

for i in range(k + 1, k + 1 + e12 + e23):
    edges.append((i, i + 1))

for i in range(1, e12 + 2):
    edges.append((i, i + k))

print(edges)
print(nodes)

G.add_nodes_from(nodes)
G.add_edges_from(edges)


nx.draw(
    G,
    pos=pos,
    labels=label,
    node_size=500,
    # font_size=16,
)
ax1.set_title("(Dual) First Contour Graph")
plt.show(block=False)


fig1, ax1 = plt.subplots()
G = nx.Graph()

# Add nodes and edges

nodes = []
pos = {}
label = {}
for i in range(1, k + 1):
    nodes.append(i)
    pos[i] = (0, i)
    label[i] = i

for i in range(k + 1, k + 1 + e23):
    nodes.append(i)
    pos[i] = (0.10, i - k + e12 + 1)
    label[i] = i - k + e12 + 1


edges = []
for i in range(1, k):
    edges.append((i, i + 1))

edges.append((e12 + 1, k + 1))

for i in range(k + 1, k + e23):
    edges.append((i, i + 1))

G.add_nodes_from(nodes)
G.add_edges_from(edges)


nx.draw(
    G,
    pos=pos,
    labels=label,
    # node_size=500,
    # font_size=16,
)
ax1.set_title("First Contour Graph")
plt.show(block=False)


# # Keep the windows open until the user closes them
plt.show()

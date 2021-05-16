from solid import *
from solid.utils import *
import numpy as np

def wire(point1=[0, 0, 0], point2=[-10, -10, -10]):
    point1 = np.array(point1)
    point2 = np.array(point2)
    diff = point2 - point1
    length = np.linalg.norm(diff)
    # print(diff/ length)
    # print(diff[:2] / np.linalg.norm(diff[:2]))
    rot_y = np.rad2deg(np.arccos(diff[2] / length))
    rot_z = np.rad2deg(np.arctan2(diff[1], diff[0]))
    print(length, rot_y, rot_z)
    obj = cylinder(h=length, r=0.5, segments=50);
    obj = rotate([0, rot_y, rot_z])(obj)
    obj = translate(point1)(obj)
    return obj

def block(nodes, edges):
    obj = wire(nodes[edges[0][0]], nodes[edges[0][1]])

    for edge in edges:
        obj += wire(nodes[edge[0]], nodes[edge[1]])

    node_obj = sphere(0.6, segments=50);
    for node in nodes:
        obj += translate(node)(node_obj)
    return obj

def make_model():
    # c1 = cube(1, center=True)
    # c2 = cube(1, 1, 0.5, center=True)
    # c1 = c1 - c2
    # c1 = cylinder(h = 10, r=1);
    # obj = wire()

    nodes = [
        [0, 0, 0],
        [10, 0, 0],
        [10, 10, 0],
        [0, 10, 0],
        [0, 0, 10],
        [10, 0, 10],
        [10, 10, 10],
        [0, 10, 10],
    ]
    nodes = 0.5 * np.array(nodes)

    edges = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            edges.append([i, j])
    # edges = [
    #     [0, 1],
    # ]

    # obj = wire(nodes[0], nodes[1])
    # # obj += wire(points[1], points[2])

    # for edge in edges:
    #     obj += wire(nodes[edge[0]], nodes[edge[1]])


    # node_obj = sphere(2);
    # for node in nodes:
    #     obj += translate(node)(node_obj)

    obj = block(nodes, edges)

    # c1 = polyhedron(
    #     points=[
    #         [10,10,0],
    #         [10,-10,0],
    #         [-10,-10,0],
    #         [-10,10,0],
    #         [0,0,10]
    #     ],
    #     faces=[
    #         [0,1,4],
    #         [1,2,4],
    #         [2,3,4],
    #         [3,0,4],
    #         [1,0,3],
    #         [2,1,3],
    #     ],
    # )

    obj_list = []
    num = 4
    for x in range(num):
        for y in range(num):
            for z in range(num):
                pos = 5 * np.array([x, y, z])
                obj_list.append(translate(pos)(obj))

    # c1_r = rotate([0, 0, 45])(c1)

    return sum(obj_list)
    # return obj

if __name__ == '__main__':
    scad_render_to_file(make_model(), 'output/output.scad', include_orig_code=False)

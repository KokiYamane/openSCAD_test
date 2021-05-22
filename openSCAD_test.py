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
    obj = cylinder(h=length, r=0.25, segments=25);
    obj = rotate([0, rot_y, rot_z])(obj)
    obj = translate(point1)(obj)
    return obj

def block(nodes, edges):
    obj = wire(nodes[edges[0][0]], nodes[edges[0][1]])

    for edge in edges:
        obj += wire(nodes[edge[0]], nodes[edge[1]])

    node_obj = sphere(0.25, segments=25)
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
        # [0, 5, 5],
        # [5, 0, 5],

        # [5, 5, 0],
        # [10, 5, 5],
        # [5, 10, 5],
        # [5, 5, 10],
        # [2.5, 2.5, 2.5],

        # [2.5, 7.5, 7.5],
        # [7.5, 2.5, 7.5],
        # [7.5, 7.5, 2.5],
    ]

    # edges = []
    # for i in range(len(nodes)):
    #     for j in range(i + 1, len(nodes)):
    #         edges.append([i, j])
    edges = [
        [0, 5],
        [1, 6],
        [2, 7],
        [3, 4],
        [0, 7],
        [1, 4],
        [2, 5],
        [3, 6]
    ]

    obj_list = []
    num = 4
    nodes = np.array(nodes) / num * 2
    obj = block(nodes, edges)
    for x in range(num):
        for y in range(num):
            for z in range(num):
                pos = 20 / num * np.array([x, y, z])
                obj_list.append(translate(pos)(obj))

    # c1_r = rotate([0, 0, 45])(c1)

    base = cube([20.5, 20.5, 0.5])
    base = translate([-0.25, -0.25, -0.25])(base)
    top = translate([0, 0, 20])(base)

    return sum(obj_list) + base
    # return obj

if __name__ == '__main__':
    scad_render_to_file(make_model(), 'output/output.scad', include_orig_code=False)

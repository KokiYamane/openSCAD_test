from solid import *
from solid.utils import *
import numpy as np

def make_model():
    c1 = cube(1)

    obj_list = []
    num = 10
    for i in range(num):
        theta = 2 * np.pi / num * i
        r = 5
        obj_list.append(translate([r * np.cos(theta), r * np.sin(theta), 0])(c1))

    c1_r = rotate([0, 0, 45])(c1)

    return c1 + sum(obj_list) + c1_r

if __name__ == '__main__':
    scad_render_to_file(make_model(), 'output/output.scad', include_orig_code=False)

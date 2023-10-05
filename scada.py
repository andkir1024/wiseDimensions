import math

from solid import *
from subprocess import run
import numpy as np

RADIUS = 10
WALL_THICKNESS = 0.2

HORIZONTAL_STEP = math.sqrt(3) * RADIUS
VERTICAL_STEP = 6 / 4. * RADIUS

V = np.array((0, HORIZONTAL_STEP, 0))
U = np.array((VERTICAL_STEP, 1 / 2. * HORIZONTAL_STEP, 0))

HEXES = [
    [ 3, 0],[ 2, 1],[ 1, 2],[ 0, 3],
    [ 3,-1],[ 2, 0],[ 1, 1],[ 0, 2],[-1, 3],
    [ 3,-2],[ 2,-1],[ 1, 0],[ 0, 1],[-1, 2],[-2, 3],
    [ 3,-3],[ 2,-2],[ 1,-1],[ 0, 0],[-1, 1],[-2, 2],[-3, 3],
    [ 2,-3],[ 1,-2],[ 0,-1],[-1, 0],[-2, 1],[-3, 2],
    [ 1,-3],[ 0,-2],[-1,-1],[-2, 0],[-3, 1],
    [ 0,-3],[-1,-2],[-2,-1],[-3, 0]
]

def hex(r):
    result = circle(r = r, segments = 6)
    return result

def hexcomb(r):
    result =difference()(
        hex(r),
        hex(r-WALL_THICKNESS),
    )
    return result

def hexgrid(primitive=None):
    shapes = []
    hc = primitive(RADIUS)
    for x,y in HEXES:
        translation = x*V + y*U
        shapes.append(translate(translation)(hc))
    result = union()(*shapes)
    return result

def main():
    base_shape = hexgrid(hex)
    base = linear_extrude(height = 1, slices = 1, twist = 0, scale=1)(base_shape)
    combs_shape = hexgrid(hexcomb)
    extrusion = linear_extrude(height = 60, slices = 80, twist = 20, scale=1.5)(combs_shape)

    model = union()(
            base,
            extrusion
    )
    out = intersection()(
        model,
        sphere(r=80)
    )

    scad_render_to_file(out, 'out.scad')

    run(["openscad", "-o",  "out.stl", "out.scad"])

main()

 
import os, solid
print(os.path.dirname(solid.__file__) + '/examples')

import sys

from solid import scad_render_to_file
from solid.objects import cylinder
from solid.utils import up

SEGMENTS = 48


def show_appended_python_code():
    a = cylinder(r=10, h=10, center=True) + up(5)(cylinder(r1=10, r2=0, h=10))

    return a


show_appended_python_code()
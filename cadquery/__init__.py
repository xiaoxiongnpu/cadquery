import warnings
print("WARNING: CadQuery 1.x is no longer supported. Please upgrade to CadQuery 2.x https://github.com/CadQuery/cadquery")
warnings.warn("CadQuery 1.x is no longer supported. Please upgrade to CadQuery 2.x https://github.com/CadQuery/cadquery", DeprecationWarning)

#these items point to the freecad implementation
from .freecad_impl.geom import Plane,BoundBox,Vector,Matrix,sortWiresByBuildOrder
from .freecad_impl.shapes import Shape,Vertex,Edge,Face,Wire,Solid,Shell,Compound
from .freecad_impl import exporters
from .freecad_impl import importers

#these items are the common implementation

#the order of these matter
from .selectors import *
from .cq import *


__all__ = [
    'CQ','Workplane','plugins','selectors','Plane','BoundBox','Matrix','Vector','sortWiresByBuildOrder',
    'Shape','Vertex','Edge','Wire','Face','Solid','Shell','Compound','exporters', 'importers',
    'NearestToPointSelector','ParallelDirSelector','DirectionSelector','PerpendicularDirSelector',
    'TypeSelector','DirectionMinMaxSelector','StringSyntaxSelector','Selector','plugins',
]

__version__ = "1.2.5"

import numpy as np
from scipy.interpolate import griddata
from .trajectory import Trajectory
from .points import Point, Origin, Uniform


def check_point(point, **kwargs):
    if issubclass(type(point), (type, Point)):
        point = point()
    if issubclass(type(point), (Point)):
        point = point(**kwargs)
    point = np.array(point)
    if point.shape[0] == 1:
        point = np.repeat(point, **kwargs)
    return point

def line_generator(*args, **kwargs):
    n_steps = kwargs.get('n_steps')
    dim = kwargs.get('dim')
    origin = kwargs.get('origin')
    end = kwargs.get('end')
    assert n_steps, "line_generator needs the n_steps argument"
    assert dim, "line_generator needs the dim argument"

    origin = check_point(origin, dim=dim)
    end = check_point(end, dim=dim)

    traj = np.linspace(0,1,n_steps)[:, np.newaxis].repeat(dim, 1) @ np.diag(end-origin) + origin
    return traj

class Line(Trajectory):
    _callback = line_generator


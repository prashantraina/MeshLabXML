""" MeshLabXML deletion functions"""

from . import util
from . import select

def nonmanifold_vert(script):
    """ Select & delete the non manifold vertices that do not belong to
        non manifold edges.

    For example two cones connected by their apex. Vertices incident on
    non manifold edges are ignored.

    Args:
        script: the FilterScript object or script filename to write
            the filter to.

    Layer stack:
        No impacts

    MeshLab versions:
        2016.12
        1.3.4BETA
    """
    select.nonmanifold_vert(script)
    selected(script, face=False)
    return None


def nonmanifold_edge(script):
    """ Select & delete the faces and the vertices incident on
        non manifold edges (e.g. edges where more than two faces are incident).

    Note that this function selects the components that are related to
    non manifold edges. The case of non manifold vertices is specifically
    managed by nonmanifold_vert.

    Args:
        script: the FilterScript object or script filename to write
            the filter to.

    Layer stack:
        No impacts

    MeshLab versions:
        2016.12
        1.3.4BETA
    """
    select.nonmanifold_edge(script)
    selected(script, face=False)
    return None


def small_parts(script, ratio=0.2, non_closed_only=False):
    """ Select & delete the small disconnected parts (components) of a mesh.

    Args:
        script: the FilterScript object or script filename to write
            the filter to.
        ratio (float): This ratio (between 0 and 1) defines the meaning of
            'small' as the threshold ratio between the number of faces of the
            largest component and the other ones. A larger value will select
            more components.
        non_closed_only (bool): Select only non-closed components.

    Layer stack:
        No impacts

    MeshLab versions:
        2016.12
        1.3.4BETA
    """
    select.small_parts(script, ratio, non_closed_only)
    selected(script)
    return None


def selected(script, face=True, vert=True):
    """ Delete selected vertices and/or faces

    Args:
        script: the FilterScript object or script filename to write
            the filter to.
        face (bool): if True the selected faces will be deleted
        vert (bool): if True the selected vertices will be deleted

    Layer stack:
        No impacts

    MeshLab versions:
        2016.12
        1.3.4BETA
    """
    if face and vert:
        filter_xml = '  <filter name="Delete Selected Faces and Vertices"/>\n'
    elif face and not vert:
        filter_xml = '  <filter name="Delete Selected Faces"/>\n'
    elif not face and vert:
        filter_xml = '  <filter name="Delete Selected Vertices"/>\n'
    util.write_filter(script, filter_xml)
    return None

def faces_from_nonmanifold_edges(script):
    """ For each non manifold edge it iteratively deletes the smallest area
        face until it becomes two-manifold.

    Args:
        script: the FilterScript object or script filename to write
            the filter to.

    Layer stack:
        No impacts

    MeshLab versions:
        2016.12
        1.3.4BETA
    """
    filter_xml = '  <filter name="Remove Faces from Non Manifold Edges"/>\n'
    util.write_filter(script, filter_xml)
    unreferenced_vert(script)
    return None


def unreferenced_vert(script):
    """ Check for every vertex on the mesh: if it is NOT referenced by a face,
        removes it.

    Args:
        script: the FilterScript object or script filename to write
            the filter to.

    Layer stack:
        No impacts

    MeshLab versions:
        2016.12
        1.3.4BETA
    """
    filter_xml = '  <filter name="Remove Unreferenced Vertex"/>\n'
    util.write_filter(script, filter_xml)
    return None


def duplicate_faces(script):
    """ Delete all the duplicate faces.

    Two faces are considered equal if they are composed by the same set of
    vertices, regardless of the order of the vertices.

    Args:
        script: the FilterScript object or script filename to write
            the filter to.

    Layer stack:
        No impacts

    MeshLab versions:
        2016.12
        1.3.4BETA
    """
    filter_xml = '  <filter name="Remove Duplicate Faces"/>\n'
    util.write_filter(script, filter_xml)
    return None


def duplicate_verts(script):
    """ "Check for every vertex on the mesh: if there are two vertices with
        the same coordinates they are merged into a single one.

    Args:
        script: the FilterScript object or script filename to write
            the filter to.

    Layer stack:
        No impacts

    MeshLab versions:
        2016.12
        1.3.4BETA
    """
    filter_xml = '  <filter name="Remove Duplicated Vertex"/>\n'
    util.write_filter(script, filter_xml)
    return None


def zero_area_face(script):
    """ Remove null faces (the ones with area equal to zero)

    Args:
        script: the FilterScript object or script filename to write
            the filter to.

    Layer stack:
        No impacts

    MeshLab versions:
        2016.12
        1.3.4BETA
    """
    filter_xml = '  <filter name="Remove Zero Area Faces"/>\n'
    util.write_filter(script, filter_xml)
    return None

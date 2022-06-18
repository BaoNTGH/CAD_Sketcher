import sys
from enum import Enum
from mathutils import Vector
from .declarations import SolverStateTypes

registered = False

PYPATH = sys.executable


entities = {}
batches = {}

offscreen = None
redraw_selection_buffer = False

hover = -1
ignore_list = []
selected = []

# Allows to highlight a constraint gizmo,
# Value gets unset in the preselection gizmo
highlight_constraint = None

highlight_entities = []

Z_AXIS = Vector((0, 0, 1))

draw_handle = None

# Workplane requirement options
class WpReq(Enum):
    OPTIONAL, FREE, NOT_FREE = range(3)


solver_state_items = [
    (
        SolverStateTypes.Ok,
        "Okay",
        "Successfully solved sketch",
        "CHECKMARK",
        0,
    ),
    (
        SolverStateTypes.Inconsistent,
        "Inconsistent",
        "Cannot solve sketch because of inconsistent constraints",
        "ERROR",
        1,
    ),
    (
        SolverStateTypes.DidNotConverge,
        "Didnt Converge",
        "Cannot solve sketch, system didn't converge",
        "ERROR",
        2,
    ),
    (
        SolverStateTypes.TooManyUnknowns,
        "Too Many Unknowns",
        "Cannot solve sketch because of too many unknowns",
        "ERROR",
        3,
    ),
    (
        SolverStateTypes.UnknownFailure,
        "Unknown Failure",
        "Cannot solve sketch because of unknown failure",
        "ERROR",
        4,
    ),
]

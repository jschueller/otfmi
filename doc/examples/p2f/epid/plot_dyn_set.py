"""
Set FMU simulation parameters
=============================
"""

# %%
# :class:`~otfmi.FMUPointToFieldFunction` is an OpenTURNS-friendly overlay of the class
# otfmi.OpenTURNSFMUPointToFieldFunction, closer to the underlying FMI backend
# implementation.
# Some FMU simulation parameters can be given to :class:`~otfmi.FMUPointToFieldFunction`,
# yet most of them can only be passed to an OpenTURNSFMUPointToFieldFunction.

# %%
# First, retrieve the path to *epid.fmu*.
import otfmi.example.utility
import openturns as ot

path_fmu = otfmi.example.utility.get_path_fmu("epid")

# %%
# The FMU simulation start and final times are the only simulation-related
# parameter that can be passed to :class:`~otfmi.FMUPointToFieldFunction`.

function = otfmi.FMUPointToFieldFunction(
    path_fmu,
    inputs_fmu=["infection_rate", "healing_rate"],
    outputs_fmu=["infected"],
    start_time=0.0,
    final_time=15.0,
)

inputPoint = ot.Point([2.0, 0.5])
outputSample = function(inputPoint)
print(outputSample)

# %%
# To set more parameters for the FMU simulation,
# OpenTURNSFMUPointToFieldFunction can be employed. Below, we rely on the
# defaults of the active FMI backend.

midlevel_function = otfmi.OpenTURNSFMUPointToFieldFunction(
    path_fmu,
    inputs_fmu=["infection_rate", "healing_rate"],
    outputs_fmu=["infected"],
    start_time=0.0,
    final_time=15.0,
)

outputPoint = midlevel_function.base.simulate(
    inputPoint, algorithm="FMICSAlg", options={"silent_mode": True}
)

# %%
# For advanced users, the middle-level class otfmi.OpenTURNSFMUPointToFieldFunction also gives
# access to the underlying backend model. We can hence access all its object methods:

fmu_model = midlevel_function.base.get_model()
print(dir(fmu_model))

# %%
# .. note::
#    otfmi' classes :class:`~otfmi.FMUPointToFieldFunction` and otfmi.OpenTURNSFMUPointToFieldFunction
#    are designed to highlight the most useful backend methods and simplify their use!

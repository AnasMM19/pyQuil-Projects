from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.quilbase import Declare
from pyquil.api import local_forest_runtime

prog = Program(
    Declare("ro", "BIT", 2),
    Z(0),
    CNOT(0, 1),
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1)),
).wrap_in_numshots_loop(10)

with local_forest_runtime():
    qvm = get_qc('9q-square-qvm')
    bitstrings = qvm.run(qvm.compile(prog)).readout_data.get("ro")

#Construct a Bell State program
p = Program(
    Declare("ro", "BIT", 2),
    H(0),
    CNOT(0, 1),
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1)),
).wrap_in_numshots_loop(10)

#Run the program on a QVM
qc = get_qc('9q-square-qvm')
result = qc.run(qc.compile(p)).readout_data.get("ro")
print(result[0])
print(result[1])
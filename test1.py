import qiskit as q
import matplotlib
matplotlib.use('TkAgg')
# %matplotlib inline

circuit = q.QuantumCircuit(2,2)  # 2 qubits, 2 classical bits 
circuit.x(0) # "x" is a "not" gate. It flips the value. Starting value is a 0, so this flips to a 1. 
circuit.cx(0, 1) #cnot, controlled not, Flips 2nd qubit's value if first qubit is 1
circuit.measure([0,1], [0,1])  # ([qbitregister], [classicalbitregister]) Measure qubit 0 and 1 to classical bits 0 and 1

circuit.draw(output="mpl")

from qiskit import IBMQ

IBMQ.save_account(open("token.txt","r").read())
IBMQ.load_account()
IBMQ.providers()
provider = IBMQ.get_provider("ibm-q")

for backend in provider.backends():
    try:
        qubit_count = len(backend.properties().qubits)
    except:
        qubit_count = "simulated"

    print(f"{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits")

from qiskit.tools.monitor import job_monitor
backend = provider.get_backend("ibmq_london")
job = q.execute(circuit, backend=backend, shots=500)
job_monitor(job)

from qiskit.visualization import plot_histogram
from matplotlib import style

style.use("dark_background") # I am using dark mode notebook, so I use this to see the chart.

result = job.result()
counts = result.get_counts(circuit)

plot_histogram([counts], legend=['Device'])
circuit = q.QuantumCircuit(2,2)  # 2 qbits, 2 classical bits.
circuit.h(0) # Hadamard gate, puts qubit 0 into superposition
circuit.cx(0, 1) #cnot, controlled not, Flips 2nd qubit's value if first qubit is 1
circuit.measure([0,1], [0,1])  # ([qbitregister], [classicalbitregister]) Measure qubit 0 and 1 to classical bits 0 and 1

circuit.draw(output="mpl")

backend = provider.get_backend("ibmq_london")
job = q.execute(circuit, backend=backend, shots=500)
job_monitor(job)

result = job.result()
counts = result.get_counts(circuit)

plot_histogram([counts], legend=['Device'])





from qiskit import Aer  # simulator framework from qiskit

# will create a statevector of possibilities.
sim_backend = Aer.get_backend('qasm_simulator')

for backend in Aer.backends():
    print(backend)


job = q.execute(circuit, backend=sim_backend, shots=500)
job_monitor(job)

result = job.result()
counts = result.get_counts(circuit)

plot_histogram([counts], legend=['Device'])



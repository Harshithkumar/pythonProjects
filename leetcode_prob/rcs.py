from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.random import random_circuit

# Generate a random quantum circuit
num_qubits = 5   # Number of qubits
depth = 4        # Circuit depth
random_circ = random_circuit(num_qubits, depth, max_operands=2)

# Display the circuit
print(random_circ)

# Simulate the circuit
simulator = Aer.get_backend('statevector_simulator')
result = execute(random_circ, simulator).result()

# Get the statevector output
statevector = result.get_statevector()
print("Statevector:", statevector)

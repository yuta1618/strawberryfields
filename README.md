# Optical Quantum Teleportation with Strawberry Fields

This project implements and simulates continuous-variable (CV) quantum teleportation using the photonic quantum computing framework **Strawberry Fields**. The core objective is to transfer an unknown coherent state ( |\alpha\rangle ) between optical modes via entanglement-assisted communication, combining EPR (Einstein–Podolsky–Rosen) correlations with classical feedforward to reconstruct the original quantum state at a remote mode.

The implementation is fully compatible with Python 3.10.5 and follows the modern Strawberry Fields (v0.23.0+) architecture based on the separation of `sf.Program` and `sf.Engine`, enabling a clearer distinction between circuit definition and execution.

The simulation is performed on the Gaussian backend, allowing efficient phase-space evolution of multimode Gaussian states without resorting to Fock-space truncation. This significantly improves computational scalability while preserving analytical tractability for continuous-variable systems.

The teleportation protocol consists of preparing a two-mode squeezed vacuum state as the entanglement resource, performing a joint Bell-like measurement on the input mode and one half of the EPR pair, and applying displacement operations conditioned on homodyne measurement outcomes via classical feedforward. This is implemented using RegRef parameters and `.par` bindings, enabling dynamic update of gate parameters based on measurement results.

This real-time classical control loop is essential to faithfully reproduce the CV teleportation protocol and highlights the hybrid quantum–classical nature of photonic quantum computing.

The performance of the protocol is evaluated by reconstructing the output state and analyzing its Wigner function, which allows direct visualization of phase-space displacement, squeezing degradation, and noise introduced by finite squeezing.

Additional analysis includes parameter sweeps over squeezing strength to quantify teleportation fidelity scaling, comparison between ideal infinite-squeezing limits and realistic resource constraints, and verification of quadrature correlations before and after teleportation.

Overall, this project provides a minimal yet physically consistent simulation framework for CV quantum state transfer and serves as a foundation for extensions toward Gaussian boson sampling, photonic quantum machine learning models, and hybrid optical–classical signal processing architectures.

```bash
pip install strawberryfields numpy matplotlib
```

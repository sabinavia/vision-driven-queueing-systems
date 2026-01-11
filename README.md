# Vision-Driven Queueing Systems

This repository provides the Python 3.10 simulation framework used in the paper:

**“Integrated Computer Vision and Queueing Theory for Intelligent Management of Large-Scale Service Systems”**

The implementation supports simulation-based experiments that integrate vision-driven demand estimation with classical and generalized queueing models for intelligent service system management.

---

## Overview

Large-scale service systems often operate under non-stationary and uncertain demand.  
This repository implements a vision-driven queueing framework in which:

- Arrival rates and queue states are dynamically inferred to emulate Computer Vision–based perception,
- These estimates are integrated into analytical queueing models (M/M/1, M/M/c),
- Reservation and admission decisions are updated adaptively under dynamic demand conditions.

The simulation framework is designed to support reproducible experimental evaluation under realistic service scenarios.

---

## Requirements

- Python 3.10  
- NumPy  
- SimPy  
- Matplotlib  
- SciPy  

Install dependencies using:

```bash
pip install -r requirements.txt

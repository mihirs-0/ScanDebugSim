# Scan Chain Debug Simulator

A Python-based simulation environment for demonstrating Design-for-Test (DFT) concepts, including scan chain testing, fault injection, and analysis.

## Project Overview

This project simulates a scan chain test environment with the following key features:
- Scan chain simulation with configurable chain length and test patterns
- Fault injection capabilities (stuck-at-0, stuck-at-1)
- Fault detection and coverage analysis
- Visual representation of test results and scan chain states

## Project Structure

```
.
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── scan_chain.py        # Core scan chain simulation
│   ├── fault_injector.py    # Fault injection logic
│   ├── test_pattern.py      # Test pattern generation
│   └── analyzer.py          # Analysis and visualization
├── tests/
│   ├── __init__.py
│   ├── test_scan_chain.py
│   └── test_fault_injector.py
└── examples/
    └── basic_usage.py
```

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

See `examples/basic_usage.py` for a quick start guide.

## Features

### Scan Chain Simulation
- Configurable chain length
- Support for multiple scan chains
- Test pattern generation and application

### Fault Injection
- Random fault injection
- Stuck-at-0 and stuck-at-1 faults
- Configurable fault probability

### Analysis and Visualization
- Fault coverage calculation
- Test pattern effectiveness analysis
- Visual representation of scan chain states

## Requirements
- Python 3.8+
- numpy
- matplotlib
- pytest (for testing)
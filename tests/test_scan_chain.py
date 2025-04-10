import pytest
from src.scan_chain import ScanChain
from src.test_pattern import TestPatternGenerator

def test_scan_chain_initialization():
    chain = ScanChain(length=4)
    assert chain.length == 4
    assert all(bit == 0 for bit in chain.shift_out())
    
def test_shift_in_out():
    chain = ScanChain(length=4)
    pattern = [1, 0, 1, 0]
    chain.shift_in(pattern)
    assert chain.shift_out() == pattern
    
def test_fault_injection():
    chain = ScanChain(length=4)
    chain.inject_fault(1, 1)  # stuck-at-1
    chain.inject_fault(2, -1)  # stuck-at-0
    
    pattern = [0, 0, 1, 0]
    chain.shift_in(pattern)
    assert chain.shift_out() == [0, 1, 0, 0]  # Faults should affect output
    
def test_fault_coverage():
    chain = ScanChain(length=4)
    chain.inject_fault(1, 1)
    chain.inject_fault(2, -1)
    
    patterns = [
        [1, 0, 1, 0],
        [0, 1, 0, 1]
    ]
    
    coverage = chain.get_fault_coverage(patterns)
    assert coverage == 100.0  # These patterns should detect both faults
    
def test_invalid_pattern_length():
    chain = ScanChain(length=4)
    with pytest.raises(ValueError):
        chain.shift_in([1, 0, 1])  # Too short
    with pytest.raises(ValueError):
        chain.shift_in([1, 0, 1, 0, 1])  # Too long
        
def test_invalid_fault_injection():
    chain = ScanChain(length=4)
    with pytest.raises(ValueError):
        chain.inject_fault(-1, 1)  # Invalid position
    with pytest.raises(ValueError):
        chain.inject_fault(4, 1)  # Invalid position
    with pytest.raises(ValueError):
        chain.inject_fault(1, 2)  # Invalid fault type 
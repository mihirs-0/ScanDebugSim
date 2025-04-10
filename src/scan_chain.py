import numpy as np
from typing import List, Optional

class ScanChain:
    def __init__(self, length: int, name: str = "scan_chain"):
        """
        Initialize a scan chain with specified length.
        
        Args:
            length (int): Number of flip-flops in the scan chain
            name (str): Name of the scan chain
        """
        self.length = length
        self.name = name
        self.chain = np.zeros(length, dtype=int)  # Initialize all bits to 0
        self.faults = np.zeros(length, dtype=int)  # 0: no fault, 1: stuck-at-1, -1: stuck-at-0
        
    def shift_in(self, pattern: List[int]) -> None:
        """
        Shift a pattern into the scan chain.
        
        Args:
            pattern (List[int]): Binary pattern to shift in
        """
        if len(pattern) != self.length:
            raise ValueError(f"Pattern length {len(pattern)} does not match chain length {self.length}")
        
        # Apply faults before shifting
        for i in range(self.length):
            if self.faults[i] == 1:  # stuck-at-1
                self.chain[i] = 1
            elif self.faults[i] == -1:  # stuck-at-0
                self.chain[i] = 0
            else:
                self.chain[i] = pattern[i]
                
    def shift_out(self) -> List[int]:
        """
        Shift out the current state of the scan chain.
        
        Returns:
            List[int]: Current state of the scan chain
        """
        return self.chain.tolist()
    
    def inject_fault(self, position: int, fault_type: int) -> None:
        """
        Inject a fault at a specific position in the scan chain.
        
        Args:
            position (int): Position to inject fault (0-based)
            fault_type (int): 1 for stuck-at-1, -1 for stuck-at-0
        """
        if position < 0 or position >= self.length:
            raise ValueError(f"Position {position} is out of range [0, {self.length-1}]")
        if fault_type not in [-1, 1]:
            raise ValueError("Fault type must be -1 (stuck-at-0) or 1 (stuck-at-1)")
        
        self.faults[position] = fault_type
        
    def clear_faults(self) -> None:
        """Clear all injected faults."""
        self.faults = np.zeros(self.length, dtype=int)
        
    def get_fault_coverage(self, test_patterns: List[List[int]]) -> float:
        """
        Calculate fault coverage for a set of test patterns.
        
        Args:
            test_patterns (List[List[int]]): List of test patterns to apply
            
        Returns:
            float: Fault coverage percentage
        """
        detected_faults = set()
        total_faults = np.sum(self.faults != 0)
        
        if total_faults == 0:
            return 100.0
            
        for pattern in test_patterns:
            # Apply pattern and check if faults are detected
            self.shift_in(pattern)
            output = self.shift_out()
            
            # Compare with expected output (pattern without faults)
            expected = pattern
            for i in range(self.length):
                if output[i] != expected[i]:
                    detected_faults.add(i)
                    
        return (len(detected_faults) / total_faults) * 100 if total_faults > 0 else 0.0 
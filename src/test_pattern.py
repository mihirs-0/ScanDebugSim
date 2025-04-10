import numpy as np
from typing import List, Optional

class TestPatternGenerator:
    @staticmethod
    def generate_random_patterns(length: int, num_patterns: int) -> List[List[int]]:
        """
        Generate random test patterns.
        
        Args:
            length (int): Length of each pattern
            num_patterns (int): Number of patterns to generate
            
        Returns:
            List[List[int]]: List of random binary patterns
        """
        return np.random.randint(0, 2, size=(num_patterns, length)).tolist()
    
    @staticmethod
    def generate_march_patterns(length: int) -> List[List[int]]:
        """
        Generate March test patterns (common memory test algorithm).
        
        Args:
            length (int): Length of each pattern
            
        Returns:
            List[List[int]]: List of March test patterns
        """
        patterns = []
        # March C- test patterns
        patterns.append([0] * length)  # Write 0
        patterns.append([1] * length)  # Write 1
        patterns.append([0] * length)  # Write 0
        return patterns
    
    @staticmethod
    def generate_atpg_patterns(length: int, fault_positions: List[int]) -> List[List[int]]:
        """
        Generate ATPG (Automatic Test Pattern Generation) patterns targeting specific faults.
        
        Args:
            length (int): Length of each pattern
            fault_positions (List[int]): Positions to target for fault detection
            
        Returns:
            List[List[int]]: List of ATPG patterns
        """
        patterns = []
        for pos in fault_positions:
            # Generate pattern to detect stuck-at-0
            pattern = [1] * length
            patterns.append(pattern)
            
            # Generate pattern to detect stuck-at-1
            pattern = [0] * length
            patterns.append(pattern)
            
        return patterns
    
    @staticmethod
    def generate_exhaustive_patterns(length: int) -> List[List[int]]:
        """
        Generate all possible patterns for exhaustive testing.
        
        Args:
            length (int): Length of each pattern
            
        Returns:
            List[List[int]]: List of all possible patterns
        """
        if length > 20:
            raise ValueError("Exhaustive patterns not recommended for length > 20")
            
        return [[(i >> j) & 1 for j in range(length)] 
                for i in range(2**length)] 
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.scan_chain import ScanChain
from src.test_pattern import TestPatternGenerator
from src.analyzer import ScanChainAnalyzer

def main():
    # Create a scan chain with 8 flip-flops
    chain = ScanChain(length=8, name="test_chain")
    
    # Inject some faults
    chain.inject_fault(2, 1)  # stuck-at-1 at position 2
    chain.inject_fault(5, -1)  # stuck-at-0 at position 5
    
    # Create analyzer
    analyzer = ScanChainAnalyzer(chain)
    
    # Generate and apply test patterns
    patterns = TestPatternGenerator.generate_random_patterns(8, 10)
    results = analyzer.run_test(patterns)
    
    # Print results
    print(analyzer.generate_report())
    
    # Plot results
    analyzer.plot_test_results(save_path="test_results.png")
    
    # Try ATPG patterns
    print("\nRunning ATPG patterns...")
    atpg_patterns = TestPatternGenerator.generate_atpg_patterns(8, [2, 5])
    atpg_results = analyzer.run_test(atpg_patterns)
    print(analyzer.generate_report())
    analyzer.plot_test_results(save_path="atpg_results.png")

if __name__ == "__main__":
    main() 
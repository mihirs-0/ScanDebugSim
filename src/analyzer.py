import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict, Optional
from .scan_chain import ScanChain

class ScanChainAnalyzer:
    def __init__(self, scan_chain: ScanChain):
        """
        Initialize analyzer for a scan chain.
        
        Args:
            scan_chain (ScanChain): The scan chain to analyze
        """
        self.scan_chain = scan_chain
        self.test_results = []
        
    def run_test(self, patterns: List[List[int]]) -> Dict:
        """
        Run a test with given patterns and record results.
        
        Args:
            patterns (List[List[int]]): Test patterns to apply
            
        Returns:
            Dict: Test results including coverage and detected faults
        """
        results = {
            'patterns': patterns,
            'outputs': [],
            'detected_faults': set(),
            'coverage': 0.0
        }
        
        for pattern in patterns:
            self.scan_chain.shift_in(pattern)
            output = self.scan_chain.shift_out()
            results['outputs'].append(output)
            
            # Check for faults
            for i in range(self.scan_chain.length):
                if output[i] != pattern[i]:
                    results['detected_faults'].add(i)
                    
        results['coverage'] = (len(results['detected_faults']) / 
                             np.sum(self.scan_chain.faults != 0)) * 100
        self.test_results.append(results)
        return results
    
    def plot_test_results(self, save_path: Optional[str] = None) -> None:
        """
        Plot test results including pattern application and fault detection.
        
        Args:
            save_path (Optional[str]): Path to save the plot
        """
        if not self.test_results:
            raise ValueError("No test results to plot")
            
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        # Plot patterns and outputs
        results = self.test_results[-1]  # Plot most recent results
        patterns = np.array(results['patterns'])
        outputs = np.array(results['outputs'])
        
        ax1.imshow(patterns, aspect='auto', cmap='binary')
        ax1.set_title('Applied Test Patterns')
        ax1.set_xlabel('Bit Position')
        ax1.set_ylabel('Pattern Number')
        
        ax2.imshow(outputs, aspect='auto', cmap='binary')
        ax2.set_title('Scan Chain Outputs')
        ax2.set_xlabel('Bit Position')
        ax2.set_ylabel('Pattern Number')
        
        # Highlight detected faults
        for pos in results['detected_faults']:
            ax2.axvline(x=pos, color='r', alpha=0.3)
            
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()
        
    def generate_report(self) -> str:
        """
        Generate a text report of test results.
        
        Returns:
            str: Formatted test report
        """
        if not self.test_results:
            return "No test results available"
            
        results = self.test_results[-1]
        report = []
        report.append(f"Scan Chain Analysis Report")
        report.append(f"========================")
        report.append(f"Chain Length: {self.scan_chain.length}")
        report.append(f"Number of Patterns: {len(results['patterns'])}")
        report.append(f"Fault Coverage: {results['coverage']:.2f}%")
        report.append("\nDetected Faults:")
        
        for pos in sorted(results['detected_faults']):
            fault_type = "stuck-at-1" if self.scan_chain.faults[pos] == 1 else "stuck-at-0"
            report.append(f"  Position {pos}: {fault_type}")
            
        return "\n".join(report) 
from src.simulation import run_simulation
import io
import sys

def test_simulation_runs_without_error():
    run_simulation(steps=5, seed=42)

def test_simulation_reproducibility():
    def capture_output():
        old = sys.stdout
        out = io.StringIO()
        sys.stdout = out
        try:
            run_simulation(steps=3, seed=100)
        finally:
            sys.stdout = old
        return out.getvalue()
    
    out1 = capture_output()
    out2 = capture_output()
    assert out1 == out2
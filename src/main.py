import typer
from src.simulation import run_simulation

app = typer.Typer()

@app.command()
def simulate(
    steps: int = typer.Option(20, "--steps", help="Number of simulation steps"),
    seed: int = typer.Option(None, "--seed", help="Random seed for reproducibility")
):
    run_simulation(steps=steps, seed=seed)


if __name__ == "__main__":
    app()
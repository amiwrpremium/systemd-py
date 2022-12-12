from typer import Typer

from .interactive.main import app as interactive_app

app = Typer(
    name="systemd-py",
    help="Systemd-py Commands",
)

app.add_typer(interactive_app, name="interactive")

if __name__ == "__main__":
    app()

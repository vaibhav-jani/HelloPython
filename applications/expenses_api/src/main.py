import subprocess
import sys
from pathlib import Path

# Add the parent directory to Python path
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))


def run_server():
    """Run the server in a separate process."""
    subprocess.run(["python", "-m", "src.server.server"], check=True)


def run_client():
    """Run the client in a separate process."""
    subprocess.run(["python", "-m", "src.client.client"], check=True)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "client":
        run_client()
    else:
        run_server()

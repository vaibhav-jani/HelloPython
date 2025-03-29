import subprocess
import sys
from pathlib import Path
import time

# Add the parent directory to Python path
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))


def run_server():
    """Run the server."""
    print("Starting server...")
    subprocess.run(["python", "-m", "src.server.server"], check=True)


def run_client():
    """Run the client."""
    print("Starting client...")
    subprocess.run(["python", "-m", "src.client.client"], check=True)


if __name__ == "__main__":
    # Run server in a separate process
    subprocess.run(["python", "-m", "src.server.server"], check=True)

    # Wait a moment for the server to start
    time.sleep(2)

    # Run the client
    run_client()

    # After client runs, terminate the server
    server_process.terminate()
    server_process.wait()
    print("Server has been stopped.")

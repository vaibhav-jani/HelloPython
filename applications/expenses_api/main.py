import subprocess
import time


def run_server():
    """Run the server."""
    print("Starting server...")
    subprocess.run(["python", "-m", "src.server.server"], check=True)


def run_client():
    """Run the client."""
    print("Starting client...")
    subprocess.run(["python", "-m", "src.client.client"], check=True)


if __name__ == "__main__":
    # Run the server in the background
    server_process = subprocess.Popen(["python", "-m", "src.server.server"])

    # Wait a moment for the server to start
    time.sleep(2)

    # Run the client
    run_client()

    # After client runs, terminate the server
    server_process.terminate()
    server_process.wait()
    print("Server has been stopped.")

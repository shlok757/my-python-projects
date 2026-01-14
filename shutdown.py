import platform
import subprocess

def shutdown(delay_seconds: int = 0) -> None:
    if delay_seconds < 0:
        raise ValueError("delay_seconds must be >= 0")

    system = platform.system().lower()

    if system == "windows":
        subprocess.run(["shutdown", "/s", "/t", str(delay_seconds)], check=True)
    elif system in ("linux", "darwin"):
        if delay_seconds == 0:
            subprocess.run(["shutdown", "-h", "now"], check=True)
        else:
            minutes = max(1, (delay_seconds + 59) // 60)
            subprocess.run(["shutdown", "-h", f"+{minutes}"], check=True)
    else:
        raise RuntimeError(f"Unsupported OS: {platform.system()}")

if __name__ == "__main__":
    shutdown(60)

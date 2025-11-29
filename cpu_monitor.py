import psutil
import time

def monitor_cpu(threshold=80):
    print("Monitoring CPU usage...")
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            if cpu > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu}%")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    monitor_cpu(80)

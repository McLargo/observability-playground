import psutil
import time

from prometheus_client import Gauge, start_http_server


cpu_gauge = Gauge("demo_cpu_utilization_percent", "Current CPU utilization percentage")
memory_gauge = Gauge("demo_memory_free_bytes", "Current free memory in bytes")

def collect_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    free_memory = memory_info.available

    # example of setting the gauge values, this values can increase or decrease depending on the system state
    cpu_gauge.set(cpu)
    memory_gauge.set(free_memory)

    print(f"CPU: {cpu:.2f}%, Free Memory: {free_memory / (1024*1024):.2f} MB")

if __name__ == "__main__":
    start_http_server(8880)
    print("Prometheus metrics exposed on port 8880")

    while True:
        collect_metrics()
        time.sleep(5)

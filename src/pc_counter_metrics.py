import time

from prometheus_client import Counter, start_http_server

from enum_types import EventType, EventStatus

demo_count = Counter(
    "demo_prometheus_client_process_events_total",
    "Demo Process Events Total",
    ["event_type", "status"]
)


def process_event(event_type, status):
    """
    Simulates processing an event in the application.
    """
    print(f"Event simulation | demo_prometheus_client_process_events_total | {event_type} | {status}")
    demo_count.labels(event_type=event_type, status=status).inc()


if __name__ == "__main__":
    # Start the Prometheus metrics server on port 8880
    # to allow scraping of metrics.
    start_http_server(8880)
    print("Prometheus metrics server started on port 8880")

    # simulate some events
    process_event(EventType.LOGIN, EventStatus.SUCCESS)
    process_event(EventType.LOGIN, EventStatus.FAILURE)

    process_event(EventType.DATA_PROCESSING, EventStatus.SUCCESS)
    process_event(EventType.DATA_PROCESSING, EventStatus.FAILURE)

    # Keep the server running, so metrics can be scraped
    # sleep for 10 minutes to allow for metric collection.
    time.sleep(600)

    # once script is stopped, metrics won't be available anymore

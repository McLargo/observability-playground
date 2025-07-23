import time
import uuid

from prometheus_client import CollectorRegistry, Counter, push_to_gateway

from enum_types import EventType, EventStatus


registry = CollectorRegistry()

demo_count = Counter(
    "demo_push_gateway_process_events_total",
    "Demo Process Events Total",
    ["event_type", "status"],
    registry=registry,
)

def init_metrics():
    demo_count.labels(event_type=EventType.LOGIN, status=EventStatus.SUCCESS).inc(0)
    demo_count.labels(event_type=EventType.LOGIN, status=EventStatus.FAILURE).inc(0)
    demo_count.labels(event_type=EventType.DATA_PROCESSING, status=EventStatus.SUCCESS).inc(0)
    demo_count.labels(event_type=EventType.DATA_PROCESSING, status=EventStatus.FAILURE).inc(0)
    # wait until the metrics are initialized
    print("Metrics initialized, waiting for 15 seconds before processing events...")
    time.sleep(15)



def process_event(event_type, status):
    """
    Simulates processing an event in the push_gateway application.
    """
    print(f"Event simulation | demo_push_gateway_process_events_total | {event_type} | {status}")
    demo_count.labels(event_type=event_type, status=status).inc()


if __name__ == "__main__":
    init_metrics()

    # simulate some events
    process_event(EventType.LOGIN, EventStatus.SUCCESS)
    process_event(EventType.LOGIN, EventStatus.FAILURE)

    process_event(EventType.DATA_PROCESSING, EventStatus.SUCCESS)
    process_event(EventType.DATA_PROCESSING, EventStatus.FAILURE)

    try:
        push_to_gateway(
            "localhost:9091",
            job="push_gateway_counter_group",
            grouping_key={"instance": str(uuid.uuid4())},
            registry=registry,
        )
        print("Metrics pushed to Pushgateway.")
    except Exception as e:
        print(f"Error sending metrics a Pushgateway: {e}")

import uuid

from prometheus_client import CollectorRegistry, Counter, push_to_gateway

from event_enum import EventType, EventStatus


registry = CollectorRegistry()

demo_count = Counter(
    "demo_push_gateway_process_events_total",
    "Demo Process Events Total",
    ["event_type", "status"],
    registry=registry,
)


def process_event(event_type, status):
    """
    Simulates processing an event in the push_gatewaylication.
    """
    print(f"Event simulation | demo_push_gateway_process_events_total | {event_type} | {status}")
    demo_count.labels(event_type=event_type, status=status).inc()


if __name__ == "__main__":
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

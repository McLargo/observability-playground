import random
import time

from enum_types import QueryType, SchemaType
from prometheus_client import Histogram, start_http_server


histogram = Histogram(
    "demo_db_query_latency_seconds",
    "Histogram demo simulating database query latency",
    labelnames=["type", "schema"],
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, float("inf")],
)


def simulate_query(query_type: QueryType, schema: SchemaType = SchemaType.USER):
    latency = None
    if query_type == QueryType.READ:
        latency = random.gauss(0.05, 0.02)
    elif query_type == QueryType.WRITE:
        latency = random.gauss(0.15, 0.05)
    elif query_type == QueryType.REPORT:
        latency = random.uniform(0.5, 3.0)

    if latency:
        histogram.labels(type=query_type, schema=schema).observe(latency)


if __name__ == "__main__":
    start_http_server(8880)
    print("Prometheus metrics exposed on port 8880")

    while True:
        # keep in mind that this is a simulation and the latencies are randomly generated.
        simulate_query(QueryType.READ)

        if random.random() < 0.3:
            simulate_query(QueryType.WRITE)

        if random.random() < 0.1:
            simulate_query(QueryType.REPORT)
            time.sleep(random.uniform(1, 5))

        time.sleep(2)

# small explanation of the histogram metric and how to use it:
# values in buckets are accumulated. So the bigger the bucket, the more values will be in it.

# demo_db_query_latency_seconds_bucket{type="QueryType.REPORT", le="2.5"} -> 5 results
# demo_db_query_latency_seconds_bucket{type="QueryType.REPORT", le="5.0"} -> at least 5 results, but could be more
# demo_db_query_latency_seconds_bucket{type="QueryType.REPORT", le="+Inf"} -> all results in the query type "REPORT"

# this metric is more useful when combined with percentiles, like:

# histogram_quantile(0.90, sum by (le, type) (rate(demo_db_query_latency_seconds_bucket[5m])))

# this will give you the 90th percentile of the latencies for each query type in the last 5 minutes.
# with query like this, you can set alerts to notify you when the latency exceeds a certain threshold.

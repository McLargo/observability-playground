# Querying

Prometheus provides a powerful
[query language](https://prometheus.io/docs/prometheus/latest/querying/basics/)
called PromQL, which allows you to perform actions such as filter, group, and
aggregate metrics.

## Rate-based Functions (for Counters)

Counters are monotonically increasing metrics. To get a meaningful value, you
need to use rate-based functions.

- rate(range-vector): calculates the per-second average rate of increase of a
  time series over a specified time range.

  Example: rate(http_requests_total[5m]) - HTTP requests per second over the
  last 5 minutes.

- irate(range-vector): calculates the instantaneous per-second rate of increase,
  using only the last two data points in the specified time range. Useful for
  volatile, rapidly changing counters.

  Example: irate(node_cpu_seconds_total[1m]) - Instantaneous CPU usage.

- increase(range-vector): calculates the total increase in the counter's value
  over the specified time range.

  Example: increase(errors_total[1h]) - Total errors in the last hour.

## Aggregation Functions

These functions aggregate values across different time series.

- sum(): calculates the sum of all values across matching time series. Often
  used with by() or without() to group results.

  Example: sum(rate(node_cpu_seconds_total[5m])) by (mode) - Total CPU usage
  summed by mode (user, system, idle).

- avg(): calculates the average of all values across matching time series.

  Example: avg(node_memory_usage_bytes) - Average memory usage across all nodes.

- max(): finds the maximum value across matching time series.

- min(): finds the minimum value across matching time series.

- count(): counts the number of time series matching the selector.

## Over-Time Functions (for Gauges and Trends)

These functions operate on a range vector and return an instant vector,
calculating a value over a specified time window for each individual series.
Useful for gauges or analyzing trends.

- `aggregation_over_time()`: a series of functions that calculate
  various statistics over a specified time range.

  Examples: avg_over_time(node_memory_free_bytes[1h]) - Average free memory in
  the last hour.

## Histogram Functions (for Latency/Distribution)

Histograms are a complex metric type used to sample observations and count them
in configurable buckets.

- histogram_quantile(`percentile`, histogram_bucket_range-vector): calculates the
  percentile from a histogram metric. This is commonly used to analyze
  latency distributions.

  Example: histogram_quantile(0.95,
  rate(http_request_duration_seconds_bucket[5m])) - 95th percentile HTTP request
  duration over the last 5 minutes.

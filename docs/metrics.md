# Metrics

Metric is the fundamental unit of measurement in Prometheus. It is a numerical
value that represents a measurement of a system or application.

[Metrics can be](https://prometheus.io/docs/concepts/metric_types/) counters
(increasing values), gauges (numerical value can go up and down), histograms
(time distribution and percentiles), or summaries (similar to histograms, but
data cannot be aggregated).

## Publish metrics

From application code, you can publish metrics to Prometheus using the push
gateway or the Prometheus client library. We are going to give examples of both
methods in this playground.

### Push gateway

The Push gateway is a service that allows you to push metrics from your
application to Prometheus. This is useful for short-lived jobs or applications
that cannot be scraped by Prometheus directly. Metrics will live in this
gateway.

```bash
task counter-push-gateway
```

Metrics are available at
[http://localhost:9091/metrics](http://localhost:9091/metrics).

### Prometheus client library

It requires to start a web server to expose the metrics. You can check the
targets being scraped by Prometheus in the
[targets page](http://localhost:9090/targets).

```bash
task counter-prometheus-client
```

While the server is running, you can access the metrics at
[http://localhost:8880/metrics](http://localhost:8880/metrics). Once the server
is stopped, the metrics will no longer be available.

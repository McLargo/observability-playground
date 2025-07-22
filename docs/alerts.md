# Alerting

Alerts are configured and managed in yaml files, which are loaded by Prometheus.
[Alerts are available](http://localhost:9090/alerts) in the interface.

Some features of the alerting system are:

- send notifications to various channels based on alert severity, labels, or
  other criteria
- grouping alerts by labels
- silencing alerts for a period of time
- inhibiting alerts based on other alerts
- if more than one alert is triggered, you can group them into a single
  notification
- you can add annotations to alerts, which can be used to provide additional
  context or information about the alert

Prometheus provides an alerting system that allows you to define rules to
trigger alerts based on the metrics collected. Alerts can be sent to
[Alertmanager](http://localhost:9093/#/alerts), which manages the alerts and
[can send notifications to various channels](https://prometheus.io/docs/alerting/latest/configuration/#general-receiver-related-settings).

In this playground, we are using Prometheus's alerting system, but Grafana can
also be used to manage alerts, if you want to reduce the number of dependencies.

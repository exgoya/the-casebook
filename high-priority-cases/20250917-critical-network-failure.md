
---
case_id: 20250917-critical-network-failure
priority: high
status: open
owner: seonghoon
created_at: 2025-09-17
updated_at: 2025-09-17
product: network
tags: [latency, outage, critical]
---

# Critical Network Failure (2025-09-17)

## 🔍 Issue Summary
- Latency spiked to 1000ms+
- Database connections dropped
- Load balancer health checks failing

## 🔧 Resolution Plan
1. Capture packets with tcpdump
2. Validate load balancer configuration
3. Coordinate with ISP

## 🔗 Related Tickets
- #60123 Network Latency

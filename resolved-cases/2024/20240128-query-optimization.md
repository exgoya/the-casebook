
---
case_id: 20240128-query-optimization
priority: medium
status: resolved
owner: seonghoon
created_at: 2024-01-28
updated_at: 2024-01-30
product: singlestore
tags: [performance, sql]
---

# Query Optimization (2024-01-28)

## 🔍 Issue Summary
- Complex JOIN query was taking >10s
- High CPU usage on leaf nodes

## ✅ Resolution Outcome
- Rewritten query using shard key filter
- Reduced execution time to <500ms

---
case_id: 20250917-slow-recovery
priority: medium
status: open
owner: seonghoon
created_at: 2025-09-17
updated_at: 2025-09-17
product: [singlestore, weka]
tags: [slow-recovery, performance]
---

# Slow Recovery Issue (20250917)

## 🔍 Issue Summary
- System recovery is slower than expected after node restart.
- Affects both Weka storage layer and SingleStore DB restart process.

## 📊 Observations & Evidence
- Logs from Weka show delayed volume attachment.
- SingleStore node takes longer to rejoin cluster.

## 🔧 Resolution Plan
1. Analyze storage logs from Weka
2. Check SingleStore node recovery parameters
3. Test recovery under controlled failure

## ✅ Resolution Outcome (Pending)
- To be filled after resolution.

## 🔗 Related Tickets
- #50123 Weka volume recovery delay
- #50124 SingleStore HA recovery

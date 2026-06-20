# Developer Analytics Platform

## Overview

A desktop activity analytics platform that monitors user activity across applications and websites, then generates usage reports and productivity analytics through a web dashboard.

The system consists of:

* Desktop Agent
* Backend API
* Analytics Processing System
* PostgreSQL Database
* Web Dashboard

### Some challenges i would face
- How do i convert the raw events into continous sessions

---

# User Flow

1. User creates an account.
2. User generates an API key.
3. User downloads the desktop agent.
4. User configures the agent with the API key.
5. Agent runs in the background.
6. Agent collects activity events.
7. Agent periodically sends event batches to the backend.
8. Backend processes and stores events.
9. Dashboard displays analytics generated from those events.

---

# Activity Collection

The desktop agent should collect the following information.

## Event

```json
{
  "timestamp": "2026-06-20T10:00:00Z",
  "application": "chrome.exe",
  "windowTitle": "Twitter / X - Home",
  "isIdle": false
}
```

## Collection Frequency

Every:

```text
10 seconds
```

## Batch Upload Frequency

Every:

```text
30 seconds
```

---

# Idle Detection

The agent should detect:

* Keyboard inactivity
* Mouse inactivity

Example:

```text
No keyboard or mouse activity for 5 minutes
```

Result:

```json
{
  "isIdle": true
}
```

Idle periods should not contribute to usage analytics.

---

# Data Storage

## Raw Events

Store every collected event.

Purpose:

* Source of truth
* Recompute analytics later
* Debugging

Example:

```text
10:00 VS Code
10:10 VS Code
10:20 Chrome
10:30 Chrome
```

---

## Sessions

Generated from raw events.

Example:

```text
VS Code
10:00 - 11:15
```

Duration:

```text
75 minutes
```

---

## Analytics Tables

Store precomputed summaries.

Examples:

```text
Today
This Week
This Month
```

---

# Dashboard Analytics

## Application Usage

Example:

```text
VS Code
3h 20m
```

```text
Chrome
2h 10m
```

---

## Website Usage

Example:

```text
x.com
50 minutes
```

```text
youtube.com
30 minutes
```

Requirements:

* Extract website/domain from browser activity
* Aggregate time by domain

---

## Activity Timeline

Example:

```text
09:00 VS Code
09:45 Chrome
10:15 Terminal
```

---

## Top Applications

Rank applications by usage duration.

---

## Top Websites

Rank domains by usage duration.

---

# Filters

Users can filter analytics by:

## Time Range

* Today
* Yesterday
* Last 7 Days
* Last 30 Days
* Custom Range

## Tags

Developer-defined categories.

Examples:

```text
Work
Learning
Social Media
Entertainment
Communication
```

Examples:

```text
x.com
→ Social Media
```

```text
youtube.com
→ Entertainment
```

```text
stackoverflow.com
→ Learning
```

---

# Phase 1 Scope

Must Have:

* User authentication
* API key generation
* Desktop agent
* Activity collection
* Idle detection
* Event ingestion API
* Raw event storage
* Basic dashboard
* Application usage analytics

---

# Phase 2 Scope

* Session generation
* Website analytics
* Time filters
* Tagging system
* Weekly reports
* Monthly reports

---

# Phase 3 Scope

* Redis
* BullMQ
* Workers
* Background analytics processing
* Cached reports

---

# Success Criteria

A user should be able to:

1. Install the desktop agent.
2. Let it run in the background.
3. Return later and see:

   * Which applications were used.
   * Which websites were visited.
   * How long each was used.
   * Usage trends over different time periods.
4. Filter analytics by date range and tags.

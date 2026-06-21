# Developer Analytics Platform

## Overview

Developer Analytics Platform is a self-hosted productivity analytics system that tracks application usage on a developer's machine and presents the data through a web dashboard.

The platform consists of a lightweight desktop agent, a backend service, a database, and a frontend dashboard.

The desktop agent runs in the background, monitors the currently focused window, detects application changes, records activity events, and periodically uploads them to the backend. The backend processes these raw events into meaningful sessions and aggregates analytics that are displayed on the dashboard.

The primary goal of the project is to learn and implement real-world backend architecture patterns such as event collection, ingestion pipelines, asynchronous processing, session generation, analytics aggregation, and dashboard visualization.

---

## Problem Statement

Developers spend a large amount of time across different applications, browsers, IDEs, terminals, communication tools, and documentation websites.

Most operating systems provide only limited visibility into how time is spent throughout the day.

This project aims to answer questions such as:

* How much time was spent coding today?
* Which applications were used most frequently?
* How much time was spent on specific websites?
* What percentage of the day was productive versus idle?
* How does activity compare across days, weeks, and months?

---

## High-Level Architecture

```text
Desktop Agent
      │
      ▼
Ingestion API
      │
      ▼
Database
      │
      ▼
Analytics API
      │
      ▼
Frontend Dashboard
```

Future architecture:

```text
Desktop Agent
      │
      ▼
Ingestion API
      │
      ▼
Queue
      │
      ▼
Workers
      │
      ▼
Database
      │
      ▼
Analytics API
      │
      ▼
Frontend Dashboard
```

---

## Core Components

### Desktop Agent

Responsibilities:

* Monitor focused window
* Detect application changes
* Detect window title changes
* Detect user idle state
* Generate activity events
* Buffer events locally
* Upload event batches to backend

Technology:

* Python
* pywin32
* psutil
* httpx
* Pydantic

---

### Backend

Responsibilities:

* Authenticate agents
* Accept event batches
* Validate incoming data
* Generate activity sessions
* Store analytics data
* Serve dashboard APIs

Technology:

* FastAPI
* PostgreSQL
* SQLAlchemy

---

### Frontend

Responsibilities:

* User authentication
* API key management
* Dashboard visualization
* Analytics exploration

Technology:

* Next.js
* TypeScript
* Tailwind CSS

---

## Activity Event Model

Each recorded event represents the current state of the user's machine at a specific timestamp.

Example:

```json
{
  "timestamp": "2026-06-20T10:00:00Z",
  "application": "Code.exe",
  "windowTitle": "main.py - Visual Studio Code",
  "isIdle": false
}
```

---

## Data Collection Strategy

### Polling

The agent polls the operating system every second.

Purpose:

* Detect focused window
* Detect title changes
* Detect idle state

### Window Change Events

An event is immediately recorded when:

* Application changes
* Window title changes

### Snapshots

An event is recorded periodically even when nothing changes.

Purpose:

* Prove continuous activity

Example:

```text
09:00 VS Code
09:10 VS Code
09:20 VS Code
```

---

## Event Buffering

Events are first written to a local buffer file.

Example:

```text
buffer.json
```

Benefits:

* Prevent data loss
* Survive crashes
* Survive network failures
* Allow retry uploads

Events remain in the buffer until successfully uploaded.

---

## Session Generation

Raw events only contain timestamps.

The backend converts them into sessions.

Example:

```text
09:00 VS Code
09:10 VS Code
09:20 VS Code
09:30 Chrome
```

Generated sessions:

```text
VS Code : 09:00 → 09:30
Chrome  : 09:30 → ...
```

These sessions become the foundation for all analytics.

---

## Dashboard Analytics

### Application Usage

Examples:

```text
VS Code      4h 12m
Chrome       2h 03m
Terminal     1h 15m
```

### Website Usage

Examples:

```text
github.com      1h 42m
stackoverflow   28m
x.com           52m
```

### Time Filters

* Today
* Yesterday
* This Week
* This Month
* Custom Range

### Idle Analytics

Examples:

* Active time
* Idle time
* Productivity ratio

---

## Learning Goals

This project is designed to teach:

### Backend Engineering

* API design
* Database modeling
* Authentication
* Data pipelines
* Event ingestion

### System Design

* Queues
* Workers
* Batch processing
* Event-driven systems
* Analytics architecture

### Desktop Development

* Operating system APIs
* Process inspection
* Background agents
* Local persistence

### Full-Stack Development

* Frontend dashboards
* Data visualization
* Client-server communication
* Authentication flows

---

## Success Criteria

A successful MVP should allow a user to:

1. Create an account.
2. Generate an API key.
3. Download and run the desktop agent.
4. Collect activity data automatically.
5. Upload events to the backend.
6. View usage analytics in a web dashboard.
7. Explore activity by day, week, and month.

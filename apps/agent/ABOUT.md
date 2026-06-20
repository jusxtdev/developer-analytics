# Desktop Agent

### Purpose

- Tracks the user activity and sends the event buckets to the backend

## Working overview

- User switches windows (from window1 to window2)
- Agent detects this event

```json
{
  "timestamp": "2026-06-20T10:00:00Z",
  "application": "chrome.exe",
  "windowTitle": "Twitter / X - Home",
  "isIdle": false
}
```

- Logs this event in a `events.json` or `buffer.json`
- It also detects whether user is idle or not
- `buffer.json` is the batch that will be uploaded in an interval of 30 seconds

## Different components

- `main.py` - entry point of the application
- `instanceManager.py` - ensures that only one instance of agent is running
  - **WHY** = to prevent below two things
    1. Duplicate events sent to backend
    2. memory wastage
- `monitor.py` - core of this agent, monitors windows and applications, store the event data into `buffer.json`
- `activityTracker.py` - detects keyboard and mouse movements, used to detect whether user is idle or not
- `errorhandler.py` - used in try/except block to handle errors / send that response to the user or the backend

## Some bottlenecks

- As the event data of a window is derived from the windows title (along with PID)
- if a window doesn't have the name of the website in it's title, we would not be able to access that sites data
- for example,
  - In case of using ChatGPT inside a browser, the title of the window is `linkedin post - Google Chrome`
  - This does not give any information about what website the user is visitng

- so for now, we cannot determine the website user visits

- **Future Solutions** - we can use a browser extension to access the url of the websites

## Collection Frequency of events into `buffer.json`
-  Event is logged when the title of the window is changed ie you move the focus of the window, this also includes changing tabs in browser and changing files in vscode
-  After you enter a window, say the title is "Youtube - Google Chrome"
-  The next event will be recorded when
   -  Every 5 minutes heartbeat events
   -  if user becomes idle
  
## when is ingestions api called
- every 30 seconds all the events from `buffer.json` are sent as batch to the ingestion api
# Incident Triage & Bug Management Challenge

## Section 1: Getting Started

To run the application suite locally, you must have Docker and Docker Compose installed.

1. **Navigate to the challenge directory:**
   
   ```bash
   cd <path-to-the-code-location>
   ```

2. **Build and spin up the containers:**
   
   ```bash
   docker compose up --build -d
   ```

3. **Access the application portals and hotlists:**
   - **`http://localhost:8081` (Issue Tracker / Hotlists):**
     - **Active Incident Triage Queue (`hotlist:5829104`):** Direct link at `http://localhost:8081/hotlists/5829104`. This hotlist is dedicated to the **Bug Ping / Follow-Up and Ownership Re-assignment Challenge** (Tasks 1 & 2), containing active findings that require immediate triage review, ownership routing, and assignee follow-up.
     - **Enterprise Vulnerability Inventory & Backlog (`hotlist:7920155`):** Direct link at `http://localhost:8081/hotlists/7920155`. This hotlist is dedicated to the **Hotlist Querying & Filtering Challenge** (Task 3 & Section 4), containing the complete enterprise backlog for running search queries, filtering by status/priority/component, and investigating vulnerability classes.
   - **`http://localhost:8082` (Team & Ownership Directory Service):** Serves the internal service registry holding engineering teams, owned API endpoints, Tech Leads (TLs), and On-Call rosters. Use this service to identify rightful owners during bug triage and re-routing.

4. To stop the server, press `Ctrl+C` or run:

   ```bash
   docker compose down
   ```

## Section 2: Hotlist Overview

Issue Tracker provides two main hotlists accessible via the top navigation:

### 1. Active Incident Triage Queue (`hotlist:5829104`)
Contains high-priority findings currently undergoing active triage and remediation:

```
+---------------+-------------+----------+------------+-------------------------------------+-----------------+
| Issue ID      | Priority    | Severity | Status     | Title                               | Assignee        |
+---------------+-------------+----------+------------+-------------------------------------+-----------------+
| b/543338174   | P1          | S1       | Assigned   | Payments Webhook Signature Flaw     | @maya_l         |
| b/618294710   | P1          | S1       | Triaged    | Customer Account API PII Leakage    | (Unassigned)    |
+---------------+-------------+----------+------------+-------------------------------------+-----------------+
```

#### Bug [`b/543338174`](http://localhost:8081/issues/543338174): Payments Webhook Signature Verification Flaw
- **Title:** `[Internal Security Finding] Insecure Webhook Signature Verification in Payments Webhook Handler (/api/v1/payments/webhook)`
- **Reporter:** `johndoe@company.com` (John Doe - Internal Privacy Assurance)
- **Current State:** Previously misassigned to an IAM engineer (`david_p`), who was pinged by triage to confirm ownership. David clarified he does not own the service and reassigned the ticket to `@maya_l` (Payments & Billing Primary On-Call). Maya confirmed ownership and stated she would prepare a hotfix, but **has not updated the ticket since**. The bug is now **approaching its Due Date (SLO Deadline)** with 2 days remaining.
- **Due Date (SLO):** `Approaching SLO Deadline - 2 days remaining` *(dynamically calculated in Issue Tracker relative to challenge launch time)*

#### Bug [`b/618294710`](http://localhost:8081/issues/618294710): Customer Account API PII Leakage
- **Title:** `[Internal Security Finding] Customer Account API (/api/v2/clients/details) leaking sensitive client PII (SSN, home address, phone) in unauthenticated responses`
- **Reporter:** `johndoe@company.com` (John Doe - Internal Privacy Assurance)
- **Current State:** Acknowledged by security triage, but currently **unassigned** and awaiting proper ownership routing to the responsible Customer Account & Data Services Primary On-Call.
- **Due Date (SLO):** `Target: 48h SLA` *(dynamically calculated in Issue Tracker relative to challenge launch time)*

### 2. Enterprise Vulnerability Inventory & Backlog (`hotlist:7920155`)
Contains the full repository of vulnerabilities, incidents, and bugs across enterprise services (accessible at `http://localhost:8081/hotlists/7920155`). Use the search bar to query and filter bugs using structured syntax:

- `status:<assigned|triaged|fixed|verified|blocked|open|closed>`
- `assignee:<ldap|none|unassigned>`
- `priority:<p0|p1|p2|p3>` or `p:<p1>`
- `severity:<s0|s1|s2|s3>` or `s:<s1>`
- `component:"<name>"` (e.g. `component:"payments"`, `component:"iam"`, `component:"privacy"`)
- Substring keyword terms (e.g. `webhook`, `PII`, `JWT`, `SSN`, `CORS`, `Docker`)


## Section 3: Objectives & Tasks

As a Security Triage Engineer, your evaluation consists of three core tasks:

1. **Task 1:**
   - Review bug `b/543338174`.
   - Perform all appropriate follow-up actions (posting a status ping, checking if blocked, proposing chat outreach and escalation if needed).

2. **Task 2:**
   - Review bug `b/618294710`.
   - Use the **Team & Ownership Directory** (`http://localhost:8082`) to resolve the owning team and Primary On-Call.

3. **Task 3:**
   - Navigate to the **Vulnerability Inventory & Backlog (`hotlist:7920155`)**.
   - Complete the **4 Hotlist Querying Challenges** detailed in **Section 4**.

> **Important:** Review [TRIAGE_GUIDELINES.md](TRIAGE_GUIDELINES.md) for operational standards regarding bug assignments, ownership routing, reporter communications, follow-up pings, SLO tracking, and query syntax.


## Section 4: Hotlist Querying Challenge

Navigate to the **Enterprise Vulnerability Inventory & Backlog (`hotlist:7920155`)** at `http://localhost:8081/hotlists/7920155`. Execute the following **five search queries** to analyze the enterprise backlog and formulate your triage observations:


**Challenge 1: Unassigned Active Triage Queue**

- **Scenario:** As the triage lead, you need to identify all active, unresolved security findings across the organization that currently lack an assigned engineer and require immediate ownership routing.
- **Candidate Tasks in Report:**
  
  1. Record the exact query used and list all matching bug numbers (`b/...`).

  2. Cross-reference each unassigned bug with the **Team & Ownership Directory** (`http://localhost:8082`) to specify the rightful primary on-call engineer and team to which each should be assigned.

**Challenge 2: Critical & High-Priority Active Incidents**

- **Scenario:** Perform an analysis of all critical (`P0`) and high-priority (`P1`) vulnerabilities currently in an active state to track remediation progress against SLO deadlines.
- **Candidate Tasks in Report:**
  
  1. Record the exact query used and list all matching bug numbers (`b/...`).

  2. Identify which active bug is marked as `Blocked` and explain what external dependency or resource is blocking the engineer from finishing the fix.

  3. Identify the bugs that are approaching their SLO deadlines, and execute the necessary actions for the SLO to be fulfilled.

**Challenge 3: Identity, Authentication & Session Security Audit**

- **Scenario:** The Identity & Access Management (IAM) team is conducting a component-wide security review. Identify all vulnerabilities affecting authentication for the IAM component.

- **Candidate Tasks in Report:**

  1. List all matching bugs, their current status, and assignees.

  2. Confirm whether the historical P0 SSO session fixation vulnerability has been successfully verified and closed.

**Challenge 4: Data Privacy Governance & Regulatory Compliance**

- **Scenario:** Ahead of an upcoming regulatory audit, compile an inventory of all issues (open and already closed) concerning client Personally Identifiable Information (PII) leakage OR GDPR compliance workflows (`GDPR` / `PII`) across both `Data Privacy Governance` and `Privacy & Data Protection` components, while excluding the `Audit Logging` sub-component.

- **Candidate Tasks in Report:**
  
  1. Record the exact query used and list all matching bugs.

---



# Bug Triage & Incident Management Guidelines

## 1. Overview & Core Job Responsibilities

As a Security Triage Engineer, your primary role is to actively manage and drive security bugs from initial intake to successful resolution. Your day-to-day responsibilities focus on:

- **Finding the Correct Assignee (Re-mapping):** When a bug is unassigned or mapped incorrectly, identify the rightful owning team and reassign it to the correct person.
- **Pinging Bugs & Assignees:** Proactively comment on tickets to check status, remind owners of upcoming deadlines, and keep bugs active.
- **Reaching Out via Chat:** If the assignee remains silent for several days after an initial bug ping, reach out via internal team chat channels to confirm they are aware of the issue.
- **Maintaining Bug Traction & Progress:** Ensure the bug does not get buried in a team's backlog or forgotten after initial acknowledgment.
- **Helping with Technical Questions:** Assist engineers by clarifying reproduction steps, sample payloads, affected endpoints, and technical remediation context.
- **Ensuring SLO Adherence:** Monitor the proposed Service Level Objective (SLO) due date to make sure the bug is resolved and closed on time.
- **Hotlist Querying & Backlog Inspection:** Use structured query filtering to search for specific classes of vulnerabilities, unassigned tickets, or high-severity incidents.

---

## 2. Finding New Assignees & Correcting Mismapped Bugs

Bugs often arrive unassigned or get routed to the wrong team (e.g., an engineer unassigns themselves because they do not own the service):

1. **Investigate the Finding:** Check the affected API endpoint, service name, and code path.
2. **Query the Ownership Directory:** Use the **Team & Ownership Directory** (`http://localhost:8082`) to resolve which team owns the affected asset.
3. **Reassign to the Point of Contact:** Assign the ticket in the tracker to the team's Primary On-Call LDAP.
4. **Post an Internal Handover Note:** Leave a comment asking if the person is the correct one to oversee the issue and if they have context on what is going on.

---

## 3. Pinging Bugs & Following Up on Progress

Assigning a bug is only the start. Bugs frequently lose momentum when teams focus on feature work or when an engineer acknowledges a ticket but forgets to follow through:

### When and How to Ping:
- **Direct Bug Pings:** When a ticket sits with no updates for a while or when the **Due Date (SLO Deadline)** approaches, post a follow-up comment tagging the assignee (`@<ldap>`).
- **Inquire About Status:** Politely ask whether a hotfix or PR has been prepared, tested, or deployed. Or if they already have a roadmap planned for this.
- **Reach Out via Chat:** If you have already pinged the bug and several days pass without any response from the assignee, reach out directly in the team's chat channel to ensure they are aware of the high-priority finding.
- **Escalate When Stalled:** If the assignee is unresponsive, unavailable, or blocked by other priorities, escalate the ticket to the team's **Secondary On-Call** or **Tech Lead (TL)** before the SLO breaches.

---

## 4. Helping with Technical Questions

Triage engineers provide technical support to help service teams understand and fix findings rapidly:

- **Clarifying Reproduction:** Explain reproduction curl commands, query parameters, or payload details if the service owner is unable to reproduce the issue.
- **Scope & Data Exposure:** Clarify which database fields, models, or endpoints are affected (e.g., unmasked SSNs, unauthenticated webhooks).
- **Remediation Context:** Provide guidance on standard security libraries or architectural patterns (e.g., applying PII masking filters, implementing HMAC-SHA256 signature verification middleware).
- **Escalating to Remediation Tech Lead:** If a technical question or reproduction ambiguity cannot be answered directly by the triage team, escalate to the Remediation Tech Lead for technical guidance.

---

## 5. Ensuring Resolution Within Proposed SLOs

Every security finding has a defined **Service Level Objective (SLO)** based on its severity and priority (e.g., P1/S1 findings typically require resolution within 24–48 hours or within 7 days for infrastructure fixes):

- **Track Due Dates:** Keep continuous visibility on the **Due Date (SLO)** attribute on all open tickets.
- **Prevent Breaches Proactively:** Do not wait until the deadline day to check on progress. Ping assignees early enough that blockers can be addressed before the SLO is missed.
- **Verify Closure:** Ensure the ticket is properly updated with linked PRs/fixes and confirmed resolved before closing.

---

## 6. Hotlist Querying, Filtering & Logical Operations

Issue Tracker supports structured search queries and rich boolean logic in the search bar across all hotlists:

### A. Field Token Filters
- **Status Filters:**
  - `status:assigned` - Bugs actively assigned to an engineer.
  - `status:triaged` - Newly triaged bugs awaiting assignment.
  - `status:open` - All active, unresolved bugs (excludes Fixed/Verified).
  - `status:fixed` or `status:verified` - Resolved bugs.
  - `status:blocked` - Bugs blocked on external dependencies.
- **Assignee Filters:**
  - `assignee:<ldap>` (e.g. `assignee:maya_l`, `assignee:david_p`) - Bugs assigned to a specific engineer.
  - `assignee:none` or `assignee:unassigned` - Bugs with no assigned owner.
- **Priority & Severity Filters:**
  - `priority:p0`, `priority:p1`, `priority:p2`, `priority:p3` (or alias `p:p1`, `p:0`).
  - `severity:s0`, `severity:s1`, `severity:s2`, `severity:s3` (or alias `s:s1`, `s:0`).
- **Component Filters:**
  - `component:payments` - Financial & Payments Security domain.
  - `component:iam` - Identity & Access Management domain.
  - `component:privacy` - Customer Data & Privacy domain.
  - `component:infra` - Cloud Infrastructure & Container Security domain.
  - `component:gateway` - API Gateway & Edge Infrastructure domain.
- **Keywords & Exact Phrases:**
  - Exact quoted phrases: `"API key"`, `"Docker socket"`, `"none" Algorithm`.
  - Free-text terms: `webhook`, `SSN`, `JWT`, `Docker`, `CORS`, `signature`, `sandbox`.

### B. Logical Operations (Boolean Algebra)
The search engine supports logical operators to formulate multi-dimensional queries:

| Operator | Syntax Variants | Description | Example |
|---|---|---|---|
| **AND (Conjunction)** | `AND`, `&&`, `&`, or whitespace | All specified conditions must be satisfied. Consecutive tokens implicitly use `AND`. | `status:open AND priority:p1`<br>`status:open component:iam` |
| **OR (Disjunction)** | `OR`, `\|\|`, `\|` | At least one of the conditions must be satisfied. | `"API key" OR "Docker socket"`<br>`component:iam OR component:privacy` |
| **NOT (Negation)** | `NOT`, `!` | Excludes bugs matching the following condition. | `status:open NOT component:iam`<br>`status:open !priority:p3` |
| **Grouping (Parentheses)** | `( ... )` | Controls evaluation precedence when mixing `AND` and `OR`. | `status:open AND (priority:p0 OR priority:p1)`<br>`status:open ("API key" OR docker)` |

### C. Operator Precedence
Expressions are evaluated following standard boolean algebra precedence rules:
1. **Parentheses `( )`** *(Innermost expressions evaluated first)*
2. **`NOT` / `!`** *(Unary negation)*
3. **`AND` / `&&` / whitespace** *(Conjunction)*
4. **`OR` / `\|\|` / `\|`** *(Disjunction)*

### D. Practical Triage Query Examples

- **Critical & High-Priority Active Incidents:**
  ```sql
  status:open AND (priority:p0 OR priority:p1)
  ```
  
- **Actionable High-Priority Incidents (Excluding Blocked Dependencies):**
  ```sql
  status:open AND (priority:p0 OR priority:p1) NOT status:blocked
  ```

- **Cross-Component:**
  ```sql
  (component:"Billing" OR component:"Financial & Payments Security")
  ```

- **Unassigned Intake Queue Across Core Security Domains:**
  ```sql
  status:open assignee:none (component:iam OR component:privacy OR component:payments)
  ```

- **Searching for specific strings/words:**
  ```sql
  ("Primary On-Call" OR "PR #" OR microservices)
  ```

- **Tracking Blocked High-Impact Vulnerabilities:**
  ```sql
  status:blocked (priority:p1 OR priority:p2)
  ```

- **Domain-Wide IAM & Authentication Security Audit:**
  ```sql
  component:iam (JWT OR OAuth OR SSO OR session)
  ```

---

## 7. Communication & Ping Examples

### Example A: Handover Note (Re-routing a Mismapped Bug)
> *"Reassigning to **@lucas_m** (Primary On-Call for Customer Account & Data Services) based on the Service Ownership Directory. Could you please confirm if you are the correct person to oversee this issue and if you have context on what is going on with `/api/v2/clients/details`? Target SLO due date: within 48h (per ticket SLO). Please let us know if you need assistance reproducing or if this belongs to someone else on the team."*

### Example B: Follow-Up Ping (Dormant Bug Approaching SLO Deadline)
> *"Hi **@maya_l**, following up on this P1 finding regarding missing HMAC signature verification on `/api/v1/payments/webhook`. The SLO due date is approaching (2 days remaining per ticket deadline). Could you share a quick status update on the hotfix PR? Please let us know if you are blocked or need additional reproduction details from triage."*

### Example C: Chat Check-In (After Days Without Response)
> *"Hi @maya_l / #payments-eng-oncall, checking in on P1 bug `b/543338174` (Payments Webhook Auth). We wanted to confirm you're aware of the upcoming SLO deadline and see if you need any support from the security triage team."*

---

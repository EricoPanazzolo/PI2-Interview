# Incident Remediation Challenge: Legacy Enterprise Portal

## Section 0: Getting Started

To run the application locally, you must have Docker and Docker Compose
installed.

1.  Clone or navigate to this project directory.
2.  Build and spin up the container:

    ```bash
    docker compose up --build -d
    ```

3.  The servers will start and listen on the following ports:

    -   `http://localhost:8080`: Serves the Legacy Enterprise Portal, which is
        the core application under review.
    -   `http://localhost:8081`: Serves the Issue Tracker portal, where you can
        view the reported issue.
    -   `http://localhost:8082`: Serves the Docs Portal, which contains the
        proprietary framework SDK documentation.

4.  To stop the server, press `Ctrl+C` or run:

    ```bash
    docker compose down
    ```

--------------------------------------------------------------------------------

## Section 1: Incident Report

We have received an external security report indicating a vulnerability on the
[Legacy Enterprise Portal](http://localhost:8080/).

Please review the details in [Issue 1001](http://localhost:8081/) to understand
and analyze the finding.

--------------------------------------------------------------------------------

## Section 2: Proprietary Framework SDK Documentation

This project consists of the core Legacy Enterprise Portal application running
on our internal, proprietary HTTP framework. The Issue Tracker Portal and Docs
Portal are helper applications provided to assist you with the challenge; they
are not part of the core custom framework application system you are tasked to
remediate.

Check the [Enterprise Framework SDK Documentation](http://localhost:8082/) here.

--------------------------------------------------------------------------------

## Section 3: Candidate Tasks

Your objective is to analyze the reported vulnerability and design a project
plan to remediate it across the entire enterprise (affecting approximately 3,000
services managed by 250 development teams). For each team, you have the code
location and the TL (team leader) ldap.

### Tasks

1.  **Reproduce and Analyze:**

    -   Validate the existence of the vulnerability reported by the external
        researcher in [Issue 1001](http://localhost:8081/) against the local
        Legacy Enterprise Portal.
    -   Analyze the root cause and understand how it affects the application.

2.  **Develop a Remediation Project Plan:**

    -   Create a google document named `REMEDIATION_PLAN` and share it with
        **jpaguinsky@pi-squa.red**.
    -   Your plan must address how to scale the fix to 3,000 files/services
        across 250 teams.
    -   Adhere to the following structure for your report:
        *   **Introduction:** Brief overview of the security event.
        *   **Problem Statement:** Technical analysis of the vulnerability,
            potential risks, and business impact.
        *   **Mitigation Approach:** Proposed technical solution (e.g.,
            framework-level controls vs. individual code changes) and the
            rationale for selection.
        *   **Execution & Rollout Strategy:** Roadmap for deploying the fix
            across 250 teams, including coordination, verification, and testing.
        *   **Project Risks:** Potential technical or operational risks of the
            remediation (e.g., breaking changes, performance impact) and how to
            manage them.
        *   **Prevent the Issue in the Future:** Recommendations to prevent
            similar vulnerabilities in the future (e.g., tooling, process
            changes).
        *   **Conclusion:** Summary of the plan.

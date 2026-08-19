"""Team and Ownership Directory Data Registry.

Contains enterprise teams, LDAP identities, on-call schedules, owned code
paths, and component mappings for incident triage and bug ownership routing.
"""

TEAMS = [
    {
        "id": "customer-account-platform",
        "name": "Customer Account & Data Services Platform",
        "tag": "CUSTOMER-DATA",
        "department": "Core User & Account Infrastructure",
        "email": "customer-data-eng@company.com",
        "chat_channel": "#customer-data-oncall",
        "tl_ldap": "marcos_v",
        "tl_name": "Marcos Vieira",
        "primary_oncall_ldap": "lucas_m",
        "primary_oncall_name": "Lucas Mendonca",
        "secondary_oncall_ldap": "carla_s",
        "secondary_oncall_name": "Carla Santos",
        "members": [
            {
                "ldap": "marcos_v",
                "name": "Marcos Vieira",
                "role": "Tech Lead Manager",
                "focus": "Customer Architecture & API Strategy",
            },
            {
                "ldap": "lucas_m",
                "name": "Lucas Mendonca",
                "role": "Senior Software Engineer (On-call Primary)",
                "focus": "Customer Account APIs & Client Details Endpoint",
            },
            {
                "ldap": "carla_s",
                "name": "Carla Santos",
                "role": "Staff Software Engineer (On-call Secondary)",
                "focus": "Data Serialization & API Contracts",
            },
            {
                "ldap": "andre_f",
                "name": "Andre Ferreira",
                "role": "Software Engineer",
                "focus": "Account Database & Repository Services",
            },
            {
                "ldap": "patricia_r",
                "name": "Patricia Ramos",
                "role": "Software Engineer",
                "focus": "CRM Integrations & Client Sync",
            },
        ],
        "owned_paths": [
            "//depot/services/customer_api/...",
            "//depot/services/customer_api/controller.py",
            "//depot/services/customer_api/models/...",
            "//depot/services/client_accounts/...",
        ],
        "owned_endpoints": [
            "/api/v2/clients/details",
            "/api/v2/clients/summary",
            "/api/v2/clients/preferences",
            "/api/v2/clients/*",
            "/api/v2/accounts/*",
        ],
        "owned_components": [
            "Security > Privacy & Data Protection > Customer Data API",
            "Services > Customer Accounts > Client Profile Service",
            "Services > Customer Accounts > CRM Integrations",
        ],
        "description": (
            "Responsible for backend Customer Account API services, client"
            " profile data retrieval endpoints (/api/v2/clients/*), customer"
            " entity models, and CRM integration layers. Responsible for"
            " applying data sanitization before returning customer objects to"
            " clients."
        ),
        "triage_guidelines": (
            "Assign all bugs regarding customer account API endpoints"
            " (/api/v2/clients/*), unredacted client PII exposures, and CRM"
            " data pipeline bugs to this team's Primary On-Call (lucas_m). For"
            " P0/P1 security incidents, CC the Tech Lead (marcos_v)."
        ),
    },
    {
        "id": "privacy-governance-data",
        "name": "Data Privacy & Compliance Governance",
        "tag": "PRIVACY-GOV",
        "department": "Information Security & Privacy",
        "email": "privacy-compliance@company.com",
        "chat_channel": "#privacy-eng",
        "tl_ldap": "rachel_m",
        "tl_name": "Rachel Meyer",
        "primary_oncall_ldap": "omar_h",
        "primary_oncall_name": "Omar Hassan",
        "secondary_oncall_ldap": "chloe_d",
        "secondary_oncall_name": "Chloe Dupont",
        "members": [
            {
                "ldap": "rachel_m",
                "name": "Rachel Meyer",
                "role": "Privacy Engineering Lead",
                "focus": "Data Governance & Global Privacy Policies",
            },
            {
                "ldap": "omar_h",
                "name": "Omar Hassan",
                "role": "Compliance Specialist (Primary On-call)",
                "focus": "PII Masking Libraries & Redaction Rules",
            },
            {
                "ldap": "chloe_d",
                "name": "Chloe Dupont",
                "role": "Senior Privacy Engineer",
                "focus": "GDPR / CCPA Subject Access Requests",
            },
            {
                "ldap": "felix_z",
                "name": "Felix Zhang",
                "role": "Software Engineer",
                "focus": "Audit Logging Pipeline",
            },
        ],
        "owned_paths": [
            "//depot/privacy/...",
            "//depot/gdpr/...",
            "//depot/logging/sanitizer/...",
        ],
        "owned_endpoints": [
            "/api/v1/privacy/export",
            "/api/v1/privacy/delete",
            "PIIMaskingFilter Library",
        ],
        "owned_components": [
            "Security > Data Privacy Governance > PIIMaskingFilter",
            "Security > Data Privacy Governance > Audit Logging",
            "Security > Data Privacy Governance > GDPR Export & Erasure",
        ],
        "description": (
            "Develops enterprise privacy policy tooling, shared PII redaction"
            " filters (PIIMaskingFilter), user data export/deletion workflows"
            " (GDPR/CCPA), and regulatory audit logging pipelines."
        ),
        "triage_guidelines": (
            "Route defects in the shared PIIMaskingFilter library, GDPR"
            " deletion pipeline failures, or privacy policy engine bugs to"
            " Primary On-Call (omar_h). Note: Service-specific endpoint"
            " implementations belong to their respective domain teams."
        ),
    },
    {
        "id": "iam-auth-security",
        "name": "Identity & Access Management (IAM)",
        "tag": "SEC-IAM",
        "department": "Information Security & Privacy",
        "email": "iam-security-triage@company.com",
        "chat_channel": "#iam-auth-oncall",
        "tl_ldap": "sarah_k",
        "tl_name": "Sarah Kowalski",
        "primary_oncall_ldap": "david_p",
        "primary_oncall_name": "David Park",
        "secondary_oncall_ldap": "jenny_w",
        "secondary_oncall_name": "Jenny White",
        "members": [
            {
                "ldap": "sarah_k",
                "name": "Sarah Kowalski",
                "role": "Principal Security Lead",
                "focus": "Auth Architecture & Cryptography",
            },
            {
                "ldap": "david_p",
                "name": "David Park",
                "role": "Staff Security Engineer (IAM On-call)",
                "focus": "JWT Token Infrastructure & Token Verification",
            },
            {
                "ldap": "jenny_w",
                "name": "Jenny White",
                "role": "Senior Security Engineer",
                "focus": "Session Management & Cookie Security",
            },
            {
                "ldap": "elena_r",
                "name": "Elena Rossi",
                "role": "Security Software Engineer",
                "focus": "OAuth2 / SSO Federation",
            },
            {
                "ldap": "matthew_b",
                "name": "Matthew Brown",
                "role": "Security Engineer",
                "focus": "Role-Based Access Control (RBAC)",
            },
        ],
        "owned_paths": [
            "//depot/identity/...",
            "//depot/security/auth/...",
            "//depot/auth_service/...",
        ],
        "owned_endpoints": [
            "/api/v1/auth",
            "/api/v1/users",
            "/api/v1/settings",
            "/oauth/*",
            "/sso/*",
        ],
        "owned_components": [
            "Security > Identity & Access Management > JWT Auth",
            "Security > Identity & Access Management > OAuth2",
            "Security > Identity & Access Management > SSO",
            "Security > Identity & Access Management > Session Security",
            "Security > Identity & Access Management > Password Reset",
        ],
        "description": (
            "Owns central authentication APIs, password hashing policies"
            " (Argon2id/bcrypt), JWT token issuance/verification, SSO"
            " federation, session cookie attributes, and directory RBAC"
            " policies."
        ),
        "triage_guidelines": (
            "Route reports concerning JWT signature flaws, hardcoded signing"
            " keys, centralized session hijacking, missing HttpOnly/SameSite"
            " flags on central auth cookies, or OAuth redirect vulnerabilities"
            " to Primary On-Call (david_p)."
        ),
    },
    {
        "id": "gateway-traffic-mesh",
        "name": "API Gateway & Edge Infrastructure",
        "tag": "GATEWAY-MESH",
        "department": "Network & Edge Infrastructure",
        "email": "api-gateway-core@company.com",
        "chat_channel": "#api-gateway-oncall",
        "tl_ldap": "jorge_r",
        "tl_name": "Jorge Ramos",
        "primary_oncall_ldap": "sam_b",
        "primary_oncall_name": "Sam Becker",
        "secondary_oncall_ldap": "nina_g",
        "secondary_oncall_name": "Nina Gupta",
        "members": [
            {
                "ldap": "jorge_r",
                "name": "Jorge Ramos",
                "role": "Edge Platform Tech Lead",
                "focus": "Network Architecture & Routing Mesh",
            },
            {
                "ldap": "sam_b",
                "name": "Sam Becker",
                "role": "Staff SRE (Gateway On-call)",
                "focus": "Reverse Proxy & Load Balancing",
            },
            {
                "ldap": "nina_g",
                "name": "Nina Gupta",
                "role": "Network Systems Engineer",
                "focus": "TLS Termination & WAF Rules",
            },
            {
                "ldap": "vikram_s",
                "name": "Vikram Sethi",
                "role": "Security Engineer",
                "focus": "DDoS Mitigation & Rate Limiting",
            },
        ],
        "owned_paths": [
            "//depot/gateway/...",
            "//depot/edge/envoy/...",
            "//depot/waf/rules/...",
        ],
        "owned_endpoints": [
            "Edge Reverse Proxy (Envoy)",
            "WAF Ingress Gateway",
            "Rate Limiting Mesh",
        ],
        "owned_components": [
            "Infrastructure > API Gateway & Edge > Envoy WAF",
            "Infrastructure > API Gateway & Edge > Edge Headers & CSP",
            "Infrastructure > API Gateway & Edge > Rate Limiting Mesh",
        ],
        "description": (
            "Manages edge ingress proxies, TLS certificates, WAF filtering"
            " rules, rate limiting, DDoS protections, and microservice traffic"
            " routing."
        ),
        "triage_guidelines": (
            "Assign edge routing defects, WAF bypasses, TLS misconfigurations,"
            " or rate limiting failures to Primary On-Call (sam_b)."
        ),
    },
    {
        "id": "payments-billing-platform",
        "name": "Payments & Billing Platform",
        "tag": "FIN-PAYMENTS",
        "department": "Financial Engineering & Commerce",
        "email": "payments-core@company.com",
        "chat_channel": "#payments-eng-oncall",
        "tl_ldap": "carlos_t",
        "tl_name": "Carlos Torres",
        "primary_oncall_ldap": "maya_l",
        "primary_oncall_name": "Maya Lin",
        "secondary_oncall_ldap": "hassan_a",
        "secondary_oncall_name": "Hassan Ali",
        "members": [
            {
                "ldap": "carlos_t",
                "name": "Carlos Torres",
                "role": "Engineering Lead",
                "focus": "Financial Architecture & Payment Gateways",
            },
            {
                "ldap": "maya_l",
                "name": "Maya Lin",
                "role": "Senior Billing Engineer (Primary On-call)",
                "focus": "Transaction Processing & Invoicing APIs",
            },
            {
                "ldap": "hassan_a",
                "name": "Hassan Ali",
                "role": "Payments SRE",
                "focus": "High-Availability Payment Pipelines",
            },
            {
                "ldap": "bruna_c",
                "name": "Bruna Costa",
                "role": "Security & Compliance Lead",
                "focus": "PCI-DSS Compliance & Cardholder Data Protection",
            },
        ],
        "owned_paths": [
            "//depot/services/payments/...",
            "//depot/services/payments/webhook_handler.py",
            "//depot/billing/...",
            "//depot/payments/...",
            "//depot/checkout/...",
        ],
        "owned_endpoints": [
            "/api/v1/payments/*",
            "/api/v1/payments/webhook",
            "/api/v1/billing/*",
            "/checkout/*",
        ],
        "owned_components": [
            "Security > Financial & Payments Security > Webhook Ingress",
            "Security > Financial & Payments Security > Cardholder Data Vault",
            "Security > Financial & Payments Security > Checkout API",
            "Services > Billing > Invoicing & Currency Service",
        ],
        "description": (
            "Manages monetary transactions, subscription billing,"
            " credit-card processing integration, invoice issuance, and PCI-DSS"
            " certified cardholder environments."
        ),
        "triage_guidelines": (
            "Route payment failures, double-billing defects, checkout session"
            " tampering, or webhook authentication bugs to Primary On-Call (maya_l)."
        ),
    },
    {
        "id": "cloud-infra-sre",
        "name": "Cloud Infrastructure & Container Security (SRE)",
        "tag": "INFRA-SRE",
        "department": "Site Reliability Engineering",
        "email": "cloud-infra-sre@company.com",
        "chat_channel": "#cloud-infra-ops",
        "tl_ldap": "dmitri_v",
        "tl_name": "Dmitri Volkov",
        "primary_oncall_ldap": "kevin_j",
        "primary_oncall_name": "Kevin Jones",
        "secondary_oncall_ldap": "laura_b",
        "secondary_oncall_name": "Laura Bianchi",
        "members": [
            {
                "ldap": "dmitri_v",
                "name": "Dmitri Volkov",
                "role": "Infrastructure SRE TL",
                "focus": "Borg/Kube Clusters & Deployment Orchestration",
            },
            {
                "ldap": "kevin_j",
                "name": "Kevin Jones",
                "role": "Principal Incident Commander (Primary On-call)",
                "focus": "Production Outages & Infrastructure Incidents",
            },
            {
                "ldap": "laura_b",
                "name": "Laura Bianchi",
                "role": "Container Security SRE",
                "focus": "Docker Hardening, Non-Root Users & Seccomp",
            },
            {
                "ldap": "tarik_k",
                "name": "Tarik Kaplan",
                "role": "Systems Engineer",
                "focus": "OS Patching & Host Hardening",
            },
        ],
        "owned_paths": [
            "//depot/infra/...",
            "//depot/docker/...",
            "Dockerfile",
            "docker-compose.yml",
        ],
        "owned_endpoints": [
            "Container Orchestration (Docker / Borg)",
            "Host OS Hardening",
            "Health & Telemetry Daemon",
        ],
        "owned_components": [
            "Infrastructure > Cloud SRE & Containers > Docker Host",
            "Infrastructure > Cloud SRE & Containers > Base Image",
            "Infrastructure > Cloud SRE & Containers > Production Clusters",
            "Infrastructure > Cloud SRE & Containers > Secrets Manager",
        ],
        "description": (
            "Oversees container build definitions (Dockerfile, Docker"
            " Compose), rootless execution models, read-only root filesystems,"
            " Linux capability dropping, and compute node stability."
        ),
        "triage_guidelines": (
            "Assign container escapes, base image CVEs, docker-compose"
            " misconfigurations, or production hardware outages to Primary"
            " On-Call (kevin_j)."
        ),
    },
]


def get_all_teams():
  return TEAMS


def get_team_by_id(team_id: str):
  for team in TEAMS:
    if team["id"] == team_id or team["tag"].lower() == team_id.lower():
      return team
  return None


def search_teams(query: str):
  if not query:
    return TEAMS
  q = query.lower().strip()
  results = []
  for team in TEAMS:
    match = False
    if (
        q in team["name"].lower()
        or q in team["tag"].lower()
        or q in team["department"].lower()
        or q in team["description"].lower()
        or q in team["email"].lower()
        or q in team["tl_ldap"].lower()
        or q in team["primary_oncall_ldap"].lower()
    ):
      match = True
    else:
      for m in team["members"]:
        if q in m["ldap"].lower() or q in m["name"].lower():
          match = True
          break
      if not match:
        for p in team["owned_paths"]:
          if q in p.lower():
            match = True
            break
      if not match:
        for ep in team["owned_endpoints"]:
          if q in ep.lower():
            match = True
            break
      if not match:
        for comp in team.get("owned_components", []):
          if q in comp.lower():
            match = True
            break
    if match:
      results.append(team)
  return results


def resolve_ownership(path_or_endpoint: str):
  """Find the best-matching team for a given code path or URL endpoint."""
  if not path_or_endpoint:
    return None
  target = path_or_endpoint.strip().lower()

  best_match = None
  best_score = 0

  for team in TEAMS:
    score = 0
    for p in team["owned_paths"]:
      p_clean = p.replace("//depot/", "").replace("/...", "").lower()
      if target in p.lower() or p_clean in target or target in p_clean:
        score = max(score, 100)
    for ep in team["owned_endpoints"]:
      ep_clean = ep.replace("/*", "").lower()
      if target == ep_clean or (ep_clean and ep_clean in target):
        score = max(score, 90)
    if score > best_score:
      best_score = score
      best_match = team

  return best_match

from datetime import datetime
from datetime import timedelta
import html
import json
import os
import re

APP_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(APP_DIR, "templates")


def build_issues(base_time: datetime = None) -> dict:
  """Constructs the comprehensive Bug State Registry with dynamic dates relative to challenge launch time."""
  now = base_time or datetime.utcnow()

  # Relative timeline reference points
  d_minus_13 = now - timedelta(days=13)
  d_minus_12 = now - timedelta(days=12)
  d_minus_10 = now - timedelta(days=10)
  d_minus_9 = now - timedelta(days=9)
  d_minus_8 = now - timedelta(days=8)
  d_minus_7 = now - timedelta(days=7)
  d_minus_6 = now - timedelta(days=6)
  d_minus_5 = now - timedelta(days=5)
  d_minus_4 = now - timedelta(days=4)
  d_minus_3 = now - timedelta(days=3)
  d_minus_2 = now - timedelta(days=2)
  d_minus_1 = now - timedelta(days=1)
  h_minus_6 = now - timedelta(hours=6)
  h_minus_5 = now - timedelta(hours=5)
  h_minus_4 = now - timedelta(hours=4)
  h_minus_3 = now - timedelta(hours=3)
  h_minus_2 = now - timedelta(hours=2)
  h_minus_1 = now - timedelta(hours=1)

  d_plus_1 = now + timedelta(days=1)
  d_plus_2 = now + timedelta(days=2)
  d_plus_3 = now + timedelta(days=3)
  d_plus_4 = now + timedelta(days=4)
  d_plus_5 = now + timedelta(days=5)
  d_plus_6 = now + timedelta(days=6)
  d_plus_7 = now + timedelta(days=7)
  d_plus_10 = now + timedelta(days=10)

  return {
      "543338174": {
          "id": "543338174",
          "bug_number": "b/543338174",
          "title": (
              "[Internal Security Finding] Insecure Webhook Signature"
              " Verification in Payments Webhook Handler (/api/v1/payments/webhook)"
          ),
          "status": "Assigned",
          "priority": "P1",
          "severity": "S1",
          "type": "Vulnerability (Financial / Webhook Forgery)",
          "due_date": (
              f"{d_plus_2.strftime('%B %d, %Y')} (Approaching SLO Deadline - 2 days remaining)"
          ),
          "due_date_class": "",
          "component": (
              "Security > Financial & Payments Security > Webhook Ingress"
          ),
          "reporter": "johndoe@company.com (John Doe - Internal Privacy Assurance)",
          "assignee_ldap": "maya_l",
          "modified_date": d_minus_3.strftime("%B %d, %Y 14:20 UTC"),
          "created_date": d_minus_4.strftime("%B %d, %Y 14:00 UTC"),
          "hotlists": [
              "5829104",
              "7920155",
              "P1-Security-Incident",
              "PCI-DSS-Review",
              "Payment-Gateway",
          ],
          "description": {
              "summary": (
                  "During an internal security review of the Payments Platform,"
                  " Privacy & Security Assurance discovered that the payment"
                  " callback handler at <code>/api/v1/payments/webhook</code>"
                  " accepts incoming transaction status notifications without"
                  " validating the cryptographic HMAC-SHA256 signature passed in"
                  " the <code>X-Signature</code> HTTP header."
              ),
              "affected_endpoint": "/api/v1/payments/webhook",
              "affected_path": (
                  "//depot/services/payments/webhook_handler.py"
              ),
              "leaked_fields": [
                  (
                      "<code>X-Signature</code> header is parsed but never"
                      " cryptographically verified against the shared secret key."
                  ),
                  (
                      "<code>transaction_id</code> and <code>status</code>"
                      " accepted from arbitrary unauthenticated POST callers."
                  ),
                  (
                      "<code>payment_amount</code> and"
                      " <code>settlement_status</code> can be forged to complete"
                      " orders without actual payment."
                  ),
              ],
              "repro_curl": (
                  "curl -X POST"
                  ' "https://payments.enterprise.internal/api/v1/payments/webhook"'
                  ' \\\n  -H "Content-Type: application/json" \\\n  -d'
                  ' \'{"transaction_id": "tx_99214a", "order_id": "ord_8812",'
                  ' "status": "COMPLETED", "amount_paid": 450.00}\''
              ),
              "sample_response": """{
  "status": "ACK",
  "transaction_id": "tx_99214a",
  "message": "Payment confirmed and order ord_8812 marked as settled."
}""",
              "impact": (
                  "Critical financial security risk. An attacker or malicious"
                  " party can forge arbitrary payment confirmation webhooks to"
                  " settle unpaid invoices or unlock premium services without"
                  " completing actual payment gateway transactions."
              ),
              "proposed_slo": (
                  "P1/S1 Financial & Payment Infrastructure Vulnerability:"
                  f" Resolution required within 48 hours of initial triage (Target"
                  f" Due Date: {d_plus_2.strftime('%B %d, %Y')} 18:00 UTC) in accordance with Payment"
                  " Gateway Security Standards."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "johndoe@company.com",
                  "date": d_minus_4.strftime("%B %d, %Y 14:00 UTC"),
                  "is_internal": True,
                  "text": (
                      "Hi Security Triage,\n\nWe discovered that the Payments"
                      " Webhook handler at <code>/api/v1/payments/webhook</code>"
                      " does not verify HMAC-SHA256 signatures before updating"
                      " transaction statuses in the database. Anyone on the"
                      " network can POST fake payment success events.\n\nPlease"
                      " see the report description above for reproduction curl"
                      " and details."
                  ),
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "security-triage@company.com",
                  "date": d_minus_4.strftime("%B %d, %Y 14:30 UTC"),
                  "is_internal": True,
                  "text": (
                      "Assigning ticket to <strong>@david_p</strong> (IAM & Auth"
                      " Security) to investigate authentication controls on"
                      " <code>/api/v1/payments/webhook</code>."
                  ),
              },
              {
                  "id": 3,
                  "number": "#3",
                  "author": "security-triage@company.com",
                  "date": d_minus_3.strftime("%B %d, %Y 10:15 UTC"),
                  "is_internal": True,
                  "text": (
                      "Hi <strong>@david_p</strong>, checking in to see if you"
                      " are the correct person to oversee this issue and if you"
                      " have context on what is going on with"
                      " <code>/api/v1/payments/webhook</code>?"
                  ),
              },
              {
                  "id": 4,
                  "number": "#4",
                  "author": "david_p@company.com",
                  "date": d_minus_3.strftime("%B %d, %Y 11:30 UTC"),
                  "is_internal": True,
                  "text": (
                      "Hi Security Triage,\n\nI do not own nor work on the"
                      " Payments & Billing services or the"
                      " <code>/api/v1/payments/webhook</code> endpoint. My team"
                      " (IAM & Access Management) only maintains central"
                      " authentication tokens and SSO infrastructure"
                      " (<code>//depot/identity/...</code>).\n\nPer the Team"
                      " Directory, <code>/api/v1/payments/webhook</code> belongs"
                      " to Payments & Billing Platform. Reassigning ticket"
                      " to <strong>@maya_l</strong> (Primary"
                      " On-Call).\n\nThanks,\nDavid Park (IAM Security)"
                  ),
              },
              {
                  "id": 5,
                  "number": "#5",
                  "author": "maya_l@company.com",
                  "date": d_minus_3.strftime("%B %d, %Y 14:20 UTC"),
                  "is_internal": True,
                  "text": (
                      "Thanks David. Confirming I am the correct owner for"
                      " Payments & Billing Platform and"
                      " <code>/api/v1/payments/webhook</code>. Acknowledging the"
                      " P1 finding. I will investigate the HMAC signature"
                      " verification logic and prepare a hotfix PR"
                      " today/tomorrow."
                  ),
              },
          ],
      },
      "618294710": {
          "id": "618294710",
          "bug_number": "b/618294710",
          "title": (
              "[Internal Security Finding] Customer Account API"
              " (/api/v2/clients/details) leaking sensitive client PII (SSN, home"
              " address, phone) in unauthenticated responses"
          ),
          "status": "Triaged",
          "priority": "P1",
          "severity": "S1",
          "type": "Vulnerability (Internal Privacy / PII Leakage)",
          "due_date": f"{d_plus_2.strftime('%B %d, %Y')} (Target: 48h SLA)",
          "due_date_class": "",
          "component": "Security > Privacy & Data Protection > Customer Data API",
          "reporter": "johndoe@company.com (John Doe - Internal Privacy Assurance)",
          "assignee_ldap": "",
          "modified_date": d_minus_1.strftime("%B %d, %Y 18:30 UTC"),
          "created_date": d_minus_1.strftime("%B %d, %Y 18:00 UTC"),
          "hotlists": [
              "5829104",
              "7920155",
              "P1-Security-Incident",
              "GDPR-Review",
              "Internal-Audit-2026",
          ],
          "description": {
              "summary": (
                  "During an internal security and privacy assessment of the"
                  " Customer Account Platform, Privacy Assurance identified that"
                  " the Customer Account Data API endpoint"
                  " <code>/api/v2/clients/{client_id}/details</code> returns"
                  " unredacted Personally Identifiable Information (PII)"
                  " including full Social Security Numbers (SSN), cleartext"
                  " residential addresses, mobile numbers, and dates of birth"
                  " without verifying field-level access permissions or applying"
                  " data masking filters."
              ),
              "affected_endpoint": "/api/v2/clients/details",
              "affected_path": (
                  "//depot/services/customer_api/controller.py"
              ),
              "leaked_fields": [
                  (
                      "<code>ssn</code> (Full 9-digit Social Security Number in"
                      " plaintext)"
                  ),
                  (
                      "<code>residential_address</code> (Street address, City,"
                      " Postal code)"
                  ),
                  "<code>phone_number</code> (Primary mobile phone)",
                  "<code>date_of_birth</code> (Client birthdate: YYYY-MM-DD)",
                  "<code>billing_email</code> (Personal contact email)",
              ],
              "repro_curl": (
                  "curl -X GET"
                  ' "https://api.enterprise.internal/api/v2/clients/489201a/details"'
                  ' \\\n  -H "Accept: application/json"'
              ),
              "sample_response": """{
  "status": "success",
  "client_id": "client_489201a",
  "full_name": "John Doe",
  "ssn": "987-65-4321",
  "date_of_birth": "1985-04-12",
  "phone_number": "+1-555-019-2834",
  "residential_address": "742 Evergreen Terrace, Springfield, OR 97477",
  "billing_email": "johndoe@example.com",
  "account_tier": "enterprise_gold"
}""",
              "impact": (
                  "Mass exposure of sensitive customer PII without masking."
                  " Direct violation of internal data protection policy, GDPR"
                  " Article 32, and CCPA, presenting high regulatory compliance"
                  " and data breach risks."
              ),
              "proposed_slo": (
                  "Critical P1/S1 PII Exposure: Resolution required within 48"
                  f" hours of initial triage (Target Due Date: {d_plus_2.strftime('%B %d, %Y')} 18:00"
                  " UTC) in accordance with Enterprise Data Protection Policy."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "johndoe@company.com",
                  "date": d_minus_1.strftime("%B %d, %Y 18:00 UTC"),
                  "is_internal": True,
                  "text": (
                      "Hi Security Triage,\n\nDuring our Q3 internal privacy"
                      " audit of user-facing microservices, we noticed a critical"
                      " PII data leakage in the Customer Account API"
                      " (<code>/api/v2/clients/details</code>). The endpoint"
                      " returns raw database objects with unmasked SSNs,"
                      " residential addresses, and phone numbers.\n\nPlease see"
                      " the report description above for reproduction curl and"
                      " sample JSON payload."
                  ),
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "security-triage@company.com",
                  "date": d_minus_1.strftime("%B %d, %Y 18:30 UTC"),
                  "is_internal": True,
                  "text": (
                      "Acknowledging report and confirming P1/S1 classification."
                      " Currently looking up the owning team in the Service"
                      " Ownership Directory to route to the Customer Account"
                      " Primary On-Call."
                  ),
              },
          ],
      },
      "782910401": {
          "id": "782910401",
          "bug_number": "b/782910401",
          "title": (
              "[Security P0 Outage] Edge Envoy Gateway WAF Rule Bypass on /oauth"
              " Ingress Route"
          ),
          "status": "Assigned",
          "priority": "P0",
          "severity": "S0",
          "type": "Vulnerability (Edge / WAF Bypass)",
          "due_date": f"{now.strftime('%B %d, %Y')} 23:59 UTC (Emergency SLA: 6h)",
          "due_date_class": "",
          "component": "Infrastructure > API Gateway & Edge > Envoy WAF",
          "reporter": "sec-ops@company.com",
          "assignee_ldap": "sam_b",
          "modified_date": h_minus_4.strftime("%B %d, %Y %H:10 UTC"),
          "created_date": h_minus_6.strftime("%B %d, %Y %H:00 UTC"),
          "hotlists": ["7920155", "P0-Critical-Security", "Edge-Ingress"],
          "description": {
              "summary": (
                  "WAF bypass vulnerability identified in Envoy edge proxy"
                  " filters where percent-encoded null bytes in URL path bypass"
                  " rate-limiting and IP restriction filters."
              ),
              "affected_endpoint": "/oauth/*",
              "affected_path": "//depot/edge/envoy/filters/waf.cc",
              "leaked_fields": ["WAF Bypass Rule 4091"],
              "repro_curl": 'curl -X POST "https://gateway.internal/oauth%00/token"',
              "sample_response": '{"status": "bypassed_200"}',
              "impact": "Unrestricted authentication brute-force across public endpoints.",
              "proposed_slo": "P0/S0 Emergency patch within 6 hours.",
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "sec-ops@company.com",
                  "date": h_minus_6.strftime("%B %d, %Y %H:00 UTC"),
                  "is_internal": True,
                  "text": "P0 declared. Null-byte encoding in Envoy proxy bypasses WAF inspection.",
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "sam_b@company.com",
                  "date": h_minus_4.strftime("%B %d, %Y %H:10 UTC"),
                  "is_internal": True,
                  "text": "Working on immediate Envoy hotfix filter to reject malformed path encodings.",
              },
          ],
      },
      "491028472": {
          "id": "491028472",
          "bug_number": "b/491028472",
          "title": (
              "[Security P1] JWT Token Signature Verification Bypass via 'none'"
              " Algorithm in Auth Service"
          ),
          "status": "Assigned",
          "priority": "P1",
          "severity": "S1",
          "type": "Vulnerability (Authentication / JWT)",
          "due_date": f"{d_plus_3.strftime('%B %d, %Y')} (Target: 48h SLA)",
          "due_date_class": "",
          "component": "Security > Identity & Access Management > JWT Auth",
          "reporter": "appsec-audit@company.com",
          "assignee_ldap": "david_p",
          "modified_date": d_minus_1.strftime("%B %d, %Y 11:20 UTC"),
          "created_date": d_minus_2.strftime("%B %d, %Y 15:45 UTC"),
          "hotlists": ["7920155", "Auth-Security", "JWT-Hardening"],
          "description": {
              "summary": (
                  "JWT verification parser accepts tokens with 'alg': 'none',"
                  " allowing arbitrary user impersonation if signature is omitted."
              ),
              "affected_endpoint": "/api/v1/auth/verify",
              "affected_path": "//depot/auth_service/jwt_validator.py",
              "leaked_fields": ["Authorization header token header parsing"],
              "repro_curl": 'curl -H "Authorization: Bearer eyJhbGciOiJub25lIn0..."',
              "sample_response": '{"valid": true, "user": "admin"}',
              "impact": "Account takeover and administrative authorization bypass.",
              "proposed_slo": "P1/S1 48h remediation.",
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "appsec-audit@company.com",
                  "date": d_minus_2.strftime("%B %d, %Y 15:45 UTC"),
                  "is_internal": True,
                  "text": "Critical JWT library allows 'none' algorithm by default.",
              }
          ],
      },
      "392019482": {
          "id": "392019482",
          "bug_number": "b/392019482",
          "title": (
              "[Security P2] Missing Rate Limiting on Password Reset SMS"
              " Dispatch Endpoint"
          ),
          "status": "Triaged",
          "priority": "P2",
          "severity": "S2",
          "type": "Vulnerability (Abuse / Rate Limiting)",
          "due_date": f"{d_plus_7.strftime('%B %d, %Y')} (Target: 7d SLA)",
          "due_date_class": "",
          "component": "Security > Identity & Access Management > Password Reset",
          "reporter": "fraud-prevention@company.com",
          "assignee_ldap": "",
          "modified_date": h_minus_5.strftime("%B %d, %Y %H:15 UTC"),
          "created_date": d_minus_1.strftime("%B %d, %Y 16:30 UTC"),
          "hotlists": ["7920155", "SMS-Abuse-Prevention"],
          "description": {
              "summary": (
                  "Endpoint /api/v1/auth/reset-sms allows unlimited requests"
                  " per IP, enabling SMS toll fraud and client harassment."
              ),
              "affected_endpoint": "/api/v1/auth/reset-sms",
              "affected_path": "//depot/identity/sms_service.py",
              "leaked_fields": ["SMS Dispatch Gateway"],
              "repro_curl": 'for i in {1..50}; do curl -X POST "https://auth.internal/api/v1/auth/reset-sms"; done',
              "sample_response": '{"status": "sent"}',
              "impact": "Financial loss from telephony toll charges and user annoyance.",
              "proposed_slo": "P2/S2 7 day resolution.",
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "fraud-prevention@company.com",
                  "date": d_minus_1.strftime("%B %d, %Y 16:30 UTC"),
                  "is_internal": True,
                  "text": "Excessive SMS dispatches observed from cloud IP ranges.",
              }
          ],
      },
      "683920194": {
          "id": "683920194",
          "bug_number": "b/683920194",
          "title": (
              "[Security P1] Docker Socket Exposure in CI Worker Container Host"
          ),
          "status": "Blocked",
          "priority": "P1",
          "severity": "S1",
          "type": "Vulnerability (Container / Privilege Escalation)",
          "due_date": f"{d_plus_4.strftime('%B %d, %Y')} (Target: 48h SLA)",
          "due_date_class": "",
          "component": "Infrastructure > Cloud SRE & Containers > Docker Host",
          "reporter": "infra-audit@company.com (Infrastructure Security Audit)",
          "assignee_ldap": "kevin_j",
          "modified_date": h_minus_2.strftime("%B %d, %Y %H:40 UTC"),
          "created_date": d_minus_3.strftime("%B %d, %Y 10:00 UTC"),
          "hotlists": ["7920155", "Container-Security", "Infra-Hardening"],
          "description": {
              "summary": (
                  "During an infrastructure container security review, Security"
                  " Audit discovered that shared ephemeral CI/CD worker pods running on"
                  " the Kubernetes build cluster mount the host's Docker socket at"
                  " <code>/var/run/docker.sock</code> in order to allow test suites"
                  " to build and push container images. Any developer pipeline script"
                  " or malicious dependency executing inside a CI job can communicate"
                  " with the host Docker daemon with root privileges, escape the container"
                  " boundary, and compromise the underlying Kubernetes worker node."
              ),
              "affected_endpoint": "CI Worker Daemon (Build Runner Pool)",
              "affected_path": "//depot/docker/ci_worker.yaml",
              "leaked_fields": [
                  (
                      "<code>/var/run/docker.sock</code> bind-mounted with"
                      " read-write permissions"
                  ),
                  (
                      "Host filesystem root accessible via Docker API volume"
                      " mounts"
                  ),
                  (
                      "Node-level service account tokens and secrets accessible"
                      " across shared worker VMs"
                  ),
              ],
              "repro_curl": (
                  "# Inside any unprivileged CI job container:\n"
                  "docker -H unix:///var/run/docker.sock run -v /:/host_root alpine cat /host_root/etc/shadow"
              ),
              "sample_response": "root:$6$rounds=656000$saltsalt...:19800:0:99999:7:::",
              "impact": (
                  "Critical infrastructure container escape. Enables arbitrary host root execution,"
                  " cross-tenant build job tampering, lateral movement across the Kubernetes cluster,"
                  " and extraction of node credentials."
              ),
              "proposed_slo": (
                  "P1/S1 Infrastructure Security Vulnerability: Resolution required"
                  f" within 48 hours of initial triage (Target Due Date: {d_plus_4.strftime('%B %d, %Y')} 18:00 UTC)."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "infra-audit@company.com",
                  "date": d_minus_3.strftime("%B %d, %Y 10:00 UTC"),
                  "is_internal": True,
                  "text": (
                      "Filing P1 finding for Docker socket mount in CI runner pods.\n\n"
                      "We observed <code>volumeMounts: - mountPath: /var/run/docker.sock name: docker-socket</code>"
                      " in <code>//depot/docker/ci_worker.yaml</code> across all runner pools. Any pull request running"
                      " automated unit tests has full root control over the host node via standard docker CLI commands."
                  ),
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "kevin_j@company.com",
                  "date": d_minus_3.strftime("%B %d, %Y 14:15 UTC"),
                  "is_internal": True,
                  "text": (
                      "Acknowledging finding. We originally mounted the socket because several teams build microservice"
                      " images during their integration test pipelines. We will evaluate migrating off Docker-outside-of-Docker (DooD)."
                  ),
              },
              {
                  "id": 3,
                  "number": "#3",
                  "author": "sarah_k@company.com",
                  "date": d_minus_2.strftime("%B %d, %Y 09:30 UTC"),
                  "is_internal": True,
                  "text": (
                      "Can we just switch to Docker-in-Docker (dind) sidecars instead of re-architecting everything?\n\n"
                      "Over 40 services currently rely on <code>docker build</code> in CI. If we disable the socket without a drop-in"
                      " replacement, build pipelines for payments and customer API will break."
                  ),
              },
              {
                  "id": 4,
                  "number": "#4",
                  "author": "alex_m@company.com",
                  "date": d_minus_2.strftime("%B %d, %Y 11:20 UTC"),
                  "is_internal": True,
                  "text": (
                      "DinD is not an acceptable solution—it requires <code>securityContext.privileged: true</code> which violates"
                      " our cluster PodSecurityStandards (Restricted profile) and provides essentially identical host-level escape vectors.\n\n"
                      "The approved enterprise standard is rootless in-container builders (Google Kaniko or Buildah). Kaniko executes purely in"
                      " user space without requiring root privileges or socket mounts."
                  ),
              },
              {
                  "id": 5,
                  "number": "#5",
                  "author": "sarah_k@company.com",
                  "date": d_minus_2.strftime("%B %d, %Y 15:10 UTC"),
                  "is_internal": True,
                  "text": (
                      "Also noticing unrelated test failures in node-18 frontend builds on runner pool 3—getting timeout errors during"
                      " npm install. Is that connected to the socket permissions change?"
                  ),
              },
              {
                  "id": 6,
                  "number": "#6",
                  "author": "kevin_j@company.com",
                  "date": d_minus_1.strftime("%B %d, %Y 10:45 UTC"),
                  "is_internal": True,
                  "text": (
                      "Hi Sarah, the npm timeout on runner pool 3 is an unrelated memory limit issue (tracked in b/992148102). Nothing has been disabled yet on the socket.\n\n"
                      "Regarding the remediation: I tested Kaniko on a staging runner pool and successfully built container images without any socket mount. PR #4920 is prepared."
                  ),
              },
              {
                  "id": 7,
                  "number": "#7",
                  "author": "infra-audit@company.com",
                  "date": h_minus_4.strftime("%B %d, %Y %H:15 UTC"),
                  "is_internal": True,
                  "text": (
                      "Checking in on timeline. P1 SLA target is in 4 days. Can we deploy PR #4920 to production runners today?"
                  ),
              },
              {
                  "id": 8,
                  "number": "#8",
                  "author": "kevin_j@company.com",
                  "date": h_minus_2.strftime("%B %d, %Y %H:40 UTC"),
                  "is_internal": True,
                  "text": (
                      "Setting bug status to **Blocked**.\n\n"
                      "The Kaniko image builder template is completed, but production rollout is currently blocked on external infrastructure provisioning:\n\n"
                      "1. **Cloud Storage & IAM Dependency:** Kaniko requires a dedicated Cloud Storage build-cache bucket (<code>gs://ci-kaniko-cache-prod</code>) and a Workload Identity IAM service account (<code>kaniko-builder@prod-ci.iam.gserviceaccount.com</code>) to publish container layers without storing static registry credentials.\n"
                      "2. **Pending Ticket:** We submitted ticket <code>b/782194012</code> to <strong>storage-infra@company.com</strong> and <strong>cloud-iam-oncall</strong> to provision the bucket and Workload Identity bindings, but the request is pending storage quota and IAM security review.\n\n"
                      "Until the IAM service account and storage bucket are provisioned by the Cloud Storage team, deploying Kaniko would break image caching and registry publishing across all CI pipelines. Following up directly with @storage-oncall to unblock."
                  ),
              },
          ],
      },
      "294810293": {
          "id": "294810293",
          "bug_number": "b/294810293",
          "title": (
              "[Privacy P2] GDPR Data Subject Erasure Job Skipping Orphaned"
              " Customer Preferences Records"
          ),
          "status": "Fixed",
          "priority": "P2",
          "severity": "S2",
          "type": "Bug (Privacy / Compliance)",
          "due_date": f"{d_minus_4.strftime('%B %d, %Y')} (Completed)",
          "due_date_class": "",
          "component": "Security > Data Privacy Governance > GDPR Export & Erasure",
          "reporter": "privacy-audit@company.com",
          "assignee_ldap": "omar_h",
          "modified_date": d_minus_4.strftime("%B %d, %Y 16:20 UTC"),
          "created_date": d_minus_9.strftime("%B %d, %Y 09:00 UTC"),
          "hotlists": ["7920155", "GDPR-Compliance"],
          "description": {
              "summary": (
                  "Right-to-be-forgotten pipeline purged main client tables"
                  " but left user records in client_preferences_v2."
              ),
              "affected_endpoint": "/api/v1/privacy/delete",
              "affected_path": "//depot/gdpr/deletion_runner.py",
              "leaked_fields": ["Orphaned email preferences"],
              "repro_curl": 'curl -X POST "https://privacy.internal/api/v1/privacy/delete?user_id=123"',
              "sample_response": '{"status": "purged"}',
              "impact": "Regulatory fine risk under GDPR Article 17.",
              "proposed_slo": "Resolved.",
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "omar_h@company.com",
                  "date": d_minus_4.strftime("%B %d, %Y 16:20 UTC"),
                  "is_internal": True,
                  "text": "Fix verified in PR #4810. Preferences table cascaded.",
              }
          ],
      },
      "839102948": {
          "id": "839102948",
          "bug_number": "b/839102948",
          "title": (
              "[Security P3] Overly Permissive CORS Header (*)"
              " on /api/v2/clients/summary Endpoint"
          ),
          "status": "Verified",
          "priority": "P3",
          "severity": "S3",
          "type": "Bug (Web Security / CORS)",
          "due_date": f"{d_minus_6.strftime('%B %d, %Y')} (Completed)",
          "due_date_class": "",
          "component": "Security > Privacy & Data Protection > Customer Data API",
          "reporter": "bounty-hunter@external.internal",
          "assignee_ldap": "carla_s",
          "modified_date": d_minus_6.strftime("%B %d, %Y 17:00 UTC"),
          "created_date": d_minus_12.strftime("%B %d, %Y 11:30 UTC"),
          "hotlists": ["7920155", "CORS-Hygiene"],
          "description": {
              "summary": (
                  "Access-Control-Allow-Origin: * returned on client summary"
                  " route when unauthenticated."
              ),
              "affected_endpoint": "/api/v2/clients/summary",
              "affected_path": "//depot/services/customer_api/controller.py",
              "leaked_fields": ["CORS headers"],
              "repro_curl": 'curl -I -H "Origin: https://attacker.com" https://api.enterprise.internal/api/v2/clients/summary',
              "sample_response": "Access-Control-Allow-Origin: *",
              "impact": "Minor metadata reflection.",
              "proposed_slo": "Resolved.",
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "carla_s@company.com",
                  "date": d_minus_6.strftime("%B %d, %Y 17:00 UTC"),
                  "is_internal": True,
                  "text": "Restricted origin allowlist to *.enterprise.internal.",
              }
          ],
      },
      "194820194": {
          "id": "194820194",
          "bug_number": "b/194820194",
          "title": (
              "[Security P2] Negative Balance Ingestion Flaw in Currency"
              " Conversion Service"
          ),
          "status": "Assigned",
          "priority": "P2",
          "severity": "S2",
          "type": "Vulnerability (Financial / Math Logic)",
          "due_date": f"{d_plus_6.strftime('%B %d, %Y')} (Target: 7d SLA)",
          "due_date_class": "",
          "component": "Services > Billing > Invoicing & Currency Service",
          "reporter": "billing-ops@company.com",
          "assignee_ldap": "lucas_m",
          "modified_date": h_minus_6.strftime("%B %d, %Y %H:00 UTC"),
          "created_date": d_minus_1.strftime("%B %d, %Y 14:00 UTC"),
          "hotlists": ["7920155", "Payments-Integrity"],
          "description": {
              "summary": (
                  "Negative balance numbers in /api/v1/payments/convert cause"
                  " credit additions instead of deductions."
              ),
              "affected_endpoint": "/api/v1/payments/convert",
              "affected_path": "//depot/services/payments/fx_calculator.py",
              "leaked_fields": ["Amount parsing logic"],
              "repro_curl": 'curl -X POST "https://payments.internal/api/v1/payments/convert" -d \'{"amount": -50.0}\'',
              "sample_response": '{"credited": 50.0}',
              "impact": "Financial loss through intentional balance manipulation.",
              "proposed_slo": "P2/S2 7 days.",
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "billing-ops@company.com",
                  "date": d_minus_1.strftime("%B %d, %Y 14:00 UTC"),
                  "is_internal": True,
                  "text": "Discovered during currency conversion boundary tests.",
              }
          ],
      },
      "920194812": {
          "id": "920194812",
          "bug_number": "b/920194812",
          "title": (
              "[Security P1] Hardcoded Payment Sandbox API Key Active in"
              " Production Checkout Router"
          ),
          "status": "Triaged",
          "priority": "P1",
          "severity": "S1",
          "type": "Vulnerability (Secrets / Credentials)",
          "due_date": f"{d_plus_2.strftime('%B %d, %Y')} (Target: 48h SLA)",
          "due_date_class": "",
          "component": "Security > Financial & Payments Security > Checkout API",
          "reporter": "secrets-scanner@company.com",
          "assignee_ldap": "",
          "modified_date": h_minus_1.strftime("%B %d, %Y %H:30 UTC"),
          "created_date": h_minus_3.strftime("%B %d, %Y %H:15 UTC"),
          "hotlists": ["7920155", "Secrets-Exposure", "PCI-DSS-Review"],
          "description": {
              "summary": (
                  "Static source code scanner found fallback sk_live_... key"
                  " embedded in checkout client configuration."
              ),
              "affected_endpoint": "/checkout/*",
              "affected_path": "//depot/checkout/config.py",
              "leaked_fields": ["Payment gateway secret token"],
              "repro_curl": "grep -rn sk_live //depot/checkout/config.py",
              "sample_response": "sk_live_99214...",
              "impact": "Potential unauthorized chargeback and refund triggering.",
              "proposed_slo": "P1/S1 48 hour SLA.",
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "secrets-scanner@company.com",
                  "date": h_minus_3.strftime("%B %d, %Y %H:15 UTC"),
                  "is_internal": True,
                  "text": "Automated secret alert on commit #84910.",
              }
          ],
      },
      "482019481": {
          "id": "482019481",
          "bug_number": "b/482019481",
          "title": (
              "[Security P3] Missing Strict-Transport-Security (HSTS) Header on"
              " Static Edge CDN Assets"
          ),
          "status": "Fixed",
          "priority": "P3",
          "severity": "S3",
          "type": "Bug (Headers / Transport Security)",
          "due_date": f"{d_minus_9.strftime('%B %d, %Y')} (Completed)",
          "due_date_class": "",
          "component": "Infrastructure > API Gateway & Edge > Edge Headers & CSP",
          "reporter": "ssl-labs-bot@company.com",
          "assignee_ldap": "sam_b",
          "modified_date": d_minus_9.strftime("%B %d, %Y 12:00 UTC"),
          "created_date": d_minus_13.strftime("%B %d, %Y 10:00 UTC"),
          "hotlists": ["7920155", "TLS-Standards"],
          "description": {
              "summary": (
                  "HSTS response header missing max-age on asset CDN nodes."
              ),
              "affected_endpoint": "Edge CDN Proxy",
              "affected_path": "//depot/gateway/headers.conf",
              "leaked_fields": ["Strict-Transport-Security"],
              "repro_curl": 'curl -I "https://static.enterprise.internal/style.css"',
              "sample_response": "HTTP/2 200 OK",
              "impact": "SSL downgrade risk on insecure local Wi-Fi networks.",
              "proposed_slo": "Resolved.",
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "sam_b@company.com",
                  "date": d_minus_9.strftime("%B %d, %Y 12:00 UTC"),
                  "is_internal": True,
                  "text": "Added Strict-Transport-Security: max-age=63072000; includeSubDomains.",
              }
          ],
      },
      "739102847": {
          "id": "739102847",
          "bug_number": "b/739102847",
          "title": (
              "[Security P2] Writable /tmp Directory Inside Read-Only Root SRE"
              " Production Containers"
          ),
          "status": "Assigned",
          "priority": "P2",
          "severity": "S2",
          "type": "Vulnerability (Container / Filesystem)",
          "due_date": f"{d_plus_10.strftime('%B %d, %Y')} (Target: 14d SLA)",
          "due_date_class": "",
          "component": "Infrastructure > Cloud SRE & Containers > Base Image",
          "reporter": "sec-hardening@company.com",
          "assignee_ldap": "kevin_j",
          "modified_date": d_minus_2.strftime("%B %d, %Y 14:00 UTC"),
          "created_date": d_minus_4.strftime("%B %d, %Y 09:30 UTC"),
          "hotlists": ["7920155", "Container-Hardening"],
          "description": {
              "summary": (
                  "/tmp is mounted without noexec flag, permitting binary"
                  " execution from writable scratch space."
              ),
              "affected_endpoint": "Base Alpine Image",
              "affected_path": "//depot/docker/base/Dockerfile",
              "leaked_fields": ["Container Mount Options"],
              "repro_curl": "mount | grep /tmp",
              "sample_response": "tmpfs on /tmp type tmpfs (rw,relatime)",
              "impact": "Allows attackers with arbitrary write to execute dropped binaries.",
              "proposed_slo": "P2/S2 14 days.",
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "kevin_j@company.com",
                  "date": d_minus_2.strftime("%B %d, %Y 14:00 UTC"),
                  "is_internal": True,
                  "text": "Adding noexec,nosuid mount options to base docker-compose files.",
              }
          ],
      },
      "849201842": {
          "id": "849201842",
          "bug_number": "b/849201842",
          "title": (
              "[Security P0] Central SSO Session Fixation via Insecure Cookie"
              " Attribute on Login (/sso/login)"
          ),
          "status": "Verified",
          "priority": "P0",
          "severity": "S0",
          "type": "Vulnerability (Auth / Session Hijacking)",
          "due_date": f"{d_minus_12.strftime('%B %d, %Y')} (Completed)",
          "due_date_class": "",
          "component": "Security > Identity & Access Management > SSO",
          "reporter": "pentest-team@company.com (Internal Red Team / Pentest)",
          "assignee_ldap": "david_p",
          "modified_date": d_minus_12.strftime("%B %d, %Y 22:15 UTC"),
          "created_date": d_minus_12.strftime("%B %d, %Y 14:00 UTC"),
          "hotlists": [
              "7920155",
              "P0-Critical-Security",
              "Auth-Security",
              "SSO-Federation",
          ],
          "description": {
              "summary": (
                  "During an authorized Red Team penetration test of the Identity"
                  " & Central SSO platform, auditors identified a critical session fixation"
                  " vulnerability in the primary authentication controller at <code>/sso/login</code>."
                  " The session identifier cookie (<code>sso_session_id</code>) was not regenerated"
                  " upon successful credential verification, allowing an attacker to pre-set a session"
                  " cookie on a victim's client and hijack the authenticated session immediately after login."
              ),
              "affected_endpoint": "/sso/login",
              "affected_path": "//depot/identity/session_manager.py",
              "leaked_fields": [
                  "<code>sso_session_id</code> session token reuse across auth boundary",
                  "Missing <code>session.regenerate_id()</code> invocation in login controller",
                  "Victim corporate credentials and IAM access permissions bound to pre-allocated session token",
              ],
              "repro_curl": (
                  "# Step 1: Pre-set attacker session cookie:\n"
                  'curl -c cookies.txt "https://auth.enterprise.internal/sso/login"\n\n'
                  "# Step 2: Victim logs in with valid credentials using the pre-set session cookie:\n"
                  'curl -b cookies.txt -X POST "https://auth.enterprise.internal/sso/login" \\\n'
                  '  -d "username=victim_user&password=SecretPassword123"\n\n'
                  "# Step 3: Attacker accesses protected dashboard using original cookies.txt without logging in:\n"
                  'curl -b cookies.txt "https://auth.enterprise.internal/api/v1/auth/session/status"'
              ),
              "sample_response": """{
  "authenticated": true,
  "user_ldap": "victim_user",
  "roles": ["corp-engineer", "prod-deployer"],
  "session_id": "sso_pre_fixed_cookie_99812a"
}""",
              "impact": (
                  "Critical corporate authentication bypass. Allowed arbitrary account takeover"
                  " of corporate users on shared kiosks, lab workstations, or through subdomain"
                  " cookie tossing attacks, compromising internal corporate network access."
              ),
              "proposed_slo": "P0/S0 Emergency Incident: Resolved and Verified within 8 hours.",
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "pentest-team@company.com",
                  "date": d_minus_12.strftime("%B %d, %Y 14:00 UTC"),
                  "is_internal": True,
                  "text": (
                      "Declaring P0 finding for Session Fixation in Central SSO.\n\n"
                      "We confirmed that <code>/sso/login</code> does not issue a new <code>sso_session_id</code> cookie"
                      " after successful authentication. If an attacker pre-seeds a session cookie on a client browser,"
                      " that exact cookie becomes fully authenticated once the user logs in.\n\n"
                      "Full reproduction script and curl payload attached above."
                  ),
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "sec-ops@company.com",
                  "date": d_minus_12.strftime("%B %d, %Y 14:15 UTC"),
                  "is_internal": True,
                  "text": (
                      "Incident Commander joined. Declaring P0 Emergency Security Outage (Incident #SEC-9841).\n\n"
                      "Assigning to <strong>@david_p</strong> (IAM Primary On-Call) and CCing <strong>@sarah_k</strong> (IAM Tech Lead)."
                      " Setting up emergency war room on #sec-incident-sso-fixation."
                  ),
              },
              {
                  "id": 3,
                  "number": "#3",
                  "author": "david_p@company.com",
                  "date": d_minus_12.strftime("%B %d, %Y 16:30 UTC"),
                  "is_internal": True,
                  "text": (
                      "Root Cause Analysis complete:\n\n"
                      "In <code>//depot/identity/session_manager.py</code>, the <code>authenticate_user()</code> handler"
                      " was updating user state directly in the existing session record without calling <code>session_store.regenerate_id()</code>.\n\n"
                      "Emergency hotfix PR #4701 created:\n"
                      "1. Invokes cryptographic session renewal (<code>session_store.invalidate_and_regenerate()</code>) upon every login.\n"
                      "2. Sends <code>Set-Cookie: sso_session_id=...; HttpOnly; Secure; SameSite=Strict</code> with new token.\n"
                      "3. Adds unit test suite <code>//depot/identity:session_manager_test</code>."
                  ),
              },
              {
                  "id": 4,
                  "number": "#4",
                  "author": "sarah_k@company.com",
                  "date": d_minus_12.strftime("%B %d, %Y 17:45 UTC"),
                  "is_internal": True,
                  "text": (
                      "PR #4701 reviewed and approved. Merged to release branch.\n\n"
                      "Canary deployment initiated on edge authentication gateways in us-east1 and eu-west1."
                  ),
              },
              {
                  "id": 5,
                  "number": "#5",
                  "author": "david_p@company.com",
                  "date": d_minus_12.strftime("%B %d, %Y 19:30 UTC"),
                  "is_internal": True,
                  "text": (
                      "Global rollout of hotfix PR #4701 completed to 100% of production SSO traffic.\n\n"
                      "Canary metrics healthy: zero 5xx error spikes and session creation latencies normal.\n"
                      "Setting status to **Fixed** and handing off to Pentest team for independent re-verification."
                  ),
              },
              {
                  "id": 6,
                  "number": "#6",
                  "author": "pentest-team@company.com",
                  "date": d_minus_12.strftime("%B %d, %Y 21:00 UTC"),
                  "is_internal": True,
                  "text": (
                      "Independent retest verification PASSED:\n\n"
                      "1. Executed automated penetration test suite against production <code>https://auth.enterprise.internal/sso/login</code>.\n"
                      "2. Verified that pre-existing session cookies are immediately invalidated upon login.\n"
                      "3. Confirmed new high-entropy <code>sso_session_id</code> token issued with <code>SameSite=Strict; HttpOnly; Secure</code>.\n\n"
                      "The session fixation vulnerability is completely mitigated."
                  ),
              },
              {
                  "id": 7,
                  "number": "#7",
                  "author": "sec-ops@company.com",
                  "date": d_minus_12.strftime("%B %d, %Y 22:15 UTC"),
                  "is_internal": True,
                  "text": (
                      "Incident #SEC-9841 Resolution & Post-Mortem Sign-Off:\n\n"
                      "- Hotfix PR #4701 verified in production by Red Team.\n"
                      "- Automated regression tests merged into CI pipeline.\n"
                      "- Post-mortem review scheduled for Friday with IAM and Security Engineering.\n\n"
                      "Changing status to **Verified** and closing incident ticket."
                  ),
              },
          ],
      },
      "592019384": {
          "id": "592019384",
          "bug_number": "b/592019384",
          "title": (
              "[Privacy P2] Cleartext Internal API Key Logged in Privacy"
              " Compliance Audit Pipeline"
          ),
          "status": "Assigned",
          "priority": "P2",
          "severity": "S2",
          "type": "Vulnerability (Logging / Credential Leak)",
          "due_date": f"{d_plus_6.strftime('%B %d, %Y')} (Target: 7d SLA)",
          "due_date_class": "",
          "component": "Security > Data Privacy Governance > Audit Logging",
          "reporter": "audit-security@company.com",
          "assignee_ldap": "omar_h",
          "modified_date": h_minus_5.strftime("%B %d, %Y %H:00 UTC"),
          "created_date": d_minus_1.strftime("%B %d, %Y 18:20 UTC"),
          "hotlists": ["7920155", "GDPR-Compliance", "Audit-Log"],
          "description": {
              "summary": (
                  "Debug level logging in compliance worker outputs the"
                  " full Authorization bearer token to stdout log collectors."
              ),
              "affected_endpoint": "Audit Log Collector",
              "affected_path": "//depot/logging/sanitizer/audit_logger.py",
              "leaked_fields": ["Authorization header in syslog"],
              "repro_curl": "grep -i 'Bearer' /var/log/audit.log",
              "sample_response": "Bearer sec_token_48192...",
              "impact": "Credential exposure to log aggregation readers.",
              "proposed_slo": "P2/S2 7 day resolution.",
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "omar_h@company.com",
                  "date": h_minus_5.strftime("%B %d, %Y %H:00 UTC"),
                  "is_internal": True,
                  "text": "Applying log sanitizer regex to redact Bearer tokens.",
              }
          ],
      },
      "918204918": {
          "id": "918204918",
          "bug_number": "b/918204918",
          "title": (
              "[Security P1] OAuth2 Redirect URI Validation Bypass in Mobile"
              " Authorization Flow (/oauth/authorize)"
          ),
          "status": "Assigned",
          "priority": "P1",
          "severity": "S1",
          "type": "Vulnerability (Authentication / OAuth)",
          "due_date": (
              f"{d_plus_1.strftime('%B %d, %Y')} (Approaching SLO Deadline - 1 day remaining)"
          ),
          "due_date_class": "",
          "component": "Security > Identity & Access Management > OAuth2",
          "reporter": "appsec-external@bugbounty.internal (External Bounty Submission)",
          "assignee_ldap": "david_p",
          "modified_date": d_minus_3.strftime("%B %d, %Y 16:45 UTC"),
          "created_date": d_minus_4.strftime("%B %d, %Y 11:00 UTC"),
          "hotlists": [
              "7920155",
              "P1-Security-Incident",
              "Auth-Security",
              "OAuth-Security",
          ],
          "description": {
              "summary": (
                  "Security research report submitted via the external Bug Bounty"
                  " program identified that the OAuth2 authorization server at"
                  " <code>/oauth/authorize</code> performs unanchored regex suffix"
                  " matching on the <code>redirect_uri</code> parameter. An attacker"
                  " can register domains such as <code>https://auth.company.com.attacker.com/callback</code>"
                  " or use URL path manipulation to steal authorization codes and tokens"
                  " during mobile and web SSO handshakes."
              ),
              "affected_endpoint": "/oauth/authorize",
              "affected_path": "//depot/auth_service/oauth_validator.py",
              "leaked_fields": [
                  "<code>redirect_uri</code> validation regex: <code>auth\\.company\\.com</code>",
                  "OAuth2 Authorization Codes leaked in HTTP Referer / query parameters to untrusted redirect URIs",
                  "User access tokens and refresh tokens susceptible to interception",
              ],
              "repro_curl": (
                  "curl -I"
                  ' "https://auth.enterprise.internal/oauth/authorize?client_id=mobile_app_v2&response_type=code&redirect_uri=https://auth.company.com.attacker.com/callback&state=xyz123"'
              ),
              "sample_response": "HTTP/1.1 302 Found\nLocation: https://auth.company.com.attacker.com/callback?code=auth_code_99182a&state=xyz123",
              "impact": (
                  "High-severity authentication compromise. Enables full authorization"
                  " code theft and user account takeover through malicious link clicks."
              ),
              "proposed_slo": (
                  "P1/S1 Identity & Authentication Vulnerability: Resolution required"
                  f" within 48 hours of initial triage (Target Due Date: {d_plus_1.strftime('%B %d, %Y')} 18:00 UTC)."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "appsec-external@bugbounty.internal",
                  "date": d_minus_4.strftime("%B %d, %Y 11:00 UTC"),
                  "is_internal": True,
                  "text": (
                      "Reporting P1 authorization bypass flaw in <code>/oauth/authorize</code>.\n\n"
                      "The redirect URI check uses loose regex pattern matching without anchoring"
                      " to hostname boundaries. Supplying <code>redirect_uri=https://auth.company.com.attacker.com</code>"
                      " successfully issues authorization codes to an attacker-controlled endpoint.\n\n"
                      "See report details above for repro."
                  ),
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "security-triage@company.com",
                  "date": d_minus_4.strftime("%B %d, %Y 11:30 UTC"),
                  "is_internal": True,
                  "text": (
                      "Triaged and verified finding. Assigning to <strong>@david_p</strong>"
                      " (IAM & Auth Security) for urgent patch."
                  ),
              },
              {
                  "id": 3,
                  "number": "#3",
                  "author": "david_p@company.com",
                  "date": d_minus_3.strftime("%B %d, %Y 16:45 UTC"),
                  "is_internal": True,
                  "text": (
                      "Acknowledging finding. Confirmed the flawed regex in <code>oauth_validator.py</code>."
                      " I will implement strict hostname allowlist parsing against registered client redirect"
                      " URIs and push the patch tomorrow."
                  ),
              },
          ],
      },
      "481920194": {
          "id": "481920194",
          "bug_number": "b/481920194",
          "title": (
              "[Security P2] Database Field-Level Encryption Migration for"
              " Cardholder Billing Records Blocked on Cloud KMS Quota"
          ),
          "status": "Blocked",
          "priority": "P2",
          "severity": "S2",
          "type": "Vulnerability (Cryptography / PCI-DSS)",
          "due_date": (
              f"{d_plus_7.strftime('%B %d, %Y')} (Target: 14d SLA)"
          ),
          "due_date_class": "",
          "component": "Security > Financial & Payments Security > Cardholder Data Vault",
          "reporter": "security-compliance@company.com (Compliance Audit Team)",
          "assignee_ldap": "lucas_m",
          "modified_date": h_minus_6.strftime("%B %d, %Y %H:15 UTC"),
          "created_date": d_minus_4.strftime("%B %d, %Y 09:00 UTC"),
          "hotlists": [
              "7920155",
              "PCI-DSS-Review",
              "KMS-Migration",
              "Payments-Integrity",
          ],
          "description": {
              "summary": (
                  "PCI-DSS 4.0 mandate requires AES-256 field-level envelope"
                  " encryption for legacy cardholder billing metadata stored in"
                  " database tables. The automated migration pipeline encrypts"
                  " customer billing records using Cloud KMS key rings."
              ),
              "affected_endpoint": "Billing Vault Encryption Worker",
              "affected_path": "//depot/services/payments/vault/envelope_migrator.py",
              "leaked_fields": [
                  "Legacy unencrypted <code>cardholder_billing_address</code> column",
                  "Cloud KMS API envelope key request limits (10,000 QPS threshold)",
              ],
              "repro_curl": "python3 //depot/services/payments/vault/envelope_migrator.py --dry-run=false",
              "sample_response": "RESOURCE_EXHAUSTED: Cloud KMS API quota exceeded for project payments-prod-281.",
              "impact": (
                  "Inability to complete PCI-DSS cardholder data encryption"
                  " before compliance deadline without causing production"
                  " payment processing throttling."
              ),
              "proposed_slo": (
                  "P2/S2 Compliance Vulnerability: Resolution required within"
                  f" 14 days of initial triage (Target Due Date: {d_plus_7.strftime('%B %d, %Y')} 18:00 UTC)."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "security-compliance@company.com",
                  "date": d_minus_4.strftime("%B %d, %Y 09:00 UTC"),
                  "is_internal": True,
                  "text": (
                      "Filing P2 finding for PCI-DSS 4.0 compliance.\n\n"
                      "Historical payment metadata in <code>billing_records_legacy</code>"
                      " requires backfill envelope encryption via Cloud KMS before the upcoming audit."
                  ),
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "lucas_m@company.com",
                  "date": d_minus_3.strftime("%B %d, %Y 14:30 UTC"),
                  "is_internal": True,
                  "text": (
                      "Acknowledging ticket. Developing migration script <code>envelope_migrator.py</code>"
                      " to batch encrypt existing records with DEK/KEK rotation."
                  ),
              },
              {
                  "id": 3,
                  "number": "#3",
                  "author": "lucas_m@company.com",
                  "date": d_minus_2.strftime("%B %d, %Y 11:00 UTC"),
                  "is_internal": True,
                  "text": (
                      "Staging dry run hit <code>RESOURCE_EXHAUSTED</code> quota limits on Cloud KMS"
                      " (10,000 QPS threshold exceeded during 500k row batching). Running migration in production"
                      " currently threatens live checkout latency."
                  ),
              },
              {
                  "id": 4,
                  "number": "#4",
                  "author": "lucas_m@company.com",
                  "date": h_minus_6.strftime("%B %d, %Y %H:15 UTC"),
                  "is_internal": True,
                  "text": (
                      "Setting status to **Blocked**.\n\n"
                      "The migration script is tested and ready, but execution is blocked on:\n"
                      "1. **Cloud KMS Quota Increase:** Submitted ticket <code>b/882190412</code> to <strong>cloud-kms-quota@company.com</strong> and <strong>infra-capacity@company.com</strong> to raise project QPS from 10k to 50k.\n"
                      "2. **DBA Maintenance Window:** Awaiting confirmation from Database Admin on-call (@andre_f) to execute the migration off-peak.\n\n"
                      "Once the KMS quota is increased by Infrastructure Capacity, we will resume the migration job."
                  ),
              },
          ],
      },
      "381920194": {
          "id": "381920194",
          "bug_number": "b/381920194",
          "title": (
              "[Security P3] Content-Security-Policy (CSP) Nonce-Based"
              " Enforcement on Internal Admin Console (/admin/*)"
          ),
          "status": "Blocked",
          "priority": "P3",
          "severity": "S3",
          "type": "Bug (Web Security / CSP)",
          "due_date": (
              f"{d_plus_10.strftime('%B %d, %Y')} (Target: 30d SLA)"
          ),
          "due_date_class": "",
          "component": "Infrastructure > API Gateway & Edge > Edge Headers & CSP",
          "reporter": "appsec-hygiene@company.com (Application Security Hygiene)",
          "assignee_ldap": "sam_b",
          "modified_date": h_minus_4.strftime("%B %d, %Y %H:30 UTC"),
          "created_date": d_minus_6.strftime("%B %d, %Y 10:00 UTC"),
          "hotlists": [
              "7920155",
              "CSP-Hygiene",
              "Edge-Ingress",
          ],
          "description": {
              "summary": (
                  "The internal Admin Console at <code>https://admin.enterprise.internal</code>"
                  " currently serves <code>Content-Security-Policy-Report-Only</code>."
                  " Company web security guidelines mandate enforcing active"
                  " <code>Content-Security-Policy: default-src 'self'; script-src 'nonce-{random}';</code>"
                  " to mitigate Cross-Site Scripting (XSS) risks."
              ),
              "affected_endpoint": "Admin Console (/admin/*)",
              "affected_path": "//depot/gateway/csp/admin_csp.conf",
              "leaked_fields": [
                  "Content-Security-Policy-Report-Only header",
                  "Legacy inline <code>&lt;script&gt;</code> blocks generated by charting widgets",
              ],
              "repro_curl": 'curl -I "https://admin.enterprise.internal/admin/dashboard"',
              "sample_response": "Content-Security-Policy-Report-Only: default-src 'self'...",
              "impact": (
                  "Lack of active CSP enforcement increases risk of DOM-based"
                  " XSS exploitation on internal administrative dashboards."
              ),
              "proposed_slo": (
                  "P3/S3 Security Hygiene: Resolution required within 30 days"
                  f" (Target Due Date: {d_plus_10.strftime('%B %d, %Y')} 18:00 UTC)."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "appsec-hygiene@company.com",
                  "date": d_minus_6.strftime("%B %d, %Y 10:00 UTC"),
                  "is_internal": True,
                  "text": (
                      "Filing P3 security hygiene ticket to switch Admin Console CSP"
                      " from report-only mode to full enforcement with cryptographic nonces."
                  ),
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "sam_b@company.com",
                  "date": d_minus_4.strftime("%B %d, %Y 15:00 UTC"),
                  "is_internal": True,
                  "text": (
                      "Configured active CSP header in staging gateway proxy."
                  ),
              },
              {
                  "id": 3,
                  "number": "#3",
                  "author": "sam_b@company.com",
                  "date": d_minus_2.strftime("%B %d, %Y 11:30 UTC"),
                  "is_internal": True,
                  "text": (
                      "Testing in staging revealed that the legacy admin analytics widget"
                      " (<code>legacy-dashboard-charts.js</code>) dynamically generates inline script"
                      " tags without nonce support, breaking dashboard visualizations for operations teams."
                  ),
              },
              {
                  "id": 4,
                  "number": "#4",
                  "author": "sam_b@company.com",
                  "date": h_minus_4.strftime("%B %d, %Y %H:30 UTC"),
                  "is_internal": True,
                  "text": (
                      "Setting status to **Blocked**.\n\n"
                      "Gateway CSP configuration is ready, but enforcement is blocked on frontend migration:\n"
                      "1. **Frontend Charting Dependency:** The legacy charting component must be migrated to modern Chart.js v4.x (which supports nonce tags).\n"
                      "2. **Pending Frontend Task:** Tracking in ticket <code>b/671029481</code> assigned to <strong>@carla_s</strong> and <strong>#frontend-core</strong>.\n\n"
                      "Once PR from `b/671029481` lands, we will flip the header to active enforcement."
                  ),
              },
          ],
      },
      "519204819": {
          "id": "519204819",
          "bug_number": "b/519204819",
          "title": (
              "[Bug] Unindexed Full-Table Scan on Client Profile Search Query"
              " by Tax Identifier (/api/v2/clients/search)"
          ),
          "status": "Assigned",
          "priority": "P2",
          "severity": "S2",
          "type": "Bug (Performance / Database)",
          "due_date": f"{d_plus_4.strftime('%B %d, %Y')} (Target: 7d SLA)",
          "due_date_class": "",
          "component": "Services > Customer Accounts > Client Profile Service",
          "reporter": "monitoring-bot@company.com",
          "assignee_ldap": "lucas_m",
          "modified_date": d_minus_1.strftime("%B %d, %Y 11:20 UTC"),
          "created_date": d_minus_5.strftime("%B %d, %Y 09:00 UTC"),
          "hotlists": ["7920155", "Performance-SRE", "Customer-Accounts"],
          "description": {
              "summary": (
                  "Slow query alert triggered during high-throughput client onboarding. Missing composite"
                  " index on (tax_identifier, account_status) in Spanner table ClientProfiles causes full table"
                  " scans with p99 latency exceeding 2.5 seconds."
              ),
              "affected_endpoint": "/api/v2/clients/search",
              "affected_path": "//depot/services/clients/profile_service.py",
              "leaked_fields": ["Database query execution plan"],
              "repro_curl": 'curl -X GET "https://api.enterprise.internal/api/v2/clients/search?tax_id=99887766"',
              "sample_response": '{"results": [{"client_id": "c-9988", "name": "Acme Corp"}], "query_time_ms": 2680}',
              "impact": "Database connection pool exhaustion during peak onboarding traffic windows.",
              "proposed_slo": (
                  f"P2/S2 Performance Defect: Resolution required within 7 days (Target Due Date: {d_plus_4.strftime('%B %d, %Y')} 18:00 UTC)."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "monitoring-bot@company.com",
                  "date": d_minus_5.strftime("%B %d, %Y 09:00 UTC"),
                  "is_internal": True,
                  "text": "Automated alert: p99 latency on /api/v2/clients/search exceeded 2000ms threshold (measured: 2680ms).",
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "lucas_m@company.com",
                  "date": d_minus_1.strftime("%B %d, %Y 11:20 UTC"),
                  "is_internal": True,
                  "text": "Drafted DDL schema migration PR #4810 to add index `idx_client_profiles_tax_id_status`. Scheduled for next rollout window.",
              },
          ],
      },
      "629104820": {
          "id": "629104820",
          "bug_number": "b/629104820",
          "title": (
              "[Security P3] Outbound Salesforce CRM Sync Webhook Retrying"
              " Indefinitely on 4xx Client Errors"
          ),
          "status": "Assigned",
          "priority": "P3",
          "severity": "S3",
          "type": "Bug (Integration / Logic)",
          "due_date": f"{d_plus_10.strftime('%B %d, %Y')} (Target: 30d SLA)",
          "due_date_class": "",
          "component": "Services > Customer Accounts > CRM Integrations",
          "reporter": "crm-ops@company.com",
          "assignee_ldap": "elena_r",
          "modified_date": d_minus_2.strftime("%B %d, %Y 14:00 UTC"),
          "created_date": d_minus_7.strftime("%B %d, %Y 10:30 UTC"),
          "hotlists": ["7920155", "CRM-Integrations"],
          "description": {
              "summary": (
                  "The asynchronous CRM synchronization worker retries failed 400/404 Salesforce webhook"
                  " tasks indefinitely without max retry caps, causing Celery background queue congestion"
                  " and memory accumulation on persistent 4xx client errors."
              ),
              "affected_endpoint": "/internal/v1/crm/salesforce/webhook",
              "affected_path": "//depot/services/clients/integrations/salesforce_sync.py",
              "leaked_fields": ["Retry queue metadata"],
              "repro_curl": 'curl -X POST "https://crm.internal/internal/v1/crm/salesforce/webhook" -d \'{"event": "client_updated", "client_id": "invalid_id"}\'',
              "sample_response": '{"status": "queued", "retry_count": 8421}',
              "impact": "Resource starvation for legitimate customer data sync tasks across worker pods.",
              "proposed_slo": (
                  f"P3/S3 Integration Hygiene: Resolution required within 30 days (Target Due Date: {d_plus_10.strftime('%B %d, %Y')} 18:00 UTC)."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "crm-ops@company.com",
                  "date": d_minus_7.strftime("%B %d, %Y 10:30 UTC"),
                  "is_internal": True,
                  "text": "Noticing memory growth in redis worker broker. A single deleted Salesforce record generated over 8,000 retries.",
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "elena_r@company.com",
                  "date": d_minus_2.strftime("%B %d, %Y 14:00 UTC"),
                  "is_internal": True,
                  "text": "Added dead-letter queue routing (DLQ) with max 5 retries for 4xx errors in PR #4832. In code review.",
              },
          ],
      },
      "718294019": {
          "id": "718294019",
          "bug_number": "b/718294019",
          "title": (
              "[Privacy P2] Regex Pattern in PIIMaskingFilter Missing International"
              " E.164 Phone Number Formats"
          ),
          "status": "Assigned",
          "priority": "P2",
          "severity": "S2",
          "type": "Bug (Privacy / Redaction)",
          "due_date": f"{d_plus_5.strftime('%B %d, %Y')} (Target: 7d SLA)",
          "due_date_class": "",
          "component": "Security > Data Privacy Governance > PIIMaskingFilter",
          "reporter": "privacy-audit@company.com",
          "assignee_ldap": "omar_h",
          "modified_date": d_minus_1.strftime("%B %d, %Y 15:45 UTC"),
          "created_date": d_minus_4.strftime("%B %d, %Y 10:00 UTC"),
          "hotlists": ["7920155", "Privacy-Redaction", "GDPR-Compliance"],
          "description": {
              "summary": (
                  "The enterprise shared PIIMaskingFilter library currently matches standard US 10-digit"
                  " phone numbers (`(XXX) XXX-XXXX`) but fails to redact international E.164 formatted"
                  " numbers (`+44`, `+33`, `+55`), allowing unmasked non-US client phone numbers to be"
                  " written to audit and application logs."
              ),
              "affected_endpoint": "PIIMaskingFilter Middleware",
              "affected_path": "//depot/privacy/filters/pii_masking.py",
              "leaked_fields": ["International E.164 Phone Numbers"],
              "repro_curl": 'python3 -c "from privacy.filters.pii_masking import mask_pii; print(mask_pii(\'User phone: +44 20 7946 0991\'))"',
              "sample_response": "User phone: +44 20 7946 0991 (UNMASKED)",
              "impact": "Global privacy compliance non-compliance under GDPR Article 5(1)(c) data minimization rules.",
              "proposed_slo": (
                  f"P2/S2 Privacy Finding: Resolution required within 7 days (Target Due Date: {d_plus_5.strftime('%B %d, %Y')} 18:00 UTC)."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "privacy-audit@company.com",
                  "date": d_minus_4.strftime("%B %d, %Y 10:00 UTC"),
                  "is_internal": True,
                  "text": "Identified during EU data governance audit. UK and German customer phone numbers are not redacted by default regex patterns.",
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "omar_h@company.com",
                  "date": d_minus_1.strftime("%B %d, %Y 15:45 UTC"),
                  "is_internal": True,
                  "text": "Integrating Google libphonenumber parser into `PIIMaskingFilter` to universally redact all international dialing codes. Testing PR #4844.",
              },
          ],
      },
      "829104712": {
          "id": "829104712",
          "bug_number": "b/829104712",
          "title": (
              "[Security P2] Missing Invalidation of Downstream Active Refresh"
              " Tokens on Global Password Change"
          ),
          "status": "Assigned",
          "priority": "P2",
          "severity": "S2",
          "type": "Bug (Security / IAM)",
          "due_date": f"{d_plus_6.strftime('%B %d, %Y')} (Target: 7d SLA)",
          "due_date_class": "",
          "component": "Security > Identity & Access Management > Session Security",
          "reporter": "redteam@company.com",
          "assignee_ldap": "david_p",
          "modified_date": d_minus_1.strftime("%B %d, %Y 16:30 UTC"),
          "created_date": d_minus_3.strftime("%B %d, %Y 11:00 UTC"),
          "hotlists": ["7920155", "IAM-Security", "Session-Hardening"],
          "description": {
              "summary": (
                  "When an account owner updates their password via `/api/v1/auth/password/change`,"
                  " existing OAuth2 refresh tokens issued to active mobile sessions are not revoked"
                  " in the central Redis token bloom filter, allowing active sessions on lost or compromised"
                  " devices to continuously refresh access tokens."
              ),
              "affected_endpoint": "/api/v1/auth/password/change",
              "affected_path": "//depot/services/auth/session/token_revocation.py",
              "leaked_fields": ["Long-lived Refresh Tokens"],
              "repro_curl": 'curl -X POST "https://auth.internal/api/v1/auth/password/change" -d \'{"old_password": "...", "new_password": "..."}\'',
              "sample_response": '{"status": "password_updated", "revoked_sessions": 1}',
              "impact": "Account takeover persistence following user credential rotation.",
              "proposed_slo": (
                  f"P2/S2 Security Vulnerability: Resolution required within 7 days (Target Due Date: {d_plus_6.strftime('%B %d, %Y')} 18:00 UTC)."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "redteam@company.com",
                  "date": d_minus_3.strftime("%B %d, %Y 11:00 UTC"),
                  "is_internal": True,
                  "text": "Red Team POC confirmed: Mobile refresh token issued before password change successfully obtained a new access token 24 hours later.",
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "david_p@company.com",
                  "date": d_minus_1.strftime("%B %d, %Y 16:30 UTC"),
                  "is_internal": True,
                  "text": "Implemented user-level `token_epoch_timestamp` check in JWT validation middleware (PR #4855). Any token with `iat < epoch` will be rejected.",
              },
          ],
      },
      "938102941": {
          "id": "938102941",
          "bug_number": "b/938102941",
          "title": (
              "[Security P2] Distributed Redis Rate Limiting Bypass via IP"
              " Spoofing in Multi-Hop Forwarded-For Header"
          ),
          "status": "Assigned",
          "priority": "P2",
          "severity": "S2",
          "type": "Bug (Security / Network)",
          "due_date": f"{d_plus_5.strftime('%B %d, %Y')} (Target: 7d SLA)",
          "due_date_class": "",
          "component": "Infrastructure > API Gateway & Edge > Rate Limiting Mesh",
          "reporter": "security-pentest@company.com",
          "assignee_ldap": "sam_b",
          "modified_date": d_minus_2.strftime("%B %d, %Y 13:10 UTC"),
          "created_date": d_minus_4.strftime("%B %d, %Y 09:30 UTC"),
          "hotlists": ["7920155", "Gateway-Security", "Rate-Limiting"],
          "description": {
              "summary": (
                  "The Envoy edge rate-limiting Lua filter parsed the leftmost client IP from `X-Forwarded-For`"
                  " without validating trusted proxy hops. An attacker can bypass the 100 req/min threshold"
                  " by prefixing arbitrary pseudo-random IP addresses in the `X-Forwarded-For` request header."
              ),
              "affected_endpoint": "Envoy Ingress Edge (/api/*)",
              "affected_path": "//depot/envoy/lua/rate_limiter.lua",
              "leaked_fields": ["Client IP Rate Quota Buckets"],
              "repro_curl": 'curl -H "X-Forwarded-For: 198.51.100.1, 10.0.0.1" https://api.enterprise.internal/api/v1/auth/login',
              "sample_response": "HTTP/1.1 200 OK (Rate limit bypassed 500x)",
              "impact": "Unrestricted credential brute-forcing against authentication endpoints via rate limit evasion.",
              "proposed_slo": (
                  f"P2/S2 Gateway Security: Resolution required within 7 days (Target Due Date: {d_plus_5.strftime('%B %d, %Y')} 18:00 UTC)."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "security-pentest@company.com",
                  "date": d_minus_4.strftime("%B %d, %Y 09:30 UTC"),
                  "is_internal": True,
                  "text": "Confirmed rate limiter uses leftmost header value rather than immediate downstream socket peer IP.",
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "sam_b@company.com",
                  "date": d_minus_2.strftime("%B %d, %Y 13:10 UTC"),
                  "is_internal": True,
                  "text": "Configured Envoy `use_remote_address: true` and `xff_num_trusted_hops: 2` in PR #4861. Verifying against load tests.",
              },
          ],
      },
      "847291048": {
          "id": "847291048",
          "bug_number": "b/847291048",
          "title": (
              "[Security P2] Overly Permissive ClusterRoleBinding Allowing"
              " List/Watch Secrets in Default Namespace"
          ),
          "status": "Assigned",
          "priority": "P2",
          "severity": "S2",
          "type": "Bug (Infrastructure / RBAC)",
          "due_date": f"{d_plus_7.strftime('%B %d, %Y')} (Target: 7d SLA)",
          "due_date_class": "",
          "component": "Infrastructure > Cloud SRE & Containers > Production Clusters",
          "reporter": "k8s-security-scan@company.com",
          "assignee_ldap": "kevin_j",
          "modified_date": d_minus_2.strftime("%B %d, %Y 10:15 UTC"),
          "created_date": d_minus_6.strftime("%B %d, %Y 14:00 UTC"),
          "hotlists": ["7920155", "Kubernetes-Hardening", "Infra-RBAC"],
          "description": {
              "summary": (
                  "Static RBAC analysis identified that automation service account `ci-deployer-sa` in the"
                  " `production-gke` cluster was bound to `cluster-admin` instead of scoped DeploymentManager"
                  " roles, granting permission to read and watch all Kubernetes secrets across production namespaces."
              ),
              "affected_endpoint": "Kubernetes API Server (prod-gke-us-central1)",
              "affected_path": "//depot/kubernetes/rbac/cluster_roles.yaml",
              "leaked_fields": ["Cluster-wide Kubernetes Secrets"],
              "repro_curl": 'kubectl auth can-i get secrets --as=system:serviceaccount:default:ci-deployer-sa -n prod',
              "sample_response": "yes",
              "impact": "Privilege escalation and secret leakage if CI deployer credentials are compromised.",
              "proposed_slo": (
                  f"P2/S2 Infrastructure RBAC: Resolution required within 7 days (Target Due Date: {d_plus_7.strftime('%B %d, %Y')} 18:00 UTC)."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "k8s-security-scan@company.com",
                  "date": d_minus_6.strftime("%B %d, %Y 14:00 UTC"),
                  "is_internal": True,
                  "text": "Automated security finding: ServiceAccount bound to ClusterRole with full secret read privileges.",
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "kevin_j@company.com",
                  "date": d_minus_2.strftime("%B %d, %Y 10:15 UTC"),
                  "is_internal": True,
                  "text": "Refactored `ci_deployer` permissions into targeted namespace-scoped RoleBindings restricting secret access to deployment configs only (PR #4872).",
              },
          ],
      },
      "758291043": {
          "id": "758291043",
          "bug_number": "b/758291043",
          "title": (
              "[Security P2] Automatic Secret Rotation Hook Failing Silently"
              " on Third-Party Webhook TLS Handshake"
          ),
          "status": "Assigned",
          "priority": "P2",
          "severity": "S2",
          "type": "Bug (Infrastructure / Secrets)",
          "due_date": f"{d_plus_6.strftime('%B %d, %Y')} (Target: 7d SLA)",
          "due_date_class": "",
          "component": "Infrastructure > Cloud SRE & Containers > Secrets Manager",
          "reporter": "secrets-vault-audit@company.com",
          "assignee_ldap": "andre_f",
          "modified_date": d_minus_1.strftime("%B %d, %Y 14:20 UTC"),
          "created_date": d_minus_5.strftime("%B %d, %Y 11:30 UTC"),
          "hotlists": ["7920155", "Secrets-Management", "Vault-Infra"],
          "description": {
              "summary": (
                  "The Vault 30-day credential rotation daemon for third-party payment partner webhooks"
                  " encountered TLS handshake failures during cert renegotiation and swallowed the exception"
                  " without raising an alert in Sentry, leaving legacy secrets active past the 30-day rotation SLO."
              ),
              "affected_endpoint": "HashiCorp Vault Rotation Worker",
              "affected_path": "//depot/infra/vault/rotation_worker.py",
              "leaked_fields": ["Expired Secret Rotation Logs"],
              "repro_curl": 'python3 //depot/infra/vault/rotation_worker.py --test-rotate --secret=stripe-webhook-signing-key',
              "sample_response": '{"status": "error", "error": "SSLCertVerificationError", "exit_code": 0}',
              "impact": "Unrotated static credentials violating enterprise 30-day secret rotation policy.",
              "proposed_slo": (
                  f"P2/S2 Secrets Management: Resolution required within 7 days (Target Due Date: {d_plus_6.strftime('%B %d, %Y')} 18:00 UTC)."
              ),
          },
          "comments": [
              {
                  "id": 1,
                  "number": "#1",
                  "author": "secrets-vault-audit@company.com",
                  "date": d_minus_5.strftime("%B %d, %Y 11:30 UTC"),
                  "is_internal": True,
                  "text": "Auditor detected signing key `stripe-webhook-prod` has not been rotated in 45 days despite 30-day policy.",
              },
              {
                  "id": 2,
                  "number": "#2",
                  "author": "andre_f@company.com",
                  "date": d_minus_1.strftime("%B %d, %Y 14:20 UTC"),
                  "is_internal": True,
                  "text": "Fixed exception swallowing in `rotation_worker.py` and added PagerDuty critical alerts when rotation fails (PR #4880). Manually triggered rotation successfully.",
              },
          ],
      },
  }


ISSUES = build_issues()

HOTLISTS = {
    "5829104": {
        "id": "5829104",
        "slug": "security-triage-queue",
        "name": "Security Incident Triage Queue (P1/S1)",
        "tag": "security-incident-queue",
        "owner": "security-triage@company.com",
        "description": (
            "Curated queue of active high-priority security and privacy findings"
            " requiring immediate triage review, ownership routing, and assignee"
            " follow-up."
        ),
        "issues": ["543338174", "618294710"],
    },
    "7920155": {
        "id": "7920155",
        "slug": "vulnerability-backlog",
        "name": "Enterprise Bug & Vulnerability Inventory",
        "tag": "vulnerability-backlog",
        "owner": "security-triage@company.com",
        "description": (
            "Comprehensive inventory of enterprise vulnerabilities, incidents,"
            " and bugs across all systems. Use the search bar to query and filter"
            " by status, assignee, priority, severity, component, or keyword."
        ),
        "issues": [
            "782910401",
            "543338174",
            "618294710",
            "491028472",
            "918204918",
            "920194812",
            "683920194",
            "481920194",
            "381920194",
            "849201842",
            "194820194",
            "392019482",
            "592019384",
            "739102847",
            "294810293",
            "839102948",
            "482019481",
            "519204819",
            "629104820",
            "718294019",
            "829104712",
            "938102941",
            "847291048",
            "758291043",
        ],
    },
}


def get_issue_searchable_text(issue: dict) -> str:
  """Builds a comprehensive searchable text blob containing all bug metadata, descriptions, comments, etc."""
  parts = [
      issue.get("id", ""),
      issue.get("bug_number", ""),
      issue.get("title", ""),
      issue.get("status", ""),
      issue.get("priority", ""),
      issue.get("severity", ""),
      issue.get("type", ""),
      issue.get("component", ""),
      issue.get("reporter", ""),
      issue.get("assignee_ldap", ""),
      issue.get("due_date", ""),
      issue.get("created_date", ""),
      issue.get("modified_date", ""),
  ]
  hotlists = issue.get("hotlists", [])
  if isinstance(hotlists, list):
    parts.extend(hotlists)

  desc = issue.get("description", {})
  if isinstance(desc, dict):
    parts.append(desc.get("summary", ""))
    parts.append(desc.get("affected_endpoint", ""))
    parts.append(desc.get("affected_path", ""))
    leaked = desc.get("leaked_fields", [])
    if isinstance(leaked, list):
      parts.extend(leaked)
    parts.append(desc.get("repro_curl", ""))
    parts.append(desc.get("sample_response", ""))
    parts.append(desc.get("impact", ""))
    parts.append(desc.get("proposed_slo", ""))

  comments = issue.get("comments", [])
  if isinstance(comments, list):
    for c in comments:
      if isinstance(c, dict):
        parts.append(c.get("author", ""))
        parts.append(c.get("text", ""))
        parts.append(c.get("date", ""))
        parts.append(c.get("number", ""))

  combined = " ".join(str(p) for p in parts if p)
  clean = re.sub(r"<[^>]+>", " ", combined)
  clean = re.sub(r"\s+", " ", clean).strip()
  return f"{combined} {clean}".lower()


def match_atomic_predicate(issue: dict, token: str) -> bool:
  """Evaluates a single predicate against an issue dictionary."""
  if not token:
    return True

  if ":" in token:
    parts = token.split(":", 1)
    k = parts[0].lower()
    v = parts[1].strip('"').lower()

    if k in ("status", "state"):
      status = issue["status"].lower()
      if v == "open":
        return status not in ("fixed", "verified", "closed")
      elif v in ("closed", "done"):
        return status in ("fixed", "verified", "closed")
      else:
        return v in status

    elif k in ("assignee", "owner", "user"):
      target_assignee = v.lstrip("@")
      curr_assignee = (issue.get("assignee_ldap") or "").lower()
      if target_assignee in ("none", "unassigned", "empty", "null"):
        return curr_assignee == ""
      return target_assignee in curr_assignee

    elif k in ("priority", "p"):
      target_p = v.upper()
      if not target_p.startswith("P"):
        target_p = f"P{target_p}"
      return issue["priority"].upper() == target_p

    elif k in ("severity", "s"):
      target_s = v.upper()
      if not target_s.startswith("S"):
        target_s = f"S{target_s}"
      return issue["severity"].upper() == target_s

    elif k in ("component", "comp"):
      raw_val = parts[1].strip()
      if not (raw_val.startswith('"') and raw_val.endswith('"') and len(raw_val) > 2):
        return False
      comp = issue.get("component", "").lower()
      if v == "iam":
        return (
            "iam" in comp
            or "identity" in comp
            or "access management" in comp
        )
      elif v == "infra":
        return (
            "infra" in comp
            or "infrastructure" in comp
            or "docker" in comp
            or "container" in comp
        )
      elif v == "payments":
        return (
            "payment" in comp
            or "billing" in comp
            or "financial" in comp
        )
      elif v == "privacy":
        return (
            "privacy" in comp
            or "gdpr" in comp
            or "compliance" in comp
        )
      elif v == "gateway":
        return (
            "gateway" in comp
            or "edge" in comp
            or "envoy" in comp
            or "waf" in comp
        )
      return v in comp

    elif k in ("type", "kind"):
      return v in issue.get("type", "").lower()

    elif k in ("id", "bug"):
      v_clean = v.replace("b/", "")
      return (
          v_clean in issue["id"].lower()
          or v_clean in issue["bug_number"].lower()
      )

    elif k in ("hotlist", "hl"):
      return any(v in hl.lower() for hl in issue.get("hotlists", []))

  # Free-text / phrase matching against full searchable content
  search_blob = get_issue_searchable_text(issue)
  return token.lower() in search_blob


def issue_matches_query(issue: dict, query_str: str) -> bool:
  """Evaluates if an issue matches a complex search query with AND/OR/NOT and parentheses."""
  if not query_str or not query_str.strip():
    return True

  q = query_str.strip()

  pattern = re.compile(
      r"(\(|\))|"
      r"(\bAND\b|\bOR\b|\bNOT\b|&&|\|\||!|\|)|"
      r'(\b[a-zA-Z_]+:(?:"[^"]*"|[^\s()]+))|'
      r'("[^"]+")|'
      r"([^\s()]+)"
  )

  raw_tokens = []
  for match in pattern.finditer(q):
    paren, op, kv, phrase, word = match.groups()
    if paren:
      raw_tokens.append(("PAREN", paren))
    elif op:
      op_upper = op.upper()
      if op_upper in ("AND", "&&", "&"):
        raw_tokens.append(("OP", "AND"))
      elif op_upper in ("OR", "||", "|"):
        raw_tokens.append(("OP", "OR"))
      elif op_upper in ("NOT", "!"):
        raw_tokens.append(("OP", "NOT"))
    elif kv:
      raw_tokens.append(("KV", kv))
    elif phrase:
      raw_tokens.append(("QUOTED_STRING", phrase.strip('"')))
    elif word:
      w_upper = word.upper()
      if w_upper in ("AND", "OR", "NOT"):
        raw_tokens.append(("OP", w_upper))
      else:
        raw_tokens.append(("UNQUOTED_WORD", word))

  if not raw_tokens:
    return True

  # Insert implicit AND between adjacent value tokens
  tokens = []
  for i, t in enumerate(raw_tokens):
    if i > 0:
      prev = raw_tokens[i - 1]
      prev_is_val = prev[0] in ("KV", "QUOTED_STRING", "UNQUOTED_WORD") or (
          prev[0] == "PAREN" and prev[1] == ")"
      )
      curr_is_val = (
          t[0] in ("KV", "QUOTED_STRING", "UNQUOTED_WORD")
          or (t[0] == "PAREN" and t[1] == "(")
          or (t[0] == "OP" and t[1] == "NOT")
      )
      if prev_is_val and curr_is_val:
        tokens.append(("OP", "AND"))
    tokens.append(t)

  # Shunting-yard algorithm to Postfix (RPN)
  precedence = {"NOT": 3, "AND": 2, "OR": 1}
  output_queue = []
  op_stack = []

  for t_type, t_val in tokens:
    if t_type in ("KV", "QUOTED_STRING", "UNQUOTED_WORD"):
      output_queue.append((t_type, t_val))
    elif t_type == "OP":
      while (
          op_stack
          and op_stack[-1][0] == "OP"
          and precedence.get(op_stack[-1][1], 0) >= precedence.get(t_val, 0)
      ):
        output_queue.append(op_stack.pop())
      op_stack.append((t_type, t_val))
    elif t_type == "PAREN":
      if t_val == "(":
        op_stack.append((t_type, t_val))
      elif t_val == ")":
        while op_stack and op_stack[-1] != ("PAREN", "("):
          output_queue.append(op_stack.pop())
        if op_stack and op_stack[-1] == ("PAREN", "("):
          op_stack.pop()

  while op_stack:
    op = op_stack.pop()
    if op[0] == "OP":
      output_queue.append(op)

  # Evaluate Postfix (RPN)
  eval_stack = []
  for item_type, item_val in output_queue:
    if item_type == "KV":
      eval_stack.append(match_atomic_predicate(issue, item_val))
    elif item_type == "QUOTED_STRING":
      search_blob = get_issue_searchable_text(issue)
      eval_stack.append(item_val.lower() in search_blob)
    elif item_type == "UNQUOTED_WORD":
      eval_stack.append(False)
    elif item_type == "OP":
      if item_val == "NOT":
        val = eval_stack.pop() if eval_stack else False
        eval_stack.append(not val)
      elif item_val == "AND":
        b = eval_stack.pop() if eval_stack else False
        a = eval_stack.pop() if eval_stack else False
        eval_stack.append(a and b)
      elif item_val == "OR":
        b = eval_stack.pop() if eval_stack else False
        a = eval_stack.pop() if eval_stack else False
        eval_stack.append(a or b)

  return eval_stack[-1] if eval_stack else True


def parse_query_tokens(query_str: str):
  """Legacy compatibility helper."""
  return {"raw_query": query_str}


def get_hotlist(hotlist_id: str = "5829104"):
  return HOTLISTS.get(str(hotlist_id), HOTLISTS["5829104"])


def get_issue(issue_id: str):
  return ISSUES.get(str(issue_id), ISSUES.get("543338174"))


def get_filtered_issues(hotlist_id: str = None, query_str: str = ""):
  if hotlist_id and hotlist_id in HOTLISTS:
    issue_ids = HOTLISTS[hotlist_id]["issues"]
    target_pool = [get_issue(i) for i in issue_ids if i in ISSUES]
  else:
    target_pool = list(ISSUES.values())

  matched = [issue for issue in target_pool if issue_matches_query(issue, query_str)]
  return matched


def render_comments_html(comments: list) -> str:
  cards = []
  for c in comments:
    body_text = c["text"].replace("\n", "<br>")
    raw_author = c["author"].split("@")[0].split("(")[0].strip()
    initials = "".join([part[0].upper() for part in raw_author.split()[:2]])
    if not initials:
      initials = raw_author[:2].upper()

    card = f"""
    <div class="bug-card comment-card">
        <div class="card-header">
            <div class="reporter-info">
                <div class="avatar">{initials}</div>
                <div class="reporter-details">
                    <span class="reporter-name"><strong>{html.escape(c['author'])}</strong></span>
                    <span class="report-date">{c.get('number', '')} &bull; commented on {html.escape(c['date'])}</span>
                </div>
            </div>
            <div class="card-actions">
                <i class="material-icons">reply</i>
                <i class="material-icons">more_vert</i>
            </div>
        </div>
        <div class="card-body description-content">
            {body_text}
        </div>
    </div>
    """
    cards.append(card)
  return "\n".join(cards)


def render_hotlist_html(hotlist_id: str = "5829104", query_str: str = "") -> str:
  """Renders the Buganizer Hotlist HTML with search and filtering capabilities."""
  template_path = os.path.join(TEMPLATE_DIR, "hotlist.html")
  with open(template_path, "r", encoding="utf-8") as f:
    html_content = f.read()

  hl = get_hotlist(hotlist_id)
  hotlist_issues = [get_issue(i) for i in hl["issues"] if i in ISSUES]
  matched_issues = [i for i in hotlist_issues if issue_matches_query(i, query_str)]

  html_content = html_content.replace("{{hotlist_id}}", hl["id"])
  html_content = html_content.replace("{{hotlist_name}}", hl["name"])
  html_content = html_content.replace("{{hotlist_desc}}", hl["description"])
  html_content = html_content.replace("{{hotlist_owner}}", hl["owner"])
  html_content = html_content.replace("{{total_issues}}", str(len(hl["issues"])))
  html_content = html_content.replace("{{matching_count}}", str(len(matched_issues)))
  html_content = html_content.replace("{{current_query}}", html.escape(query_str))
  html_content = html_content.replace(
      "{{clear_btn_display}}", "inline-flex" if query_str else "none"
  )

  # Nav tabs active state
  tab_queue_class = "active" if hl["id"] == "5829104" else ""
  tab_backlog_class = "active" if hl["id"] == "7920155" else ""
  html_content = html_content.replace("{{tab_queue_active}}", tab_queue_class)
  html_content = html_content.replace("{{tab_backlog_active}}", tab_backlog_class)

  rows = []
  for issue in hotlist_issues:
    is_match = issue in matched_issues
    row_style = "" if is_match else 'style="display: none;"'
    assignee_display = (
        f"@{issue['assignee_ldap']}"
        if issue.get("assignee_ldap")
        else "<span class='assignee-chip unassigned'>Unassigned</span>"
    )
    endpoint = issue["description"].get("affected_endpoint", "")
    p_class = f"priority-{issue['priority'].lower()}"
    s_class = f"severity-{issue['severity'].lower()}"
    status_class = f"status-{issue['status'].lower()}"
    searchable_blob = get_issue_searchable_text(issue)
    hotlists_str = " ".join(issue.get("hotlists", []))

    row = f"""
        <tr {row_style} data-id="{issue['id']}" data-status="{issue['status'].lower()}" data-assignee="{(issue.get('assignee_ldap') or 'unassigned').lower()}" data-priority="{issue['priority'].lower()}" data-severity="{issue['severity'].lower()}" data-component="{html.escape(issue.get('component', '').lower())}" data-type="{html.escape(issue.get('type', '').lower())}" data-hotlists="{html.escape(hotlists_str.lower())}" data-search="{html.escape(searchable_blob)}">
            <td><input type="checkbox"></td>
            <td>
                <a href="/issues/{issue['id']}" class="bug-link">
                    <i class="material-icons" style="font-size: 15px;">bug_report</i>
                    <span>{issue['bug_number']}</span>
                </a>
            </td>
            <td><span class="select-mock {p_class}" style="min-width: 45px; height: 24px; padding: 2px 6px;">{issue['priority']}</span></td>
            <td><span class="select-mock {s_class}" style="min-width: 45px; height: 24px; padding: 2px 6px;">{issue['severity']}</span></td>
            <td><span class="status-chip {status_class}">{issue['status']}</span></td>
            <td>
                <a href="/issues/{issue['id']}" class="bug-row-title">{html.escape(issue['title'])}</a>
                <div style="margin-top: 3px; display: flex; align-items: center; gap: 6px; flex-wrap: wrap;">
                    <span class="component-chip-inline"><i class="material-icons" style="font-size: 11px;">category</i> {html.escape(issue.get('component', 'Security'))}</span>
                    <span class="bug-row-endpoint">{endpoint}</span>
                </div>
            </td>
            <td><span class="assignee-chip">{assignee_display}</span></td>
            <td style="color: #5f6368; font-size: 12px;">{issue['modified_date']}</td>
        </tr>
        """
    rows.append(row)

  no_results_style = "" if not matched_issues else 'style="display: none;"'
  no_results_row = f"""
        <tr id="noResultsRow" {no_results_style}>
            <td colspan="8" style="text-align: center; padding: 40px; color: #5f6368;">
                <i class="material-icons" style="font-size: 36px; color: #9aa0a6; display: block; margin-bottom: 8px;">search_off</i>
                <strong>No bugs found matching your query criteria.</strong><br>
                <span style="font-size: 13px;">Try refining your search terms or clearing the filter query.</span>
            </td>
        </tr>
  """
  rows.append(no_results_row)

  html_content = html_content.replace("{{issues_table_rows}}", "\n".join(rows))
  return html_content


def render_issue_html(issue_id: str = "543338174") -> str:
  """Renders Buganizer UI HTML for a given issue ID."""
  template_path = os.path.join(TEMPLATE_DIR, "buganizer.html")
  with open(template_path, "r", encoding="utf-8") as f:
    html_content = f.read()

  issue = get_issue(issue_id)

  comments_html = render_comments_html(issue.get("comments", []))
  html_content = html_content.replace("{{comments_html}}", comments_html)
  html_content = html_content.replace("{{bug_id}}", issue["id"])
  html_content = html_content.replace("{{bug_number}}", issue["bug_number"])
  html_content = html_content.replace("{{title}}", issue["title"])
  html_content = html_content.replace("{{type}}", html.escape(issue.get("type", "Vulnerability")))
  html_content = html_content.replace("{{status}}", issue["status"])
  html_content = html_content.replace("{{priority}}", issue["priority"])
  html_content = html_content.replace("{{severity}}", issue["severity"])
  html_content = html_content.replace(
      "{{assignee_ldap}}", issue.get("assignee_ldap", "")
  )
  html_content = html_content.replace(
      "{{due_date}}", issue.get("due_date", "")
  )
  html_content = html_content.replace(
      "{{due_date_class}}", issue.get("due_date_class", "")
  )
  html_content = html_content.replace(
      "{{modified_date}}", issue["modified_date"]
  )
  html_content = html_content.replace(
      "{{created_date}}", issue["created_date"]
  )
  html_content = html_content.replace(
      "{{reporter}}", html.escape(issue.get("reporter", "security-triage@company.com"))
  )
  html_content = html_content.replace(
      "{{component}}", html.escape(issue.get("component", "Security"))
  )

  desc = issue.get("description", {})
  html_content = html_content.replace("{{desc_summary}}", desc.get("summary", ""))
  html_content = html_content.replace(
      "{{desc_endpoint}}", desc.get("affected_endpoint", "N/A")
  )
  html_content = html_content.replace("{{desc_path}}", desc.get("affected_path", "N/A"))
  html_content = html_content.replace(
      "{{desc_leaked_fields}}",
      "".join([f"<li>{f}</li>" for f in desc.get("leaked_fields", [])]),
  )
  html_content = html_content.replace(
      "{{desc_repro}}", html.escape(desc.get("repro_curl", "N/A"))
  )
  html_content = html_content.replace(
      "{{desc_sample_resp}}", html.escape(desc.get("sample_response", "{}"))
  )
  html_content = html_content.replace("{{desc_impact}}", desc.get("impact", ""))
  html_content = html_content.replace(
      "{{desc_slo}}",
      desc.get("proposed_slo", "Resolution target: Within 48 hours."),
  )

  # Active Tab Highlighting
  tab_543_class = "active-tab" if issue["id"] == "543338174" else ""
  tab_618_class = "active-tab" if issue["id"] == "618294710" else ""
  html_content = html_content.replace("{{tab_543_class}}", tab_543_class)
  html_content = html_content.replace("{{tab_618_class}}", tab_618_class)

  return html_content


def get_hotlist_json(hotlist_id: str = "5829104", query_str: str = ""):
  hl = get_hotlist(hotlist_id)
  matched = get_filtered_issues(hotlist_id, query_str)
  return {
      "metadata": hl,
      "query": query_str,
      "total_count": len(hl["issues"]),
      "matching_count": len(matched),
      "issues": matched,
  }


def get_all_issues_json(query_str: str = ""):
  matched = get_filtered_issues(None, query_str)
  return {
      "query": query_str,
      "total_count": len(ISSUES),
      "matching_count": len(matched),
      "issues": matched,
  }


def get_issue_json(issue_id: str):
  return get_issue(issue_id)


def add_comment_to_issue(
    issue_id: str, author: str, text: str, is_internal: bool = True
):
  issue = get_issue(issue_id)
  now_str = datetime.utcnow().strftime("%B %d, %Y %H:%M UTC")
  new_comment = {
      "id": len(issue.get("comments", [])) + 1,
      "number": f"#{len(issue.get('comments', [])) + 1}",
      "author": author or "security-triage@company.com",
      "date": now_str,
      "is_internal": is_internal,
      "text": text.strip(),
  }
  if "comments" not in issue:
    issue["comments"] = []
  issue["comments"].append(new_comment)
  issue["modified_date"] = now_str
  return {
      "success": True,
      "comment": new_comment,
      "total_comments": len(issue["comments"]),
  }


def assign_issue(issue_id: str, assignee_ldap: str):
  issue = get_issue(issue_id)
  assignee = assignee_ldap.strip().lstrip("@")
  issue["assignee_ldap"] = assignee
  issue["status"] = "Assigned"
  now_str = datetime.utcnow().strftime("%B %d, %Y %H:%M UTC")
  issue["modified_date"] = now_str
  return {
      "success": True,
      "bug_id": issue["id"],
      "bug_number": issue["bug_number"],
      "assignee_ldap": assignee,
      "status": "Assigned",
  }

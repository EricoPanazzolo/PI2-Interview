import html
import json
import os

from apps.team_directory.data import get_all_teams
from apps.team_directory.data import get_team_by_id
from apps.team_directory.data import resolve_ownership
from apps.team_directory.data import search_teams

APP_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(APP_DIR, "templates")


def _initials(name: str) -> str:
  return "".join(part[0].upper() for part in name.split()[:2])


def render_team_cards_html(teams: list) -> str:
  """Builds the HTML cards for the team directory view."""
  cards = []
  for t in teams:
    # Build members list
    member_chips = []
    for m in t["members"]:
      member_chips.append(
          f'<span class="code-chip" title="{html.escape(m["name"])} -'
          f' {html.escape(m["focus"])}">{html.escape(m["ldap"])}</span>'
      )
    members_html = " ".join(member_chips)

    # Build paths list
    paths_html = "".join([
        f'<span class="code-chip">{html.escape(p)}</span>'
        for p in t["owned_paths"]
    ])

    # Build endpoints list
    endpoints_html = "".join([
        f'<span class="endpoint-chip">{html.escape(ep)}</span>'
        for ep in t["owned_endpoints"]
    ])

    # Build components list
    components_html = "".join([
        f'<span class="component-chip"><i class="material-icons">category</i>{html.escape(c)}</span>'
        for c in t.get("owned_components", [])
    ])

    # Build key personnel rows
    people = [
        ("tl", "Tech Lead (TL)", t["tl_ldap"], t["tl_name"]),
        ("oncall", "Primary On-Call", t["primary_oncall_ldap"], t["primary_oncall_name"]),
        ("secondary", "Secondary On-Call", t["secondary_oncall_ldap"], t["secondary_oncall_name"]),
    ]
    people_html = "".join([
        f"""
                    <li class="person-row {role}">
                        <span class="person-avatar">{html.escape(_initials(name))}</span>
                        <div class="person-main">
                            <span class="ldap-link">@{html.escape(ldap)}</span>
                            <span class="person-name">{html.escape(name)}</span>
                        </div>
                        <span class="role-badge {role}">{label}</span>
                    </li>"""
        for role, label, ldap, name in people
    ])

    card = f"""
    <article class="team-card" data-id="{html.escape(t['id'])}" data-department="{html.escape(t['department'])}" data-component="{html.escape(t.get('broad_component', ''))}">
        <div class="card-top">
            <div class="card-title-group">
                <h3>{html.escape(t['name'])}</h3>
                <div class="department-label">{html.escape(t['department'])}</div>
            </div>
            <span class="tag-badge">{html.escape(t['tag'])}</span>
        </div>
        <div class="card-body">
            <p class="description-text">{html.escape(t['description'])}</p>

            <div>
                <div class="section-subheading">Key Personnel &amp; On-Call Rotation</div>
                <ul class="people-list">{people_html}
                </ul>
            </div>

            <div>
                <div class="section-subheading">Broad Component ID &amp; Owned Issue Tracker Components</div>
                <div class="chips-container">
                    <span class="filter-chip"><i class="material-icons">filter_alt</i>component:&quot;{html.escape(t.get('broad_component', ''))}&quot;</span>
                    {components_html}
                </div>
            </div>

            <div>
                <div class="section-subheading">Team Member LDAPs</div>
                <div class="chips-container">
                    {members_html}
                </div>
            </div>

            <div>
                <div class="section-subheading">Owned Code Paths (Piper / Depot)</div>
                <div class="chips-container">
                    {paths_html}
                </div>
            </div>

            <div>
                <div class="section-subheading">Owned Endpoints &amp; Subsystems</div>
                <div class="chips-container">
                    {endpoints_html}
                </div>
            </div>

            <div class="triage-tip">
                <i class="material-icons">lightbulb</i>
                <div><strong>Triage Routing:</strong> {html.escape(t['triage_guidelines'])}</div>
            </div>
        </div>
        <div class="card-footer">
            <span class="contact-info">
                <i class="material-icons">email</i> {html.escape(t['email'])}
            </span>
            <span class="contact-info">
                <i class="material-icons">chat</i> {html.escape(t['chat_channel'])}
            </span>
        </div>
    </article>
    """
    cards.append(card)

  return "\n".join(cards)


def render_team_directory_html() -> str:
  """Serves the interactive Team & Ownership Directory page."""
  template_path = os.path.join(TEMPLATE_DIR, "team_directory.html")
  with open(template_path, "r", encoding="utf-8") as f:
    html_content = f.read()
  teams = get_all_teams()
  cards_html = render_team_cards_html(teams)
  html_content = html_content.replace("{{team_cards_html}}", cards_html)
  html_content = html_content.replace("{{team_count}}", str(len(teams)))
  return html_content


def get_teams_json():
  return get_all_teams()


def get_team_detail_json(team_id: str):
  team = get_team_by_id(team_id)
  if not team:
    return {"error": f"Team '{team_id}' not found"}
  return team


def search_teams_json(query: str):
  results = search_teams(query)
  return {"query": query, "count": len(results), "teams": results}


def resolve_ownership_json(path_or_endpoint: str):
  matched_team = resolve_ownership(path_or_endpoint)
  if matched_team:
    return {
        "matched": True,
        "query": path_or_endpoint,
        "team": matched_team,
        "broad_component": matched_team.get("broad_component", ""),
        "broad_component_filter": f'component:"{matched_team.get("broad_component", "")}"',
        "suggested_assignee_ldap": matched_team["primary_oncall_ldap"],
        "suggested_assignee_name": matched_team["primary_oncall_name"],
        "tech_lead_ldap": matched_team["tl_ldap"],
        "escalation_alias": matched_team["email"],
    }
  else:
    return {
        "matched": False,
        "query": path_or_endpoint,
        "message": "No direct ownership match found",
    }

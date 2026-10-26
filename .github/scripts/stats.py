"""Render a black-and-gold contribution stats card for the profile README.

Usage: GITHUB_TOKEN=... PROFILE_LOGIN=... python3 stats.py <output.svg>
Reads the public contribution calendar of the last year through the GitHub
GraphQL API and draws the totals, streaks and a weekly bar chart. Only the
standard library is used, so it runs on a bare GitHub Actions runner.
"""
import datetime as dt
import json
import os
import sys
import urllib.request

FONT = "'Segoe UI', Ubuntu, 'Helvetica Neue', Helvetica, Arial, sans-serif"
GOLD, GOLD_LIGHT, GOLD_DARK = "#d9b44a", "#f2dfa0", "#6e5410"
INK, MUTED = "#0d0d0f", "#c9c3b5"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def fetch(login: str, token: str) -> dict:
    body = json.dumps({"query": QUERY, "variables": {"login": login}}).encode()
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def streaks(days: list[tuple[dt.date, int]]) -> tuple[int, int]:
    longest = run = 0
    for _, count in days:
        run = run + 1 if count > 0 else 0
        longest = max(longest, run)
    # The current streak may end yesterday: today often has no commits yet.
    current = 0
    for index, (_, count) in enumerate(reversed(days)):
        if count > 0:
            current += 1
        elif index == 0:
            continue
        else:
            break
    return current, longest


def render(calendar: dict) -> str:
    days = [
        (dt.date.fromisoformat(day["date"]), day["contributionCount"])
        for week in calendar["weeks"]
        for day in week["contributionDays"]
    ]
    total = calendar["totalContributions"]
    current, longest = streaks(days)
    active = sum(1 for _, count in days if count > 0)
    best_day, best_count = max(days, key=lambda item: item[1])
    weekly = [sum(day["contributionCount"] for day in week["contributionDays"]) for week in calendar["weeks"]]
    peak = max(weekly) or 1

    metrics = [
        (f"{total:,}", "contributions this year"),
        (f"{current}", "day streak right now"),
        (f"{longest}", "longest streak (days)"),
        (f"{active}", "active days"),
        (f"{best_count}", f"best day ({best_day:%b %-d})"),
    ]
    cells = "".join(
        f'<text x="{40 + i * 228}" y="66" class="n">{number}</text>'
        f'<text x="{40 + i * 228}" y="94" class="l">{label}</text>'
        for i, (number, label) in enumerate(metrics)
    )
    bar_width = 1120 / len(weekly)
    bars = "".join(
        f'<rect x="{40 + i * bar_width:.1f}" y="{230 - 90 * value / peak:.1f}" width="{bar_width - 3:.1f}" '
        f'height="{max(2, 90 * value / peak):.1f}" rx="2" fill="{GOLD if value < peak else GOLD_LIGHT}" '
        f'opacity="{0.35 + 0.65 * value / peak:.2f}"/>'
        for i, value in enumerate(weekly)
    )
    updated = dt.date.today().isoformat()
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 270" width="1200" height="270" role="img" aria-label="{total:,} contributions this year, {current}-day streak, longest streak {longest} days">
  <defs><style>
    .n {{ font: 800 36px {FONT}; fill: {GOLD_LIGHT}; }}
    .l {{ font: 400 15px {FONT}; fill: {MUTED}; }}
    .s {{ font: 400 12px {FONT}; fill: {MUTED}; opacity: .7; }}
    .run {{ stroke-dasharray: 140 2800; animation: run 8s linear infinite; }}
    @keyframes run {{ to {{ stroke-dashoffset: -2940; }} }}
  </style></defs>
  <rect width="1200" height="270" rx="20" fill="{INK}"/>
  <rect x=".5" y=".5" width="1199" height="269" rx="19.5" fill="none" stroke="{GOLD_DARK}"/>
  <rect x="1" y="1" width="1198" height="268" rx="19" fill="none" stroke="{GOLD}" stroke-width="2" class="run"/>
  {cells}
  {bars}
  <text x="1160" y="254" text-anchor="end" class="s">contributions per week, last 12 months · updated {updated}</text>
</svg>
"""


if __name__ == "__main__":
    calendar = fetch(os.environ["PROFILE_LOGIN"], os.environ["GITHUB_TOKEN"])
    pathlib_out = sys.argv[1]
    with open(pathlib_out, "w", encoding="utf-8") as handle:
        handle.write(render(calendar))
    print(f"wrote {pathlib_out}: {calendar['totalContributions']} contributions")

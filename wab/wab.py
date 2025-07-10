import requests
from bs4 import BeautifulSoup
from rich.console import Console

console = Console()

def get_laliga_table(season: int):
    url = f"https://www.transfermarkt.com/laliga/tabelle/wettbewerb/ES1?saison_id={season}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    table = soup.find("table", {"class": "items"})
    if not table:
        console.print("[❌] 순위표 테이블을 찾을 수 없습니다.", style="bold red")
        return

    console.print(f"[⚽] 라리가 {season}-{season+1} 시즌 순위표\n", style="bold cyan")

    for row in table.select("tbody tr"):
        cols = row.select("td")
        if len(cols) < 8:
            continue

        pos = cols[0].get_text(strip=True)
        team = cols[1].get_text(strip=True)
        played = cols[2].get_text(strip=True)
        win = cols[3].get_text(strip=True)
        draw = cols[4].get_text(strip=True)
        loss = cols[5].get_text(strip=True)
        goals = cols[6].get_text(strip=True)
        pts = cols[7].get_text(strip=True)

        console.print(
            f"{pos}위 | {team} | {played}경기 {win}승 {draw}무 {loss}패 | 득실: {goals} | 승점: {pts}"
        )

if __name__ == "__main__":
    try:
        season_input = int(input("원하는 시즌 연도(예: 2023)를 입력하세요: "))
        get_laliga_table(season=season_input)
    except ValueError:
        console.print("[❌] 잘못된 입력입니다. 숫자만 입력해주세요.", style="bold red")

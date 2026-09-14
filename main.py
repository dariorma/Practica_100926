import pandas as pd
df = pd.read_csv('games.csv')
df = df.dropna(subset=['PTS_home', 'PTS_away'])

df['TOTAL_POINTS'] = df['PTS_home'] + df['PTS_away']
df['POINT_DIFF'] = abs(df['PTS_home'] - df['PTS_away'])
df['GAME_DATE'] = df['GAME_DATE_EST']
df['HOME_TEAM'] = df['HOME_TEAM_ID']
df['HOME_PTS'] = df['PTS_home']
df['AWAY_TEAM'] = df['VISITOR_TEAM_ID']
df['AWAY_PTS'] = df['PTS_away']

games = df.to_dict('records')
sample = games[:1000] 

def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][key] < arr[j + 1][key]: # descendente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

palizas = bubble_sort(sample, "POINT_DIFF")

print("\nTop 10 mayores palizas")
pos = 1
for g in palizas[:10]:
    print(f"{pos}.  {g['HOME_TEAM']} ({int(g['HOME_PTS'])}) vs {g['AWAY_TEAM']} ({int(g['AWAY_PTS'])}) - Dif: {int(g['POINT_DIFF'])} puntos")
    pos += 1
import requests
import pandas as pd

def display_hormuz_10_weeks_summary():
    # 1. API Configuration
    base_url = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query"
    
    # 2. Query Parameters (Hormuz: chokepoint6)
    params = {
        'where': "portid = 'chokepoint6'", 
        'outFields': 'date, n_total', 
        'orderByFields': 'date DESC',
        'resultRecordCount': 200, # Sufficient to get at least 10 weeks
        'f': 'json'
    }
    
    try:
        print("📡 Requesting Strait of Hormuz Transit Data...")
        res = requests.get(base_url, params=params)
        res.raise_for_status()
        data = res.json()
        
        features = data.get('features', [])
        if not features:
            print("❌ No data found.")
            return

        # 3. Data Parsing
        rows = [f['attributes'] for f in features]
        df = pd.DataFrame(rows)
        
        # Convert timestamp to datetime
        df['date'] = pd.to_datetime(df['date'], unit='ms').dt.date
        # ISO Week Grouping
        df['week_group'] = df.apply(lambda x: x['date'].strftime('%G-W%V'), axis=1)

        print("\n" + "="*45)
        print("📊 Strait of Hormuz: Last 10 Weeks Summary")
        print("="*45)

        # 4. Filter for only the last 10 unique weeks
        unique_weeks = sorted(df['week_group'].unique(), reverse=True)[:10]

        for week in unique_weeks:
            week_data = df[df['week_group'] == week].sort_values(by='date', ascending=False)
            
            start_date = week_data['date'].min()
            end_date = week_data['date'].max()
            weekly_sum = week_data['n_total'].sum()

            print(f"\n[Week: {week}] ({start_date} ~ {end_date})")
            print("-" * 45)
            print(week_data[['date', 'n_total']].to_string(index=False))
            print("-" * 45)
            print(f"✅ Weekly Total: {int(weekly_sum)} vessels")
            
        print("\n" + "="*45)

    except Exception as e:
        print(f"⚠️ Error occurred: {e}")

if __name__ == "__main__":
    display_hormuz_10_weeks_summary()

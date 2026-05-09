import streamlit as st
import requests
import pandas as pd

# Page configuration
st.set_page_config(page_title="Hormuz Strait Tracker", page_icon="🚢")

def display_hormuz_summary():
    # 1. API Configuration
    base_url = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query"
    
    params = {
        'where': "portid = 'chokepoint6'", 
        'outFields': 'date, n_total', 
        'orderByFields': 'date DESC',
        'resultRecordCount': 200,
        'f': 'json'
    }
    
    st.title("🚢 Strait of Hormuz Transit Tracker")
    st.write("Fetching real-time maritime data from ArcGIS...")

    try:
        res = requests.get(base_url, params=params)
        res.raise_for_status()
        data = res.json()
        
        features = data.get('features', [])
        if not features:
            st.warning("❌ No data found.")
            return

        # 2. Data Parsing
        rows = [f['attributes'] for f in features]
        df = pd.DataFrame(rows)
        
        # Convert timestamp to datetime
        df['date'] = pd.to_datetime(df['date'], unit='ms').dt.date
        df['week_group'] = df.apply(lambda x: x['date'].strftime('%G-W%V'), axis=1)

        # 3. Filter for only the last 10 unique weeks
        unique_weeks = sorted(df['week_group'].unique(), reverse=True)[:10]

        # 4. Streamlit UI Layout
        st.divider()
        st.subheader("📊 Last 10 Weeks Summary")

        for week in unique_weeks:
            week_data = df[df['week_group'] == week].sort_values(by='date', ascending=False)
            
            start_date = week_data['date'].min()
            end_date = week_data['date'].max()
            weekly_sum = week_data['n_total'].sum()

            with st.expander(f"📅 Week: {week} ({start_date} ~ {end_date})"):
                st.write(f"**Weekly Total: {int(weekly_sum)} vessels**")
                # Table display
                st.dataframe(week_data[['date', 'n_total']], use_container_width=True)
                
    except Exception as e:
        st.error(f"⚠️ Error occurred: {e}")

if __name__ == "__main__":
    display_hormuz_summary()

import pandas as pd

# Load sample threat data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"✅ Loaded {len(data)} threat entries.")
        return data
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return pd.DataFrame()

# Display basic stats
def show_summary(data):
    print("\n📊 Cyber Threat Summary")
    print(f"- Total Entries: {len(data)}")
    print(f"- Unique Threat Types: {data['threat_type'].nunique()}")
    print(f"- Date Range: {data['date'].min()} to {data['date'].max()}")

# Entry point
if __name__ == "__main__":
    file_path = "../data/sample_threats.csv"
    threat_data = load_data(file_path)

    if not threat_data.empty:
        show_summary(threat_data)

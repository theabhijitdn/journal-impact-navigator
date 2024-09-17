import streamlit as st
import pandas as pd

# Load data with caching
@st.cache_data
def load_data():
  data = pd.read_csv('combined_final.csv')
  # Convert the 'IF' column to numeric, coercing errors to NaN
  data['IF'] = pd.to_numeric(data['IF'], errors='coerce')
  return data

data = load_data()

# Title
st.title('Journal Impact Navigator')

# Sidebar filters
st.sidebar.header('Filter Options')

# Initialize session state for filters
if 'if_min' not in st.session_state:
  st.session_state['if_min'] = float(data['IF'].min())
if 'if_max' not in st.session_state:
  st.session_state['if_max'] = float(data['IF'].max())
if 'quartile_filter' not in st.session_state:
  st.session_state['quartile_filter'] = []
if 'publisher_filter' not in st.session_state:
  st.session_state['publisher_filter'] = []
if 'category_filter' not in st.session_state:
  st.session_state['category_filter'] = []
if 'region_filter' not in st.session_state:
  st.session_state['region_filter'] = []
if 'country_filter' not in st.session_state:
  st.session_state['country_filter'] = []

# Filter by Impact Factor (IF) range
if_min, if_max = st.sidebar.slider(
  'Impact Factor Range',
  min_value=float(data['IF'].min()),
  max_value=float(data['IF'].max()),
  value=(st.session_state['if_min'], st.session_state['if_max'])
)

# Filter by Quartile
quartile_filter = st.sidebar.multiselect('Quartile', data['Q'].unique(), default=st.session_state['quartile_filter'])

# Filter by Publisher
publisher_filter = st.sidebar.multiselect('Publisher', data['Publisher'].unique(), default=st.session_state['publisher_filter'])

# Filter by Category
category_filter = st.sidebar.multiselect('Category', data['Category'].unique(), default=st.session_state['category_filter'])

# Filter by Region
region_filter = st.sidebar.multiselect('Region', data['Region'].unique(), default=st.session_state['region_filter'])

# Filter by Country
country_filter = st.sidebar.multiselect('Country', data['Country'].unique(), default=st.session_state['country_filter'])

# Apply filters
filtered_data = data[
  (data['IF'] >= if_min) & (data['IF'] <= if_max) &
  (data['Q'].isin(quartile_filter) if quartile_filter else True) &
  (data['Publisher'].isin(publisher_filter) if publisher_filter else True) &
  (data['Category'].isin(category_filter) if category_filter else True) &
  (data['Region'].isin(region_filter) if region_filter else True) &
  (data['Country'].isin(country_filter) if country_filter else True)
]

# Display filtered data with full width
st.write('Filtered Data:')
st.dataframe(filtered_data, use_container_width=True)

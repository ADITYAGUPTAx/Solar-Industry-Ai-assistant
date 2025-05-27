import streamlit as st
import requests
import json
from PIL import Image
import io
import base64
import numpy as np

# Placeholder for OpenRouter API key (replace with actual key or environment variable)
OPENROUTER_API_KEY = "your-openrouter-api-key"
API_URL = "https://api.openrouter.ai/v1/analyze"  # Hypothetical endpoint

# Sample solar data (replace with real data source or API)
SOLAR_IRRADIANCE = 5.0  # kWh/m²/day (average for sample location)
PANEL_EFFICIENCY = 0.2  # 20% efficiency
PANEL_COST_PER_WATT = 0.8  # $0.8/W
INSTALLATION_COST = 5000  # Fixed cost in $
INCENTIVE_RATE = 0.3  # 30% tax credit
ELECTRICITY_RATE = 0.15  # $0.15/kWh

def analyze_image(image):
    """Analyze satellite image using vision AI API."""
    try:
        # Convert image to base64
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        # Prepare API request
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "image": img_str,
            "prompt": "Analyze this satellite image of a rooftop. Provide: area (m²), orientation (degrees), shading (%), and obstructions (yes/no)."
        }

        # Make API call (mock response for demo)
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            return {
                "area": result.get("area", 100),  # Default 100 m²
                "orientation": result.get("orientation", 180),  # South-facing
                "shading": result.get("shading", 10),  # 10% shading
                "obstructions": result.get("obstructions", "no")
            }
        else:
            st.error("Error analyzing image. Using default values.")
            return {"area": 100, "orientation": 180, "shading": 10, "obstructions": "no"}
    except Exception as e:
        st.error(f"Error: {str(e)}. Using default values.")
        return {"area": 100, "orientation": 180, "shading": 10, "obstructions": "no"}

def calculate_solar_potential(area, shading):
    """Calculate solar potential based on rooftop area and shading."""
    effective_area = area * (1 - shading / 100)
    daily_output = effective_area * SOLAR_IRRADIANCE * PANEL_EFFICIENCY  # kWh/day
    annual_output = daily_output * 365  # kWh/year
    return annual_output

def calculate_roi(annual_output, area):
    """Calculate ROI and payback period."""
    system_size = area * PANEL_EFFICIENCY * 1000  # Watts
    total_cost = system_size * PANEL_COST_PER_WATT + INSTALLATION_COST
    incentives = total_cost * INCENTIVE_RATE
    net_cost = total_cost - incentives
    annual_savings = annual_output * ELECTRICITY_RATE
    payback_period = net_cost / annual_savings if annual_savings > 0 else float('inf')
    return {
        "system_size": system_size / 1000,  # kW
        "total_cost": total_cost,
        "incentives": incentives,
        "net_cost": net_cost,
        "annual_savings": annual_savings,
        "payback_period": payback_period
    }

# Streamlit app
st.title("Solar Industry AI Assistant")
st.write("Upload a satellite image of a rooftop to assess solar installation potential.")

uploaded_file = st.file_uploader("Choose a satellite image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Rooftop Image", use_column_width=True)

    with st.spinner("Analyzing image..."):
        analysis = analyze_image(image)
        st.subheader("Rooftop Analysis")
        st.write(f"**Area**: {analysis['area']} m²")
        st.write(f"**Orientation**: {analysis['orientation']}° (South = 180°)")
        st.write(f"**Shading**: {analysis['shading']}%")
        st.write(f"**Obstructions**: {analysis['obstructions']}")

        if analysis["obstructions"] == "yes":
            st.warning("Obstructions detected. Manual inspection recommended.")
        
        annual_output = calculate_solar_potential(analysis["area"], analysis["shading"])
        roi = calculate_roi(annual_output, analysis["area"])

        st.subheader("Solar Potential")
        st.write(f"**Annual Energy Output**: {annual_output:.2f} kWh")
        st.write(f"**System Size**: {roi['system_size']:.2f} kW")
        st.write(f"**Total Cost**: ${roi['total_cost']:.2f}")
        st.write(f"**Incentives**: ${roi['incentives']:.2f}")
        st.write(f"**Net Cost**: ${roi['net_cost']:.2f}")
        st.write(f"**Annual Savings**: ${roi['annual_savings']:.2f}")
        st.write(f"**Payback Period**: {roi['payback_period']:.1f} years")

        st.subheader("Recommendations")
        if analysis["shading"] > 20:
            st.write("- Consider shading mitigation (e.g., tree trimming).")
        if roi["payback_period"] > 10:
            st.write("- Evaluate local incentives for better ROI.")
        st.write("- Consult a professional for permitting and installation.")
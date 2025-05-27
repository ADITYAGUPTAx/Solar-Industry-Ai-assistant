# Solar Industry AI Assistant

## Overview
This project is an AI-powered rooftop analysis tool designed to assess solar installation potential using satellite imagery. It integrates vision AI for image analysis, calculates solar potential, and provides ROI estimates for homeowners and solar professionals.

## Features
- **Image Analysis**: Uses vision AI to extract rooftop area, orientation, shading, and obstructions.
- **Solar Potential**: Calculates annual energy output based on rooftop characteristics and solar irradiance.
- **ROI Analysis**: Estimates system size, costs, incentives, savings, and payback period.
- **User Interface**: Streamlit-based web app for easy image upload and result visualization.

## Setup Instructions
### Prerequisites
- Python 3.8+
- Streamlit
- PIL (Pillow)
- Requests
- OpenRouter API key (for vision AI, replace placeholder in code)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/solar-ai-assistant.git
   cd solar-ai-assistant
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install streamlit pillow requests
   ```
4. Set up OpenRouter API key:
   - Replace `OPENROUTER_API_KEY` in `main.py` with your actual API key or set it as an environment variable.

### Running the Application
1. Start the Streamlit app:
   ```bash
   streamlit run main.py
   ```
2. Open your browser to `http://localhost:8501`.
3. Upload a satellite image (PNG/JPG) to analyze.

## Example Usage
1. Upload a satellite image of a rooftop.
2. View analysis results (area, orientation, shading, obstructions).
3. Review solar potential and ROI estimates.
4. Follow recommendations for installation or further inspection.

## Example Analysis
**Input**: A 1000x1000 PNG satellite image of a residential rooftop.
**Output**:
- Area: 100 m²
- Orientation: 180° (South)
- Shading: 10%
- Obstructions: No
- Annual Energy Output: 3650 kWh
- System Size: 2 kW
- Total Cost: $6600
- Incentives: $1980
- Net Cost: $4620
- Annual Savings: $547.50
- Payback Period: 8.4 years

## Future Improvements
- Integrate real-time solar irradiance data via API.
- Add support for multiple panel types and efficiencies.
- Implement advanced error handling for API failures.
- Enhance UI with interactive charts and maps.

## Deployment (Optional)
To deploy on Hugging Face Spaces:
1. Create a Hugging Face account and Space.
2. Upload `main.py`, `requirements.txt`, and other files.
3. Configure `requirements.txt`:
   ```text
   streamlit
   pillow
   requests
   ```
4. Set environment variables for API keys in Space settings.
5. Deploy and access the live app via the provided URL.
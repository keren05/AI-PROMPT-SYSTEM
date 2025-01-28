# AI-Powered Travel Itinerary Planner

## Overview

The **AI-Powered Travel Itinerary Planner** is a Streamlit-based web application that uses OpenAI's GPT-4 to generate personalized, day-by-day travel itineraries. Users can input their travel details, preferences, and constraints, and the app provides a well-structured travel plan tailored to their needs.  

## Features

- Generate travel itineraries for any destination worldwide.
- Personalize the plan based on:
  - Destination
  - Trip duration
  - Budget (Affordable, Moderate, Luxury)
  - Purpose of travel (Adventure, Relaxation, Family Time, Cultural Exploration)
  - Preferences (e.g., art, food, museums, beaches, nature)
- Includes a mix of popular attractions and hidden gems.
- Provides a clear and feasible schedule for morning, afternoon, and evening activities.
- Hosted on Streamlit for easy access.

---

## Installation

Follow these steps to set up the project locally:

### Prerequisites
1. Python 3.9 or above
2. An OpenAI API Key
3. Streamlit library installed

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/keren05/AI-PROMPT-SYSTEM
   cd travel-itinerary-planner
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key:
   - Open the `app.py` file.
   - Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key in the secrets.toml file

5. Run the application:
   ```bash
   streamlit run app.py
   ```

6. Access the app at "https://ai-prompt-system-um5h2rutfd8m9glnlpnsjq.streamlit.app/"

---

## Usage

1. Open the app in your browser.
2. Fill in the details:
   - **Destination**: Enter the city or country you'd like to visit (e.g., Paris, Tokyo).
   - **Trip Duration**: Specify the number of days for your trip.
   - **Budget**: Choose from Affordable, Moderate, or Luxury.
   - **Purpose**: Select the reason for travel (e.g., Adventure, Cultural Exploration).
   - **Preferences**: Add personal preferences (e.g., art, food, beaches).
3. Click the **Generate Itinerary** button.
4. View your personalized, day-by-day travel itinerary.

---

## Deployment

The application can be hosted on any free hosting platform like **Streamlit Community Cloud**.  

### Deploying on Streamlit Community Cloud:
1. Sign in to [Streamlit Community Cloud](https://streamlit.io/cloud).
2. Create a new app and connect it to this repository.
3. Add your OpenAI API key as a secret in the Streamlit app settings.
4. Deploy the app and share the generated link.

---

## Sample Input/Output

### Sample Input
- **Destination**: Paris
- **Trip Duration**: 5 days
- **Budget**: Moderate
- **Purpose**: Cultural Exploration
- **Preferences**: art, museums, good food

### Sample Output (Excerpt)
```
Day 1:
- Morning: Visit the Louvre Museum and explore its renowned art collections.
- Afternoon: Enjoy a leisurely lunch at a traditional French bistro near the Seine.
- Evening: Take a sunset river cruise on the Seine to see the Eiffel Tower illuminated.

Day 2:
- Morning: Explore the Montmartre district, including the Sacré-Cœur Basilica.
- Afternoon: Visit the Musée d'Orsay for impressionist art.
- Evening: Dine at a Michelin-starred restaurant offering authentic French cuisine.
...
```

---

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Frontend framework for building web apps.
- **OpenAI GPT-4**: AI model for generating itineraries.

---

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---

Let me know if you'd like help customizing this further or creating the `requirements.txt` file!

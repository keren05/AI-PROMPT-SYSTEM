import streamlit as st
import openai
from datetime import datetime, timedelta


def initialize_openai():
    """Initialize OpenAI client with API key."""
    if 'openai_client' not in st.session_state:
        api_key = st.secrets["OPENAI_API_KEY"]
        st.session_state.openai_client = openai.OpenAI(api_key=api_key)
    return st.session_state.openai_client


def get_system_prompt():
    """Define the base system prompt for the travel planner."""
    return """You are an expert travel planner with extensive knowledge of destinations worldwide. 
    Your role is to create personalized travel itineraries based on user preferences and requirements. 
    Be specific, practical, and consider local customs and seasonal factors in your recommendations."""


def gather_user_preferences():
    """Collect detailed user preferences through a structured form."""
    st.title("AI Travel Planner")
    st.write("Let's plan your perfect trip! Please fill in your preferences below.")

    col1, col2 = st.columns(2)

    with col1:
        destination = st.text_input("Where would you like to go?")
        start_date = st.date_input("When do you plan to start your trip?")
        duration = st.number_input("How many days is your trip?", min_value=1, max_value=30, value=3)
        budget = st.selectbox("What's your budget level?",
                              ["Budget", "Moderate", "Luxury"])

    with col2:
        interests = st.multiselect("What are your interests?",
                                   ["History & Culture", "Food & Dining", "Nature & Outdoors",
                                    "Shopping", "Art & Museums", "Adventure Activities",
                                    "Relaxation", "Nightlife"])
        dietary_prefs = st.multiselect("Any dietary preferences?",
                                       ["Vegetarian", "Vegan", "Halal", "Kosher", "None"])
        mobility_level = st.select_slider("Walking tolerance level?",
                                          options=["Low", "Medium", "High"])
        accommodation_pref = st.selectbox("Preferred accommodation type?",
                                          ["Budget Hostel/Guesthouse", "Mid-range Hotel",
                                           "Luxury Resort", "Boutique Hotel"])

    return {
        "destination": destination,
        "start_date": start_date,
        "duration": duration,
        "budget": budget,
        "interests": interests,
        "dietary_prefs": dietary_prefs,
        "mobility_level": mobility_level,
        "accommodation_pref": accommodation_pref
    }


def generate_itinerary_prompt(preferences):
    """Create a detailed prompt based on user preferences."""
    prompt = f"""Create a detailed {preferences['duration']}-day itinerary for {preferences['destination']} with the following specifications:

Budget Level: {preferences['budget']}
Interests: {', '.join(preferences['interests'])}
Dietary Preferences: {', '.join(preferences['dietary_prefs'])}
Mobility Level: {preferences['mobility_level']}
Accommodation: {preferences['accommodation_pref']}

Please provide:
1. A day-by-day breakdown of activities, including:
   - Morning, afternoon, and evening activities
   - Estimated time for each activity
   - Recommended restaurants matching dietary preferences
   - Transportation suggestions between locations
2. Specific accommodation recommendations
3. Estimated costs for activities and meals
4. Local tips and cultural considerations
5. Backup activities or rainy day alternatives

Format the itinerary in a clear, easy-to-read structure with markdown formatting."""
    return prompt


def generate_itinerary(client, preferences):
    """Generate the travel itinerary using OpenAI API."""
    system_prompt = get_system_prompt()
    user_prompt = generate_itinerary_prompt(preferences)

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating itinerary: {str(e)}"


def main():
    """Main application flow."""
    st.set_page_config(page_title="AI Travel Planner", layout="wide")

    try:
        client = initialize_openai()
    except Exception as e:
        st.error(f"Error initializing OpenAI client: {str(e)}")
        return

    preferences = gather_user_preferences()

    if st.button("Generate Itinerary"):
        if not preferences["destination"]:
            st.warning("Please enter a destination.")
            return

        with st.spinner("Generating your personalized itinerary..."):
            itinerary = generate_itinerary(client, preferences)
            st.markdown(itinerary)

        # Add download button for the itinerary
        st.download_button(
            label="Download Itinerary",
            data=itinerary,
            file_name=f"travel_itinerary_{preferences['destination']}.txt",
            mime="text/plain"
        )


if __name__ == "__main__":
    main()
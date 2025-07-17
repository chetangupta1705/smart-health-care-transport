import streamlit as st

st.title("Emergency First Aid Chatbot 🤖")
st.write("Ask me basic first aid questions!")

# Simple rule-based chatbot responses
def get_first_aid_response(user_input):
    user_input = user_input.lower()

    if "burn" in user_input:
        return "For minor burns, cool the burn under running water for at least 10 minutes. Don't apply ice or butter."
    elif "bleeding" in user_input:
        return "Apply pressure to the wound with a clean cloth. If bleeding doesn't stop, seek medical help immediately."
    elif "fracture" in user_input:
        return "Keep the injured area immobile. Apply a splint if trained and seek medical attention quickly."
    elif "choking" in user_input:
        return "If the person can't breathe, perform the Heimlich maneuver or call emergency services."
    elif "heart attack" in user_input:
        return "Call emergency services immediately. Have the person sit down, stay calm, and chew aspirin if not allergic."
    elif "snake bite" in user_input:
        return "Keep the person calm and still. Do not suck out venom. Immobilize the bitten area and seek emergency help."
    elif "fever" in user_input:
        return "Keep hydrated and rest. Use a cold compress and consult a doctor if fever persists above 102°F."
    else:
        return "Sorry, I don't have information on that. Please contact a medical professional or call emergency services."

# Chat UI
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

if user_input:
    response = get_first_aid_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")

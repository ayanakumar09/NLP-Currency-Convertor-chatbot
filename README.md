# NLP-Currency-Convertor-chatbot
## 1. Overview
This project is a conversational chatbot built using Google Dialogflow for natural language understanding and a custom Flask backend to handle runtime computations and logic-based responses. It integrates NLP with dynamic fulfillment for responsive and intelligent conversations.

---

## 2. Components

### a) Dialogflow and Conversational Logic

Dialogflow is a cloud-based platform that provides natural language understanding to process user input. It is used to define:

- **Intents**: Represent the goal or action behind a user’s query (e.g., "get age", "calculate area").
- **Entities**: Extract parameters or variables from user input (e.g., years, numbers, locations).
- **Training Phrases**: Sample inputs provided to help Dialogflow learn the different ways users might express an intent.
- **Fulfillment**: Webhook-based mechanism that allows external backend services to dynamically generate responses.

Dialogflow detects the intent, extracts parameters, and if fulfillment is enabled, sends a JSON request to the backend webhook with those parameters.

### b) Backend API (Flask and Ngrok)

The backend consists of a lightweight Flask application that serves as a webhook endpoint.

- **Flask**: Processes HTTP POST requests sent from Dialogflow’s fulfillment.
- **Ngrok**: Creates a secure tunnel from the local server to the internet, allowing Dialogflow to access the local webhook during development.
- **Response Logic**: The Flask server processes input values based on the detected intent, performs necessary computations or lookups, and sends back a structured response.

---

## 3. Intent Fulfillment Workflow

The system follows a four-step lifecycle from input to response:

1. **User Input**  
   The user sends a message through the Dialogflow interface or integrated platform.

2. **Intent Detection**  
   Dialogflow processes the input and matches it to a trained intent. If that intent requires backend processing, it triggers the fulfillment webhook with all extracted parameters.

3. **Runtime Execution in Backend**  
   The Flask webhook receives the request, processes it according to the intent (e.g., performing arithmetic, generating text, querying data), and prepares a response message.

4. **Response Delivery**  
   The backend sends a JSON response back to Dialogflow, which then presents the result to the user in the interface.

---

## Example Use Case

**Intent**: Age Calculator  
- **User Input**: "How old will I be in 2040 if I was born in 2005?"  
- **Entities Extracted**:  
  - `birthYear = 2005`  
  - `targetYear = 2040`  
- **Backend Logic**: `2040 - 2005 = 35`  
- **Response**: "You will be 35 years old in 2040."

---

## Technologies Used

- Google Dialogflow (for NLU and intent classification)  
- Python Flask (for webhook backend)  
- Ngrok (for tunneling the local server to the web)  
- JSON (for communication between Dialogflow and the webhook)


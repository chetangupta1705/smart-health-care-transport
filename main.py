from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymongo
from pydantic import BaseModel
from fastapi import Request

app = FastAPI()

# ✅ CORS configuration
origins = [
    "http://127.0.0.1:5500",   # Frontend port
    "http://localhost:5500"     # Alternative frontend origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ MongoDB connection
client = pymongo.MongoClient("mongodb+srv://chetan:chetan12345@ambulance-cluster.iwxq5.mongodb.net/?retryWrites=true&w=majority&appName=ambulance-cluster")
mydb = client["ambulance"]
mycol = mydb["userlogin"]

# ✅ Use Pydantic models to handle JSON data
class User(BaseModel):
    name: str = None
    email: str
    password: str

# ✅ Register endpoint
@app.post("/register")
async def register(user: User):
    data = {
        "Name": user.name,
        "Email": user.email,
        "Password": user.password
    }
    result = mycol.insert_one(data)
    if result.inserted_id:
        return {"message": "User registered successfully", "user": user}
    return {"error": "Registration failed"}

# ✅ Login endpoint
@app.post("/login")
async def login(user: User):
    found_user = mycol.find_one({"Email": user.email, "Password": user.password})
    if found_user:
        return {"message": "Login successful", "user": user}
    return {"error": "Invalid credentials"}
# ✅ Chatbot endpoint


@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    # Dummy chatbot response logic
    if "ambulance" in user_message.lower():
        reply = "Yes, we provide 24/7 ambulance services in Chennai."
    elif "services" in user_message.lower():
        reply = "We offer ALS, BLS, Air Ambulance, Mortuary transport, and more."
    else:
        reply = "I’m here to help you with our ambulance services. How can I assist you?"

    return {"reply": reply}

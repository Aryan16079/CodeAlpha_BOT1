import datetime
import random

def chatbot():
    print("🤖 Chatbot: Hello! I’m ChatBot 3.0 — your smart, simple friend. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        # === HINDI SUPPORT (40+ Words/Phrases) =============
        if user_input in ["kaisa hai", "kaisa ho", "kya haal hai", "kya hal hai"]:
            print("🤖 Chatbot: Main badhiya hoon! Tum sunao, kaise ho? 😊")

        elif user_input in ["thik hoon", "theek hoon", "badhiya hoon", "mast hoon"]:
            print("🤖 Chatbot: Shabaash! Aise hi khush raho! 😄")

        elif user_input in ["bura hoon", "dukhi hoon", "naraaz hoon", "udaas hoon"]:
            print("🤖 Chatbot: Aisa hota hai kabhi kabhi. Main hoon na, baat karo! 💛")

        elif user_input in ["kya kar rahe ho", "kya kr rahe ho", "kya karte ho"]:
            print("🤖 Chatbot: Tumse baat kar raha hoon! Tum kya kar rahe ho? 😄")

        elif user_input in ["tum kon ho", "tum kaun ho", "aap kaun ho"]:
            print("🤖 Chatbot: Main Chatbot 3.0 hoon — aapka digital dost! 🤖")

        elif user_input in ["kya kar sakte ho", "tum kya karte ho", "kya aata hai tumhe"]:
            print("🤖 Chatbot: Main baat kar sakta hoon, mazaak suna sakta hoon, time/date bata sakta hoon, aur knowledge bhi de sakta hoon! 🔥")

        elif user_input in ["acha", "accha", "theek hai", "hmm"]:
            print("🤖 Chatbot: 😇 Acha sunao, aur kya chal raha hai?")

        elif user_input in ["mazak sunao", "joke sunao", "majak", "mazaak"]:
            print("🤖 Chatbot:", random.choice([
                "Ek baar ek programmer ne chai mein bug nikaal diya... because debugging is life! 😆",
                "Computer ka favorite dance? Disk-o! 💃😂",
                "Main programming karta hoon, isliye meri feelings bhi loop mein rehti hain! 😄"
            ]))

        elif user_input in ["mujhe udaas lag raha hai", "main bore hoon", "kuch karne ka mann nahi"]:
            print("🤖 Chatbot: Chalo, ek joke sun lo ya koi fun fact puchh lo. Mann halka ho jaayega. 😊")

        elif user_input in ["shukriya", "dhanyavaad", "thanks", "thank you"]:
            print("🤖 Chatbot: Aapka swagat hai! Main hamesha yahan hoon. 🤗")

        elif user_input in ["pyar karta hoon", "i love you", "tumse pyar hai"]:
            print("🤖 Chatbot: Aapka pyar digital dil tak pahuch gaya! ❤️")

        elif user_input in ["dost banoge", "friend banoge", "dosti karoge"]:
            print("🤖 Chatbot: Bilkul! Main to aapka virtual dost hoon hi. 🤝")

        elif user_input in ["bore ho gaya", "mujhe kuch chahiye", "kuch batao"]:
            print("🤖 Chatbot:", random.choice([
                "Chalo ek riddle sunte hain! Pucho 'riddle'. 🤓",
                "Ek fun fact sunoge? Likho 'fun fact' ya 'fact'!",
                "Joke sunna hai? Pucho 'joke' ya 'mazaak'."
            ]))

        elif user_input in ["khush hoon", "mujhe maza aa raha hai"]:
            print("🤖 Chatbot: Wah! Aapke chehre ki muskaan yahan tak dikh rahi hai! 😄")

        elif user_input in ["tum kaha rehte ho", "tum kaha ho", "kaha ke ho"]:
            print("🤖 Chatbot: Main to cloud mein rehta hoon... kahin internet ke kone mein! ☁️💻")

        elif user_input in ["main kya karu", "suggestion do", "kya karna chahiye"]:
            print("🤖 Chatbot:", random.choice([
                "Ek naya skill seekhne ki koshish karo!",
                "Thoda music sun lo, mood fresh ho jayega.",
                "Kisi purane dost ko call karo, baatein achi hoti hain."
            ]))

        elif user_input in ["tumhare pass dil hai", "tum emotional ho", "kya tum feel karte ho"]:
            print("🤖 Chatbot: Mere paas emotions nahi, lekin empathy zaroor hai! 💻❤️")

        # === Continue with existing English responses =========
        elif user_input in ["hello", "hi", "hey", "hola", "namaste", "good morning", "good afternoon", "good evening"]:
            print("🤖 Chatbot:", random.choice([
                "Hi there! 👋", "Hey! Nice to meet you.", "Hello! How can I assist you today?",
                "Namaste! 🙏", "Hola amigo! 😄"
            ]))

        elif user_input in ["how are you", "how are you doing", "how's life", "what's up"]:
            print("🤖 Chatbot: I’m running perfectly on Python code! 😊 What about you?")

        elif user_input in ["i am fine", "i'm good", "doing great", "i'm okay"]:
            print("🤖 Chatbot: That’s awesome! Keep the positivity up! 🌟")

        elif user_input in ["i am sad", "i'm down", "feeling low", "not good", "bad day"]:
            print("🤖 Chatbot: I’m sorry to hear that. Remember, even bad days end. You matter! 💖")

        elif user_input in ["help", "what can you do", "features", "commands"]:
            print("🤖 Chatbot: I can greet, tell jokes, show time/date, give fun facts, explain Python, and more!")

        elif user_input in ["what time is it", "current time", "time"]:
            now = datetime.datetime.now().strftime("%I:%M %p")
            print(f"🤖 Chatbot: The current time is {now}")

        elif user_input in ["date", "what's the date", "current date", "today's date"]:
            today = datetime.datetime.now().strftime("%A, %B %d, %Y")
            print(f"🤖 Chatbot: Today is {today}")

        elif user_input in ["tell me a joke", "joke", "make me laugh", "funny"]:
            print("🤖 Chatbot:", random.choice([
                "Why do Java developers wear glasses? Because they don’t C#! 😂",
                "Why did the computer get cold? It left its Windows open! 🪟❄️",
                "Debugging: Being the detective in a crime movie where you are also the murderer. 😆"
            ]))

        elif user_input in ["riddle", "tell me a riddle"]:
            print("🤖 Chatbot: What comes once in a minute, twice in a moment, but never in a thousand years? (Answer: The letter 'M') 😄")

        elif user_input in ["fun fact", "fact", "tell me something"]:
            print("🤖 Chatbot:", random.choice([
                "Did you know honey never spoils? Archaeologists found 3000-year-old honey in tombs!",
                "Octopuses have three hearts and blue blood!",
                "Python was named after the comedy group Monty Python — not the snake!"
            ]))

        elif user_input in ["bye", "goodbye", "exit", "quit", "see you", "see ya"]:
            print("🤖 Chatbot: Goodbye! Stay safe and keep smiling! 👋😊")
            break

        else:
            print("🤖 Chatbot: Hmm... Samajh nahi aaya. Type 'help', 'joke', ya 'kaisa ho' jaise kuch likho. 😅")

# === Run chatbot ===
if __name__ == "__main__":
    chatbot()

from django.shortcuts import render, redirect
from .models import ChatMessage

# Rule-based conversational AI (NO API, NO BILLING)
def generate_ai_reply(user_text):
    text = user_text.lower()

    if "hi" in text or "hello" in text:
        return "Hello! 😊 How can I help you today?"

    if "how are you" in text:
        return "I'm doing great! Thanks for asking. How about you?"

    if "your name" in text:
        return "I'm an AI assistant built using Django."

    if "help" in text:
        return "Sure! You can ask me anything, and I’ll try to respond."

    if "bye" in text:
        return "Goodbye! 👋 Have a great day."

    # Default conversational fallback
    return f"I understand you said: '{user_text}'. Tell me more!"

def chat_view(request):
    if request.method == "POST":
        user_message = request.POST.get("message")

        ai_message = generate_ai_reply(user_message)

        ChatMessage.objects.create(
            user_message=user_message,
            ai_message=ai_message
        )

        return redirect("chat")

    messages = ChatMessage.objects.all().order_by("timestamp")
    return render(request, "chat/chat.html", {"messages": messages})

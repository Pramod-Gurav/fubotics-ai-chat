from django.shortcuts import render, redirect
from .models import ChatMessage

# Simple AI reply function
def generate_ai_reply(user_text):
    return f"I received your message: '{user_text}'. This is a demo AI response."

def chat_view(request):
    if request.method == "POST":
        user_message = request.POST.get("message")

        # Generate AI reply
        ai_message = generate_ai_reply(user_message)

        # Save to database
        ChatMessage.objects.create(
            user_message=user_message,
            ai_message=ai_message
        )

        return redirect("/")

    # Load full chat history
    messages = ChatMessage.objects.all().order_by("timestamp")
    return render(request, "chat/chat.html", {"messages": messages})

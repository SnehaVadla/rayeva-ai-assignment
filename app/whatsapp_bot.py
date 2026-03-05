from .ai_service import generate_ai_response


def detect_intent(message):

    msg = message.lower()

    if "order" in msg:
        return "order_status"

    elif "refund" in msg:
        return "refund"

    elif "return" in msg:
        return "return_policy"

    else:
        return "general_query"


def generate_whatsapp_reply(message):

    intent = detect_intent(message)

    if intent == "order_status":
        return {
            "intent": intent,
            "reply": "Your order is currently being processed and will be shipped soon."
        }

    elif intent == "refund":
        return {
            "intent": intent,
            "reply": "Your refund request has been forwarded to our support team."
        }

    elif intent == "return_policy":
        return {
            "intent": intent,
            "reply": "You can return products within 30 days of delivery."
        }

    else:

        prompt = f"""
        You are a helpful ecommerce support bot.
        Answer the customer question clearly.

        Customer question: {message}
        """

        response = generate_ai_response(prompt)

        return {
            "intent": intent,
            "reply": response
        }
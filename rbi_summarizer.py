import openai

class RBISummarizer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize_update(self, update_text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Please summarize the following RBI update: {update_text}"}
            ]
        )
        return response['choices'][0]['message']['content']

    def analyze_investment_banking_impact(self, update_text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Analyze the investment banking impact of the following RBI update: {update_text}"}
            ]
        )
        return response['choices'][0]['message']['content']

    def categorize_update(self, update_text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Categorize the following RBI update: {update_text}"}
            ]
        )
        return response['choices'][0]['message']['content']

    def generate_executive_summary(self, update_text, target_audience):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Generate an executive summary for the following RBI update for {target_audience}: {update_text}"}
            ]
        )
        return response['choices'][0]['message']['content']

# Example usage (to be removed from production):
# summarizer = RBISummarizer(api_key='your_api_key')
# print(summarizer.summarize_update('sample RBI update text'))
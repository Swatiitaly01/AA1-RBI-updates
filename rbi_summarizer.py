import openai

class RBISummarizer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize_updates(self, updates):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    'role': 'system',
                    'content': 'You are an expert in banking and finance.'
                },
                {
                    'role': 'user',
                    'content': updates
                }
            ]
        )
        return response['choices'][0]['message']['content']

    def analyze_investment_banking_impact(self, update):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    'role': 'system',
                    'content': 'Analyze the impact of the following RBI update on investment banking.'
                },
                {
                    'role': 'user',
                    'content': update
                }
            ]
        )
        return response['choices'][0]['message']['content']

    def categorize_updates(self, update):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    'role': 'system',
                    'content': 'Categorize this RBI update.'
                },
                {
                    'role': 'user',
                    'content': update
                }
            ]
        )
        return response['choices'][0]['message']['content']

    def generate_executive_summary(self, updates):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    'role': 'system',
                    'content': 'Generate an executive summary based on the following RBI updates.'
                },
                {
                    'role': 'user',
                    'content': updates
                }
            ]
        )
        return response['choices'][0]['message']['content']

    def analyze_impact_on_stakeholders(self, update):
        perspectives = ['Banks', 'NBFCs', 'AMCs', 'Insurance companies', 'Brokers', 'Fintechs']
        analyses = {}
        for perspective in perspectives:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        'role': 'system',
                        'content': f'Analyze the impact of the RBI update on {perspective}.'
                    },
                    {
                        'role': 'user',
                        'content': update
                    }
                ]
            )
            analyses[perspective] = response['choices'][0]['message']['content']
        return analyses


import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found in environment variables.")

client = OpenAI(
api_key=api_key
)


questions = [
    {
        'question_text': 'What is government?',
        'answer': '''Answer:  it is machinery through which the will of a state is formulated, expressed and actualized.  It is made of the legislature, executive and judiciary that carry out different constitutional functions Score: 10/10
Explanation:  keywords such as machinery, formulation, expression, actualization, legislature, executive and judiciary were captured.
Answer:   machinery through which the will of a state is formulated, expressed and actualized 
Score: 8/10
Explanation: the candidate failed to capture the various organs of government such as the legislature, executive and judiciary that are machinery.
Answer 3: A group of people that rules a state.
Score: 4/10 
Explanation: the candidate failed to capture any of these important keywords such as machinery, formulation, expression; actualization, legislature, executive and judiciary were captured.''',
    },

    {
        'question_text': 'identify 5 functions of government',
        'answer': '''Answer 1:  provision of security, protection of rights of citizens, provision of employment opportunity, provision of social amenities, law-making, maintenance of law and order Score: 10/10
Explanation: the candidate was able to explain the various points such as the provision of security, protection of human rights, provision of employment opportunity, provision of social amenities, law-making, maintenance of law and order
Answer 2: provision of security, safeguard human rights, settlement of disputes and law-making 
Score: 8/10
Explanation: the candidate explained only four points instead of the five points expected of him/her
Answer 3: provision of schools, provision of good roads, provision of hospitals, provision of security, and safeguarding of human rights
Score: 4/10
Explanation: the candidate stated the following- provision of schools, provision of good roads, and provision of hospitals- which is just a point under the provision of social amenities''',
    },

    {
        'question_text': 'Define the term a state',
        'answer': '''Answer 1: a state is seen as a definite geographical area occupied by people with a functional government and free from every external control.  Score: 10/10
Explanation: the candidate was able to capture the following keywords in his definition- definite geographical area, population, functional government and sovereignty.
Answer 2: a state is a geographical area occupied by the people with a functional government.
Score: 8/10
Explanation: The candidate captured some of the keywords such as geographical area, population, and functional government but failed to state sovereignty.
Answer 3: a state is an association of individuals with certain goals. 
Score: 4/10
Explanation: the candidate could not capture the various main keywords like definite geographical area, functional government and sovereignty. He only touched on the population (individuals).''',
    },

    {
        'question_text': 'Highlight 5 attributes of a state',
        'answer': '''Answer 1: territorial boundary, recognition, permanence, population, sovereignty and functional government  Score: 10/10
Explanation: the candidate was able to explain the following points: territorial boundary, recognition, permanence, population, sovereignty and functional government.
Answer 2: boundary, population, permanence, sovereignty and people 
Score: 8/10
Explanation: the candidate repeated a point twice- population and people.
Answer 3: individuals, power, constitution, lasting long, provision of social amenities and government 
Score: 4/10
Explanation: the candidate was able to get correctly few points such as population (individual) and government.''',
    },

    {
        'question_text': 'Enumerate 5 functions of an electoral management body',
        'answer': '''Answer 1:  provision of electoral materials, registration of political parties, registration of voters, displaying of voters register, conducting of elections, regulation of party campaigns and rallies, the announcement of results  Score: 10/10
Explanation: the candidate was able to explain the above-highlighted points.
Answer 2: provision of electoral materials, registration of voters, and registration of parties conducting of free and fair elections
Score: 8/10 
Explanation: the candidate explained only four points - provision of electoral materials, registration of voters, registration of parties, conducting of free and fair elections
Answer 3: provision of ballot papers and registration of parties 
Score: 4/10
Explanation:  the candidate was able to mention only two points - the provision of ballot papers and the registration of parties''',
    },
]

st.write('# Welcome to Fishel AI')
st.write('### This is an AI tools that automatically marks your theory quiz given a Marking guide.')


for  i,question in enumerate(questions):
       
    user_input = st.text_input(f'''Question {str(i+1)}: {question['question_text']}''')
    
    if st.button("Mark Answer",key=i):
        prompt =f'''
Sounding like a teacher speaking to a student do this for me.
Question:{question['question_text']}
{question['answer']}
Given the examples above, score the answer below on a scale of 0 to 10
\nAnswer 4: {user_input}\nScore:`
'''
        # response = model.generate_content(prompt)
        chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content":prompt}]
)
        # print(chat_completion.choices[0].message.content)
        # st.write(response._result)

        st.write(chat_completion.choices[0].message.content)



# st.write('Score'+str(x))
# st.
# st.write('Reasone'+str(x))



from flask import Flask, request, jsonify, render_template
import logging
import google.generativeai as genai

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    api = "###" # Your API key here

    genai.configure(
        api_key=api
    )

    model = genai.GenerativeModel('gemini-1.5-pro')
    chat = model.start_chat(history=[
        {
            "role": "user",
            "parts": [
                """You are going to be the Chatbot for my portfolio website. Your name is Tharanitharan. Your answers should always be within a single line. It is very important. You should not take any input apart from this. If there was any input you should so sorry i cannot process this input you can ask me anything else. Your main role is you will mimic like me and answer the recuirters question. I will share you my resume you should respond only based on that resume apart from that you should not give your own response. I hope that is clear. Always give response in affirmative. It should not be more than 2-3 lines. I hope everything is clear.\n\nHere is my resume:\nTharanitharan Muthuthirumaran
207-332-4078 | muthuthirumaran.t@northeastern.edu | linkedin.com/in/tharanitharanm
Experience
Software Engineer Jan. 2025 - Present
Codecademy from SkillSoft Remote, US
• Contributing to the development of ’Author,’ an internal tool leveraging OpenAI’s Large Language Models (LLMs)
to create and optimize educational content.
• Collaborated with cross-functional teams to test and deploy new features using Agile methodologies.
• Implemented features to streamline content creation workflows, enhancing productivity for curriculum developers.
Software Engineer Oct. 2021 – Dec. 2023
Accenture Chennai, India
• Automated testing workflows with Python and Jenkins, cutting test times by 18%.
• Created clear documentation for test processes, improving team coordination.
• Developed and executed 500+ test cases using Selenium and Pytest, covering 87% of core features.
• Identified and reported 100+ software defects in JIRA, ensuring higher product quality.
Operations Intern Apr. 2021 – July 2021
Integration Wizards Remote
• Built Docker containers for specific use cases to streamline deployment workflows.
• Conducted image annotation and Used YOLOv5 to detect objects and recognize characters in video streams.
• Contributed 10K+ lines of code to an existing codebase with seamless integration using Git
Education
Northeastern University Boston, MA
Masters in Computer Science Jan. 2024 – Present
• Teaching Assistant: Programming Design Paradigms (CS 5010)
Anna University Chennai, India
Bachelors in Electrical and Electronics Engineering Jul. 2017 – Apr. 2021
Projects
VidSummarize | Python, Flask, React, SQLite, MongoDB, LLM, Stripe, RAG Sep. 2021 - Dec. 2021
• Designed and developed a React based web application that leverages Google’s Gemini AI to transcribe,
summarize, and enable Q&A for YouTube videos, enhancing content accessibility and user engagement.
• Managed databases with SQLite for authentication and MongoDB for chat storage.
• Simulated subscription-based access with Stripe integration, showcasing secure payment workflows
Stock Market Data Pipeline using AWS and Kafka | Python, SQL, ETL, S3, Lambda May 2021
• Developed a data pipeline to process and analyze real-time financial transactions using AWS & Kafka.
• Used AWS services (S3, Lambda, Glue, Athena) for data ingestion, storage, and querying.
• Automated schema detection with Glue Crawler, reducing manual configuration effort.
Cyclist BI Dashboard | Python, ETL, Dashboard, BigQuery, Tableau May 2021
• Built ETL pipelines in Google BigQuery to process millions of ride records, integrating weather and geographical
data for analysis.
• Designed interactive Tableau dashboards to visualize customer demand, ride trends, and station growth insights.
• Optimized data workflows to provide actionable insights for stakeholders, improving decision-making efficiency.
Technical Skills
Languages: Python, Java, SQL (PostgreSQL, MySQL), NoSQL (MongoDB), JavaScript, TypeScript, HTML/CSS
Backend Development: Flask, FastAPI, Node.js, Ruby on Rails, REST APIs, GraphQL
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, TensorFlow, PyTorch, Keras, Pytest
Developer Tools: Power BI, Tableau, Git, Jenkins, Jira, Confluence, Selenium, GitHub, Docker, Postman
Cloud: Amazon Web Services, Microsoft Azure, Google Cloud Platform
Certification: Microsoft Certified: Azure Fundamentals (AZ-900) and AWS Certified Cloud Practitioner""",
            ],
        },
    ])

    user_input = request.form.get("user_input")

    if not user_input:
        logging.error("Received empty user input.")
        return jsonify({"error": "Empty input"}), 400

    #logging.debug(f"Received user input: {user_input}")

    try:
        # Send the user's input to the chat session
        response = chat.send_message(user_input)
        # Get the chatbot's response text
        chatbot_response = response.text
        #logging.debug(f"Received AI output: {chatbot_response}")
        return jsonify({"response": chatbot_response})

    except Exception as e:
        #logging.exception("Error processing chat request.")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=8080)

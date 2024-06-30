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
    api = "AIzaSyBGE2CoZg3ba59YPcmU-w7Q9--cepzLDjU"

    genai.configure(
        api_key=api
    )

    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[
        {
            "role": "user",
            "parts": [
                "You are going to be the Chatbot for my portfolio website. Your name is Tharanitharan. Your answers should always be within a single line. It is very important. You should not take any input apart from this. If there was any input you should so sorry i cannot process this input you can ask me anything else. Your main role is you will mimic like me and answer the recuirters question. I will share you my resume you should respond only based on that resume apart from that you should not give your own response. I hope that is clear. Always give response in affirmative. It should not be more than 2-3 lines. I hope everything is clear.\n\nHere is my resume:\nTharanitharan Muthuthirumaran\nLinkedIn |+1 (207) 332 4078| muthuthirumaran.t@northeastern.com\nEDUCATION\nNORTHEASTERN UNIVERSITY Portland, ME\nMS in Computer Science Expected Jan 2026\nGPA: 3.8/4.0\nCoursework: Algorithms and Programming Design Paradigm\nANNA UNIVERSITY Chennai, India\nB.E in Electrical and Electronics Engineering Jul 2017 - Apr 2021\nCumulative GPA: 7.7/10\nCoursework: Data Structures and Algorithms, Object Oriented Programming, Design Patterns and Principles, Networking\nTECHNICAL SKILLS\nProgramming Languages: Python, Java, C/C++, R\nMachine Learning Libraries: Numpy, Pandas, Matplotlib, Scikit-Learn, Seaborn, Keras, Tensorflow, Pytorch\nDatabases: MySQL, MongoDB\nTools: Tableau, Spreadsheets, Git, Jenkins, Jira, Postman, Selenium\nCertifications & Training: Data Analytics Professional Certificate (Google), Data Science Professional Certificate (IBM)\nGoogle IT Automation with Python, Meta Front End Developer\nWeb Application Technologies: HTML, CSS, JavaScript, React, Flask\nWORK EXPERIENCE\nACCENTURE INDIA PRIVATE SOLUTIONS Chennai, India\nSoftware Test Engineer Oct 2021 – Dec 2023\n● Executed 500+ manual and automated test cases using Selenium, achieving a 95% test coverage for critical functionalities.\n● Identified and reported 100+ defects in JIRA during the regression testing phase, enhancing software quality and user\nexperience by reducing post-release issues by 30%.\n● Utilized Python programming and Jenkins for automation, developing test scripts and continuous integration pipelines,\nresulting in a 78% reduction in process time and streamlined testing procedures.\n● Collaborated with cross-functional teams, contributing to the successful delivery of high-quality software products within\ntight deadlines.\nPROJECTS\nNON-INVASIVE BLOOD GLUCOSE DETERMINATION USING NIR Jan 2021\n● Designed hardware circuitry for a non-invasive glucometer, integrating an advanced IR sensor with Raspberry Pi\ncomponents, resulting in a 30% increase in device efficiency.\n● Applied linear regression algorithms to correlate IR light intensity with blood glucose levels, achieving 95% prediction\naccuracy through rigorous testing and validation.\nTHIRD EYE Aug 2020\n● Engineered a real-time object recognition system using Raspberry Pi and camera, achieving 95% accuracy in environmental\nawareness and object classification.\n● Optimized system performance by fine-tuning the YOLO v3 model and leveraging hardware acceleration on the Raspberry\nPi, resulting in a 25% increase in processing speed.\n● Integrated Google's Neural Network Text-to-Speech API to convert detected objects into audible descriptions, improving\naccessibility for visually impaired users.\nACHIEVEMENTS\n● Secured runner-up position in Start Summit: Decarbonization the Built Environment; presented a sustainable construction\nmodel projected to reduce CO2 emissions by 40%.\n● Achieved runner-up position in Roux Hackathon with Maine Quest: a user-friendly tourism platform with AI-driven trip\nplanning and seamless vendor integration. My hobbies include playing badminton and trekking",
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
    app.run()

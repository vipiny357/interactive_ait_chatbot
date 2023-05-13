import gradio as gr

patterns = {
	'greeting': ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'],
	'leaving': ['bye', 'goodbye', 'good bye', 'end', 'stop', 'leave', 'see you', 'farewell'],
	'admission': ['admission', 'admissions', 'apply', 'requirements', 'eligibility'],
	'courses': ['courses', 'programs', 'departments', 'specializations'],
	'facilities': ['facilities', 'infrastructure', 'labs', 'library', 'hostel', 'sports facilities'],
	'contact': ['contact', 'address', 'phone', 'email']
}

responses = {
	'greeting': ['Hello! How can I assist you?'],
	'admission': [
		'To apply for admission at Army Institute of Technology (AIT), you need to fulfill the following requirements:\n',
		' • For undergraduate programs, candidates Admission to AIT is on the basis of All India Rank obtained in the Joint Entrance Exam (JEE) Main.',
		' • For postgraduate programs,  Candidate must have successfully completed his/her bachelors degree in Engineering / Technology in any branch with a minimum score of 50% (45% for the reserved category) along with a valid non-zero GATE score\n',
		'For detailed information and the admission process, please visit the AIT website at https://www.aitpune.com/'
	],
	'leaving': [
		'Thank you for your interaction! If you have any more questions in the future, feel free to ask. Have a great day!'
	],
	'courses': [
		'AIT offers the following undergraduate and postgraduate programs:\n',
		' • Bachelor of Engineering (B.E.) in Computer Engineering with 120 students in each year',
		' • Bachelor of Engineering (B.E.) in Electronics and Telecommunication Engineering with 120 students in each year',
		' • Bachelor of Engineering (B.E.) in Mechanical Engineering with 60 students in each year',
		' • Bachelor of Engineering (B.E.) in Information Technology with 120 students in each year',
		' • Master of Engineering (M. E.) in Data Science with 24 Seats each year\n',
		'For more details about the courses and their curriculum, please visit the AIT website at https://www.aitpune.com/'],
	'facilities': [
		'Army Institute of Technology (AIT) provides excellent facilities to its students, including:\n',
		' • Well-equipped laboratories with the latest technology',
		' • Modern classrooms and lecture halls',
		' • Library with a vast collection of books, journals, and e-resources',
		' • Sports facilities for various indoor and outdoor games',
		' • Hostel accommodation for both boys and girls',
		' • Cafeteria serving hygienic food\n',
		'The college prioritizes providing a conducive environment for learning and overall development.'
	],
	'contact': [
		'You can contact Army Institute of Technology (AIT) at the following address:',
		'  Army Institute of Technology',
		'  Dighi Hills, Alandi Road, Pune - 411015, Maharashtra, India\n',
		'Phone: 7249250184 / 7249250185',
		'Email: ait@aitpune.edu.in\n',
		'For more contact information and directions, please visit the AIT website at https://www.aitpune.com/'
	]
}

def match_query(query):
	for intent, patterns_list in patterns.items():
		for pattern in patterns_list:
			if pattern in query.lower():
				return intent
	return None

def generate_response(intent):
	if intent in responses:
		return '\n'.join(responses[intent])
	else:
		return "I'm sorry, I don't have information about that at the moment.\nCan I help you with something else (admission, courses, facilities, contact details)?"

def answer(question):
	return generate_response(match_query(question))

with gr.Blocks(
	title="AIT Chatbot",
	theme="soft"
) as demo:
	with gr.Row():
		o = gr.Textbox(
			lines=10,
			label="AIT Chatbot",
			value="Welcome to the Army Institute of Technology (AIT) Chatbot!\nHow can I assist you today?"
		)
	with gr.Row():
		q = gr.Textbox(label="Question")
		q.submit(fn=answer, inputs=q, outputs=o)
	with gr.Row():
		btn = gr.Button("Ask", variant="primary")
		btn.click(fn=answer, inputs=q, outputs=o)

demo.launch(inbrowser=True)

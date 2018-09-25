from evaluate import parse_input_story, getAnswer, get_ran_task, get_vocab, load_babi_task
from flask import Flask, request,jsonify

app = Flask(__name__)
print(app)

   
@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"

@app.route('/sample', methods=['GET'])
def task():
    task = request.args.get('task')
    print("Server task ID : " ,task)
    load_babi_task(task)  
    return  jsonify({'sample': get_ran_task()})
   

@app.route('/vocab', methods=['GET'])
def vocab():
    task = request.args.get('task')
    load_babi_task(task)
    return jsonify({'vocab': get_vocab()})
    


@app.route('/post', methods=['POST'])
def post_route():
    if request.method == 'POST':
        
        task = request.args.get('task')
        data = request.get_json()
        inputStory = data['story']
        inputQuestion = data['question']  
        load_babi_task(task)
        parsed_stories = parse_input_story(inputStory,inputQuestion)
        result = getAnswer(parsed_stories)
        return jsonify({'Answer': result})


if __name__ == '__main__':
    app.run(port=5000)

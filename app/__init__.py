from flask import Flask, jsonify, request, url_for
import subprocess
import shlex
from pathlib import Path
from .decorators import check_for_keys

# logger = logging.getLogger(__name__)
# logging.basicConfig(filename="received_commands.log", level=logging.DEBUG)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@check_for_keys("commands")
def test_command_reception():

    if request.method == "POST":
        data = request.get_json()
        commands = data.get("commands")
        all_outputs = []
        for command_data in commands:
            domino_commands = command_data.get("commands")
            for com in domino_commands:
                output = subprocess.check_output(shlex.split(com), start_new_session=True) 
                all_outputs.append({f"{com}": output})
        return jsonify({"message":"chain of commands executed", "output": [str(output) for output in all_outputs]}), 200
    
    else:
        return {"message":"hello"}, 200


with app.test_request_context():
    print(url_for('test_command_reception'))
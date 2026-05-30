from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

knowledge_base = {
    "bfs": {
        "reply": """
⭐ <b>Breadth First Search (BFS)</b><br><br>

BFS explores nodes level by level using a queue.<br><br>

<b>Steps:</b>
<ul>
<li>Start from source node</li>
<li>Visit neighbors first</li>
<li>Store nodes in queue</li>
</ul>

<b>Used In:</b><br>
Shortest path, web crawling, networking.
""",
        "trace": [
            "Understanding your question",
            "Detected topic: BFS",
            "Retrieving algorithm details",
            "Generating explanation",
            "Response ready"
        ]
    },

    "dfs": {
        "reply": """
⭐ <b>Depth First Search (DFS)</b><br><br>

DFS explores deeply before backtracking.<br><br>

<b>Uses stack/recursion.</b>

<ul>
<li>Visit node</li>
<li>Go deep into branch</li>
<li>Backtrack when needed</li>
</ul>

<b>Applications:</b><br>
Maze solving, cycle detection, AI search.
""",
        "trace": [
            "Analyzing query",
            "Detected DFS topic",
            "Generating recursive explanation",
            "Preparing examples",
            "Done"
        ]
    },

    "a*": {
        "reply": """
⭐ <b>A* Search Algorithm</b><br><br>

A* finds the shortest path using:

<div style='background:#111827;padding:10px;border-radius:10px;margin:10px 0;color:#4ade80;font-weight:bold;'>
f(n) = g(n) + h(n)
</div>

<ul>
<li>g(n): path cost</li>
<li>h(n): heuristic estimate</li>
<li>f(n): total estimated cost</li>
</ul>

<b>Applications:</b><br>
Pathfinding, robotics, games.
""",
        "trace": [
            "Understanding your question",
            "Detected topic: A* Search",
            "Retrieving heuristic concepts",
            "Generating explanation",
            "Done"
        ]
    },

    "bayes": {
        "reply": """
⭐ <b>Bayesian Networks</b><br><br>

Bayesian Networks represent probabilistic relationships between variables.<br><br>

<b>Core Idea:</b><br>
Use probability to reason under uncertainty.

<b>Applications:</b><br>
Medical diagnosis, AI reasoning, prediction systems.
""",
        "trace": [
            "Analyzing uncertainty topic",
            "Detected Bayesian reasoning",
            "Generating probability explanation",
            "Preparing response",
            "Done"
        ]
    },

    "minimax": {
        "reply": """
⭐ <b>Minimax Algorithm</b><br><br>

Minimax is used in game-playing AI.<br><br>

<b>Concept:</b>
<ul>
<li>MAX player tries to maximize score</li>
<li>MIN player tries to minimize score</li>
</ul>

<b>Applications:</b><br>
Chess, Tic-Tac-Toe, adversarial AI.
""",
        "trace": [
            "Detected adversarial search",
            "Applying game theory logic",
            "Generating minimax explanation",
            "Done"
        ]
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower()

    if "assignment" in user_message or "solve this" in user_message:
        return jsonify({
            "reply": """
⚠ <b>Academic Integrity Guard</b><br><br>

I won't provide direct assignment answers.<br><br>

Let's solve it step-by-step together.
""",
            "trace": [
                "Assignment-like query detected",
                "Academic integrity guard activated",
                "Providing guided learning",
                "Done"
            ]
        })

    for key in knowledge_base:
        if key in user_message:
            return jsonify({
                "reply": knowledge_base[key]["reply"],
                "trace": knowledge_base[key]["trace"]
            })

    return jsonify({
        "reply": """
🤖 I understand your question.<br><br>

Try asking about:
<ul>
<li>BFS</li>
<li>DFS</li>
<li>A*</li>
<li>Bayesian Networks</li>
<li>Minimax</li>
</ul>
""",
        "trace": [
            "Analyzing query",
            "Searching knowledge base",
            "No exact topic match",
            "Suggesting related topics"
        ]
    })


if __name__ == "__main__":
    app.run(debug=True)
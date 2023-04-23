'''
	AIM4 - Flask - [A] Basic - [02] Routing
	
	Orbit Future Academy - AI Mastery - KM Batch 4
	Tim Deployment
	2023
'''

# =[Modules dan Packages]========================
from flask import Flask
from flask_ngrok import run_with_ngrok

# =[Variabel Global]=============================
app = Flask(__name__)

# =[Routing]=====================================
@app.route("/")
def beranda():
    return "Halo Dunia ! Belajar AI di Orbit Future Academy"
	
@app.route("/belajar")
def belajar():
    return """
		   Di Program AI Mastery, siswa akan mempelajari : 
		   <ul>
		      <li> Pemograman Python </li>
			  <li> Dasar AI dan ML </li>
			  <li> Data Science </li>
			  <li> Computer Vision </li>
			  <li> Natural Language Processing </li>
			  <li> Reinforcement Learning </li>
			  <li> Deployment </li>
		   </ul>
		   """

# =[Main]========================================
if __name__ == '__main__':
    run_with_ngrok(app)
    app.run()
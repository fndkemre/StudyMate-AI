from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Motivasyon veritabanı
QUOTES = [
    "Başarı, her gün tekrarlanan küçük çabaların toplamıdır.",
    "Gelecek, bugünden hazırlananlara aittir.",
    "Yorgun olduğunda dinlenmeyi öğren, bırakmayı değil.",
    "Zirveye giden yol yokuştur ama manzarası güzeldir.",
    "Kendine inan, çünkü senin içinde düşündüğünden daha fazlası var.",
    "Bugün yapacağın her çalışma, yarınki başarının bir tuğlasıdır."
]

def generate_study_plan_logic(exam, duration, mood):
    """
    Plan oluşturma mantığı.
    """
    duration = int(duration)
    plan = []
    
    # Ruh haline göre yoğunluk ve mola ayarı
    if mood.lower() in ['yorgun', 'stresli', 'gergin']:
        study_block = 25
        break_time = 10
        tone = "light"
    elif mood.lower() in ['enerjik', 'mutlu', 'hırslı']:
        study_block = 45
        break_time = 10
        tone = "intense"
    else: # Normal
        study_block = 40
        break_time = 10
        tone = "normal"

    total_minutes = duration * 60
    current_time = 0
    
    while current_time < total_minutes:
        # Çalışma bloğu
        remaining = total_minutes - current_time
        actual_study = min(study_block, remaining)
        
        if actual_study > 0:
            plan.append({
                "type": "study",
                "duration": actual_study,
                "activity": f"{exam} Çalışması"
            })
            current_time += actual_study
        
        # Mola bloğu (son blok değilse)
        if current_time < total_minutes:
            plan.append({
                "type": "break",
                "duration": break_time,
                "activity": "Kısa Mola & Su İç"
            })
            current_time += break_time # Mola süreden yiyor mu? Genelde çalışmaya dahil edilmez ama basitlik için toplam süreye dahil edelim veya opsiyonel. 
            # Kullanıcı "3 saat çalışacağım" dediğinde 3 saatlik bir slot ayırırız.

    return plan, tone

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/generate_plan', methods=['POST'])
def generate_plan():
    data = request.json
    exam = data.get('exam', 'Genel')
    duration = data.get('duration', 2)
    mood = data.get('mood', 'Normal')

    plan, tone = generate_study_plan_logic(exam, duration, mood)
    quote = random.choice(QUOTES)

    return jsonify({
        "plan": plan,
        "quote": quote,
        "tone": tone
    })

if __name__ == '__main__':
    app.run(debug=True)

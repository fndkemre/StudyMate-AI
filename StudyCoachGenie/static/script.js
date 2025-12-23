document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('study-form');
    const inputSection = document.getElementById('input-section');
    const resultSection = document.getElementById('result-section');
    const planContainer = document.getElementById('plan-container');
    const quoteText = document.getElementById('quote-text');
    const resetButton = document.getElementById('reset-button');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const exam = document.getElementById('exam').value;
        const duration = document.getElementById('duration').value;
        // Radyo butonlarından seçili olanı al
        const mood = document.querySelector('input[name="mood"]:checked').value;

        // UI'da yükleniyor hissi verilebilir (Opsiyonel)
        document.querySelector('.cta-button').textContent = "Hazırlanıyor...";

        try {
            const response = await fetch('/api/generate_plan', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ exam, duration, mood }),
            });

            if (!response.ok) {
                throw new Error('Bir hata oluştu');
            }

            const data = await response.json();

            displayPlan(data);

            // Geçiş Animasyonu
            inputSection.classList.add('hidden');
            resultSection.classList.remove('hidden');

        } catch (error) {
            console.error('Hata:', error);
            alert('Plan oluşturulurken bir hata oluştu. Lütfen tekrar dene.');
        } finally {
            document.querySelector('.cta-button').textContent = "Planı Oluştur ✨";
        }
    });

    resetButton.addEventListener('click', () => {
        resultSection.classList.add('hidden');
        inputSection.classList.remove('hidden');
        planContainer.innerHTML = ''; // Temizle
    });

    function displayPlan(data) {
        quoteText.textContent = `"${data.quote}"`;
        planContainer.innerHTML = '';

        data.plan.forEach((item, index) => {
            const div = document.createElement('div');
            // Mola mı ders mi kontrolü
            const isBreak = item.type === 'break' ? 'break' : '';
            div.className = `plan-item ${isBreak}`;

            div.innerHTML = `
                <span class="activity-name">${item.activity}</span>
                <span class="time-badge">${item.duration} dk</span>
            `;

            // Animasyonlu giriş için (CSS'de ele alınabilir veya JS ile)
            div.style.opacity = '0';
            div.style.animation = `fadeInUp 0.5s ease-out ${index * 0.1}s forwards`;

            planContainer.appendChild(div);
        });
    }
});

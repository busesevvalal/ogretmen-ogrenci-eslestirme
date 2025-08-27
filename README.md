Amaç / Purpose:
Öğrencileri branş + seviye + bütçe kriterlerine göre en uygun öğretmenlerle eşleştiren, Python & Streamlit ile geliştirilmiş basit bir web uygulaması.

🇹🇷 Türkçe
🎯 Amaç

Öğrencilerin hedef branş (Türkçe, Matematik, İngilizce, Fen), seviye (İlkokul / Ortaokul) ve bütçe bilgilerine göre uygun öğretmenleri bulmak.

Uygun öğretmenler arasından puanı (rating) en yüksek olanı “en iyi öneri” olarak sunmak.

✨ Özellikler

👩‍🎓 Tek öğrenci seçip anlık öneri görme

📊 Tüm öğrenciler için toplu eşleşme sonuçları

⭐ Puanı en yüksek öğretmeni öne çıkarma

📥 Sonuçları CSV olarak indirebilme (opsiyonel)

🔧 Teknoloji

Python, Pandas, Streamlit

▶️ Hızlı Başlangıç (Yerel)
pip install -r requirements.txt
streamlit run app.py

📁 Veri Şeması (örnek)

teachers.csv

TeacherID	Branch	Level	HourlyRate	Location	Rating
T001	Türkçe	İlkokul	180	İstanbul	4.8

students.csv

StudentID	TargetBranch	TargetLevel	Budget
S001	Türkçe	İlkokul	200
🧠 Eşleştirme Kuralları

Branch tam eşleşmeli

Level tam eşleşmeli

HourlyRate ≤ Budget

“En iyi öneri”: Rating’e göre en yüksek olan

-----------------------------------------------

🇬🇧 English
🎯 Goal

Match students with teachers using subject + level + budget.

Among all valid teachers, show the highest-rated as the “best suggestion”.

✨ Features

👩‍🎓 Single-student instant recommendation

📊 Bulk matching for all students

⭐ Best teacher by rating

📥 Export results to CSV (optional)

🔧 Stack

Python, Pandas, Streamlit

▶️ Quick Start (Local)
pip install -r requirements.txt
streamlit run app.py

📁 Data Schema (sample)

teachers.csv

TeacherID	Branch	Level	HourlyRate	Location	Rating
T001	Turkish	Primary	180	Istanbul	4.8

students.csv

StudentID	TargetBranch	TargetLevel	Budget
S001	Turkish	Primary	200
🧠 Matching Rules

Branch must match

Level must match

HourlyRate ≤ Budget

“Best suggestion”: highest Rating

💡 Yol Haritası / Roadmap

Öğretmen uygunluk/rezervasyon durumu

Tercih edilen gün/saat filtreleri

Gelişmiş sıralama (deneyim, konum, vs.)

📄 Lisans / License

Bu proje eğitim amaçlı bir demodur. (İhtiyacına göre lisans metni ekleyebilirsin.)

🔗 Canlı Uygulama / Live App

(Streamlit adresini buraya ekleyebilirsin)

Amaç / Purpose:
Öğrencileri branş + seviye + bütçe kriterlerine göre en uygun öğretmenlerle eşleştiren, Python & Streamlit ile geliştirilmiş basit bir web uygulaması.

------------------------------------------------------------------------------------------------------------------------------------------------------

🎯 Amaç

Öğrencilerin hedef branş (Türkçe, Matematik, İngilizce, Fen), seviye (İlkokul / Ortaokul) ve bütçe bilgilerine göre uygun öğretmenleri bulmak.

Uygun öğretmenler arasından puanı (rating) en yüksek olanı “en iyi öneri” olarak sunmak.

----------------------------------------------------------------------------------------

✨ Özellikler

👩‍🎓 Tek öğrenci seçip anlık öneri görme

📊 Tüm öğrenciler için toplu eşleşme sonuçları

⭐ Puanı en yüksek öğretmeni öne çıkarma

📥 Sonuçları CSV olarak indirebilme (opsiyonel)

🔧 Teknoloji

---------------------------------------------

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



Bu proje eğitim amaçlı bir demodur. 

🔗 Canlı Uygulama / Live App

https://ogretmen-ogrenci-eslestirme-msx2qsappdkawbh9qwwcmz4.streamlit.app/

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Öğrenci–Öğretmen Eşleştirme", page_icon="🎓", layout="wide")

# ---------- Örnek veri ----------
teachers = pd.DataFrame({
    "TeacherID": ["T001","T002","T003","T004","T005","T006","T007","T008"],
    "Branch": ["Türkçe","Türkçe","Matematik","Matematik","İngilizce","İngilizce","Fen","Fen"],
    "Level": ["İlkokul","Ortaokul","İlkokul","Ortaokul","İlkokul","Ortaokul","İlkokul","Ortaokul"],
    "HourlyRate": [180,220,200,250,210,240,190,230],
    "Location": ["İstanbul","Ankara","İstanbul","İzmir","Bursa","İstanbul","Ankara","İzmir"],
    "Rating": [4.8,4.5,4.6,4.7,4.9,4.4,4.3,4.6]
})

students = pd.DataFrame({
    "StudentID": [f"S{i:03d}" for i in range(1,17)],
    "TargetBranch": ["Türkçe","Matematik","İngilizce","Fen",
                     "Türkçe","Matematik","İngilizce","Fen",
                     "Türkçe","Matematik","İngilizce","Fen",
                     "Türkçe","Matematik","İngilizce","Fen"],
    "TargetLevel": ["İlkokul","Ortaokul","İlkokul","Ortaokul",
                    "Ortaokul","İlkokul","Ortaokul","İlkokul",
                    "İlkokul","İlkokul","Ortaokul","Ortaokul",
                    "Ortaokul","Ortaokul","İlkokul","İlkokul"],
    "Budget": [200,260,220,240,210,230,250,180,190,270,210,260,200,280,240,220]
})

# ---------- Eşleştirme fonksiyonları ----------
def match_student(student, teachers_df):
    return teachers_df[
        (teachers_df["Branch"] == student["TargetBranch"]) &
        (teachers_df["Level"] == student["TargetLevel"]) &
        (teachers_df["HourlyRate"] <= student["Budget"])
    ]

def best_match_student(student, teachers_df):
    m = match_student(student, teachers_df)
    return m.sort_values("Rating", ascending=False).head(1) if not m.empty else m

# ---------- Arayüz ----------
st.title("🎓 Öğrenci – Öğretmen Eşleştirme")
st.caption("Kriterler: **Branş + Seviye + Bütçe** (lokasyon yok).")

tab1, tab2 = st.tabs(["🔍 Tek Öğrenci", "📊 Tüm Öğrenciler"])

with tab1:
    colA, colB = st.columns([1,2])
    with colA:
        sid = st.selectbox("Öğrenci seç", students["StudentID"])
        student = students[students["StudentID"] == sid].iloc[0]
        st.write("🎯 Hedef:", dict(student[["TargetBranch","TargetLevel","Budget"]]))

    with colB:
        st.subheader("Uygun Öğretmenler")
        matches = match_student(student, teachers)
        if matches.empty:
            st.warning("Uygun öğretmen bulunamadı.")
        else:
            st.dataframe(matches[["TeacherID","Branch","Level","HourlyRate","Rating"]], use_container_width=True)

        st.subheader("✅ En İyi Öneri (Rating’e göre)")
        best = best_match_student(student, teachers)
        if best.empty:
            st.info("Öneri yok")
        else:
            b = best.iloc[0]
            st.success(f"{b.TeacherID} · {b.Branch} · {b.Level} · {b.HourlyRate}₺/saat · ⭐ {b.Rating}")

with tab2:
    st.subheader("Toplu Eşleşme Sonuçları")
    rows = []
    for _, s in students.iterrows():
        m = match_student(s, teachers)
        best = best_match_student(s, teachers)
        rows.append({
            "StudentID": s["StudentID"],
            "FoundMatch": not m.empty,
            "NumMatches": len(m),
            "BestTeacher": None if best.empty else best["TeacherID"].values[0],
            "Branch": s["TargetBranch"],
            "Level": s["TargetLevel"]
        })
    results_df = pd.DataFrame(rows)
    st.dataframe(results_df, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Toplam Öğrenci", len(students))
        st.metric("Eşleşme Bulan Öğrenci", int(results_df["FoundMatch"].sum()))
    with col2:
        branch_counts = results_df[results_df["FoundMatch"]].groupby("Branch").size().reindex(
            ["Türkçe","Matematik","İngilizce","Fen"], fill_value=0
        )
        st.bar_chart(branch_counts, height=260)

    st.bar_chart(results_df.set_index("StudentID")["NumMatches"], height=260)

st.caption("© Eşleştirme demo – Streamlit")

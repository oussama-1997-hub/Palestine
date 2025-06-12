import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime

st.set_page_config(page_title="قافلة السموت نحو غزة", layout="wide")

# Advanced Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Cairo', sans-serif;
        background-color: #f3f4f6;
    }
    .hero {
        background-image: url('https://images.unsplash.com/photo-1633478088795-df6e8f2c137b');
        background-size: cover;
        background-position: center;
        color: white;
        padding: 5rem 2rem;
        text-align: center;
        border-radius: 1rem;
        margin-bottom: 3rem;
        box-shadow: 0 8px 30px rgba(0,0,0,0.2);
    }
    .hero h1 {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .hero p {
        font-size: 1.3rem;
    }
    .section {
        background-color: white;
        border-radius: 1rem;
        padding: 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.05);
    }
    .title {
        font-size: 2.2rem;
        color: #065f46;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #374151;
        margin-bottom: 1.5rem;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #6b7280;
        margin-top: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>🇵🇸 قافلة السموت نحو غزة</h1>
    <p>من تونس إلى غزة… صوتٌ للحرية، وعزمٌ لفك الحصار</p>
    <a href="#" style="padding: 0.8rem 2.5rem; background-color: #ffffffcc; color: #065f46; border-radius: 0.5rem; font-weight: bold; text-decoration: none;">📦 ساهم الآن</a>
</div>
""", unsafe_allow_html=True)

# Live Location
st.markdown("""
<div class="section">
  <div class="title">📍 تتبّع مباشر لموقع القافلة</div>
  <div class="subtitle">تابع تحركات القافلة لحظة بلحظة على الخريطة</div>
""", unsafe_allow_html=True)

m = folium.Map(location=[36.81881, 10.16579], zoom_start=6)
folium.Marker([36.81881, 10.16579], tooltip="آخر موقع معروف للقافلة").add_to(m)
st_folium(m, width=700, height=450)

st.markdown("</div>", unsafe_allow_html=True)

# Raise Your Voice
st.markdown("""
<div class="section">
  <div class="title">📢 ارفع صوتك</div>
  <div class="subtitle">أرسل رسالة تلقائية إلى برلمانات العالم والمنظمات الإنسانية لدعم القافلة وفك الحصار.</div>
""", unsafe_allow_html=True)

if st.button("✉️ أرسل رسالتك الآن"):
    st.success("✅ تم إرسال رسالتك بنجاح!")

st.markdown("</div>", unsafe_allow_html=True)

# Voices from Gaza
st.markdown("""
<div class="section">
  <div class="title">🎙️ أصوات من غزة</div>
  <div class="subtitle">شهادات حية من قلب المعاناة تسلّط الضوء على أهمية القافلة</div>
  <blockquote style="background:#ecfdf5; padding:1.2rem; border-left: 6px solid #10b981; font-style: italic;">
    "نحن ننتظر صوتكم... هذه القافلة ليست مجرد شاحنات، بل رسالة أمل لنا." – أم محمد، غزة
  </blockquote>
</div>
""", unsafe_allow_html=True)

# Solidarity Wall
st.markdown("""
<div class="section">
  <div class="title">✍️ حائط التضامن</div>
  <div class="subtitle">اكتب رسالتك لأهل غزة وسيتم إيصالها مع القافلة</div>
""", unsafe_allow_html=True)

msg = st.text_area("اكتب رسالتك هنا:", height=120)
if st.button("📨 أرسل الرسالة"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    st.success(f"✅ تم إرسال رسالتك بتاريخ {timestamp}!")

st.markdown("</div>", unsafe_allow_html=True)

# Global Event
st.markdown("""
<div class="section">
  <div class="title">🌍 ساعة الصمت من أجل غزة</div>
  <div class="subtitle">شارك في الحدث الرقمي العالمي للتضامن: ساعة من الصمت لرفع الوعي العالمي.</div>
""", unsafe_allow_html=True)

if st.button("🕊️ انضم الآن"):
    st.balloons()
    st.success("✅ تم تسجيل مشاركتك. شكراً لك!")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
  تم التطوير بدعم المتطوعين | 🇵🇸 الحرية لغزة ✊
</div>
""", unsafe_allow_html=True)

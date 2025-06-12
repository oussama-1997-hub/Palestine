import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime

st.set_page_config(page_title="قافلة السموت نحو غزة", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
    body { background-color: #f4f4f4; font-family: 'Cairo', sans-serif; }
    .hero {
        background: linear-gradient(90deg, #14532d 0%, #16a34a 100%);
        padding: 3rem;
        border-radius: 1rem;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section {
        background: white;
        padding: 2rem;
        border-radius: 1rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 14px rgba(0,0,0,0.1);
    }
    .title {
        font-size: 2rem;
        color: #14532d;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #333;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero">
    <h1>🇵🇸 قافلة السموت نحو غزة</h1>
    <p>من تونس إلى غزة… صوتٌ للحرية، وعزمٌ لفك الحصار</p>
    <a href="#" style="padding: 0.7rem 2rem; background-color: white; color: #14532d; border-radius: 0.5rem; text-decoration: none; font-weight: bold;">📦 ساهم الآن</a>
</div>
""", unsafe_allow_html=True)

# Live Location Tracker
st.markdown("""
<div class="section">
    <div class="title">📍 تتبّع مباشر لموقع القافلة</div>
    <div class="subtitle">تابع تحركات القافلة لحظة بلحظة على الخريطة</div>
""", unsafe_allow_html=True)

m = folium.Map(location=[36.81881, 10.16579], zoom_start=6)
folium.Marker([36.81881, 10.16579], tooltip="آخر موقع معروف للقافلة").add_to(m)
st_folium(m, width=700, height=400)

st.markdown("</div>", unsafe_allow_html=True)

# Raise Your Voice
st.markdown("""
<div class="section">
    <div class="title">📢 ارفع صوتك</div>
    <div class="subtitle">أرسل رسالة تلقائية إلى برلمانات العالم والمنظمات الإنسانية لدعم القافلة وفك الحصار.</div>
""", unsafe_allow_html=True)

if st.button("✉️ أرسل رسالتك الآن"):
    st.success("شكراً لدعمك! تم إرسال رسالتك التضامنية.")

st.markdown("</div>", unsafe_allow_html=True)

# Voices from Gaza
st.markdown("""
<div class="section">
    <div class="title">🎙️ أصوات من غزة</div>
    <div class="subtitle">شهادات حية من قلب المعاناة تسلّط الضوء على أهمية القافلة</div>
    <blockquote style="background:#f0fdf4; padding:1rem; border-left: 5px solid #16a34a;">
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

msg = st.text_area("اكتب رسالتك هنا:", height=100)
if st.button("📨 أرسل الرسالة"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    st.success(f"تم إرسال رسالتك بتاريخ {timestamp}!")

st.markdown("</div>", unsafe_allow_html=True)

# Global Event
st.markdown("""
<div class="section">
    <div class="title">🌍 ساعة الصمت من أجل غزة</div>
    <div class="subtitle">شارك في الحدث الرقمي العالمي للتضامن: ساعة من الصمت لرفع الوعي العالمي.</div>
""", unsafe_allow_html=True)

if st.button("🕊️ انضم الآن"):
    st.balloons()
    st.success("تم تسجيل مشاركتك. شكراً لك!")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; color: #555; padding: 2rem;">
    تم التطوير بدعم المتطوعين | 🇵🇸 الحرية لغزة ✊
</div>
""", unsafe_allow_html=True)

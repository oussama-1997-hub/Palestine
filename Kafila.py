import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="قافلة السموت نحو غزة", layout="wide")

# Hero Section
st.markdown("""
# 🇵🇸 قافلة السموت نحو غزة
من تونس إلى غزة… صوتٌ للحرية، وعزمٌ لفك الحصار
""")
st.button("📦 ساهم الآن")

st.markdown("---")

# Live Location Tracker
st.subheader("📍 تتبّع مباشر لموقع القافلة")
m = folium.Map(location=[36.81881, 10.16579], zoom_start=6)
folium.Marker([36.81881, 10.16579], tooltip="آخر موقع معروف للقافلة").add_to(m)
st_folium(m, width=700, height=450)

st.markdown("---")

# Raise Your Voice
st.subheader("📢 ارفع صوتك")
st.write("أرسل رسالة تلقائية إلى برلمانات العالم، سفاراتك، والمنظمات الإنسانية لدعم القافلة وفك الحصار.")
if st.button("✉️ أرسل رسالتك الآن"):
    st.success("شكراً لدعمك! تم إرسال رسالتك التضامنية.")

st.markdown("---")

# Voices from Gaza
st.subheader("🎙️ أصوات من غزة")
st.info("\"نحن ننتظر صوتكم... هذه القافلة ليست مجرد شاحنات، بل رسالة أمل لنا.\" – أم محمد، غزة")

st.markdown("---")

# Solidarity Wall
st.subheader("✍️ حائط التضامن")
message = st.text_area("اكتب رسالتك لأهل غزة وسيتم إيصالها مع القافلة:")
if st.button("📨 أرسل الرسالة"):
    st.success("تم إرسال رسالتك بنجاح!")

st.markdown("---")

# Global Event
st.subheader("🌍 ساعة الصمت من أجل غزة")
st.write("شارك في الحدث الرقمي العالمي للتضامن مع غزة: ساعة من الصمت العالمي لرفع الوعي.")
if st.button("🕊️ انضم الآن"):
    st.balloons()
    st.success("تم تسجيل مشاركتك في ساعة الصمت.")

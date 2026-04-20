import streamlit as st

st.header("📂 Projects")

projects = {
    "📂 Portfolio App": {
        "desc": "A Streamlit app that showcases my profile and projects.",
        "img": "https://via.placeholder.com/400"
    },
    "📊 ScanSafe System": {
        "desc": "This System is a digital solution designed to improve safety, monitoring, and record management using QR code technology. It allows institutions such as schools, barangays, or offices to efficiently track individuals’ attendance and movement in real time.",
       "img": "portfolio_app/Screenshot 2025-12-13 135827.png"
    },
    "🏫 Barangay Record System": {
        "desc": "A system is a digital solution designed to make barangay services faster, more organized, and accessible through mobile devices like smartphones or tablets. Instead of relying on manual records (paper-based), the system stores and manages data electronically, allowing barangay staff and sometimes residents to access important information anytime.",
        "img": "portfolio_app/mobile barangay records access system.png"
    }
}

for name, details in projects.items():
    st.subheader(name)
    st.write(details["desc"])
    st.image(details["img"], use_container_width=True)
  

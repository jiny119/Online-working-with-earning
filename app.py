import streamlit as st
import pandas as pd

# صارفین کا ڈیٹا بیس
users = {
    "admin": {"password": "admin123", "coins": 0, "refrels": 0, "clicks": 0}
}

# لاگ ان فنکشن
def login(username, password):
    if username in users and users[username]["password"] == password:
        return True
    return False

# سائن اپ فنکشن
def signup(username, password):
    if username not in users:
        users[username] = {"password": password, "coins": 0, "refrels": 0, "clicks": 0}
        return True
    return False

# Streamlit ایپ
st.title("🤑 Ads Watch, Survey, Gaming Task App")
st.sidebar.title("لاگ ان / سائن اپ")

# لاگ ان / سائن اپ کا سسٹم
choice = st.sidebar.selectbox("اپنا انتخاب کریں", ["لاگ ان", "سائن اپ"])

if choice == "لاگ ان":
    username = st.sidebar.text_input("یوزرنیم")
    password = st.sidebar.text_input("پاس ورڈ", type="password")
    if st.sidebar.button("لاگ ان"):
        if login(username, password):
            st.success(f"خوش آمدید, {username}!")
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("غلط یوزرنیم یا پاس ورڈ۔")

elif choice == "سائن اپ":
    new_username = st.sidebar.text_input("نیا یوزرنیم")
    new_password = st.sidebar.text_input("نیا پاس ورڈ", type="password")
    if st.sidebar.button("سائن اپ"):
        if signup(new_username, new_password):
            st.success("کامیابی سے سائن اپ ہو گیا ہے۔")
        else:
            st.error("یہ یوزرنیم پہلے سے موجود ہے۔")

# اگر صارف لاگ ان ہے
if st.session_state.get("logged_in"):
    username = st.session_state.username
    st.header(f"ڈیش بورڈ - {username}")
    st.write(f"آپ کے سکے: {users[username]['coins']}")
    st.write(f"ریفریلز: {users[username]['refrels']}")
    st.write(f"کلکس: {users[username]['clicks']}")

    # ٹاسک سسٹم
    st.subheader("ٹاسکز")
    task = st.selectbox("ٹاسک منتخب کریں", ["Ads Watch", "App Install", "Survey", "Gaming"])
    if st.button("ٹاسک مکمل کریں"):
        users[username]["coins"] += 5
        st.success("ٹاسک مکمل ہو گیا ہے! 5 سکے شامل کر دیے گئے ہیں۔")

    # ریفریل سسٹم
    st.subheader("ریفریلز")
    if st.button("ریفریل لنک کاپی کریں"):
        st.write("ریفریل لنک: https://example.com/ref/" + username)
    if users[username]["refrels"] >= 10 and users[username]["clicks"] >= 5:
        st.success("ریفریلز اور کلکس مکمل ہو گئے ہیں!")

    # نکالنے کا سسٹم
    st.subheader("نکالنے کی درخواست")
    withdrawal_amount = st.number_input("سکے کی تعداد درج کریں", min_value=15000)
    withdrawal_method = st.selectbox("نکالنے کا طریقہ", ["JazzCash", "EasyPaisa", "Payoneer", "PayPal"])
    if st.button("نکالنے کی درخواست کریں"):
        if users[username]["coins"] >= withdrawal_amount:
            users[username]["coins"] -= withdrawal_amount
            st.success(f"نکالنے کی درخواست کامیابی سے جمع کر دی گئی ہے۔ طریقہ: {withdrawal_method}")
        else:
            st.error("کم از کم 15,000 سکے درکار ہیں۔")

    # شیئر کا بٹن
    st.subheader("شیئر کریں")
    st.write("اپنے دوستوں کے ساتھ شیئر کریں اور مزید سکے کمائیں!")
    st.button("شیئر کریں")

# اگر صارف لاگ ان نہیں ہے
else:
    st.warning("براہ کرم لاگ ان یا سائن اپ کریں۔")

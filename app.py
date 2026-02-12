import streamlit as st
import random

# إعدادات الصفحة
st.set_page_config(page_title="Harreef Games", page_icon="🪓")

# قائمة الكلمات
words_list = ["PYTHON", "ANDROID", "GITHUB", "STREAMLIT", "HARREEF", "MOBILE", "INTELLIGENCE", "GAMES", "DEVELOPER"]

# تهيئة اللعبة
if 'word' not in st.session_state:
    st.session_state.word = random.choice(words_list)
    st.session_state.guessed_letters = set()
    st.session_state.attempts = 6 # البداية بـ 6 محاولات

def reset_entire_game():
    st.session_state.word = random.choice(words_list)
    st.session_state.guessed_letters = set()
    st.session_state.attempts = 6

# الواجهة
st.title("🪓 لعبة الرجل المشنوق")
st.sidebar.markdown(f"### المبرمج: **Harreef** 😎")

# عرض الكلمة
display_word = "".join([l if l in st.session_state.guessed_letters else " _ " for l in st.session_state.word])
st.header(display_word)
st.write(f"المحاولات المتبقية: **{st.session_state.attempts}** ❤️")

# إدخال الحروف
if st.session_state.attempts > 0:
    input_letter = st.text_input("خمن حرف:", max_chars=1, key="input").upper()
    if st.button("تخمين"):
        if input_letter and input_letter not in st.session_state.guessed_letters:
            st.session_state.guessed_letters.add(input_letter)
            if input_letter not in st.session_state.word:
                st.session_state.attempts -= 1
            st.rerun()

# التحقق من الفوز
if all(l in st.session_state.guessed_letters for l in st.session_state.word):
    st.balloons()
    st.success(f"عبقري يا Harreef! الكلمة هي: {st.session_state.word}")
    if st.button("كلمة جديدة"):
        reset_entire_game()
        st.rerun()

# التحقق من الخسارة (هنا التعديل اللي طلبته)
elif st.session_state.attempts <= 0:
    st.error(f"للاسف المحاولات خلصت!")
    if st.button("إضافة 5 محاولات جديدة ➕"):
        st.session_state.attempts = 5  # هيديك 5 محاولات وتكمل نفس الكلمة
        st.rerun()
    
    if st.button("استسلام (كلمة جديدة)"):
        reset_entire_game()
        st.rerun()
      

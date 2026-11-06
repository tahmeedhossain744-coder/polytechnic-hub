import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="CST Campus Hub - Pabna Polytechnic Institute",
    page_icon="💻",
    layout="centered",
)

# Custom CSS Styling (Dark Theme & Colors matching your design)
st.markdown(
    """
    <style>
        :root {
            --bg-color: #0d1117;
            --card-bg: #161b22;
            --accent-gold: #d4af37;
            --text-color: #f0f6fc;
            --text-secondary: #8b949e;
            --border-color: #30363d;
        }
        .stApp {
            background-color: var(--bg-color);
            color: var(--text-color);
        }
        .hero {
            text-align: center;
            padding: 30px;
            background: linear-gradient(180deg, rgba(212, 175, 55, 0.1) 0%, rgba(13, 17, 23, 0) 100%);
            border-radius: 12px;
            border: 1px solid var(--border-color);
            margin-bottom: 20px;
        }
        h1, h2, h3 {
            color: var(--accent-gold) !important;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Header Section
st.markdown(
    "<h2 style='color: #d4af37; display: flex; justify-content: space-between;'><span>💻 CST Campus Hub</span></h2>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Hero Section
st.markdown(
    """
    <div class="hero">
        <h1>পাবনা সরকারি পলিটেকনিক ইনস্টিটিউট</h1>
        <p>কম্পিউটার সায়েন্স অ্যান্ড টেকনোলজি (1st--CST) — গ্রুপ B</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Main Grid Layout (Using Streamlit Columns)
col1, col2 = st.columns(2)

with col1:
    # Notice Board
    st.markdown("### 📌 নোটিশ বোর্ড")
    st.info(
        "* ১ম সেমিস্টার ক্লাস টেস্টের সময়সূচী প্রকাশিত হয়েছে।\n\n"
        "* ল্যাব প্র্যাকটিক্যাল অ্যাসাইনমেন্ট জমা দিন।\n\n"
        "* CST গ্রুপের নতুন ওয়েবসাইট লঞ্চ করা হয়েছে।\n\n"
        "* নতুন প্রজেক্ট টিমের সাথে পরিচিত হোন।\n\n"
        "* আগামী সপ্তাহে সেমিস্টার ফাইনাল পরীক্ষা অনুষ্ঠিত হবে।\n"
        "আগামী ০৭ তারিখ রোজ বৃহস্পতিবার থেকে ১২ তারিখ রোজ রবিবার পর্যন্ত কলেজ বন্ধ থাকবে। "
        "তাই সকল শিক্ষার্থীকে অনুরোধ করা হচ্ছে যে, এই সময়ের মধ্যে সকল অ্যাসাইনমেন্ট এবং প্রজেক্ট তৈরি করবেন। "
        "আর ১৩ তারিখ রোজ সোমবার থেকে ক্লাস শুরু হবে। সকল শিক্ষার্থীকে অনুরোধ করা হচ্ছে যে সকলেই সবার অ্যাসাইনমেন্ট এবং প্রজেক্ট জমা দিবেন।\n\n"
        "* সকল্কে সবাই নিজেদের উপবিত্তির জন্য প্রদান ক্রিত বিকাশ, নগদ, রকেট এবং ব্যাংক একাউন্টের স্টেটমেন্ট জমা দেওয়ার জন্য অনুরোধ করা হল।"
    )

    # Quick Action
    st.markdown("### 🔗 কুইক অ্যাকশন সবাইকেই অংশগ্রহন করতে হবে")
    if st.button("নোটিফিকেশন অন করুন"):
        st.success("সফল! আপডেট লাইভ দেওয়া হয়েছে!")
        st.info(
            "আপনি এখন থেকে নতুন নোটিশ এবং রুটিন আপডেট পাবেন।\n\n"
            "আপডেটের জন্য ধন্যবাদ! আপনার CST AI সহকারী।"
        )
        st.markdown(
            "আমদের সাথে যোগাযোগ করুন: [CST AI সহকারী](https://www.cstprotel.com)"
        )
        st.markdown(
            "আমাদের টিমের সাথে যোগাযোগ করুন: [tahmeed](whatsapp://send?phone=01341725738) / [tahmeed](https://www.linkedin.com/in/tahmeed/) / [nirab](https://www.linkedin.com/in/nirab-rahman-2b0a1b1b3/)"
        )

with col2:
    # Routine
    st.markdown("### 📅 ক্লাস রুটিন")
    st.markdown(
        """
        - ১০:০০ AM - Computer Application  
        - ১১:০০ AM - Basic Electronics  
        - ১২:০০ PM - Mathematics-1  
        - ১২:৩০ PM - Mathematics-2  
        - ০১:০০ PM - Lunch Break  
        - ০২:০০ PM - Physics-1  
        - ০২:৩০ PM - Physics-2  
        - ০৩:০০ PM - Chemistry-1  
        - ০৩:৩০ PM - Chemistry-2  
        - ০৪:০০ PM - English-1  
        - ০৪:৩০ PM - English-2  
        - ০৫:০০ PM - Engineering Drawing  
        - ০৫:০০ PM - Programming Fundamentals  
        - ০৬:০০ PM - Lab Session  
        - ০৭:০০ PM - End of Day  
        - ০৮:০০ PM - Optional Study Time  
        - ০৯:০০ PM - Group Discussion  
        - ১০:০০ PM - Wrap Up and Review  
        - ১১:০০ PM - End of Routine  
        - ১২:০০ AM - Night Study (Optional)  
        - ০১:০০ AM - Sleep Time  
        - ০২:০০ AM - Midnight Snack (Optional)  
        - ০৩:০০ AM - Late Night Study (Optional)  
        - ০৪:০০ AM - Early Morning Exercise (Optional)  
        - ০৫:০০ AM - Breakfast  
    """
    )

# AI Chat Section
st.markdown("---")
st.markdown("### 🤖 CST AI সহকারী")

# Initialize chat history in session state if not exists
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "হ্যালো! আমি আপনার CST AI সহকারী। রুটিন বা নোটিশ সম্পর্কে কিছু জানতে চান?",
        }
    ]

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input for AI Chat
if user_text := st.chat_input("কিছু জিজ্ঞেস করুন..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # Generate AI response logic
    text_lower = user_text.lower()
    if "routine" in text_lower or "রুটিন" in text_lower:
        ai_reply = "আজকের রুটিনে ১০টায় Computer Application এবং ১১টায় Basic Electronics ক্লাস রয়েছে!"
    elif "notice" in text_lower or "নোটিশ" in text_lower:
        ai_reply = (
            "নতুন নোটিশ অনুযায়ী আগামী সপ্তাহে সেমিস্টার ফাইনাল পরীক্ষা অনুষ্ঠিত হবে এবং আগামী ৭ থেকে ১২ তারিখ পর্যন্ত কলেজ বন্ধ থাকবে।"
        )
    elif "team" in text_lower or "টিম" in text_lower:
        ai_reply = "এই প্রজেক্টের টিম মেম্বাররা হলেন: তাহমিদ (Software Engineer), নিরব (Project Manager), mehedi (UI/UX Designer), এবং prithibi (Backend Developer)।"
    else:
        ai_reply = "দুঃখিত, আমি এই মুহূর্তে অফলাইনে আছি। তবে টিম খুব শীঘ্রই আমাকে ফুল-স্ট্যাক AI হিসেবে আপডেট করবে!"

    # Append AI response
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_reply}
    )
    with st.chat_message("assistant"):
        st.markdown(ai_reply)

# Team Section
st.markdown("---")
st.markdown(
    "<h3 style='text-align: center;'>🚀 প্রজেক্ট টিম</h3>", unsafe_allow_html=True
)

t_col1, t_col2, t_col3, t_col4 = st.columns(4)
with t_col1:
    st.markdown(
        """
        <div style="background-color: #161b22; padding: 12px; border-radius: 8px; border: 1px solid #30363d; text-align: center;">
            <h4>তাহমিদ</h4>
            <p style="color: #d4af37; font-weight: bold; font-size: 13px;">Software Engineer</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

with t_col2:
    st.markdown(
        """
        <div style="background-color: #161b22; padding: 12px; border-radius: 8px; border: 1px solid #30363d; text-align: center;">
            <h4>নিরব</h4>
            <p style="color: #d4af37; font-weight: bold; font-size: 13px;">Project Manager</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

with t_col3:
    st.markdown(
        """
        <div style="background-color: #161b22; padding: 12px; border-radius: 8px; border: 1px solid #30363d; text-align: center;">
            <h4>mehedi</h4>
            <p style="color: #d4af37; font-weight: bold; font-size: 13px;">UI/UX Designer</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

with t_col4:
    st.markdown(
        """
        <div style="background-color: #161b22; padding: 12px; border-radius: 8px; border: 1px solid #30363d; text-align: center;">
            <h4>prithibi</h4>
            <p style="color: #d4af37; font-weight: bold; font-size: 13px;">Backend Developer</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
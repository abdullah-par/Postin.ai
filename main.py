import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="🪶",
    layout="centered"
)

# ---------- CUSTOM STYLES ----------
st.markdown(
    """
    <style>
        /* Page container */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 700px;
        }

        /* Dropdowns */
        div[data-baseweb="select"] > div {
            border-radius: 10px;
        }

        /* Button style */
        div.stButton > button:first-child {
            background-color: #0073e6;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 0.6em 1.5em;
            transition: 0.3s;
        }
        div.stButton > button:first-child:hover {
            background-color: #005bb5;
            color: white;
            transform: translateY(-2px);
        }

        /* Generated post box */
        .generated-post {
            background: #f8f9fa;
            padding: 1.2em 1.5em;
            border-radius: 10px;
            margin-top: 1em;
            font-size: 1.05rem;
            line-height: 1.6;
            color: #222;
        }

        /* Footer */
        .footer {
            margin-top: 3rem;
            text-align: center;
            font-size: 0.9rem;
            color: #666;
        }

        .footer a {
            color: #0073e6;
            text-decoration: none;
            margin: 0 6px;
        }

        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- MAIN APP ----------
def main():
    st.markdown("## 🪶 LinkedIn Post Generator")
    st.caption("Generate Codebasics-style posts effortlessly.")

    fs = FewShotPosts()
    tags = fs.get_tags()

    col1, col2, col3 = st.columns(3)
    with col1:
        selected_tag = st.selectbox("Topic", options=tags)
    with col2:
        selected_length = st.selectbox("Length", options=["Short", "Medium", "Long"])
    with col3:
        selected_language = st.selectbox("Language", options=["English", "Hinglish"])

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("✨ Generate Post"):
        with st.spinner("Crafting your post..."):
            post = generate_post(selected_length, selected_language, selected_tag)
        st.markdown(f"<div class='generated-post'>{post}</div>", unsafe_allow_html=True)

    # Footer with your links
    st.markdown(
        """
        <div class="footer">
            Built with ❤️ using Streamlit<br>
            <a href="https://linkedin.com/in/abdullah-parvez-565693246/" target="_blank">LinkedIn</a> |
            <a href="https://github.com/abdullah-par" target="_blank">GitHub</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------- RUN ----------
if __name__ == "__main__":
    main()

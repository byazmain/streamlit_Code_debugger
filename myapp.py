import streamlit as st
from function_api import issue_generator
from function_api import solve_generator


st.title("Code Debugger")
st.subheader("Upload Snapshot of Code and Debug it...")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader("Upload the photos of you code",
                     type=['png','jpeg','jpg'],
                     accept_multiple_files=True)
    st.subheader("Uploaded Images")
    if images:
        if len(images)>3:
            st.error("Warning : Upload 3 images max")
        col = st.columns(len(images))
        for i,img in enumerate(images):
            with col[i]:
                st.image(img)

    process = st.selectbox("How you want to solve the problem",
                           ("Hints","Solution with code"),
                           index=None)
    pressed = st.button("Click to initiate the AI",type="primary")
    if pressed:
        if images == None:
            st.error("Please upload Images")
        if process == None:
            st.error("Please choose the way you want to solve")
if images and process and pressed : 
    with st.container(border=2):
        st.subheader("Issues")
        with st.spinner("AI is thinking..."):
            st.write(issue_generator(images))

            
    with st.container(border=2):
        st.subheader(f"{process}")
        with st.spinner("AI is thinking...") :
            st.write(solve_generator(images,process))

            
            

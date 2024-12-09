import streamlit as st
st.set_page_config(
    page_title="Home",
)

st.header("More Than Studying in South Korea")
st.write("We are students at the University of Utah who studied abroad at the University of Utah Asia Campus, which is located in Incheon, South Korea, during the fall of 2024.")
st.write("Our goal in this blog is to create a place where people can enjoy our experiences as much as we have. Check out our personalized recommendations, frequently asked questions, and leave your own reviews for others to consider.")
st.write("We are Z and Lucy and we will be your virtual tour guides!")
st.divider()

st.header("The University of Utah Asia Campus")
details = "The University of Utah Asia Campus, or UAC, is located in Incheon, South Korea. This campus is a sister campus to the main University of Utah Campus in Salt Lake City, Utah. For students who are enrolled full-time at UAC, one year of education at the Salt Lake City campus is required. However, students enrolled at the main campus are not required to attend UAC at all. "
st.write(details)
details = "The UAC is a great option for students at the main campus who want to study abroad, as it an affordable option and it allows students to stay connected to their home campus while abroad."
st.write(details)
st.divider()

st.markdown("<p style='text-align: center;'>Learn More About Us Below!</p>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
   st.header("Lucy")
   st.image("LucyImage.JPG")
   details = "Lucy is a third year student studying Marketing with a minor in Parks, Recreation, and Tourism. She loves all things outdoors, including hiking, skiing, hiking, running, and camping. Her favorite animal is a moose because of their cool personalities. Lucy has always dreamed of studying abroad and she is thankful that the University of Utah has this affordable study abroad option available. Coming to South Korea was Lucy's first time in Asia and she has fallen in love with it."
   st.write(details)

with col2:
    st.header("Z")
    st.image("Zpic.jpeg.JPG")
    details = "Z is currently completing her final year of University with a major in Information Systems. Z enjoys figure skating, drawing, and playing the piano. Her favorite animal is a house cat because they are the best pet. Z chose to study abroad at the University of Utah Asia Campus because of the affordability and because she wanted the opportunity to live in South Korea. After spending the semester in South Korea, Z has a desire to live in Asia permanently at some point of her life."
    st.write(details)


st.sidebar.success("Choose a page above.")
import streamlit as st

# page setup
about_page = st.Page(
    page= "view/home_page.py",
    title= "Home Page" ,
    icon= ":material/account_circle:",
    default= True,
)

project_1_page=st.Page(
    page= "view/lost_at_sea.py",
    title= "Lost at sea",
    icon= ":material/person_search:",
)

project_2_page= st.Page(
    page="view/beacon.py",
    title="Bushland Beacon",
    icon= ":material/e911_emergency:",
)


# Navigation setup
# pg = st.navigation(pages=[about_page, project_1_page,  project_2_page])

# Navigation setup with section
pg = st.navigation(
    {
    "Info": [about_page],
    "Demo":[ project_1_page,  project_2_page]
    }
)
pg.run()


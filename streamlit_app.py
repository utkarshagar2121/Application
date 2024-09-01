import streamlit as st
from pdf_creator1 import generate_pdf1
from pdf_creator2 import generate_pdf2
from pdf_creator3 import generate_pdf3
from io import BytesIO

def intro():
    import streamlit as st

    st.write("# Welcome to Application Maker! 👋")
    st.sidebar.success("Select an Application Type above.")

    st.markdown(
        """

        **👈 Select a Application Type from the dropdown on the left**

        ### What this app do?

        - This app generates PDFs for different types of applications.
        - You can select the type of application you want to generate from the dropdown on the left.
        - Fill the form and click on the "Generate PDF" button to get the PDF.
        - Click on the "Download PDF" button to download the PDF.
        - You can also add multiple participants or requirements in the form.
        - The PDF will be generated with the details you have filled in the form.
        - You can generate PDFs for the following types of applications:
            - Request for Attendance for the Event 
            - Request for Approval to Print Standee Poster for Event
            - Request for the requirements for Event

        ### Future Scope:
        - We will be adding more types of applications in the future.
        - We will soon be adding Data Analysis and Visualization features to the app.Through data analysis, we can Automate the process of Data and Information
        - If you have any suggestions or feedback, feel free to reach out to us.
            📨 utkarshagar21@gmail.com
    """
    )


# Function for "Request for attendance for the Event" page
def attendance_request():
    st.title("Request for Attendance for the Event")
    club=st.selectbox("Club",options=["Megapixel","HID Club","Green Golden Society"],index=None,placeholder="Select Club")    
    to_line_1 = st.text_input("Reciepient Designation",placeholder="Reciepient Designation")
    to_line_2 = st.text_input("Reciepient Address",value="NIET")
    respected = st.text_input("Greetings",placeholder="Respected sir/madam")
    event_name = st.text_input("Event Name",placeholder="Event Name")
    event_date = st.date_input("Event Date",value=None)
    start_time = st.time_input("Event Start Time",value=None)
    end_time = st.time_input("Event End Time",value=None)
    location = st.text_input("Event Location",placeholder="Event Location")
    sincerely = st.text_input("Sender's Name")
    sincerely_post = st.text_input("Sender's Designation")

    if club=="Megapixel":
        logo_loc="megapixel.png"
    elif club=="HID Club":
        logo_loc="HID.png"
    elif club=="Green Golden Society":
        logo_loc="GGC.png"

    # Participants Form
    if 'participants' not in st.session_state:
        st.session_state.participants = []
    st.markdown("### Participants")
    with st.form(key='participant_form', clear_on_submit=True):
        st.markdown("Fill the details of the participants below:")
        name = st.text_input("Name",placeholder="Name")
        branch = st.text_input("Branch",placeholder="Branch")
        roll_number = st.text_input("Roll Number",placeholder="Roll Number")
        st.markdown("""👇Click on the button to add Participant""")
        add_participant_button = st.form_submit_button("Add Participant")
        
        if add_participant_button and name and branch and roll_number:
            st.session_state.participants.append({
                'name': name,
                'branch': branch,
                'roll_number': roll_number
            })
            st.success("Participant added successfully!")

    st.write("Current Participants:")
    for participant in st.session_state.participants:
        st.write(f"Name: {participant['name']}, Branch: {participant['branch']}, Roll Number: {participant['roll_number']}")

    if st.button("Generate PDF"):
        data = {
            'to_line_1': to_line_1,
            'to_line_2': to_line_2,
            'subject': "Request for attendance for the Event",
            'respected': respected,
            'event_name': event_name,
            'event_date': event_date.strftime('%Y-%m-%d'),
            'start_time': start_time.strftime('%H:%M'),
            'end_time': end_time.strftime('%H:%M'),
            'location': location,
            'sincerely': sincerely,
            'sincerely_post': sincerely_post,
            'participants': st.session_state.participants,
            'logo_loc': logo_loc
        }
        pdf_output = generate_pdf1(data)
        st.success("PDF generated successfully!")
        st.download_button(
            label="Download PDF",
            data=pdf_output,
            file_name="attendance_request.pdf",
            mime="application/pdf"
        )

# Function for "Request for Approval to Print Standee Poster for Event" page
def approval_request():
    st.title("Request for Approval to Print Standee Poster for Event")
    club=st.selectbox("Club",options=["Megapixel","HID Club","Green Golden Society"],index=None,placeholder="Select Club")    
    to_line_1 = st.text_input("Reciepient Designation",placeholder="Reciepient Designation")
    to_line_2 = st.text_input("Reciepient Address",value="NIET")
    respected = st.text_input("Greetings",placeholder="Respected sir/madam")
    event_name = st.text_input("Event Name",placeholder="Event Name")
    poster_size = st.selectbox("Poster Size", options=["2x3 feet", "3x4 feet", "4x5 feet"],index=None,placeholder="Select Poster Size")
    quantity = st.number_input("Number of Posters", min_value=1, max_value=100, value=1, step=1, format="%d")
    sincerely = st.text_input("Sender's Name")
    sincerely_post = st.text_input("Sender's Designation")

    if club=="Megapixel":
        logo_loc="megapixel.png"
    elif club=="HID Club":
        logo_loc="HID.png"
    elif club=="Green Golden Society":
        logo_loc="GGC.png"

    if st.button("Generate PDF"):
        data = {
            'to_line_1': to_line_1,
            'to_line_2': to_line_2,
            'subject': "Request for Approval to Print Standee Poster for Event",
            'respected': respected,
            'event_name': event_name,
            'poster_size': poster_size,
            'quantity': quantity,
            'sincerely': sincerely,
            'sincerely_post': sincerely_post,
            'logo_loc': logo_loc
        }
        pdf_output = generate_pdf2(data)
        st.success("PDF generated successfully!")
        st.download_button(
            label="Download PDF",
            data=pdf_output,
            file_name="approval_request.pdf",
            mime="application/pdf"
        )

# Function for "Request for the requirements for Event" page
def requirements_request():
    st.title("Request for the Requirements for Event")
    club=st.selectbox("Club",options=["Megapixel","HID Club","Green Golden Society"],index=None,placeholder="Select Club")    
    to_line_1 = st.text_input("Reciepient Designation",placeholder="Reciepient Designation")
    to_line_2 = st.text_input("Reciepient Address",value="NIET")
    respected = st.text_input("Greetings",placeholder="Respected sir/madam")
    event_name = st.text_input("Event Name",placeholder="Event Name")
    event_date = st.date_input("Event Date",value=None)
    start_time = st.time_input("Event Start Time",value=None)
    end_time = st.time_input("Event End Time",value=None)
    sincerely = st.text_input("Sender's Name")
    sincerely_post = st.text_input("Sender's Designation")

    if club=="Megapixel":
        logo_loc="megapixel.png"
    elif club=="HID Club":
        logo_loc="HID.png"
    elif club=="Green Golden Society":
        logo_loc="GGC.png"

    
    # Requirements Form
    if 'requirements' not in st.session_state:
        st.session_state.requirements = []

    with st.form(key='requirement_form', clear_on_submit=True):
        st.write("Add Requirements")
        requirement_name = st.text_input("Requirement")
        quantity = st.number_input("Quantity", min_value=1, step=1)
        add_requirement_button = st.form_submit_button("Add Requirement")
        
        if add_requirement_button and requirement_name:
            st.session_state.requirements.append({
                'requirement_name': requirement_name,
                'quantity': quantity
            })
            st.success("Requirement added successfully!")

    st.write("Current Requirements:")
    for requirement in st.session_state.requirements:
        st.write(f"Requirement: {requirement['requirement_name']}, Quantity: {requirement['quantity']}")

    if st.button("Generate PDF"):
        data = {
            'to_line_1': to_line_1,
            'to_line_2': to_line_2,
            'subject': "Request for the requirements for Event",
            'respected': respected,
            'event_name': event_name,
            'event_date': event_date.strftime('%Y-%m-%d'),
            'start_time': start_time.strftime('%H:%M'),
            'end_time': end_time.strftime('%H:%M'),
            'requirements': st.session_state.requirements,
            'sincerely': sincerely,
            'sincerely_post': sincerely_post,
            'logo_loc': logo_loc
        }
        pdf_output = generate_pdf3(data)
        st.success("PDF generated successfully!")
        st.download_button(
            label="Download PDF",
            data=pdf_output,
            file_name="requirements_request.pdf",
            mime="application/pdf"
        )

st.sidebar.title("Application Generator")
# page = st.sidebar.selectbox(
#     "Choose a subject:",
#     options=[
#         "Attendence Application",
#         "Poster Request for Standie",
#         "Requirement Request for Event"
#     ]
# )

page_names_to_funcs = {
    "—": intro,
    "Attendence Application": attendance_request,
    "Poster Request for Standie": approval_request,
    "Requirement Request for Event": requirements_request
}

page_name = st.sidebar.selectbox("Choose a type of Application", page_names_to_funcs.keys())
page_names_to_funcs[page_name]()


# # Page selection based on the user's choice
# if page == "Attendence Application":
#     attendance_request()
# elif page == "Poster Request for Standie":
#     approval_request()
# elif page == "Requirement Request for Event":
#     requirements_request()

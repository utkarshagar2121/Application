import streamlit as st
from pdf_creator1 import generate_pdf1
from pdf_creator2 import generate_pdf2
from pdf_creator3 import generate_pdf3
from io import BytesIO

# Inject custom CSS
st.markdown("""
    <style>
    /* Body background color */
    .reportview-container {
        background-color: #f5f5f5;
    }
    /* Sidebar background color */
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    /* Title font color */
    .css-1d391kg {
        color: #007bff;
    }
    /* Subtitle font color */
    .css-1v0mbdj {
        color: #333;
    }
    /* Button style */
    .stButton>button {
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# Function for "Request for attendance for the Event" page
def attendance_request():
    st.title("Request for Attendance for the Event")
    
    to_line_1 = st.text_input("To Line 1")
    to_line_2 = st.text_input("To Line 2")
    respected = st.text_input("Respected")
    event_name = st.text_input("Event Name")
    event_date = st.date_input("Event Date")
    start_time = st.time_input("Event Start Time")
    end_time = st.time_input("Event End Time")
    location = st.text_input("Event Location")
    sincerely = st.text_input("Sincerely")
    sincerely_post = st.text_input("Sincerely Post")

    # Participants Form
    if 'participants' not in st.session_state:
        st.session_state.participants = []
        
    with st.form(key='participant_form', clear_on_submit=True):
        st.write("Add Participants")
        name = st.text_input("Name")
        branch = st.text_input("Branch")
        roll_number = st.text_input("Roll Number")
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
            'participants': st.session_state.participants
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
    
    to_line_1 = st.text_input("To Line 1")
    to_line_2 = st.text_input("To Line 2")
    respected = st.text_input("Respected")
    event_name = st.text_input("Event Name")
    poster_size = st.selectbox("Poster Size", options=["2x3 feet", "3x4 feet", "4x5 feet"])
    quantity = st.number_input("Number of Posters", min_value=1, max_value=100, value=1, step=1)
    purpose = st.text_area("Purpose of Printing")
    sincerely = st.text_input("Sincerely")
    sincerely_post = st.text_input("Sincerely Post")

    if st.button("Generate PDF"):
        data = {
            'to_line_1': to_line_1,
            'to_line_2': to_line_2,
            'subject': "Request for Approval to Print Standee Poster for Event",
            'respected': respected,
            'event_name': event_name,
            'poster_size': poster_size,
            'quantity': quantity,
            'purpose': purpose,
            'sincerely': sincerely,
            'sincerely_post': sincerely_post,
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
    
    to_line_1 = st.text_input("To Line 1")
    to_line_2 = st.text_input("To Line 2")
    respected = st.text_input("Respected")
    event_name = st.text_input("Event Name")
    event_date = st.date_input("Event Date")
    start_time = st.time_input("Event Start Time")
    end_time = st.time_input("Event End Time")
    sincerely = st.text_input("Sincerely")
    sincerely_post = st.text_input("Sincerely Post")

    
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
            'sincerely_post': sincerely_post
        }
        pdf_output = generate_pdf3(data)
        st.success("PDF generated successfully!")
        st.download_button(
            label="Download PDF",
            data=pdf_output,
            file_name="requirements_request.pdf",
            mime="application/pdf"
        )

st.sidebar.title("PDF Generator")
page = st.sidebar.selectbox(
    "Choose a subject:",
    options=[
        "Request for attendance for the Event",
        "Request for Approval to Print Standee Poster for Event",
        "Request for the requirements for Event"
    ]
)

# Page selection based on the user's choice
if page == "Request for attendance for the Event":
    attendance_request()
elif page == "Request for Approval to Print Standee Poster for Event":
    approval_request()
elif page == "Request for the requirements for Event":
    requirements_request()

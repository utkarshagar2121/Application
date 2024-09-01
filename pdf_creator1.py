# Attendence Application
from base64 import encode
from fpdf import FPDF
from date import get_date
from date import format_event_date
from io import BytesIO

# data={to_line_1: "To Line 1", to_line_2: "To Line 2", subject: "Request for attendance for the Event", respected: "Respected", event_name: "Event Name", event_date: "Event Date", start_time: "Start Time", end_time: "End Time", location: "Location", participants: "Participants"}

class PDF(FPDF):
    def add_text(self, text, fstyle='', cell_type='', text_align='L'):
        """Adds text in desired letter format to the PDF page
        Parameters:
        argument1 (string): Text to be added"""
        self.set_font("Arial", style=fstyle, size=15)

        if cell_type == 'm':
            self.multi_cell(0, 7, txt=text, align=text_align)
        else:
            self.cell(0, 7, txt=text, ln=True, align=text_align)

def generate_pdf1(data):
    pdf = PDF(orientation="portrait", format="letter")
    pdf.add_page()
    # pdf.add_font("Inter", style='', fname=r"inter\static\\Inter_18pt-Medium.ttf", uni=True)
    # pdf.add_font("Inter", style='B', fname=r"inter\static\\Inter_18pt-SemiBold.ttf", uni=True)
    pdf.set_x(25)
    pdf.set_y(50)
    pdf.set_left_margin(12.5)

    pdf.set_line_width(.8)
    pdf.line(7, 0, 7, 500)

    pdf.image('circle.png', 175, 10, 25)
    pdf.image('NIET New Logo Engineering.png',12,15,35)

    pdf.add_text("To", 'b')
    pdf.add_text(data['to_line_1'], 'b')
    pdf.add_text(data['to_line_2'], 'b')
    pdf.add_text("")
    pdf.add_text(get_date())
    pdf.add_text("")
    pdf.add_text(f"Subject: {data['subject']}")
    pdf.add_text("")
    pdf.add_text(f"Respected {data['respected']},")
    pdf.add_text("")
    pdf.add_text(f"We are writing to kindly request your permission to be marked present for the duration of {data['start_time']} to {data['end_time']} on {format_event_date(data['event_date'])}. During this time, we will be actively participating in the {data['event_name']} organized by Megapixels.", '', 'm', 'J')
    pdf.add_text("")
    pdf.add_text("We would be grateful if our attendance could be adjusted accordingly.", '', 'm', 'J')
    pdf.add_text("")
    pdf.add_text("Sincerely,")
    pdf.add_text(data['sincerely'])
    pdf.add_text(data['sincerely_post'])
    pdf.add_text("")
    pdf.add_text(f"{data['event_name']} | {data['start_time']} - {(data['end_time'])} | {(format_event_date(data['event_date']))}", 'b')
    pdf.add_text(f"Location:{data['location']}")
    pdf.add_text("")

    for entry in data['participants']:
        pdf.add_text(f"{entry['name']} ({entry['branch']}) - {entry['roll_number']}")

    # Save PDF to a BytesIO object
    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest='S'))
    pdf_output.seek(0)
    return pdf_output

# Requirement application
from fpdf import FPDF
from date import get_date
from date import format_event_date
from io import BytesIO

# data={"to_line_1": "Mr. John Doe", "to_line_2": "Manager, XYZ Company", "subject": "Request for Requirements for Upcoming Event", "respected": "Sir", "event_name": "Annual Fest", "start_time": "10:00 AM", "end_time": "5:00 PM", "event_date": "2022-12-25", "sincerely": "Jane Doe", "sincerely_post": "Event Coordinator", "requirements": [{"item": "Projector"}, {"item": "Sound System"}, {"item": "Stage"}]}

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

def generate_pdf3(data):
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
    pdf.add_text(f"I am writing to request the necessary requirements for our upcoming event,{data['event_name']}, organized by Megapixel. To ensure the event's success, we need the following items and arrangements:", '', 'm', 'J')
    pdf.add_text("")
    pdf.add_text("We kindly request your support in arranging these items to ensure a smooth and successful event. If you need any further details or have suggestions, please feel free to let us know. Your prompt response and approval will help us proceed with our preparations efficiently.", '', 'm', 'J')
    pdf.add_text("")
    pdf.add_text("Sincerely,")
    pdf.add_text(data['sincerely'])
    pdf.add_text(data['sincerely_post'])
    pdf.add_text("")
    pdf.add_text(f"{data['event_name']} | {data['start_time']} - {(data['end_time'])} | {(format_event_date(data['event_date']))}", 'b')
    pdf.add_text("")
    pdf.add_text("Requirements:",)

    for entry in data['requirements']:
        item = entry.get('requirement_name', 'Unknown Item')
        quantity = entry.get('quantity', 'N/A')
        pdf.add_text(f"{item} - {quantity}")

    # Save PDF to a BytesIO object
    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest='S'))
    pdf_output.seek(0)
    return pdf_output

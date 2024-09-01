# Poster Request PDF
from base64 import encode
from fpdf import FPDF
from date import get_date
from date import format_event_date
from io import BytesIO

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

def generate_pdf2(data):
    pdf = PDF(orientation="portrait", format="letter")
    pdf.add_page()
    # pdf.add_font("Inter", style='', fname=r"inter\static\\Inter_18pt-Medium.ttf", uni=True)
    # pdf.add_font("Inter", style='B', fname=r"inter\static\\Inter_18pt-SemiBold.ttf", uni=True)
    pdf.set_x(25)
    pdf.set_y(50)
    pdf.set_left_margin(12.5)

    pdf.set_line_width(.8)
    pdf.line(7, 0, 7, 500)

    pdf.image(data['logo_loc'], 175, 10, 25)
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
    pdf.add_text(f"I am writing to request your approval to print a standee poster for our upcoming event,{data['event_name']}organized by the HID Club. The poster will play a crucial role in promoting the event, which includes collaborations with various cultural clubs.", '', 'm', 'J')
    pdf.add_text("")
    pdf.add_text("Your prompt approval of this request would be greatly appreciated, as it will allow us to proceed with the necessary arrangements. Thank you for your time and consideration.", '', 'm', 'J')
    pdf.add_text("")
    pdf.add_text("Sincerely,")
    pdf.add_text(data['sincerely'])
    pdf.add_text(data['sincerely_post'])
    pdf.add_text("")
    pdf.add_text(f"{data['event_name']} ", 'b')
    pdf.add_text("")

    # Save PDF to a BytesIO object
    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest='S'))
    pdf_output.seek(0)
    return pdf_output
from fpdf import FPDF

title = "Flatmates' Bill"


class Bill:
    """Object that contains data about the bill, such as the total amount
    and period"""

    def __init__(self, amount, period):

        self.amount = amount
        self.period = period


class Flatmate:

    """
    Creates a flatmate instance representing a person
    who lives in the flat and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, days_total):

        owed = self.days_in_house / days_total
        to_pay = owed * bill.amount

        return round(to_pay, 2)


class PdfReport(FPDF):

    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 60
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(200, 220, 255)
        self.set_text_color(0, 80, 180)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(20)

    def period_header(self, period):
        # Arial 12
        self.set_font('Arial', 'B', 20)

        # Background color
        self.set_fill_color(200, 220, 255)
        # Title

        self.cell(0, 12, 'Period: %s' % (period), 0, 1, 'C', 1)
        # Line break
        self.ln(4)

    def add_section(self, period):

      # Period
        self.period_header(period)

      # Times 16
        self.set_font('Times', '', 16)
        # Report headers
        w = [60, 130]
        h = 10
        self.set_fill_color(200, 220, 255)
        self.cell(w[0], h, "Flatmate", 0, 0, "C", True)
        self.set_fill_color(200, 250, 200)
        self.cell(w[1], h, "Amount owed", 0, 1, "C", True)

        self.ln(0)

    def generate_report(self, flatmate, bill):

        w = [60, 130]
        h = 10
        self.set_fill_color(255, 255, 255)
        self.cell(w[0], h, flatmate, 0, 0, "C", True)
        self.set_fill_color(255, 255, 255)
        self.cell(w[1], h, str(bill), 0, 1, "C", True)

    # def generate(self, flatmate1, flatmate2, bill):
    #     pass

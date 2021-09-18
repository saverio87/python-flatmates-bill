from classes import Bill, Flatmate, PdfReport

flatmates = []
days_total = 0


def create_pdf(bill):

    pdf = PdfReport()
    pdf.add_page()
    pdf.add_section(bill.period)

    for flatmate in flatmates:

        pdf.generate_report(flatmate.name, flatmate.pays(bill, days_total))

    pdf.output(f"{bill.period}.pdf")


def input_values():

    global flatmates, days_total

    bill_amount = float(input("Please enter bill amount: "))
    period = input("Please enter the period (Ex.: June 2018): ")
    bill = Bill(bill_amount, period)

    num_flatmates = int(
        input("How many flatmates in the house? (Maximum of 5): "))

    # Create as many instances of the Flatmate object as there are flatmates > dynamic variable name assignment

    for index, flatmate in enumerate(range(num_flatmates)):

        name = input("Insert flatname %d's name: " % (index + 1))
        days_in_house = int(input(
            "How many days did {} stay in the house?: ".format(name)))

        days_total += days_in_house

        globals()['flatmate%s' % str(index + 1)] = Flatmate(
            name, days_in_house)

        flatmates.append(globals()['flatmate%s' % str(index + 1)])

    return bill


bill = input_values()
create_pdf(bill)

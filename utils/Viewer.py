from math import ceil
from os import device_encoding
from fpdf import FPDF


class Viewer():
    def create_pdf(self, schedules: dict, name_paths: dict, path: str, filename: str) -> str:
        pdf = FPDF()
        pdf.add_page()

        for i in range(2):
            pdf.set_font('Arial', 'B', size=25)
            pdf.write(8, 'SENTIDO: {}'.format(name_paths[i]))
            pdf.ln(20)

            for schedule in schedules[i]['Value']:
                pdf.set_font('Arial', size=20)
                pdf.write(8, '{}'.format(schedule['Key']))
                pdf.ln(15)

                length = ceil(len(schedule['Value']) / 10)
                start_value = 0
                end_value = 10

                for j in range(0,  length):
                    if j == (length-1):
                        end_value = len(schedule['Value'])

                    for x in range(start_value, end_value):
                        pdf.set_font('Arial', size=16)
                        pdf.write(8, '{}\t\t\t'.format(schedule['Value'][x]))

                    pdf.ln(10)
                pdf.ln(10)
                start_value = end_value
                end_value += 10

        pdf.output('{}/{}.pdf'.format(path, filename), 'F')

        return '{}/{}.pdf'.format(path, filename)

    def to_pdf(self, path: str, filename: str, delete_previous_file=False) -> str:
        pdf = FPDF()

        pdf.add_page()

        pdf.set_font('Arial', size=15)

        f = open('{}/{}.md'.format(path, filename), 'r')

        for x in f:
            pdf.cell(200, 10, txt=x, ln=1)

        pdf.output('{}/{}.pdf'.format(path, filename))

        return '{}/{}.pdf'.format(path, filename)

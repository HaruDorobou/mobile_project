from fpdf import FPDF
import datetime


class function:
    def init_pdf(self):
        pdf = FPDF(format='A4')
        pdf.add_page()
        return pdf

    def set_title(self, pdf, text):
        pdf.set_font('NanumGothic', size=32)
        pdf.cell(120, 10, txt=text, center=True)

    def set_report_date(self, pdf):
        pdf.set_font('NanumGothic', size=18)
        pdf.write(txt='분석일시 : ' + str(datetime.datetime.now()))

    def set_where(self, pdf):
        print('분석장소 입력')
        where = input()
        pdf.set_font('NanumGothic', size=18)
        pdf.write(txt='분석장소 : ' + where)

    def set_target(self, pdf):
        print('분석대상 입력')
        target = input()
        pdf.set_font('NanumGothic', size=18)
        pdf.write(txt='분석대상 : ' + target)

    def set_organ(self, pdf):
        print('분석기관 입력')
        organ = input()
        pdf.set_font('NanumGothic', size=18)
        pdf.write(txt='분석기관 : ' + organ)

    def make_table(self, pdf, data):
        line_height = pdf.font_size * 2.5
        col_width = pdf.epw / len(data[0])  # distribute content evenly
        for row in data:
            for datum in row:
                pdf.multi_cell(col_width, line_height, datum, border=1, ln=3, max_line_height=pdf.font_size)
            pdf.ln(line_height)
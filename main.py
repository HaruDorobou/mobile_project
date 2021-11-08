from fpdf import FPDF
import datetime

def init_pdf():
    pdf = FPDF(format='A4')
    pdf.add_page()
    return pdf

def set_title(pdf, text):
    pdf.set_font('NanumGothic', size=32)
    pdf.cell(120, 10, txt=text, center=True)

def set_report_date(pdf):
    pdf.set_font('NanumGothic', size=18)
    pdf.write(txt='분석일시 : ' + str(datetime.datetime.now()))

def set_where(pdf):
    print('분석장소 입력')
    where = input()
    pdf.set_font('NanumGothic', size=18)
    pdf.write(txt='분석장소 : ' + where)

def set_target(pdf):
    print('분석대상 입력')
    target = input()
    pdf.set_font('NanumGothic', size=18)
    pdf.write(txt='분석대상 : ' + target)

def set_organ(pdf):
    print('분석기관 입력')
    organ = input()
    pdf.set_font('NanumGothic', size=18)
    pdf.write(txt='분석기관 : ' + organ)
    
def make_table(pdf, data):
    line_height = pdf.font_size * 2.5
    col_width = pdf.epw / len(data[0])  # distribute content evenly
    for row in data:
        for datum in row:
            pdf.multi_cell(col_width, line_height, datum, border=1, ln=3, max_line_height=pdf.font_size)
        pdf.ln(line_height)

if __name__ == "__main__":
    pdf = init_pdf() # automatic add_page

    # Setting Init Font Set
    pdf.add_font('NanumGothic', fname='NanumGothic.ttf', uni=True)
    pdf.set_font('NanumGothic', size=16)

    pdf.ln(10)

    set_title(pdf, '디지털 포렌식 분석 보고서')
    pdf.ln(30)

    set_report_date(pdf) # 보고서 작성 일시
    pdf.ln(15)

    set_where(pdf) # 보고서 작성 장소
    pdf.ln(15)

    set_target(pdf) # 보고서 의뢰 대상
    pdf.ln(15)

    set_organ(pdf) # 보고서 의뢰 기관
    pdf.ln(15)

    pdf.set_font('NanumGothic', size=18)
    pdf.write(txt='Timezone : ' + 'time_zone_value') # Target의 OS Timezone
    pdf.ln(15)

    pdf.write(txt='OS : ' + 'OS') # Target Device의 OS
    pdf.ln(15)

    pdf.write(txt='기종 번호 : ' + 'device_type') # Target Device의 Model 식별 번호
    pdf.ln(15)

    # 보고서 첫 페이지 내용 끝 #
    # 분석내용 시작

    pdf.set_font('NanumGothic', size=26)
    pdf.write(txt='분석내용')
    pdf.ln(15)

    pdf.set_font('NanumGothic', size=18)
    pdf.ln(15)

    pdf.write(txt='다운로드 이력')
    pdf.ln(10)

    # d_data = (
    #     ("col1", "col2", "col3", "col4"),
    #     ("2015-01-23", "Caron", "34", "San Juan"),
    #     ("2012-05-16", "Ramos", "45", "Orlando"),
    #     ("2021-11-03", "Banks", "19", "Los Angeles"),
    #     ("2020-12-22", "Cimon", "31", "Saint-Mahturin-sur-Loire"),
    #     ("2019-07-30", "Garfunkle", "31", "Saint-Mahturin-sur-Loire"),
    #     ("2007-08-19", "Yamato", "31", "Saint-Mahturin-sur-Loire"),
    #     ("2006-02-07", "Akagi", "31", "Saint-Mahturin-sur-Loire")
    # )


    make_table(pdf, data=d_data) # Download History From Database

    pdf.output("result.pdf")
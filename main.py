from function import pdf_function

if __name__ == "__main__":
    func_obj = pdf_function()
    pdf = func_obj.init_pdf()

    # pdf = init_pdf() # automatic add_page

    # Setting Init Font Set
    pdf.add_font('NanumGothic', fname='NanumGothic.ttf', uni=True)
    pdf.set_font('NanumGothic', size=16)

    func_obj.set_title(pdf, '디지털 포렌식 분석 보고서')
    pdf.ln(30)

    func_obj.set_report_date(pdf) # 보고서 작성 일시
    pdf.ln(15)

    func_obj.set_where(pdf) # 보고서 작성 장소
    pdf.ln(15)

    func_obj.set_target(pdf) # 보고서 의뢰 대상
    pdf.ln(15)

    func_obj.set_organ(pdf) # 보고서 의뢰 기관
    pdf.ln(15)

    func_obj.set_timezone(pdf) # 기기의 Timezone
    pdf.ln(15)

    func_obj.set_os(pdf) # 기기의 OS
    pdf.ln(15)

    func_obj.set_buildID(pdf) # 기기의 추출당시 Build ID
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

    d_data = (
        ("col1", "col2", "col3", "col4"),
        ("2015-01-23", "Caron", "34", "San Juan"),
        ("2012-05-16", "Ramos", "45", "Orlando"),
        ("2021-11-03", "Banks", "19", "Los Angeles"),
        ("2020-12-22", "Cimon", "31", "Saint-Mahturin-sur-Loire"),
        ("2019-07-30", "Garfunkle", "31", "Saint-Mahturin-sur-Loire"),
        ("2007-08-19", "Yamato", "31", "Saint-Mahturin-sur-Loire"),
        ("2006-02-07", "Akagi", "31", "Saint-Mahturin-sur-Loire")
    ) # example data

    func_obj.make_table(pdf, data=d_data) # talbe result

    pdf.output("result.pdf")
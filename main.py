from function import function
import data

if __name__ == "__main__":
    func_obj = function()
    pdf = func_obj.init_pdf()
    data_control = data.Data()

    # Setting Init Font Set
    pdf.add_font('NanumGothic', fname='NanumGothic.ttf', uni=True)
    pdf.set_font('NanumGothic', size=16)

    # 보고서 첫 페이지 시작 #

    func_obj.set_title(pdf, '디지털 포렌식 분석 보고서')
    pdf.ln(30)

    func_obj.set_report_date(pdf)  # 보고서 작성 일시
    pdf.ln(15)

    func_obj.set_where(pdf)  # 보고서 작성 장소
    pdf.ln(15)

    func_obj.set_target(pdf)  # 보고서 의뢰 대상
    pdf.ln(15)

    func_obj.set_organ(pdf)  # 보고서 의뢰 기관
    pdf.ln(15)

    func_obj.set_modelname(pdf)  # 기기의 이름
    pdf.ln(15)

    func_obj.set_os(pdf)  # 기기의 OS
    pdf.ln(15)

    func_obj.set_buildID(pdf)  # 기기의 추출당시 Build ID
    pdf.ln(15)

    func_obj.set_timezone(pdf)  # 기기의 Timezone
    pdf.ln(15)

    # 보고서 첫 페이지 내용 끝 #
    # 분석내용 시작

    pdf.set_font('NanumGothic', size=26)
    pdf.write(txt='분석내용')
    pdf.ln(15)

    # Contacts
    sql = 'select raw_contacts._id as id, raw_contacts.display_name as name, \
        phone_lookup.normalized_number as number \
        from raw_contacts inner join phone_lookup on \
        raw_contacts._id = phone_lookup.raw_contact_id \
        order by raw_contacts._id'
    data, record_num = data_control.data_extract_db('./data/contacts2.db', sql)

    pdf.set_font('NanumGothic', size=18)
    pdf.write(txt='연락처 합계 : ' + record_num)
    pdf.ln(10)

    pdf.set_font('NanumGothic', size=10)
    pdf.write(txt='연락처 목록')
    pdf.ln(5)
    func_obj.make_table(pdf, data=data)  # table result
    pdf.ln(15)

    # Calendar
    sql = 'select title as event, description as memo, dtstart as date_start, dtend as date_end \
        from Events where calendar_id = 1 order by date_start'
    data, record_num = data_control.data_extract_db('./data/calendar.db', sql)

    pdf.set_font('NanumGothic', size=18)
    pdf.write(txt='캘린더 이벤트 합계 : ' + record_num)
    pdf.ln(10)

    pdf.set_font('NanumGothic', size=10)
    pdf.write(txt='캘린더 이력')
    pdf.ln(5)
    func_obj.make_table(pdf, data=data)  # table result
    pdf.ln(15)

    # MMS
    sql = 'select date, address, body as message_body from sms \
        order by date'
    data, record_num = data_control.data_extract_db('./data/mmssms.db', sql)

    pdf.set_font('NanumGothic', size=18)
    pdf.write(txt='문자메시지 합계 : ' + record_num)
    pdf.ln(10)

    pdf.set_font('NanumGothic', size=10)
    pdf.write(txt='문자메시지 이력')
    pdf.ln(5)
    func_obj.make_table(pdf, data=data)  # table result
    pdf.ln(15)

    # Call Log
    sql = 'select date, number, name from calls \
        order by date'
    data, record_num = data_control.data_extract_db('./data/calllog.db', sql)

    pdf.set_font('NanumGothic', size=18)
    pdf.write(txt='전화 이력 합계 : ' + record_num)
    pdf.ln(10)

    pdf.set_font('NanumGothic', size=10)
    pdf.write(txt='전화 이력')
    pdf.ln(5)
    func_obj.make_table(pdf, data=data)  # table result
    pdf.ln(15)

    # 연동 계정
    pdf.set_font('NanumGothic', size=18)
    pdf.write(txt='연동 계정')
    pdf.ln(10)
    pdf.set_font('NanumGothic', size=10)
    sql = 'select _id as id, account_name from accounts'
    data, _ = data_control.data_extract_db('./data/accounts.notifications.db', sql)
    func_obj.make_table(pdf, data=data)  # table result
    pdf.ln(15)

    # wifi 연결 이력
    pdf.set_font('NanumGothic', size=18)
    pdf.write(txt='wifi 연결 이력')
    pdf.ln(10)
    pdf.set_font('NanumGothic', size=10)
    data = data_control.parsing_wifi_xml('./data/WifiConfigStore.xml')
    func_obj.make_table(pdf, data=data)  # table result
    pdf.ln(15)

    # 분석내용 끝

    # 보고서 저장
    pdf.output("result.pdf")

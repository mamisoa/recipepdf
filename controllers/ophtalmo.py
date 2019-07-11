# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from ophtalmo.py")

def pdf_lun():
    #import base64
    axe_img_path = '/home/www-data/web2py/applications'+URL('static','images/axe.png')
    logo_img_path = '/home/www-data/web2py/applications'+URL('static','images/logo.jpg')
    axe_img64 = embed64(filename= axe_img_path, file=axe_img_path, data=None, extension='image/png')
    logo_img64 = embed64(filename= logo_img_path, file=logo_img_path, data=None, extension='image/jpg')
    # with open('/home/www-data/web2py/applications'+URL('static','images/axe.png'), "rb") as image_file:
    #    axe_img64 = base64.b64encode(image_file.read())
    def format2(x):
        return "{0:+.2f}".format(x)
    sph_r=XML("{ text: '"+format2(+0.25)+"', color: 'green'}") # "{ text: '"+format2(+0.25)+"', color: 'green'}"
    cyl_r=format2(-0.50)
    axis_r=str(170)+'°'
    return locals()

def ads_fpdf():
    adjust_y = 20
    pdf = FPDF('P', 'mm', (127, 305+adjust_y))
    # pdf.set_margins(0, 0, 0)
    pdf.set_auto_page_break(0, margin = 0.0)
    pdf.add_page()
    # Set font
    pdf.set_font('Arial', '', 10)
    persons_count = db(db.person.id > 0).count()
    # nom prenom
    ref_x = 10
    ref_y = 30 #32
    pdf.set_xy(76,ref_y)
    pdf.cell(18,6,'Nom Prenom', 0, 0, 'C')
    # date
    date_exam = '01/01/2016'
    pdf.set_xy(24,ref_y+17)
    pdf.cell(18,6, date_exam, 0, 0, 'C')
    # nomenclature
    pdf.set_x(76)
    pdf.cell(18,6, '102535',0,0,'C')
    y_tech = ref_y + 39
    x_tech = ref_x
    # actes techniques
    pdf.set_y(y_tech)
    pdf.set_font('Arial', '', 10)
    if persons_count < 11:
        for data in db(db.person.id > 0).select():
            # Centered text in a framed 20*10 mm cell and line break
            pdf.cell(18, 4, str(data.name), 0, 0, 'C')
            # Centered text in a framed 20*10 mm cell and line break
            pdf.cell(18, 4, str(data.age), 0, 0, 'C')
            pdf.cell(15, 4, '', 0, 1, 'C')
        i = 10-persons_count
        while i>0:
            # Centered text in a framed 20*10 mm cell and line break
            pdf.cell(18, 4, '***', 0, 0, 'C')
            # Centered text in a framed 20*10 mm cell and line break
            pdf.cell(18, 4, '***', 0, 0, 'C')
            pdf.cell(15, 4, '', 0, 1, 'C')
            i=i-1
        ordi = y_tech
        r=9
        while r >= 0:
            pdf.set_xy(61,ordi)
            # Centered text in a framed 20*10 mm cell and line break
            pdf.cell(18, 4, '***', 0, 0, 'C')
            # Centered text in a framed 20*10 mm cell and line break
            pdf.cell(18, 4, '***', 0, 0, 'C')
            pdf.cell(15, 4, '', 0, 1, 'C')
            r=r-1
            ordi=ordi+4
    elif persons_count < 21:
        r = 10 - (persons_count - 10)
        i = 10
        for data in db(db.person.id > 0).select():
            if i > 0:
                # Centered text in a framed 20*10 mm cell and line break
                pdf.cell(18, 4, str(data.name), 0, 0, 'C')
                # Centered text in a framed 20*10 mm cell and line break
                pdf.cell(18, 4, str(data.age), 0, 0, 'C')
                pdf.cell(15, 4, '', 0, 1, 'C')
                i = i-1
            elif i == 0:
                pdf.set_xy(61,y_tech)
                pdf.cell(18, 4, str(data.name), 0, 0, 'C')
                # Centered text in a framed 20*10 mm cell and line break
                pdf.cell(18, 4, str(data.age), 0, 0, 'C')
                pdf.cell(15, 4,'' , 0, 1, 'C') # 'i='+str(i)
                i=i-1
                pdf.set_xy(64,y_tech+6)
            elif ((i<0) & (r>=0)):
                pdf.set_x(61)
                # Centered text in a framed 20*10 mm cell and line break
                pdf.cell(18, 4, str(data.name), 0, 0, 'C')
                # Centered text in a framed 20*10 mm cell and line break
                pdf.cell(18, 4, str(data.age), 0, 0, 'C')
                pdf.cell(15, 4, '', 0, 1, 'C') # 'r='+str(r)
                #r=r-1
        ordi = pdf.y + y_tech
        while r > 0:
            pdf.set_xy(61,ordi)
            # Centered text in a framed 20*10 mm cell and line break
            pdf.cell(18, 4, '***', 0, 0, 'C')
            # Centered text in a framed 20*10 mm cell and line break
            pdf.cell(18, 4, '***', 0, 0, 'C')
            pdf.cell(15, 4, '', 0, 1, 'C') # str(r)
            r=r-1
            ordi=ordi+4
    else:
        pass
    pdf.set_font('Arial', '', 10)
    # honoraires
    price_y = ref_y+127
    price = '90,00'
    pdf.set_xy(82,price_y)
    pdf.cell(18,6,price ,0,1,'C')
    # dispensateur
    disp_y = ref_y+140
    pdf.set_xy(16,disp_y)
    doctor = "Dr. ANDRIANTAFIKA Raberahona\n1-8950632-370\nCentre Medical Bruxelles-Schuman\n66 Av de Cortenbergh, 1000 Bruxelles"
    pdf.multi_cell(76,6, doctor,1,1,'C')
    # date impression
    print_date = ref_y + 172
    pdf.set_xy(82,print_date)
    date_printing = '31/12/2016'
    pdf.cell(16,6,date_printing,0,1,'C')
    # bce_num
    bce_y = ref_y + 199
    bce_num = '0890999999'
    pdf.set_xy(60,bce_y)
    pdf.cell(16,6, bce_num, 0,1,'C')
    # date receipt
    date_receipt_y = ref_y + 210
    pdf.set_xy(68,date_receipt_y)
    pdf.cell(16,6,date_printing,0,1,'C')
    # price receipt
    price_receipt_y = ref_y + 219
    pdf.set_xy(57,price_receipt_y)
    pdf.cell(18,6,price ,0,1,'C')
    response.headers['Content-Type']='application/pdf'
    return pdf.output(dest='S')

def presc_med():
    doctorinami = XML('189506323700')
    doctorinami_display = XML('1.89506.32.370')
    return locals()

def cee_pdf():
    ce_img_path = '/home/www-data/web2py/applications'+URL('static','images/entete_cee.png')
    ce_img64 = embed64(filename= ce_img_path, file=ce_img_path, data=None, extension='image/png')
    prescriber_lastname="SAN JOSE AGUDO"
    prescriber_firstname="Maria Ruth"
    patient_lastname="CASTINEIRA VIZOSO"
    patient_firstname="Rocio"
    patient_dob="27/03/1976"
    exam_date="03/07/2019"
    eyemd_fn="Mamisoa"
    eyemd_ln="ANDRIANTAFIKA"
    patient_id="154317"
    bc_num=XML('NDPC---338810')
    ce_id = XML('154317')
    return locals()

def test_template():
    from gluon.contrib.pyfpdf import Template
    import os.path
    axe=os.path.join(request.env.web2py_path,"applications",request.application,"static","images","axe.png")
    csv=os.path.join(request.env.web2py_path,"applications",request.application,"static","template_pdf","template_lun.csv")
    elements = db(db.pdf_element.pdf_template_id==4).select(orderby=db.pdf_element.priority)
    f = Template(format="A4",
             elements = elements,
             title="Prescription de lunettes", author="Ophtalmologiste.be",
             subject="lunettes", keywords="prescription lunettes")
    f.add_page()
    f["company_name_l1"] = "Brussels-Schuman Medical Center"
    f["logo"] = str(axe)
    f["tabo_img"] = str(axe)
    f["axe_left"] = str(axe)
    f["axe_right"] = str(axe)
    response.headers['Content-Type']='application/pdf'
    return f.render('test.pdf', dest='S')

def template_lun():
    import os.path
    response.title = "Prescription de lunettes"
    axe=os.path.join(request.env.web2py_path,"applications",request.application,"static","images","axe.png")
    # include a google chart!
    chart = IMG(_src=URL('static','images/axe.png'), _width="200",_height="200")

    # create a small table with some data:
    rows = [THEAD(TR(TH("Key",_width="70%"), TH("Value",_width="30%"))),
            TBODY(TR(TD(XML('<font face="Arial">This is some text!</font>')),TD("60")),
                  TR(TD("World"),TD("40")))]
    table = TABLE(*rows, _border="0", _align="center", _width="50%")

    if request.extension=="pdf":
        from gluon.contrib.pyfpdf import FPDF, HTMLMixin

        # create a custom class with the required functionalities
        class MyFPDF(FPDF, HTMLMixin):
            #pdf = FPDF('P', 'mm', (128, 305))
            def header(self):
                "hook to draw custom page header"
                logo=os.path.join(request.env.web2py_path,"applications",request.application,"private","tutorial","logo_pb.png")
                self.image(logo,10,8,33)
                self.set_font('Arial','B',15)
                self.cell(65) # padding
                self.cell(60,10,response.title,1,0,'C')
                self.ln(20)

            def footer(self):
                "hook to draw custom page header (printing page numbers)"
                self.set_y(-15)
                self.set_font('Arial','I',8)
                txt = 'Page %s of %s' % (self.page_no(), self.alias_nb_pages())
                self.cell(0,10,txt,0,0,'C')

        pdf=MyFPDF() # pdf=MyFPDF('P', 'mm', (128, 305))
        # create a page and serialize/render HTML objects
        pdf.add_page()
        pdf.set_font('Arial', '', 15)
        pdf.write_html(XML(table, sanitize=False))
        pdf.write_html(XML(CENTER(IMG(_src=str(XML(axe,sanitize=False)),_width='200',_height='200')), sanitize=False))
        pdf.write_html(XML('<font face="Courier" size ="18" color="#000000">This is some text!</font>')) #
        # prepare PDF to download:
        response.headers['Content-Type']='application/pdf'
        return pdf.output(dest='S')
    else:
        # normal html view:
        return dict(chart=chart, table=table)

import pandas
import pandas as pd
import fpdf
import glob
import pathlib

files = glob.glob("data/*.xlsx")
df_list = []
net_data = pd.DataFrame()

for file in files:
    df = pandas.read_excel(file)
    pdf = fpdf.FPDF(orientation="P", unit='mm', format='A4')
    pdf.add_page()

    filename = pathlib.Path(file).stem
    invoice_nr = filename.split("-")[0]
    date = filename.split("-")[1]

    pdf.set_font(family='Times', size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice Number: {invoice_nr}", ln=1)

    pdf.set_font(family='Times', size=14, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=2)

    df_list.append(df)

    headers = df.columns
    headers = [header.replace('_', ' ').title() for header in headers]
    pdf.set_font(family="Times", size=12, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=headers[0], border=1)
    pdf.cell(w=60, h=8, txt=headers[1], border=1)
    pdf.cell(w=35, h=8, txt=headers[2].replace("Purchased", ''), border=1)
    pdf.cell(w=30, h=8, txt=headers[3], border=1)
    pdf.cell(w=30, h=8, txt=headers[4], border=1, ln=1)

    net_price = 0
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=60, h=8, txt=row['product_name'], border=1)
        pdf.cell(w=35, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)
        net_price = net_price + int(row['total_price'])

    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=60, h=8, txt='', border=1)
    pdf.cell(w=35, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt=str(net_price), border=1, ln=1)

    pdf.set_font(family='Times', size=10, style="B")
    pdf.cell(w=50, h=8, txt=f"The total amount due is {str(net_price)} Euros", ln=1)

    pdf.set_font(family='Times', size=10, style="B")
    pdf.cell(w=50, h=8, txt=f"PythonHow", ln=1)
    pdf.image("data/pythonhow.png", w=10)

    pdf.output(f"PDF's/{invoice_nr}.pdf")

net_data = pd.concat(df_list, ignore_index=True)



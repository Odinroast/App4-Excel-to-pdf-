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

    pdf.set_font(family='Times', size=14, style="B")
    pdf.cell(w=20, h=8, txt=f"Invoice Number: {invoice_nr}", ln=1)

    pdf.set_font(family='Times', size=14, style="B")
    pdf.cell(w=20, h=8, txt=f"Date: {date}")

    df_list.append(df)
    pdf.output(f"PDF's/{invoice_nr}.pdf")

net_data = pd.concat(df_list, ignore_index=True)



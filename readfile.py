import pandas as pd
import pdfplumber

pdf=pdfplumber.open("5th_wave_statistics.pdf")
data=pdf.pages[3]
table=data.extract_table()
pdf.close()

# columns1=["年齡組別","累計死亡個案數","高危險個案數","住院個案數","累計呈報個案數","曾在香港接種至少一劑個案","接種一劑","接種二劑","接種三劑","接種四劑","接種五劑","2021年底香港人口統計"]
columns2=["年齡組別","接種四劑","接種三劑","接種二劑","接種一劑","沒接種疫苗","總計"]
df = pd.DataFrame(table[7:], columns=columns2)
# df.drop(index=0,inplace=True)

df.to_excel("pdftoexcel2.xlsx",index=False)
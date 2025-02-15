# step no.1
# pip install qrcode

# step no.2
import qrcode
data = 'https://final-portfolio-qs.vercel.app/' 
img = qrcode.make(data)
img.save('qr code project.png')

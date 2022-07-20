# Envía texto plano, código HTML e imagen.
# Modificado por Juan A. Villalpando
# kio4.com

import smtplib,ssl  
from email.mime.multipart import MIMEMultipart   
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

enviador = 'smartdoorman5@gmail.com'
receptor = 'lumomoro@gmail.com'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'ALGUIEN TE QUIERE VISITAR :)'
msgRoot['From'] = enviador
msgRoot['To'] = receptor
msgRoot.preamble = 'Esto es el preambulo.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

# Envío en texto plano
msgText = MIMEText('Este texto se enviará, pero no en HTML.')
msgAlternative.attach(msgText)

# Envío en formato HTML
msgText = MIMEText('<b>TIENES UNA VISITA, PARA VISUALIZAR QUIEN ES... DA CLICK AQUI =>  http://192.168.90.152:5000/ </b><br><img src="cid:image1"><', 'html')
msgAlternative.attach(msgText)

# Dirección de la imagen
#fp = open('/home/pi/ladron.jpg', 'rb')
#msgImage = MIMEImage(fp.read())
#fp.close()

# Adjunta imagen1
#msgImage.add_header('Content-ID', '<image1>')
#msgRoot.attach(msgImage)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()  
s.starttls()  
s.login(user = enviador, password = 'D4m123456p')
s.sendmail(enviador, receptor, msgRoot.as_string())
s.quit()  
print ("CORREO ENVIADO CORRECTAMENTE :)")
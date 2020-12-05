from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shareRes.models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string



# Create your views here.
def sendEmail(request):
    try:
        checked_res_list =request.POST.getlist('checks')
        inputReceiver = request.POST['inputReceiver']
        inputTitle = request.POST['inputTitle']
        inputContent = request.POST['inputContent']
        restaurants = []


        for checked_res_id in checked_res_list:
            restaurants.append( Restaurant.objects.get(id = checked_res_id) )

        content = {'inpurtContent' : inputContent, 'restaurants' : restaurants}
        # return render(request, 'sendEmail/email_format.html', content)


        msg_html = render_to_string('sendEmail/email_format.html', content)

        msg = EmailMessage(subject = inputTitle, body=msg_html, from_email= "djangoemailtester001@gmail.com",bcc=inputReceiver.split(','))

        msg.content_subtype = 'html'
        msg.send()
        
        return render(request, 'sendEmail/emailSucess.html')
        

    except:
        return render(request, 'sendEmail/emailFail.html')
        
        
        



    # mail_html = "<html><body>"
    # mail_html += "<h1> 맛집 공유 </h1>"
    # mail_html += "<p>"+inputContent+"<br>"
    # mail_html += "발신자님께서 공유하신 맛집은 다음과 같습니다.</p>"
    # for checkedres_id in checked_res_list:
    #     restaurant = Restaurant.objects.get(id = checkedres_id)
    #     mail_html += "<h2>"+restaurant.restaurant_name+"</h3>"
    #     mail_html += "<h4>* 관련 링크</h4>"+"<a href='"+restaurant.restaurant_link+"'>"+restaurant.restaurant_link+"</a><br>"
    #     mail_html += "<h4>* 상세 내용</h4>"+"<p>"+restaurant.restaurant_content+"</p>" 
    
    # #여기 미완성
    # #p281  30번째줄
    

    
    # gmail_user = 'seehoo27@gmail.com'
    # gmail_password = 'itlhrzrfxmiylbnu'
    
    # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # server.ehlo()
    # server.login(gmail_user, gmail_password)
    
    # msg = MIMEMultipart('alternative')
    # msg["Subject"] = inputTitle
    # msg["From"] = "test@gmail.com"
    # msg["To"] = inputReceiver
    # mail_html = MIMEText(mail_html, 'html')
    # msg.attach(mail_html)
    # print(msg["To"], type(msg["To"]))
    # server.sendEmail(msg['From'],msg["To"].split(','),msg.as_string())
    # server.quit()
    
    
    
    # return HttpResponseRedirect(reverse('index'))


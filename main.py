import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
import requests
MY_EMAIL = 'sending_email'
EMAIL_PASSWORD = 'password'

response = requests.get('https://news.ycombinator.com/')
yc_web_page = response.text


# Using beautifulsoup to parse the information from the website
soup = BeautifulSoup(yc_web_page, 'html.parser')
stories = soup.find_all(name='a', class_='titlelink')
story_links = []
story_title = []
for each in stories[:10]:
    story_links.append(each.get('href'))
    story_title.append(each.getText())
email_body = {}
for each in range(0, 10):
    email_body[story_title[each]] = story_links[each]

# getting the email message setup

msg = EmailMessage()
msg['Subject'] = 'Latest News from Hacker News'
msg['From'] = MY_EMAIL
msg['To'] = 'recipient_email'
msg.set_content(f"""\
Here are today's top stories from Hacker News:
{email_body}

""")
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
    connection.send_message(msg)







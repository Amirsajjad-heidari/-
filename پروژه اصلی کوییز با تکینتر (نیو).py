from tkinter import *
import random
	

#پنجره اجرا
window=Tk()
window.title('quze')

#خوش امد گویی
welcome=Label(window,text='welcome to quiz game\nIn this game:«whoever knows more wins»')
welcome.pack(pady=(60,50))

#فریم گیم و راهنما
first_frame=Frame(window,pady=20)
first_frame.pack()

#بخش راهنما
#تعیین وضعیت راهنما
guide_status=False

#لیبل راهنما
guide_label=Label(window,text='This game is a general information challenge, in this game you will be asked five questions with four options, the time limit for answering each question is 15 seconds, and for each question you answer correctly, you will be given one point, and at the end  Your score will be displayed. Good luck :)',wraplength=2000)
#تابع قطع و وصل
def vis_guide():
	global guide_status ,game_button
	if guide_status:
		guide_label.pack_forget()
		guide_status=False
		game_button['state']="normal"
		guide_button.config(bg='#87CEFA')
		game_button.config(bg='#87CEFA')
	else :
		guide_label.pack()
		guide_status=True
		game_button['state']="disabled"
		guide_button.config(bg='#2ebc45')
		game_button.config(bg='white')
#دکمه راهنما
guide_button=Button(first_frame,text='guide',width=6,height=2,command=vis_guide,bg='#87CEFA',)
guide_button.pack(side=LEFT,padx=20)		


#بخش بازی
#تعیین وضعیت بازی
game_status=False
#بخش اصلی بازی
def main_game():
	ready_button.pack_forget()
	score=0
	#تعداد سوال بازی
	for i in range(5):
		source_questions = [
    [{'طول یک ماراتن چند مایل است؟': [26.2, 26.4, 27.2, 27.4]} ,{'چند بازیکن در یک تیم بیسبال وجود دارد؟':[9 , 10, 8, 11]} , {'کدام کشور قهرمان جام جهانی 2018 شد؟':[ 'فرانسه', 'المان', 'برزیل', 'اسپانیا']},{'چند پارو در کایاک استفاده می شود؟':[1 ,2 , 3, 4 ]} , {'کدام سبک شنا در المپیک ممنوع است؟':['دست و پا زدن سگ','پروانه' , 'پشت پا' , 'آزاد']} , {'کدام کشور بیشترین مدال طلای المپیک را در شنا دارد؟':['ایالات متحده آمریکا' , 'چین', 'استرالیا', 'ژاپن']}]
    ,
    
[{'نخستین فیلم رنگی ایرانی چه بود؟': ['گرداب' ,'سلطان قلبها', 'گنج قارون', 'حلقه']} , {'پدر تئاتر ایران کیست؟':[ 'سید علی نصر','حمید سمندریان' ,'مالک ابسالان' , 'شیخ شیپور']} , {'اولین دوره جشنواره فجر در چه سالی برگزار شد؟  ':[1361,1365,1357,1368]}]
,

[{'کدام سیاره به سیاره سرخ معروف است؟':[ 'مریخ', 'مشتری', 'عطارد', 'زحل']} , {'کدام گاز در جو زمین بیشتر است؟':[ 'نیتروژن','اکسیژن' ,'کربن دی اکسید' ,'ارگون']} , {'بزرگ‌ترین سیاره منظومه شمسی چیست؟':['مشتری' , 'زمین', 'اورانوس','زمین']} , {'کدام کشور به سرزمین طلوع خورشید معروف است؟':['ژاپن' , 'چین','اسکاتلند' ,'هلند']}]
]
		#تعیین شاخه و سوال
		bleach = random.choice(source_questions)
		question = random.choice(bleach)
		 #چاپ سوال
		key = list(question.keys())[0]
		label_question=Label(window ,text=f'question  :{key}')
		label_question.pack()
		#چاپ کلمه پاسخ
		answers_word=Label(window,text='answers:')
		answers = question[key]
		#لیست پاسخ
		heck_ultimate = answers.copy()
		#کپی برای مقایسه نهایی
		random.shuffle(answers)
		#مکان پنجره ای جواب ها
		frame_top_answer=Frame(window,pady=30)
		frame_botton_answer=Frame(window , pady=30)
		#
		#دکمه رادیویی پاسخ ها 
		radio1=Radiobutton(frame_top_answer ,text=answers[0] , value=0 , variable=selected)
		radio2=Radiobutton(frame_top_answer ,text=answers[1] , value=1 , variable=selected)
		radio3=Radiobutton(frame_botton_answer ,text=answers[2] , value=2 , variable=selected)
		radio4=Radiobutton(frame_botton_answer ,text=answers[3] , value=3 , variable=selected)
		radio1.pack(side=LEFT)
		radio2.pack(side=LEFT)
		radio3.pack(side=LEFT)
		radio4.pack(side=LEFT)
		
		
		
		
#دکمه امادگی
ready_button=Button(window,text='im ready',command=main_game)
#تابع قطع و وصل
def vis_game():
	global game_status,guide_button
	if game_status:
		ready_button.pack_forget()
		game_status=False
		guide_button['state']='normal'
	else :
		ready_button.pack(pady=(60,0))
		game_status=True
		guide_button['state']='disabled'
#دکمه بازی
game_button=Button(first_frame , text='game' ,width=6,height=2 ,bg='#87CEFA',command=vis_game)
game_button.pack(side=LEFT,padx=20)

#اجرای پیوسته
window.mainloop()
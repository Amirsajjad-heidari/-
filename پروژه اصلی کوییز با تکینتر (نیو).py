from tkinter import *
import random

		
#پنجره اجرا
window=Tk()
window.title('quze')
window.geometry('600×500')



#خوش امد گویی
welcome=Label(window,text='welcome to quiz game\nIn this game:«whoever knows more wins»' , fg='#761a1a')
welcome.pack(pady=(60,10))




#فریم گیم و راهنما
first_frame=Frame(window,pady=20)
first_frame.pack()

#بخش راهنما
#تعیین وضعیت راهنما
guide_status=False

#لیبل راهنما
guide_label=Label(window,text='This game is a general information challenge, in this game you will be asked five questions with four options, the time limit for answering each question is 15 seconds, and for each question you answer correctly, you will be given one point, and at the end  Your score will be displayed. Good luck :)',wraplength=2000 , relief='solid',highlightbackground="#d49121",highlightthickness=5,pady=50,padx=40)
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
a=0
score=0
remove_list=[]
timer=10
#بخش اصلی بازی
def main_game():
	global a , score , remove_list, timer
	ready_button.pack_forget()
	for deray in remove_list:
		deray.destroy()
	c=True
	#تعداد سوال بازی
	while c :
		source_questions = [
    [{'How many miles is a marathon?': [26.2, 26.4, 27.2, 27.4]} ,{'How many players are there on a baseball team?':[9 , 10, 8, 11]} , {'Which country won the 2018 World Cup?':[ 'France', 'Germany', 'Brazil','Spain']},{'How many paddles are used in a kayak?': [1, 2, 3, 4]},  
{'Which swimming style is banned in the Olympics?': ['Dog paddle', 'Butterfly', 'Backstroke', 'Freestyle']},  
{'Which country has won the most Olympic gold medals in swimming?': ['United States of America', 'China', 'Australia', 'Japan']},{"What is the standard length of a football (soccer) field?":['90-120 meters' ,'80-100 meters' , '100-130 meters','110-140 meters']}, {"How long is each quarter in an NBA basketball game?": ["12 minutes", "10 minutes", "15 minutes", "20 minutes"]},  {"Which country has won the most FIFA World Cups?": ["Brazil", "Germany", "Argentina", "Italy"]},  {"In tennis, what term is used when the score is 40-40?": ["Deuce", "Advantage", "Tie", "Equal"]},{"How many referees are on the court in an official volleyball match?": ["2", "1", "3", "4"]}]
    ,
  
[{'What was the first Iranian color film?': ['Gerdab', 'Sultan of Hearts', 'Ganj-e Qarun', 'Halgheh']},{'Who is the father of Iranian theater?': ['Seyed Ali Nasr', 'Hamid Samandarian', 'Malek Afsalan', 'Sheikh Sheypoor']},{'In what year was the first Fajr Film Festival held?': [1361, 1365, 1357, 1368]}, {"Which movie is considered the first feature-length animated film?": ["Snow White and the Seven Dwarfs", "Fantasia", "Cinderella", "Pinocchio"]},  {"Which actor has won the most Academy Awards for acting?": ["Katharine Hepburn", "Meryl Streep", "Jack Nicholson", "Daniel Day-Lewis"]},{"What is the highest-grossing movie of all time (adjusted for inflation)?": ["Gone with the Wind", "Avatar", "Titanic", "Avengers: Endgame"]}, {"Which director is known for movies like 'Pulp Fiction' and 'Kill Bill'?": ["Quentin Tarantino", "Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]},   {"Which film studio created the Marvel Cinematic Universe (MCU)?": ["Marvel Studios", "Warner Bros.", "Universal Pictures", "20th Century Fox"]},{"Who played the character of Harry Potter in the movie series?": ["Daniel Radcliffe", "Elijah Wood", "Rupert Grint", "Tom Holland"]},{"What was the first science fiction movie ever made?": ["A Trip to the Moon", "Metropolis", "2001: A Space Odyssey", "Blade Runner"]}, {"Which actress played the lead role in the 2023 movie 'Barbie'?": ["Margot Robbie", "Emma Stone", "Scarlett Johansson", "Anne Hathaway"]},
 ]
,

[{'Which planet is known as the Red Planet?': ['Mars', 'Jupiter', 'Mercury', 'Saturn']},  
 {"Which gas is most abundant in Earth's atmosphere?": ['Nitrogen', 'Oxygen', 'Carbon Dioxide', 'Argon']},  
 {'What is the largest planet in the solar system?': ['Jupiter', 'Earth', 'Uranus', 'Earth']},  
 {'Which country is known as the Land of the Rising Sun?': ['Japan', 'China', 'Scotland', 'Netherlands']},  {"What is the capital of France?": ["Paris", "London", "Berlin", "Rome"]},
    {"Who wrote 'Romeo and Juliet'?": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"]},
    {"What is the largest ocean on Earth?": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]},
    {"Which planet is known as the Red Planet?": ["Mars", "Jupiter", "Mercury", "Saturn"]},
    {"What is the chemical symbol for gold?": ["Au", "Ag", "Pb", "Fe"]},
    {"Who was the first president of the United States?": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"]},
    {"Which is the longest river in the world?": ["Nile", "Amazon", "Yangtze", "Mississippi"]},
    {"How many continents are there on Earth?": ["7", "5", "6", "8"]},
    {"Which country is famous for inventing pizza?": ["Italy", "France", "Greece", "Spain"]},
    {"What is the hardest natural substance on Earth?": ["Diamond", "Gold", "Iron", "Quartz"]}
]
 ]
		#تعیین شاخه و سوال
		bleach = random.choice(source_questions)
		question = random.choice(bleach)
		#دکمه های اولیه
		game_button['state']='disabled'
		game_button.config(bg='white')
		 #چاپ سوال
		key = list(question.keys())[0]
		label_question=Label(window ,text=f'question  :{key}')
		label_question.pack(pady=(100,2))
		remove_list.append(label_question)
		#چاپ کلمه پاسخ
		answers_word=Label(window,text='answers:')
		answers_word.pack(pady=(40,20))
		answers = question[key]
		remove_list.append(answers_word)
		#لیست پاسخ
		heck_ultimate = answers.copy()
		#کپی برای مقایسه نهایی
		random.shuffle(answers)
		
		#متغیر مقدار
		selected=IntVar(value=0)
		#دکمه رادیویی پاسخ ها 
		for i , ans in  enumerate(answers ,0):
			ans_radio=Radiobutton(window , text=ans , value=i , variable=selected,)
			ans_radio.pack()
			remove_list.append(ans_radio)
		c=False
		def home():
			global guide_game
			game_button['state']='normal'
			guide_button['state']='normal'
			game_status=False
			guide_status=False
			game_button.config(bg='#87CEFA')
			guide_button.config(bg='#87CEFA')
			for dray in remove_list:
				dray.destroy()
		#تایمر
		label_time=Label(window ,text=f'timer : {timer} seconds' , fg='red')
		label_time.pack(pady=(70 ,10))
		def timer_game():
			global timer
			try:
				if timer>0:
					timer -= 1
					label_time.config(text=f"timer : {timer} seconds")
					window.after(1000, timer_game)
				else:
					submit_chek()
			except :
				pass
		timer_game()
		remove_list.append(label_time)
		def submit_chek():
			global score , a , timer
			timer=10
			a +=1
			choice=selected.get()
			if answers[choice]==heck_ultimate[0]:
				score +=1
			if a <5:
				for j in remove_list:
					j.destroy()
				main_game()
			else :
				for j in remove_list:
					j.destroy()
				
				user_score=Label(window , text=f'Your final score is : {score}')
				user_score.pack()
				remove_list.append(user_score)
				a=0
				score=0
				frame_finish_game=Frame(window,pady=30)
				home_button=Button(frame_finish_game, text='home' ,command=home)
				again_game=Button(frame_finish_game , text='again', command=main_game)
				frame_finish_game.pack()
				again_game.pack(side=LEFT,padx=20)
				home_button.pack(side=LEFT,padx=20)
				remove_list.append(frame_finish_game)
					 	
		button_submit=Button(window,text='submit' , command=submit_chek)
		button_submit.pack()
		remove_list.append(button_submit)				
#دکمه امادگی
ready_button=Button(window,text='im ready',command=main_game , bg='#da7f1c' , borderwidth=5 , relief='solid',highlightbackground="#d49121")

#تابع قطع و وصل
game_status=False
def vis_game():
	global game_status,guide_button
	if game_status:
		ready_button.pack_forget()
		game_status=False
		guide_button['state']='normal'
		game_button.config(bg='#87CEFA')
		guide_button.config(bg='#87CEFA')
	else :
		ready_button.pack(pady=(60,0))
		game_status=True
		guide_button['state']='disabled'
		game_button.config(bg='#2ebc45')
		guide_button.config(bg='white')
		
#دکمه بازی
game_button=Button(first_frame , text='game' ,width=6,height=2 ,bg='#87CEFA',command=vis_game)
game_button.pack(side=LEFT,padx=20)


#دکمه خروج
exit_button=Button(first_frame,text='exit' ,width=6,height=2,bg='#87CEFA', command=lambda:window.destroy()
,activebackground='#2ebc45')
exit_button.pack(padx=20,side=LEFT)
#اجرای پیوسته
window.mainloop()
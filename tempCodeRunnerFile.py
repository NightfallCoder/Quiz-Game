class Question:
    def __init__(self,que_text,que_answer):
        self.text=que_text
        self.answer=que_answer

new_que=Question("is sky blue?","Yes")
print(new_que.text)
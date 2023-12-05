class QuizBrain:

    def __int__(self, question_list):
        
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):

        index = self.question_number
        question = self.question_list[index].question
        answer = self.question_list[index].answer
        user_answer = input(f"Q.{index + 1} {question}: ")

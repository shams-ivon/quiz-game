from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = item["question"]
    answer = item["answer"]
    question_object = Question(question, answer)
    question_bank.append(question_object)

quizes = QuizBrain(question_bank)


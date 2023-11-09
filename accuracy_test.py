# This file is used for testing the accuracy of the chatbot, using evaluete_string method

#-------------------------Imports-------------------------#

from langchain.evaluation import load_evaluator
from main import get_ans

#-------------------------Main Code-------------------------#

evaluator = load_evaluator("labeled_criteria", criteria="correctness")

# We can even override the model's learned knowledge using ground truth labels

questions = []
answers = []
predictions = []

questions.append("Quantas questoes de matematica possui a primeira fase?")
questions.append("Qual as vagas oferecidas pelo Vestibular Unicamp 2024?")
questions.append("Qual o numero de vagas regulares para o curso de enfermagem (integral)?")
questions.append("Quantos dias dura a segunda fase?")
questions.append("Qual a porcetagem de cota minima para alunos PPI?")

answers.append("12")
answers.append("2537")
answers.append("40")
answers.append("Dois dias")
answers.append("27,5%")

for question in questions:
    predictions.append(get_ans(question)[0])

# Print all the Questions, Answers and Predictions

for i in range(len(questions)):
    print("Question Number: " + str(i+1))
    print("Question: " + questions[i])
    print("Answer: " + answers[i])
    print("Prediction: " + predictions[i])
    print("")
    print("")
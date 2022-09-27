from polls.models import Question

def run():
    # Fetch all questions
    # questions = Question.objects.all()
    # Delete questions
    # questions.delete()
    myObj = Question()
    myObj.question_text = 'hi how r you'
    import datetime

    time = datetime.datetime.now()

    myObj.pub_date = time
    myObj.save()



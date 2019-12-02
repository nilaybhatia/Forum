# Forum
### A forum for juniors to ask doubts and for seniors/team members to reply
## Instructions to run the project locally
1. git clone https://www.github.com/nilaybhatia/Forum.git
2. cd Forum/
3. Activate your virtual environment (help [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/))
4. pip install -r requirements.txt (Assuming pip is installed)
5. python manage.py runserver


## About project
In most of the colleges, all the students, who are in different divisions and even in different years, communicate through WhatsApp. All the important announcements are received on WhatsApp. Questions get asked on WhatsApp. But all students are not part of all groups (group limit). Due to this, important info might not reach someone. Seniors might have to give the same answers to common questions(for example, during this very Unicode interview period). This forum serves as a bridging gap between juniors and seniors. It can also be used to ask general queries about the college. It has the functionality of upvoting, downvoting and editing answers, similar to StackOverflow.

---

**The Home Page**
![homepage](/images/homepage.png?raw=true "Forum Home Page")

---

**Using the StackOverflow API to show recent questions on homepage**
![stack_api](/images/stack_api.png?raw=true "Using API")
I have made use of the StackOverflow API to fetch the most recent questions.
TODO: Shift the questions to a sidebar to utilise space efficiently.

---

**The Question Detail Page**
![ques_detail](/images/ques_detail.png?raw=true "QnA page for a particular question")

Has features like **upvoting, downvoting and editing** questions and answers.
Answers are **sorted by upvotes**.

It also shows questions related to a language when the current question contains the language as a word. For eg. if somebody asks "In python, how to open a file in append mode?", then all recent questions from StackOverflow with the [```python```](https://stackoverflow.com/questions/tagged/python) will show up. I have used **Regular Expression** for this feature.

---
**Adding a new question**
![new_question](/images/new_question.png?raw=true "Asking a new question")

---
**Answering a question**
![new_question](/images/new_answer.png?raw=true "A Unicode Team Member answers the question")

---

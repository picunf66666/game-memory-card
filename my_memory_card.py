from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QGroupBox, QButtonGroup, QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton

class Quest():
    def __init__(self, quest, right_ans, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')
def show_quest():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    
    
    RadioGroup.setExclusive(False)
    btn_ans1.setChecked(False)
    btn_ans2.setChecked(False)
    btn_ans3.setChecked(False)
    btn_ans4.setChecked(False)
    RadioGroup.setExclusive(True)


def ask(q: Quest):
    shuffle(ans)
    ans[0].setText(q.right_ans)
    ans[1].setText(q.wrong1)
    ans[2].setText(q.wrong2)
    ans[3].setText(q.wrong3)
    lb_Qest.setText(q.quest)
    lb_Correct.setText(q.right_ans)
    show_quest()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_ans():
    main_win.total += 1
    if ans[0].isChecked():
        show_correct('харуш')
        main_win.score += 1
    else:
        if ans[1].isChecked() or ans[2].isChecked() or ans[3].isChecked():
            show_correct('ни маладэц')
    print('кол-во вопросов', str(main_win.total))
    print('кол-во правильных', str(main_win.score))
    print('результат:', str(main_win.score/main_win.total * 100))
        
def next_quest():
    main_win.cur_quest += 1
    if main_win.cur_quest >= len(quests_list):
        main_win.cur_quest = 0
    q = quests_list[main_win.cur_quest]
    ask(q)

def click_OK():
    if btn_ok.text() == 'Ответить':
        check_ans()
    else:
        next_quest()


# def start_test():
#     if btn_ok.text() == 'Ответить':
#         show_result()
#     else:
#         show_quest()


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
quest = QLabel('Кто я?')

btn_ok = QPushButton('Ответить')
lb_Qest = QLabel('Кто я?')

RadioGroupBox = QGroupBox('Варианты ответов')
btn_ans1 = QRadioButton('хз')
btn_ans2 = QRadioButton('пон')
btn_ans3 = QRadioButton('щкебеде туалет')
btn_ans4 = QRadioButton('пятка носорога')

ans = [btn_ans1, btn_ans2, btn_ans3, btn_ans4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_ans1)
RadioGroup.addButton(btn_ans2)
RadioGroup.addButton(btn_ans3)
RadioGroup.addButton(btn_ans4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(btn_ans1)
layout_ans2.addWidget(btn_ans2)
layout_ans3.addWidget(btn_ans3)
layout_ans3.addWidget(btn_ans4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат')
lb_Result = QLabel('кто же я?')
lb_Correct = QLabel('ответ будет тут:)')

layout_res  = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Qest, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.show()
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


quests_list = []
quests_list.append(Quest('узбеки спят?', 'да', 'нет', 'возможно частично', 'нипон'))
quests_list.append(Quest('вы женщина?', 'возможно частично', 'нет', 'да', 'нипон'))
quests_list.append(Quest('любишь спать?', 'да', 'нет', 'возможно частично', 'нипон'))
quests_list.append(Quest('гоу гоу гоу гоу?', 'да', 'нет', 'возможно частично', 'нипон'))
quests_list.append(Quest('прговбс', 'прго', 'прнит', 'првозможночастично', 'прнипон'))
quests_list.append(Quest('ти бибизян?', 'да', 'да', 'да', 'да'))
quests_list.append(Quest('ипопо?', 'возможно частично', ' нит', 'да', 'нипон'))
quests_list.append(Quest('привет щкебеде няшка', 'чиво тебе?', 'отстань', 'пр', 'ку'))
quests_list.append(Quest('грустная мордащке', 'ну отстань', 'нит', 'бб', 'данамо'))
quests_list.append(Quest('в л', 'хз', 'л', 'ф', 'в'))

main_win.cur_quest = -1
btn_ok.clicked.connect(click_OK)
main_win.score = 0
main_win.total = 0
next_quest()
main_win.setLayout(layout_card)
main_win.show()
app.exec_()
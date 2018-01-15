from tkinter import *

##root라는 참조변수 생성
root = Tk()

##메모리에 만듬
lb1=Label(root, text='이름')##누구를 부모로 할 것인가? >> root

## 메모리에 있는 것을 pack하여 준비시킴


## 텍스트는 한줄이냐 여러줄이냐로 나누어짐 한줄 > Entry 여러줄 Text
## parent를 선언해주어야 한다.
txt = Entry(root)
txt.pack()
## pack으로 실행시킴
##pack의 선언 순서에 따라 배치도가 달라진다.
lb1.pack()
btn =Button(root,text= "OK")
btn.pack()
root.mainloop()






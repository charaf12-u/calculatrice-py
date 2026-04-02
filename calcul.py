from tkinter import *
fen = Tk()
fen.title("CALCULATRICE")

# إنشاء حقل الإدخال
e = Entry(fen, width=60, bg="light blue", borderwidth=10)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# دالة لإضافة الأزرار
def addButton(num):
    return Button(fen, padx=16, bd=8, fg="blue", text=num, width=5, command=lambda: clickButton(str(num)))

# دالة لإنشاء الأزرار
def createButton():
    b = addButton(0)    # إنشاء زر الرقم 0
    b1 = addButton(1)
    b2 = addButton(2)
    b3 = addButton(3)
    b4 = addButton(4)
    b5 = addButton(5)
    b6 = addButton(6)
    b7 = addButton(7)
    b8 = addButton(8)
    b9 = addButton(9)
    B_add = addButton("+")
    B_sub = addButton("-")
    B_mult = addButton("*")
    B_div = addButton("/")
    B_clear = addButton("AC")
    B_equal = addButton("=")

    # تنظيم الأزرار في صفوف
    row = [b7, b8, b9, B_add]    # صف الأزرار الأول
    row1 = [b4, b5, b6, B_sub]   # صف الأزرار الثاني
    row2 = [b1, b2, b3, B_mult]  # صف الأزرار الثالث
    row3 = [B_clear, b, B_equal, B_div]   # صف الأزرار الرابع

    r = 1
    for row in [row, row1, row2, row3]:
        c = 0
        for button in row:
            button.grid(row=r, column=c, columnspan=1)
            c += 1
        r += 1

# دالة للتعامل مع الأزرار عند النقر عليها
def clickButton(value):
    current_eq = str(e.get())
    if value == 'AC':
        e.delete(0, END)   # حذف المحتوى في حالة النقر على زر "AC"
    elif value == '=':
        answer = str(eval(current_eq))
        e.delete(0, END)
        e.insert(0, answer)   # إدراج الإجابة في حالة النقر على زر "="
    else:
        e.delete(0, END)
        e.insert(0, current_eq + value)   # إضافة القيمة المضغوطة إلى الحقل

createButton()
fen.mainloop()
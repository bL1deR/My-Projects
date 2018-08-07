
from tkinter import StringVar, Tk, Entry, Button, DISABLED, RIGHT, RAISED
import encodings 

# Main Window

window = Tk()
window.title("Calculator")
window.geometry("200x295")
window.grab_set()
window.resizable(0, 0)
strVar = str() # String variable to operate with in programme itself
floatVar1 = float() # floateger variable of 1st number to operate with in programme itself
floatVar2 = float() # floateger variable of 2nd number to operate with in programme itself
resultVar = float() # floateger variable of result to operate with in programme itself
oprSymb = str() # Symbol of operation
outputStr = StringVar() # Special string variable for displaying numbers in the entry
outputStr.set("0")

# buttonNumX click function
def buttonNumX_click(var):
	global strVar
	if var == 0 and outputStr.get() == "0" and strVar == "0":
		pass
	elif var != 0 and outputStr.get() == "0" and strVar == "0":
		strVar = str(var)
		outputStr.set(strVar)
	else:
		strVar += str(var)
		outputStr.set(strVar)

# buttonCE (CLEAR) click function
def buttonCE_click():
	global strVar
	global floatVar1
	global floatVar2
	global resultVar
	global oprSymb
	strVar = "0"
	floatVar1 = 0
	floatVar2 = 0
	resultVar = 0
	oprSymb = str()
	outputStr.set(strVar)

# buttonBackSpace click function
def buttonBackSpace_click():
	global strVar
	if len(strVar) == 1:
		strVar = strVar[:-1]
		buttonNumX_click(0)
	else:
		strVar = strVar[:-1]
		outputStr.set(strVar)

# buttonOpr click function
def buttonOpr_click(strOprSymb):
	global strVar
	global floatVar1
	global oprSymb
	floatVar1 = float(strVar)
	oprSymb = strOprSymb
	strVar = "0"
	outputStr.set(strVar)

# buttonEqual click function
def buttonEqual_click():
	global strVar
	global floatVar2
	global resultVar
	floatVar2 = float(strVar)

	if oprSymb == "+":
		resultVar = floatVar1 + floatVar2
		strVar = str(resultVar)
		outputStr.set(strVar)
	elif oprSymb == "-":
		resultVar = floatVar1 - floatVar2
		strVar = str(resultVar)
		outputStr.set(strVar)
	elif oprSymb == "*":
		resultVar = floatVar1 * floatVar2
		strVar = str(resultVar)
		outputStr.set(strVar)
	elif oprSymb == "/":
		resultVar = floatVar1 / floatVar2
		strVar = str(resultVar)
		outputStr.set(strVar)


# Creating and placing widgets floato window
# Entry (output) for displaying variables
output = Entry(window, font = "arial 10", state = DISABLED, justify = RIGHT, textvariable = outputStr, fg = "black", cursor = "arrow", bd = 3)
output.place(x = 5, y = 10, bordermode = "inside", width = 190, height = 25)

# Buttons
# 1st row of buttons - "CE", "←"
buttonCE = Button(window, font = "arial 14", relief = RAISED, text = "CE", command = lambda:buttonCE_click())
buttonCE.place(x = 5, y = 50, width = 90, height = 40)
buttonBackSpace = Button(window, font = "arial 18", relief = RAISED, text = "←", command = lambda:buttonBackSpace_click())
buttonBackSpace.place(x = 105, y = 50, width = 90, height = 40)

# 2nd row of buttons - "7", "8", "9", "/"
buttonNum7 = Button(window, font = "arial 14", relief = RAISED, text = "7", command = lambda:buttonNumX_click(7))
buttonNum7.place(x = 5, y = 100, width = 40, height = 40)
buttonNum8 = Button(window, font = "arial 14", relief = RAISED, text = "8", command = lambda:buttonNumX_click(8))
buttonNum8.place(x = 55, y = 100, width = 40, height = 40)
buttonNum9 = Button(window, font = "arial 14", relief = RAISED, text = "9", command = lambda:buttonNumX_click(9))
buttonNum9.place(x = 105, y = 100, width = 40, height = 40)
buttonDiv = Button(window, font = "arial 14", relief = RAISED, text = "/", command = lambda:buttonOpr_click("/"))
buttonDiv.place(x = 155, y = 100, width = 40, height = 40)

# 3rd row of buttons - "4", "5", "6", "×"
buttonNum4 = Button(window, font = "arial 14", relief = RAISED, text = "4", command = lambda:buttonNumX_click(4))
buttonNum4.place(x = 5, y = 150, width = 40, height = 40)
buttonNum5 = Button(window, font = "arial 14", relief = RAISED, text = "5", command = lambda:buttonNumX_click(5))
buttonNum5.place(x = 55, y = 150, width = 40, height = 40)
buttonNum6 = Button(window, font = "arial 14", relief = RAISED, text = "6", command = lambda:buttonNumX_click(6))
buttonNum6.place(x = 105, y = 150, width = 40, height = 40)
buttonMult = Button(window, font = "arial 14", relief = RAISED, text = "*", command = lambda:buttonOpr_click("*"))
buttonMult.place(x = 155, y = 150, width = 40, height = 40)

# 4th row of buttons - "1", "2", "3", "-"
buttonNum1 = Button(window, font = "arial 14", relief = RAISED, text = "1", command = lambda:buttonNumX_click(1))
buttonNum1.place(x = 5, y = 200, width = 40, height = 40)
buttonNum2 = Button(window, font = "arial 14", relief = RAISED, text = "2", command = lambda:buttonNumX_click(2))
buttonNum2.place(x = 55, y = 200, width = 40, height = 40)
buttonNum3 = Button(window, font = "arial 14", relief = RAISED, text = "3", command = lambda:buttonNumX_click(3))
buttonNum3.place(x = 105, y = 200, width = 40, height = 40)
buttonSub = Button(window, font = "arial 14", relief = RAISED, text = "-", command = lambda:buttonOpr_click("-"))
buttonSub.place(x = 155, y = 200, width = 40, height = 40)

# 5th row of buttons - "0", "=", "+"
buttonNum0 = Button(window, font = "arial 14", relief = RAISED, text = "0", command = lambda:buttonNumX_click(0))
buttonNum0.place(x = 5, y = 250, width = 90, height = 40)
buttonEqual = Button(window, font = "arial 14", relief = RAISED, text = "=", command = lambda:buttonEqual_click())
buttonEqual.place(x = 105, y = 250, width = 40, height = 40)
buttonAdd = Button(window, font = "arial 14", relief = RAISED, text = "+", command = lambda:buttonOpr_click("+"))
buttonAdd.place(x = 155, y = 250, width = 40, height = 40)

window.mainloop()

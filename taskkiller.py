import os
import pyautogui

while True:
    task_name = pyautogui.prompt(title='Enter task Name', text='Enter the name of the task you want to kill')
    if ".exe" not in task_name:
        task_name = task_name + ".exe"
    command = "taskkill /f /IM " + "\"" + task_name + "\""
    result = os.system(command)
    if result == 0:
        pyautogui.alert(text='Task Killed')
        break
    if result == 128:
        pyautogui.alert(text="Task not found! try again")
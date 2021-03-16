import tkinter as tk
from playsound import playsound
from automata.fa.dfa import DFA

root = tk.Tk()
root.title("UTuvcs Vehicle Control System")
root.geometry('600x400')
greeting = tk.PhotoImage(file="Multimedia/Road.png")
greeting_label = tk.Label(root, image=greeting)
greeting_label.place(relwidth=1, relheight=1)

lbl = tk.Label(root, text="Welcome to our UTuvcs Vehicle Control System", font=('Times New Roman Bold', 16))
lbl.grid(column=0, row=0)


def response(dfa, entry):
    try:
        if dfa.accepts_input(entry):
            title = "Accepted"
            string = entry
            sequence = list(dfa.read_input_stepwise(entry))
            speed = "0"
            output = 'State: %s \nString entered is: %s \nSteps: %s \nSpeed is: %s' % (title, string, sequence, speed)
        else:
            title = "Rejected"
            string = entry
            # speed = "1"
            output = 'State: %s \nString entered is: %s ' % (title, string)
    except:
        output = 'Entry is invalid. Try again'

    return output


def generate(entry, label):
    dfa = DFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', ''},
        input_symbols={'1', '2', '3', '4', '5', '6', '7', '8', '9', ' '},
        transitions={
            'q0': {'1': 'q1', '2': 'q2', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '', ' ': ''},
            'q1': {'1': '', '2': 'q3', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '', ' ': ''},
            'q2': {'1': 'q1', '2': 'q0', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '', ' ': ''},
            'q3': {'1': '', '2': 'q0', '3': 'q4', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '', ' ': ''},
            'q4': {'1': '', '2': '', '3': '', '4': 'q5', '5': 'q4', '6': 'q3', '7': 'q6', '8': '', '9': '', ' ': ''},
            'q5': {'1': '', '2': '', '3': '', '4': '', '5': 'q5', '6': '', '7': '', '8': 'q5', '9': 'q7', ' ': 'q4'},
            'q6': {'1': 'q4', '2': '', '3': '', '4': '', '5': 'q6', '6': '', '7': '', '8': 'q6', '9': '', ' ': ''},
            'q7': {'1': 'q4', '2': '', '3': '', '4': '', '5': 'q7', '6': '', '7': '', '8': 'q5', '9': '', ' ': ''},
            '': {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '', ' ': ''}
        },
        initial_state='q0',
        final_states={'q0'}
    )

    label['text'] = response(dfa, entry)


def clicked():
    root.title("DFA")
    root.geometry('600x430')
    playsound('Multimedia/Vehicle.wav')

    frame = tk.Frame(root, bg='black', bd=3)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry = tk.Entry(frame, font=('Times New Roman', 14))
    entry.place(relwidth=0.65, relheight=1)

    btn = tk.Button(frame, text="Generate DFA", font=('Times New Roman', 12), command=lambda: generate(entry.get(), label))
    btn.place(relx=0.7, relwidth=0.3, relheight=1)

    lower_frame = tk.Frame(root, bg='black', bd=5)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = tk.Label(lower_frame, font=('Times New Roman', 16))
    label.place(relwidth=1, relheight=1)


btn1 = tk.Button(root, text="Let's begin", command=clicked, width=12, font=('Times New Roman', 12))
btn1.place(x=205, y=150)

root.mainloop()

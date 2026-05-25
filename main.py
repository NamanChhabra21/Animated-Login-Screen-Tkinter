# Login Window Using Tkinter

success = False
from tkinter import *
import pandas as pd
import json
import time # Beginner Friendly | You can use after() function too!
import threading
import datetime

# Basic Setup
window = Tk()
window.geometry("500x500")
window.title("Login Screen")
window.configure(background="gray5")
running = True

# LOADING DATA FROM `Data.json`
with open("Data.json") as f:
    file_data = json.load(f)
Data = pd.DataFrame(file_data["users"])

wrong_label = Label()
def on_close():
    global running,wrong_label
    running = False
    loginFrame.destroy()
    loginLabel.destroy()
    wrong_label.destroy()
    wrong_label = None
    window.destroy()


window.protocol("WM_DELETE_WINDOW", on_close) # Direct Exits the Window





loginLabel = Label(window, text="Login", fg="white", bg="gray5",font=("cooper black", 40))
loginLabel.pack(pady=20)

loadinglabel = Label() # Will be defined later
# Animating Login Text
def change_login_color():
    global loadinglabel
    colors = [
        "#140a1f", "#1c0f2b", "#241437", "#2c1943", "#341e4f",
        "#3c235b", "#442867", "#4c2d73", "#54327f", "#5c378b",
        "#643c97", "#7a52ad", "#9470c2", "#b08fd6", "#cbb0e8",
        "#e6d4f7", "#f5ecff", "#ffffff",
        "#f5ecff", "#e6d4f7", "#cbb0e8", "#b08fd6", "#9470c2",
        "#7a52ad", "#643c97", "#5c378b", "#54327f", "#4c2d73",
        "#442867", "#3c235b", "#341e4f", "#2c1943", "#241437",
        "#1c0f2b", "#140a1f","#2c3e50", "#34495e", "#3b5998", "#4a69bd", "#5f7adb",
        "#6c8cff", "#7ea1ff", "#90b5ff", "#a3c9ff", "#b7dcff",
        "#cbeaff", "#dff5ff", "#f0fbff", "#ffffff",
        "#f0fbff", "#dff5ff", "#cbeaff", "#b7dcff", "#a3c9ff",
        "#90b5ff", "#7ea1ff", "#6c8cff", "#5f7adb", "#4a69bd",
        "#3b5998", "#34495e", "#2c3e50",
        "#3a2e1f", "#4a3723", "#5a4027", "#6a4a2b", "#7a542f",
        "#8a5e33", "#9a6837", "#aa733b", "#ba7d3f", "#ca8843",
        "#daa247", "#eabf6b", "#f5d58f", "#fff3d6", "#ffffff",
        "#fff3d6", "#f5d58f", "#eabf6b", "#daa247", "#ca8843",
        "#ba7d3f", "#aa733b", "#9a6837", "#8a5e33", "#7a542f",
        "#6a4a2b", "#5a4027", "#4a3723", "#3a2e1f",
        "#1a0808", "#2a0d0d", "#3a1212", "#4a1717", "#5a1c1c",
        "#6a2121", "#7a2626", "#8a2b2b", "#9a3030", "#aa3535",
        "#ba3a3a", "#cc4a4a", "#dd6a6a", "#ee9a9a", "#f7caca",
        "#fdeeee", "#ffffff",
        "#fdeeee", "#f7caca", "#ee9a9a", "#dd6a6a", "#cc4a4a",
        "#ba3a3a", "#aa3535", "#9a3030", "#8a2b2b", "#7a2626",
        "#6a2121", "#5a1c1c", "#4a1717", "#3a1212", "#2a0d0d",
        "#1a0808",
        "#2a2622", "#332e29", "#3c3731", "#454038", "#4e4940",
        "#575248", "#605b50", "#696458", "#726d60", "#7b7668",
        "#847f70", "#9a9587", "#b3aea1", "#d4cec3", "#eee7dc",
        "#f7f1e7", "#fffaf0", "#ffffff",
        "#fffaf0", "#f7f1e7", "#eee7dc", "#d4cec3", "#b3aea1",
        "#9a9587", "#847f70", "#7b7668", "#726d60", "#696458",
        "#605b50", "#575248", "#4e4940", "#454038", "#3c3731",
        "#332e29", "#2a2622"

    ]
    while running:
        a = 15
        # Fade In
        for color in colors:
            if running:
                loginLabel.configure(fg = color)
                time.sleep(0.05)
            else:
                break

            if a ==15:
                a+=1
            else:
                a-=1

            # Check if Login Success
        if success:
            loginFrame.destroy()
            loadinglabel.destroy()
            loginLabel.configure(text="Successfully Logged In", fg="Green", pady=175, font=("cooper black", 20))
            return

color_thread = threading.Thread(target=change_login_color)
color_thread.start()



# Creating Login Frame
loginFrame = Frame(window, bg="black", width=350, height=300,borderwidth=2,border=2,relief="groove")
loginFrame.pack(pady=20)
loginFrame.grid_propagate(False)

# Creating Quotes Animation
def enable_quotes():
    # Deleting Frame will delete this too
    quotes =[
    "First password system (1960s) got hacked quickly",
    "`123456` is still widely used",
    "People manage 70+ passwords on average",
    "Fingerprint/face login is growing fast",
    "Passwordless login is now a thing",
    "Strong passwords use mixed characters",
    "2FA adds an extra security layer",
    "Thousands of logins happen every second",
    "Long passwords = better security"
    ]
    while running and not success:
        if not success and running:
            for text in quotes:
                if success or not running:
                    break
                if running:
                    quote.configure(text=f"Fun Fact: {text}")
                for i in range(0,100):
                    if success or not running:
                        break
                    quote.configure(fg=f"gray{i}")
                    time.sleep(0.02)

                time.sleep(1)
                for i in range(100,0,-1):
                    if success:
                        break
                    if running:
                        quote.configure(fg=f"gray{i}")
                    else:
                        break
                    time.sleep(0.02)




anime_frame = Frame(loginFrame,bg="black", width=325, height=25,borderwidth=0,border=0,relief="groove")
anime_frame.grid(row=6,columnspan=2)
anime_frame.pack_propagate(False)
quote =Label(anime_frame,text="Developed By Naman ~",fg="white",bg="black",font=("Montserrat",8))
quote.pack()
quote_thread = threading.Thread(target=enable_quotes)
quote_thread.start()

# Username input
username_label = Label(loginFrame, text="Username :", fg="white", bg="black",font=("cooper black", 15))
username_label.grid(row=0, column=0,pady=40,padx=10)
username_entry = Entry(loginFrame, fg="black", bg="gray80", font=("arial",13,"bold"),cursor="xterm",insertbackground="red",)
username_entry.grid(row=0, column=1,pady=40,padx=10)

# Password input
pass_label = Label(loginFrame, text="Password :", fg="white", bg="black",font=("cooper black", 15))
pass_label.grid(row=1, column=0,padx=10)
pass_entry = Entry(loginFrame, fg="black", show="*",bg="gray80", font=("arial",13,"bold"),cursor="xterm",insertbackground="red",)
pass_entry.grid(row=1, column=1,padx=10)

mail_entry = Entry(loginFrame, fg="black", bg="gray80", font=("arial", 13, "bold"), cursor="xterm",
                       insertbackground="red")
mail_entry.grid(row=3, column=1, padx=10,pady=15)
mail_entry.grid_forget()


def show_text(text,color="red",pause=3):
    def wrong_thread():
        global wrong_label
        signin.configure(state="normal")
        loadinglabel.destroy()
        wronglabel = Label(window, text=f"{text}", fg=color, bg="gray5", font=("None", 12))
        wronglabel.pack()
        time.sleep(pause)
        if wrong_label:
            wronglabel.destroy()
    threading.Thread(target=wrong_thread).start()

# Check Password
correct = 0
def check():
    global loadinglabel,correct
    global success
    signin.configure(state="disabled")
    loadinglabel = Label(window, text="Please Wait...", fg="white", bg="gray5", font=("None", 12))
    loadinglabel.pack()
    InputPass = pass_entry.get()
    InputUsername = username_entry.get()

    result = Data.loc[Data["userId"] == InputUsername,"password"]
    print(result.values)
    # Check if all the entries are filled
    if "" in [InputUsername.strip(),InputPass.strip()]:
        show_text("Username or Password cannot be empty!")
        return
    # Check if Username exists
    if not result.empty:
        correct += 1
    else:
        show_text("No Username found. Try Again!")
        correct = 0
        return # dont check password

    # Check Password is correct or not

    if InputPass == result.values: # result.values is password
        correct += 1
    else:
        show_text("Incorrect Password. Try Again!")
        correct = 0

    # If Both are correct
    if correct == 2:
        success = True

def add_new_entry():
    username = username_entry.get().strip()
    password = pass_entry.get().strip()
    mail = mail_entry.get().strip()

    if "" in [username,password,mail]:
        show_text("Username/Password/Mail cannot be empty!")
        return
    check_username = Data.loc[Data["userId"] == username]
    if not check_username.empty:
        show_text("Username already exists! If this is you, Please LogIn")
        return
    if len(password) < 7:
        show_text("Password length must be more than 6 characters.")
        return

    new_user = {
        "userId": username,
        "password": password,
        "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mail": mail
    }
    Data.loc[len(Data)] = new_user
    new_data = {"users": Data.to_dict(orient="records")}

    with open("Data.json", "w") as Q:
        json.dump(new_data, Q, indent=4)
    show_text("Successfully Registered! Please login again to continue!",color="green",pause=8)
    signincmd()




mail_label = Label(loginFrame, text="Mail :", fg="white", bg="black", font=("cooper black", 15))
def signincmd():
    global mail_label,mail_entry
    loginLabel.configure(text="Login")
    signin.configure(text="Sign In",command=check)
    signUpButton.configure(text="Sign Up",command=signup)
    mail_label.grid_forget()
    mail_entry.grid_forget()

    pass_entry.configure(show="*")
    username_entry.grid_configure(pady=40)
    username_label.grid_configure(pady=40)

    # Clear User Entries
    username_entry.delete(0,"end")
    pass_entry.delete(0, "end")



def signup():
    global mail_label, mail_entry
    # loginFrame.configure(height=420)
    loginLabel.configure(text="Sign Up")
    username_entry.grid_configure(pady=15)
    username_label.grid_configure(pady=15)
    signin.configure(text="Sign Up",command=add_new_entry)
    signUpButton.configure(text="Sign In",command=signincmd)
    pass_entry.configure(show="")


    mail_label.grid(row=3, column=0, padx=15)

    # mail_entry = Entry(loginFrame, fg="black", bg="gray80", font=("arial", 13, "bold"), cursor="xterm",
    #                    insertbackground="red")
    mail_entry.grid(row=3, column=1, padx=10,pady=15)

    # Clear User Entries
    username_entry.delete(0, "end")
    pass_entry.delete(0, "end")
# Sign In button
signin = Button(loginFrame,text="Sign In",fg ="white",bg ="black",font=("none",15),relief="sunken",borderwidth=4,command=check)
signin.grid(row=4,columnspan=2,pady=20)

signUpButton = Button(loginFrame,text="Sign Up",command=signup,fg="blue",bg="black",borderwidth=0,highlightcolor="red")
signUpButton.grid(row=5,columnspan=2,pady=10)
window.mainloop()



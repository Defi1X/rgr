import customtkinter
import modules.configuration
from CTkMessagebox import CTkMessagebox

def unlockProcedure():
    parentWindow = customtkinter.CTk()
    parentWindow.geometry("120x120+500+500")
    parentWindow.state("withdrawn")

    unlocked = False
    while not unlocked:
        unlockWindow = customtkinter.CTkInputDialog(title="Unlock procedure", text="Enter a valid password:")
        entered = unlockWindow.get_input()
        if entered == modules.configuration.password:
            unlocked = True
            parentWindow.destroy()
            return unlocked
        else:
            if entered != modules.configuration.password and entered != "":
                toplevel = customtkinter.CTkToplevel()
                toplevel.title("Error")
                
                label = customtkinter.CTkLabel(toplevel, text="Incorrect password providied! Try again.")
                label.pack()

                def close_window():
                    toplevel.destroy()

                button = customtkinter.CTkButton(toplevel, text="Close", command=close_window)
                button.pack()

                toplevel.focus()
            else:
                unlocked = False
                parentWindow.destroy()
                return unlocked
            
def isTextValid(text):
    try:
        for i in text:
            if i.lower() in "йцукенгшщзхъфывапролджэячсмитьбю":
                return False
    except Exception as e:
        return False
    
    return True
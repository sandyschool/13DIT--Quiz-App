from first_gui import TriviaQuiz
import tkinter as tk
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Trivia Game")
    root.geometry("400x500")
    root.resizable(False, False)
    
    app = TriviaQuiz(root)
    
    # Start the main loop
    root.mainloop()

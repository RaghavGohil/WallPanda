import gui
import file_manager

def main():
    application = gui.App()
    file_manager.set_gui_instance(application)
    application.mainloop()

main()
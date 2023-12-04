import gui
import button_generator

def main():
    application = gui.App()
    button_generator.set_gui_instance(application)
    application.mainloop()

main()
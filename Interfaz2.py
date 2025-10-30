import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk



class Interfaz2(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ventana Main")

        frame1=Gtk.Frame.new("Frame")
        frame1.



        self.show()

if  __name__ == "__main__":
    Interfaz2()
    Gtk.main()
import gi
import CaixaCor
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject

class EjemploBox(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de uso de box layout")

        #definimod partes de la caja
        caixa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 5)
        caixav1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 5)

        caixav1.pack_start(CaixaCor.CaixaCor('red'), True, True, 2)
        caixav1.pack_start(CaixaCor.CaixaCor('yellow'), True, True, 2)
        caixav1.pack_start(CaixaCor.CaixaCor('red'), True, True, 2)

        caixa.pack_start(caixav1, True, True, 5)
        caixa.pack_start(CaixaCor.CaixaCor('grey'), True, True, 2)

        caixav2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)
        caixav2.pack_start(CaixaCor.CaixaCor('black'), True, True, 2)
        caixav2.pack_start(CaixaCor.CaixaCor('red'), True, True, 2)
        caixav2.pack_start(CaixaCor.CaixaCor('yellow'), True, True, 2)

        caixa.pack_start(caixav2, True, True, 5)


        self.add(caixa)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()

if  __name__ == "__main__":
    EjemploBox()
    Gtk.main()






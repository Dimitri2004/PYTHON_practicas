import gi
import caixaCor
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject

class Ejemplogrid(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de uso de box layout")

        vermello = caixaCor.CaixaCor("red")
        azul = caixaCor.CaixaCor("blue")
        verde = caixaCor.CaixaCor("green")
        laranxa = caixaCor.CaixaCor("orange")
        amarelo = caixaCor.CaixaCor("yellow")
        negro = caixaCor.CaixaCor("black")
        marron = caixaCor.CaixaCor("brown")
        lila = caixaCor.CaixaCor("purple")

        #empleando attach_nextto y GTK.positiontype.(left o right) topo buttom
        maia =Gtk.Grid()

        maia.attach_next_to(vermello,None,Gtk.PositionType.LEFT,1,2)
        maia.attach_next_to(amarelo, vermello, Gtk.PositionType.RIGHT, 1, 1)
        maia.attach_next_to(verde, amarelo, Gtk.PositionType.BOTTOM, 2, 1)
        maia.attach_next_to(azul, vermello, Gtk.PositionType.BOTTOM, 2, 1)
        maia.attach_next_to(negro, azul, Gtk.PositionType.RIGHT, 1, 1)
        maia.attach_next_to(laranxa, negro, Gtk.PositionType.RIGHT, 1, 1)
        maia.attach_next_to(negro, azul, Gtk.PositionType.RIGHT, 1, 1)
        maia.attach_next_to(marron, laranxa, Gtk.PositionType.TOP, 1, 2)
        maia.attach_next_to(lila, amarelo, Gtk.PositionType.RIGHT, 1, 1)






        # Añadir la cuadrícula a la ventana
        self.add(maia)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()

if  __name__ == "__main__":
    Ejemplogrid()
    Gtk.main()
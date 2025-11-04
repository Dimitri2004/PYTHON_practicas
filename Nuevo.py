import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class EjemplosBoxColor(Gtk.Window):
    def __init__(self):
        super().__init__(title="Ejemplo de layout")
        self.set_default_size(600, 500)

        # === Contenedor general dentro del Frame principal ===
        grid_main = Gtk.Grid()
        frame_caption = Gtk.Frame(label="Panel Caption")
        frame_caption.add(grid_main)
        self.add(frame_caption)

        # === Frame del Panel principal ===
        frame_panel = Gtk.Frame(label="Panel")
        grid_main.add(frame_panel)

        panel_content = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        frame_panel.add(panel_content)

        # === Lista ===
        lista_contenido = Gtk.ListStore(str)
        for item in ("Item1", "Item2"):
            lista_contenido.append([item])

        treeview = Gtk.TreeView(model=lista_contenido)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Contenido", renderer, text=0)
        treeview.append_column(column)
        panel_content.pack_start(treeview, True, True, 0)

        # === Panel de botones ===
        botones_panel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        panel_content.pack_start(botones_panel, False, False, 0)

        # Radio buttons
        radio1 = Gtk.RadioButton.new_with_label_from_widget(None, "Botón 1")
        radio2 = Gtk.RadioButton.new_with_label_from_widget(radio1, "Botón 2")
        radio3 = Gtk.RadioButton.new_with_label_from_widget(radio1, "Botón 3")
        radio_inactivo = Gtk.RadioButton.new_with_label_from_widget(radio1, "Botón inactivo")
        radio_inactivo.set_sensitive(False)

        # Relleno y botón
        relleno = Gtk.Label()
        relleno.set_size_request(0, 50)
        boton = Gtk.Button(label="Botón")

        # Añadir botones al panel
        for widget in (radio1, radio2, radio3, radio_inactivo, relleno, boton):
            botones_panel.pack_start(widget, False, False, 0)

        # === Panel de pestañas ===
        frame_tabs = Gtk.Frame()
        frame_tabs.set_size_request(-1, 100)
        grid_main.attach_next_to(frame_tabs, frame_panel, Gtk.PositionType.RIGHT, 1, 1)

        panel_tabs = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        frame_tabs.add(panel_tabs)

        # Stack + Switcher
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(500)

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        panel_tabs.pack_start(stack_switcher, False, False, 0)

        # Tabs
        label_tab1 = Gtk.Label(label="")
        label_tab2 = Gtk.Label(label="")

        stack.add_titled(label_tab1, "tab1", "Tab 1")
        stack.add_titled(label_tab2, "tab2", "Tab 2")

        panel_tabs.pack_start(stack, True, True, 0)

        # === Final ===
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemplosBoxColor()
    Gtk.main()

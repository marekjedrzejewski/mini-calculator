import re
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


def enter_text_from_button_label(button):
    cursor_position = entry.props.cursor_position
    entry.insert_text(button.get_label(), cursor_position)
    entry.set_position(cursor_position + 1)


class Handler:
    def on_delete_window(self, *args):
        Gtk.main_quit(*args)

    def on_number_button_clicked(self, button):
        enter_text_from_button_label(button)

    def on_operator_button_clicked(self, button):
        enter_text_from_button_label(button)

    def calculate(self, obj):
        try:
            value = eval(entry.props.text)
        except:
            dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR,
                                       Gtk.ButtonsType.CANCEL,
                                       'Something happened.')
            dialog.format_secondary_text('Something happened.')
            dialog.run()
            dialog.destroy()
        else:
            entry.props.text = str(value)

    def validate_insert(self, obj, text, text_length, position):
        if re.match('[^\d\.\*\/\-\+]', text):
            GObject.signal_stop_emission_by_name(obj, 'insert-text')


builder = Gtk.Builder()
builder.add_from_file("mini_calculator.glade")
builder.connect_signals(Handler())

window = builder.get_object("main_window")
entry = builder.get_object("entry_window")
window.show_all()

Gtk.main()

import gdb
import pygal

class plot(gdb.Command):
    """Diplays the content of an opencv image"""

    def __init__(self):
        super(plot, self).__init__('plot',
                                        gdb.COMMAND_SUPPORT,
                                        gdb.COMPLETE_FILENAME)

    def invoke (self, arg, from_tty):
        args = gdb.string_to_argv(arg)
        img_var = args[0]
        if len(args) > 1:
            self._filename = args[1]
        else:
            self._filename = '/tmp/gdb_plot.svg'

        frame = gdb.selected_frame()
        val = frame.read_var(img_var)
        type_str = str(val.type.strip_typedefs())
        print(type_str)

        chart = pygal.Line()
        chart.title = 'Browser usage evolution (in %)'
        chart.x_labels = map(str, range(2002, 2013))
        chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
        chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
        chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
        chart.render_to_file(self._filename)
        print('Chart saved to ' + self._filename)


plot()

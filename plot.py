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
        var_name = args[0]
        if len(args) > 1:
            self._filename = args[1]
        else:
            self._filename = '/tmp/gdb_plot.svg'

        frame = gdb.selected_frame()

        # size = int(gdb.parse_and_eval('({}).size()'.format(var_name)))
        # print(size)
        # print(gdb.parse_and_eval('{}._M_impl._M_start[{}]'.format(var_name, 1)))

        chart = pygal.Line()
        chart.title = 'GDB plot'
        chart.x_labels = range(size)
        chart.add(var_name,
                  [float(gdb.parse_and_eval('{}._M_impl._M_start[{}]'.format(var_name, i))) for i in range(size)])
        chart.render_to_file(self._filename)
        print('Chart saved to ' + self._filename)


plot()

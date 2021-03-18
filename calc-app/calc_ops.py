

class CalcOp:

    def __init__(self, calc_op_id, calc_op_label, calc_op_command, calc_op_fn):
        self.id = calc_op_id
        self.label = calc_op_label
        self.command = calc_op_command
        self.fn = calc_op_fn


calc_ops = [
    CalcOp(1, "Add", "add", lambda x, y: x + y),
    CalcOp(2, "Subtract", "subtract", lambda x, y: x - y),
    CalcOp(3, "Multiply", "multiply", lambda x, y: x * y),
    CalcOp(4, "Divide", "divide", lambda x, y: x / y),
    CalcOp(5, "Exponent", "exponent", lambda x, y: x ** y),
]

calc_op_commands = [calc_op.command for calc_op in calc_ops]

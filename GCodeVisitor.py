from generated_code.gcode_grammarParser import gcode_grammarParser
from generated_code.gcode_grammarVisitor import gcode_grammarVisitor


class GCodeVisitor(gcode_grammarVisitor):
    def visitProgram(self, ctx: gcode_grammarParser.ProgramContext):
        for command_ctx in ctx.command():
            self.visitCommand(command_ctx)

    def visitCommand(self, ctx: gcode_grammarParser.CommandContext):
        if ctx.simple_motion_command():
            self.visitSimple_motion_command(ctx.simple_motion_command())

    def visitSimple_motion_command(self, ctx: gcode_grammarParser.Simple_motion_commandContext):
        motion_type = ctx.getChild(0).getText()
        x_arg = ctx.X_ARG().getText() if ctx.X_ARG() else None
        y_arg = ctx.Y_ARG().getText() if ctx.Y_ARG() else None
        z_arg = ctx.Z_ARG().getText() if ctx.Z_ARG() else None
        e_arg = ctx.EXTRUSION_ARG().getText() if ctx.EXTRUSION_ARG() else None
        f_arg = ctx.FEEDRATE_ARG().getText() if ctx.FEEDRATE_ARG() else None
        print(f"Motion type: {motion_type}, X: {x_arg}, Y: {y_arg}, Z: {z_arg}, E: {e_arg}, F: {f_arg}")

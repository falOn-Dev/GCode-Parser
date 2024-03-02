from generated_code.gcode_grammarParser import gcode_grammarParser
from generated_code.gcode_grammarVisitor import gcode_grammarVisitor
import processing as proc


class GCodeVisitor(gcode_grammarVisitor):
    def visitProgram(self, ctx: gcode_grammarParser.ProgramContext):
        for command in ctx.command():
            self.visitCommand(command)

    def visitCommand(self, ctx: gcode_grammarParser.CommandContext):
        if ctx.simple_motion_command():
            self.visitSimple_motion_command(ctx.simple_motion_command())

    def visitSimple_motion_command(self, ctx: gcode_grammarParser.Simple_motion_commandContext):
        args = []
        for arg in ctx.arguement():
            args.append(self.visitArguement(arg))
        motion_type = ctx.getChild(0).getText() if ctx.getChild(0) else None

        if motion_type == "G0":
            print("Rapid move with args:")
            for arg in args:
                proc.handle_arguement(arg[0], arg[1])
        elif motion_type == "G1":
            print("Linear move with args:")
            for arg in args:
                proc.handle_arguement(arg[0], arg[1])
        print("\n")

    def visitArguement(self, ctx: gcode_grammarParser.ArguementContext):
        key = ctx.ID().getText()
        number = float(ctx.NUMBER().getText())
        return [key, number]

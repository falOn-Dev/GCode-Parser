grammar gcode_grammar;

    // Motion Control
    LINEAR_MOTION_KEY: 'G1';
    RAPID_MOTION_KEY: 'G0';

    NUMBER: '-'? [0-9]+ ('.' [0-9]+)?;

    // Arguments
    X_ARG: ' '? 'X' NUMBER;
    Y_ARG: ' '? 'Y' NUMBER;
    Z_ARG: ' '? 'Z' NUMBER;
    EXTRUSION_ARG: ' '? 'E' NUMBER;
    FEEDRATE_ARG: ' '? 'F' NUMBER;


    NEW_LINE: '\r'? '\n';

    COMMENT: '\n;' ~[\r\n]* -> skip;

    program: command (NEW_LINE command)*;

    command: simple_motion_command;

    // Motion Control
    simple_motion_command: (LINEAR_MOTION_KEY | RAPID_MOTION_KEY) X_ARG? Y_ARG? Z_ARG? EXTRUSION_ARG? FEEDRATE_ARG?;



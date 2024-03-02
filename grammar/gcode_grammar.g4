grammar gcode_grammar;

    // Motion Control
    LINEAR_MOTION_KEY: 'G1';
    RAPID_MOTION_KEY: 'G0';

    NUMBER: '-'? [0-9]+ ('.' [0-9]+)?;
    ID: [A-Z]+;

    // Arguments


    // Whitespace Rules
    NEW_LINE: '\r'? '\n';
    COMMENT: '\n;' ~[\r\n]* -> skip;

    /*
     * Program Entry Point
     * Programs are comprised of single commands followed by newlines
     */
    program: command (NEW_LINE command)*;

    // Command Rules
    command: simple_motion_command;

    // Motion Control
    simple_motion_command: (LINEAR_MOTION_KEY | RAPID_MOTION_KEY) arguement+;

    arguement: ' ' ID NUMBER;



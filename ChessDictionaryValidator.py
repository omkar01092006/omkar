def isValidChessBoard(board):
    piece_limits = {
        'pawn': 8,
        'rook': 2,
        'knight': 2,
        'bishop': 2,
        'queen': 1,
        'king': 1
    }

    valid_positions = [f"{r}{c}" for r in '12345678' for c in 'abcdefgh']
    valid_pieces = {'pawn', 'rook', 'knight', 'bishop', 'queen', 'king'}

    piece_count = {
        'w': {},
        'b': {}
    }

    total_pieces = {'w': 0, 'b': 0}

    for position, piece in board.items():

        if position not in valid_positions:
            print(f"Invalid position: {position}")
            return False


        if len(piece) < 2 or piece[0] not in 'wb':
            print(f"Invalid piece format: {piece}")
            return False

        color = piece[0]
        piece_type = piece[1:]

        if piece_type not in valid_pieces:
            print(f"Invalid piece type: {piece_type}")
            return False

        piece_count[color][piece_type] = piece_count[color].get(piece_type, 0) + 1
        total_pieces[color] += 1

    for color in ['w', 'b']:

        if total_pieces[color] > 16:
            print(f"Too many {color} pieces: {total_pieces[color]}")
            return False

        for piece_type, limit in piece_limits.items():
            if piece_count[color].get(piece_type, 0) > limit:
                print(f"Too many {color}{piece_type}s: {piece_count[color][piece_type]}")
                return False


        if piece_count[color].get('king', 0) != 1:
            print(f"{color} must have exactly one king.")
            return False

    return True



chessBoard = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
    '3e': 'wking'
}

print(isValidChessBoard(chessBoard)) 

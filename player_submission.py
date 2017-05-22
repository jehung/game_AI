#!/usr/bin/env python
from isolation import Board, game_as_text


# This file is your main submission that will be graded against. Do not
# add any classes or functions to this file that are not part of the classes
# that we want.

# Submission Class 1
class OpenMoveEvalFn:
    def score(self, game, maximizing_player_turn=True):
        """Score the current game state

        Evaluation function that outputs a score equal to how many 
        moves are open for AI player on the board minus the moves open 
        for opponent player.

        Args
            param1 (Board): The board and game state.
            param2 (bool): True if maximizing player is active.

        Returns:
            int: The current state's score. Your agent's moves minus the opponent's moves.

        """
        if maximizing_player_turn:
            eval_fn = game.get_legal_moves().__len__()
        else:
            eval_fn = game.get_opponent_moves().__len__()
        return eval_fn



# Submission Class 2
class CustomEvalFn:
    def __init__(self):
        pass

    def score(self, game, maximizing_player_turn=True):
        """Score the current game state

        Custom evaluation function that acts however you think it should. This 
        is not required but highly encouraged if you want to build the best 
        AI possible.

        Args
            game (Board): The board and game state.
            maximizing_player_turn (bool): True if maximizing player is active.

        Returns:
            bool: The current state's score, based on your own heuristic.

        """
        # TODO: update for stochastic game
        if maximizing_player_turn:
            eval_fn = game.get_legal_moves().__len__()
        else:
            eval_fn = game.get_opponent_moves().__len__()
        return eval_fn



class CustomPlayer:
    """Player that chooses a move using 
    your evaluation function and 
    a depth-limited minimax algorithm 
    with alpha-beta pruning.
    You must finish and test this player
    to make sure it properly uses minimax
    and alpha-beta to return a good move
    in less than 5 seconds."""

    def __init__(self, search_depth=3, eval_fn=OpenMoveEvalFn()):
        """Initializes your player.

        if you find yourself with a superior eval function, update the default 
        value of `eval_fn` to `CustomEvalFn()`

        Args:
            search_depth (int): The depth to which your agent will search
            eval_fn (function): Utility function used by your agent
        """
        self.eval_fn = eval_fn
        self.search_depth = search_depth

    def move(self, game, legal_moves, time_left):
        """Called to determine one move by your agent

        Args:
            game (Board): The board and game state.
            legal_moves (dict): Dictionary of legal moves and their outcomes
            time_left (function): Used to determine time left before timeout

        Returns:
            (tuple, int): best_move, best_queen
        """
        best_move, best_queen, utility = self.minimax(game, time_left, depth=self.search_depth)
        # change minimax to alphabeta after completing alphabeta part of assignment
        return best_move, best_queen

    def utility(self, game):
        """Can be updated if desired"""
        # TODO: update utility for stochastic game
        return self.eval_fn.score(game)

    def minimax(self, game, time_left, depth=float("inf"), maximizing_player=True):
        """Implementation of the minimax algorithm

        Args:
            game (Board): A board and game state.
            time_left (function): Used to determine time left before timeout
            depth: Used to track how deep you are in the search tree
            maximizing_player (bool): True if maximizing player is active.

        Returns:
            (tuple, int, int): best_move, best_queen, best_val
        """
        moves = game.get_legal_moves().values()[0]
        #print(game.get_legal_moves().values()[0])
        best_move = None
        best_score = float('-inf')
        best_queen = None
        best_val = None
        for move_key, move_value in moves.items():
            #print('move_key', move_key)
            #print('move_value', move_value)
            # gamestate = game.forecast_move(move, game.get_active_player())
            gamestate = game.forecast_move(move_key, self)
            score = self.minimax_maxvalue(gamestate, depth, time_left, maximizing_player)*move_value[0][1]
            if score > best_score:
                best_move = move_key
                print('best_move', best_move)
                best_score = score
                print('best_score', best_score)
                now_queen = game.get_active_player()
                best_queen = now_queen == game.__active_player__
                best_val = self.utility(gamestate)
                print('best_val', best_val)
        return best_move, best_queen, best_val

    def minimax_maxvalue(self, gamestate, depth, time_left, maximizing_player):
        if depth == 0 or time_left < 5 or (not gamestate.get_legal_moves().values()[0]):
            return self.utility(gamestate)

        moves = gamestate.get_legal_moves().values()[0]
        best_score = float('-inf')
        for move_key, move_value in moves.items():
            gamestate = gamestate.forecast_move(move_key, gamestate.get_active_player())
            score = self.minimax_minvalue(gamestate, depth-1, time_left, False)*move_value[0][1]
            if score > best_score:
                best_score = score
        return best_score

    def minimax_minvalue(self, gamestate, depth, time_left, maximizing_player):
        if depth == 0 or time_left < 5 or (not gamestate.get_legal_moves().values()[0]):
            return self.utility(gamestate)

        moves = gamestate.get_legal_moves().values()[0]
        best_score = float('inf')
        for move_key, move_value in moves.items():
            gamestate = gamestate.forecast_move(move_key, gamestate.get_active_player())
            score = self.minimax_maxvalue(gamestate, depth-1, time_left, True)
            if score < best_score:
                best_score = score
        return best_score

    def alphabeta(self, game, time_left, depth=float("inf"), alpha=float("-inf"), beta=float("inf"),
                  maximizing_player=True):
        """Implementation of the alphabeta algorithm

        Args:
            game (Board): A board and game state.
            time_left (function): Used to determine time left before timeout
            depth: Used to track how deep you are in the search tree
            alpha (float): Alpha value for pruning
            beta (float): Beta value for pruning
            maximizing_player (bool): True if maximizing player is active.

        Returns:
            (tuple, int, int): best_move, best_queen, best_val
        """
        # TODO: finish this function!
        raise NotImplementedError
        #return best_move, best_queen, val
# AI-3

# Minimax
```
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
```

# Alfa-Beta
```
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
```

# Expectimax
```
python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3
python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10
python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10
```

# Better Eval Function
```
python pacman.py -p ExpectimaxAgent -l smallClassic -a depth=3 -q -n 10
```


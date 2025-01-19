from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
from .stockfish import opponent
import chess
import chess.engine
import chess.engine as configure

stockfish_path = "./stockfish/stockfish-windows-x86-64-avx2.exe"

time_limit = chess.engine.Limit(time=0.1)

engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
print(os.curdir,'this is it')

# Create your views here.

@api_view(['POST'])
def enginePost(request):
    
    data= request.data
    fen = data['fen']
    depth = data['depth']
    board = chess.Board(fen)
    print(depth)
    best_move = engine.play(board, configure.Limit(time=10000,depth=depth)).move
    
    return Response({'value':str(best_move)})


@api_view(['POST'])
def getCp(request):
    data = request.data
    fen = data['fen']
    turn = data['turn']
    print(data)
    previous_best_cp = data['best_cp']
    board = chess.Board(fen)
    best_move = engine.play(board, time_limit).move
    board.push(best_move)
    info = engine.analyse(board, time_limit)

    if info['score'].is_mate():
        return Response({'best_cp':previous_best_cp})
    if turn==1:
        best_cp = info['score'].white().score()
    elif turn==2:
        best_cp = info['score'].black().score()

    return Response({'best_cp':best_cp})

@api_view(['POST'])
def engineGet(request):
    data= request.data
    fen = data['fen']
    turn = data['turn']
    previous_best_cp = data['best_cp']
    previous_cp = data['cp']
    print(data)
    board = chess.Board(fen)
    winning=''

    info = engine.analyse(board, time_limit)
    
    if info['score'].is_mate():
        mate_move = info.get('score').relative.score(mate_score=True)
        total_move = f"Mate in {mate_move}"
        return Response({'value':total_move,'cp':previous_cp,'best_cp':previous_best_cp})
    if turn == 1:
        
        cp = info['score'].white().score()
    elif turn == 2:
        
        cp = info['score'].black().score()

    if cp > 0:
        winning='You are winning'
    elif cp < 0:
        winning='You are losing'
    else:
        winning='Balanced position'

    
   
    
    

    print(cp)
    value = opponent(cp,previous_cp,previous_best_cp)
 
    
        

    return Response({'value':value,'cp':cp,'winning':winning})
        

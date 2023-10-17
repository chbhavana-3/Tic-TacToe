from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def game_board(request):
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    context = {'board': board}
    return render(request, 'game/board.html', context)
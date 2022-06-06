wall(1,2,2,2).
wall(1,3,2,3).
wall(1,4,2,4).
wall(1,5,2,5).
wall(1,6,2,6).
wall(1,7,2,7).
wall(1,7,1,8).
wall(1,8,1,9).
wall(1,10,2,10).

wall(2,2,2,3).
wall(2,5,2,6).
wall(2,7,2,8).
wall(2,8,2,9).
wall(2,9,2,10).

wall(3,2,3,3).
wall(3,3,3,4).
wall(3,7,3,8).
wall(3,8,3,9).
wall(3,1,4,1).
wall(3,4,4,4).

wall(4,2,4,3).
wall(4,2,5,2).
wall(4,3,5,3).
wall(4,4,4,5).
wall(4,7,4,8).
wall(4,8,4,9).
wall(4,9,5,9).

wall(5,1,6,1).
wall(5,2,6,2).
wall(5,3,6,3).
wall(5,4,6,4).
wall(5,5,6,5).
wall(5,6,6,6).
wall(5,4,5,5).

wall(6,4,6,5).
wall(6,8,7,8).
wall(6,9,7,9).

wall(7,4,7,5).
wall(7,7,7,8).
wall(7,9,8,9).

wall(8,2,8,3).
wall(8,7,8,8).
wall(8,8,8,9).
wall(8,9,8,10).
wall(8,5,9,5).
wall(8,6,9,6).
wall(8,7,9,7).

wall(9,2,9,3).
wall(9,4,9,5).
wall(9,7,9,8).
wall(9,8,9,9).
wall(9,9,9,10).
wall(9,9,10,9).
wall(9,1,10,1).
wall(9,2,10,2).




moveable(X,Y,X1,Y1):-
    notmoveable(X,Y,X1,Y1) -> false; true.


notmoveable(X,Y,X1,Y1):-
    wall(X,Y,X1,Y1), !;
    wall(X1,Y1,X,Y).











/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Michal Wojtasik
 * Creation Date: Apr 25, 2023 at 9:34:12 AM
 *********************************************/
using CP;

//MacMahon
int height = 4;
int width = 6;
{int} colors = {3, 5, 7};
int max_color = ftoi(ceil((height * width * 4) / card(colors)));
range h = 1..height;
range w = 1..width;

dvar int color[h][w][1..4];
// height x width x 4 edges(góra, prawo, dół, lewo)
// nxn
dvar boolean visited[h][w][1..4];

dexpr float sum_visited = (sum(row in h, col in w, edge in 1..4) visited[row][col][edge]) / 2;
//dexpr int sum3 = count(all(i in h, j in w, k in 1..4) color[i][j][k], 3);
//dexpr int sum5 = count(all(i in h, j in w, k in 1..4) color[i][j][k], 5);
//dexpr int sum7 = count(all(i in h, j in w, k in 1..4) color[i][j][k], 7);

maximize sum_visited;

subject to{
  	forall(i in w){
    //Ściany góra i dół
    	(color[1][i][1] == first(colors) && color[height][i][3] == first(colors))
  		&&
  		((visited[1][i][1] == 0) && (visited[height][i][3] == 0));
  	}
  	forall(i in h){
    //Ściany lewa i prawa
    	(color[i][1][4] == first(colors) && color[i][width][2] == first(colors))
    	&&
  		((visited[i][1][4] == 0) && (visited[i][width][2] == 0));
  	}

	//Można tylko kolory z colors
  	forall(row in h){
    	forall(col in w){
      		forall(edge in 1..4){
        		color[row][col][edge] in colors;
      		}        
      	}
    }

// Zrobione ^
  	
  	forall(clr in colors){
  		count(all(i in h, j in w, k in 1..4) color[i][j][k], clr) <= max_color;
 	}  	
  	
	// sprawdzenie każdego połączenie czy występują sąsiedzi
	// przechodząc z [2][2] do [height-1][width-1] (poza obramowaniem)
  	forall(row in 2..height-1){
  		forall(col in 2..width-1){
  		  	//[n][m]Góra == [n-1][m]dół
  	   		((color[row][col][1] == color[row-1][col][3]) == (visited[row][col][1] == 1 && visited[row-1][col][3] == 1))
  	   		|| 
  	   		(visited[row][col][1] == 0 && visited[row-1][col][3] == 0);
  	   		
  	   		//[n][m]Prawo == [n][m+1]lewo
  	    	((color[row][col][2] == color[row][col+1][4]) == (visited[row][col][2] == 1 && visited[row][col+1][4] == 1))
  	    	||
  	    	(visited[row][col][2] == 0 && visited[row][col+1][4] == 0);
  	    	
  	    	//[n][m]Dół == [n+1][m]Góra
  	    	((color[row][col][3] == color[row+1][col][1]) == (visited[row][col][3] == 1 && visited[row+1][col][1] == 1))
  	    	||
  	    	(visited[row][col][3] == 0 && visited[row+1][col][1] == 0);
  	    	
  	    	//[n][m]Lewo == [n][m-1]Prawo
  	    	((color[row][col][4] == color[row][col-1][2]) == (visited[row][col][4] == 1 && visited[row][col-1][2] == 1))
  	    	||
  	    	(visited[row][col][4] == 0 && visited[row][col-1][2] == 0);
  	  	}
  	}

  	// [1][1] do [height-1][1] U [1][1] do [1][width-1] (w obramowaniu)
  	forall(i in 1..width-1){
    	//Prawo-Lewo z obramowania
    	((color[1][i][2] == color[1][i+1][4]) == (visited[1][i][2] == 1 && visited[1][i+1][4] == 1))
    	||
    	(visited[1][i][2] == 0 && visited[1][i+1][4] == 0);
    	
    	((color[height][i][2] == color[height][i+1][4]) == (visited[height][i][2] == 1 && visited[height][i+1][4] == 1))
    	||
    	(visited[height][i][2] == 0 && visited[height][i+1][4] == 0);
  	}
  	forall(i in 1..height-1){
    	//Góra-Dół z obramowania
    	((color[i][1][3] == color[i+1][1][1]) == (visited[i][1][3] == 1 && visited[i+1][1][1] == 1))
    	||
    	(visited[i][1][3] == 0 && visited[i+1][1][1] == 0);
    	
    	((color[i][width][3] == color[i+1][width][1]) == (visited[i][width][3] == 1 && visited[i+1][width][1] == 1))
    	||
    	(visited[i][width][3] == 0 && visited[i+1][width][1] == 0);
	}
}

execute {
  writeln(sum_visited);
  //writeln(sum3);
  //writeln(sum5);
  //writeln(sum7);
}
package GameofLife;

import com.sun.source.util.SourcePositions;

import javax.swing.*;
import java.net.StandardProtocolFamily;
import java.sql.SQLOutput;

/**
 * Game of Life
 * Author; Perry Boh
 * (go here <> for rules of the game
 */
public class Play
{
    static Grid myGrid = new Grid();
    public static  char[][] myUniverse = myGrid.grid;

    public static void main(String[] args)
    {
        //instantiate original generation
        myUniverse[1][2] = '*'; myUniverse[1][3] = '*';myUniverse[1][1] = '*'; //make a cell alive
        myUniverse[5][2] = '*'; myUniverse[5][3] = '*';myUniverse[5][1] = '*'; //
//        myGrid.showGrid(myUniverse);
        timePlay(40);
    }

    static void timePlay(int generations)//play gameOfLife
    {
        System.out.println("Orginal Generation"); myGrid.showGrid(myUniverse);
        int genPassed = 0; //
        while (genPassed<generations)
        {
            for (int row=1; row<9; row+=2)//myMap.grid == two dimensional array 30 X 100: start from row_1-9 to ignore edge cells // move by increment of 3 to not repeat visited cells
            {
                for (int column=1;column<29;column++ )// start from column_1-29 to ignore edge cells
                {
                    char cell = myUniverse[row][column];// will prefer cell numbers using cell numbers instead of rows/columns

                    if (isAlive(cell))//if cell is living
                    {
                        if (isAlive(neighBours(row,column))<2 || isAlive(neighBours(row,column))>3 )
                        {
                            kill(row,column);//cell dies from under/over population
                        }
                    }
                    else//if cell is dead
                    {
                        if(isAlive(neighBours(row,column))==3) giveLife(row,column);// cell is born
                    }
                }

            }

            System.out.println("Next Generation"); myGrid.showGrid(myUniverse); genPassed++;
        }
    }
    
    static int[][] neighBours(int rowCell, int columnCell )//returns array of neighbour cells
    {
        int[][] neighbours;
//        if (rowCell == 0)  // did the conditional to handle edge cells (just decided to ignore for this time)
//        {
//            neighbours = new int[5][2]; // rown zero cells have 5 columns only
//            neighbours[0][0] = rowCell; neighbours[0][1]=columnCell+1;//first neigbour cell
//            neighbours[1][0] = rowCell+1; neighbours[0][1]=columnCell+1; // 2nd neighbour
//            neighbours[2][0] = rowCell; neighbours[2][1]=columnCell;//3rd neigbour
//            neighbours[3][0] = rowCell+1; neighbours[3][1]=columnCell-1;//4th neighbour
//            neighbours[4][0] = rowCell; neighbours[4][1]=columnCell-1; //5th neigbour
//            return neighbours;
//        }
        neighbours = new int[8][2];// cell anywhere in mid grid has eight neighbours
        neighbours[0][0] = rowCell-1; neighbours[0][1]=columnCell;//first neigbour cell
        neighbours[1][0] = rowCell-1; neighbours[0][1]=columnCell+1; // 2nd neighbour
        neighbours[2][0] = rowCell; neighbours[2][1]=columnCell+1;//3rd neigbour
        neighbours[3][0] = rowCell+1; neighbours[3][1]=columnCell+1;//4th neighbour
        neighbours[4][0] = rowCell+1; neighbours[4][1]=columnCell; //5th neigbour
        neighbours[5][0] = rowCell+1; neighbours[5][1]=columnCell-1; //6th neigbour
        neighbours[6][0] = rowCell; neighbours[6][1]=columnCell-1; //7th neigbour
        neighbours[7][0] = rowCell-1; neighbours[7][1]=columnCell-1; //8th neigbour

        return  neighbours;

    }

    static int isAlive (int[][] neighbourCells)//return number of living neighbour cells
    {
        int numOflifeNeighbours = 0;
        for (int[] cells : neighbourCells)
        {
            if (isAlive(myUniverse[cells[0]] [cells[1]] ))    numOflifeNeighbours++;//cells == array[]; index 0/1 == to row/column index of a neighbour cell in myUniverse
        }
        return numOflifeNeighbours;
    }

    static boolean isAlive(char cell)
    {
        return cell == '*';// * is life and - is dead
    }

    static void kill(int row, int column)//kills living cell
    {
        myUniverse[row][column] = '-';
    }

    static void giveLife(int row, int column)//gives life to dead cell
    {
        myUniverse[row][column] = '*';
    }

}

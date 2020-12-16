package TeLoVoyAMeterEnLaBoca;
import java.util.Scanner;


/**
 * Write a description of class factoriaV2 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class factorialV2 {
    
    public static long factorial(){
        
        Scanner escaner = new Scanner(System.in);
        
        int n = escaner.nextInt();
        long factorial = 1;
        
        for(int i = 1 ; i <= n ; i++ ){
            
            System.out.println("i:" + i + "factorial: " + factorial);
            factorial = factorial*i;
            
        
        }
    
        return factorial;
    }   

    public static void main (String args[]){
        
        System.out.println(factorial());
    
    }
        
}

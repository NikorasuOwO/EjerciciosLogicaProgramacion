package TeLoVoyAMeterEnLaBoca;

import java.util.Scanner;


/**
 * Write a description of class factoriaV2 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class FactorialConRecursion {
    
    public static long factorial(int n){
        
        if (n == 0){
            return 1;
        }
        long factorial = n*factorial(n-1);
        return factorial;
    }   

    public static void main (String args[]){
        
        Scanner escaner = new Scanner(System.in);
        
        int n = escaner.nextInt();
        
        
        System.out.println(factorial(n));
    
    }
        
}


package TeLoVoyAMeterEnLaBoca;

import java.util.Scanner;


public class factorial {
    
    public static long factorial(){
        
        Scanner escaner = new Scanner(System.in);
        
        int n = escaner.nextInt();
        long factorial = n;
        
        for(int i = n ; i > 1 ; i-- ){
            
            System.out.println("i:" + i + "factorial: " + factorial);
            factorial = factorial*(i-1);
            
        
        }
    
        return factorial;
    }
    public static void main (String args[]){
        
        System.out.println(factorial());
    
    }



}

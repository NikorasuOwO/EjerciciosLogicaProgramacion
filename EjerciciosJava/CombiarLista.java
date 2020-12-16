package EjPaloma;


public class CombiarLista {
    
    public static int[] combinarArrays(int[] lista1, int[] lista2){
        
        int[] listafinal = new int[lista1.length + lista2.length];
        
        for (int i = 0 ; i < lista1.length; i++){
            listafinal[i] = lista1[i];
            System.out.println(listafinal[i]);
        }
        for (int i = lista1.length -1 ; i <= lista1.length +lista2.length; i++){
            listafinal[i] = lista2[i - (lista1.length -2)];
            System.out.println(listafinal[i - (lista1.length -2)]);
        }
    
        return listafinal;
    }
    
    public static void main (String args[]){
    
        int[] lista1 = {1,2,3,4,5,6};
        int[] lista2 = {7,8,9,10};
        
        System.out.println(combinarArrays(lista1, lista2));
        
        
    
    }
}

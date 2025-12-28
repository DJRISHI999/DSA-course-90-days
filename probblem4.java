public class probblem4 {
    public static boolean isPrime(int n) {
        if(n==1){
            return false;
        }
        
        for(int i=2;i*i<=n;i++){
            if(n%i==0){
                return false;
            }

        }
        return true;
    }
        public static int PrimeinRange(int n){
            for(int i=2;i<=n;i++){
                if(isPrime(i)){
                    System.out.println(i);
                }
        }
        return -1;
        }
        public static void main(String args[]){
            PrimeinRange(5);
        }

    
    
}
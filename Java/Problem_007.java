/**
 *
 * @author Christian Seely
 *
 */
public class Problem_007
{

    private static boolean isPrime(int t_n)
    {
        int div = 2;
        while(div <= Math.sqrt(t_n))
        {
            if(t_n%div == 0) return false;
            div += 1;
        }
        return true;
    }

    public static int problemSeven(){
        int nPrimes = 0;
        int i = 2;
        while(nPrimes < 10001)
        {
            if(isPrime(i)) nPrimes += 1;
            i += 1;
        }
        return (i - 1);
    }

    public static void main(String[] args) { System.out.println(problemSeven()); }
}

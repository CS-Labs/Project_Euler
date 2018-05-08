import java.util.ArrayList;
import java.util.Collections;

/**
 *
 * @author Christian Seely
 *
 */
public class Problem_010 {

    public static long problemTen(){
        int scope = 2_000_000;
        ArrayList<Integer> n = new ArrayList<>(Collections.nCopies(scope, 1));
        int bound = (int)Math.sqrt(n.size());
        int j,k;
        for(int i = 2; i < bound; i++)
        {
            if(n.get(i) == 1)
            {
                j = (i*i);
                k = 1;
                while (j < scope)
                {
                    n.set(j,0);
                    j = (i*i) + (k*i);
                    k += 1;
                }
            }
        }
        long sum = 0;
        for(int i = 2; i < scope; i++)
        {
            if(n.get(i) > 0) sum += i;
        }
        return sum;
    }

    public static void main(String[] args) { System.out.println(problemTen()); }
}

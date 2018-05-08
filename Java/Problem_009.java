import javafx.util.Pair;

/**
 *
 * @author Christian Seely
 *
 */
public class Problem_009
{

    /*
    Method to find the Pythagorean Triple such that
    a+b+c = 1000. This method uses Euclid's formula
    for increased speed. Euclid's formula works by
    providing two numbers in this case i, and j such
    that i>j and generates a unique Pythagorean Triple.
    This version of Euclid's formula does not make use
    of the constant k so all possible combinations of
    i and j | i>j only encompass a subset of the total
    solution set of Pythagorean Triples. In this case the
    answer we were looking for was contained in the subset.
    */
    private static Pair<Boolean, Integer> euclidsFormulaHelper(int t_i, int t_j)
    {
        int a = (t_i*t_i) - (t_j*t_j);
        int b = 2 * t_i*t_j;
        int c = (t_i*t_i) + (t_j*t_j);
        if (a + b + c == 1000) return new Pair<Boolean, Integer>(true, a*b*c);
        else return new Pair<Boolean, Integer>(false, 0);
    }

    public static int problemNine(){
        for(int i = 0; i < 1000; i++)
        {
            for(int j = 0; j < 1000; j++)
            {
                if(i > j)
                {
                    Pair<Boolean, Integer> result = euclidsFormulaHelper(i, j);
                    if(result.getKey()) return result.getValue();
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) { System.out.println(problemNine()); }
}

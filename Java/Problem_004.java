import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 *
 * @author Christian Seely
 *
 */

public class Problem_004 {


    private static boolean m_IsPalindromicMultiple(int t_mult) {
        int forward = t_mult;
        int reverse = 0;
        while (t_mult > 0) {
            int currDigit = t_mult % 10;
            t_mult /= 10;
            reverse = reverse * 10 + currDigit;
        }
        return forward == reverse;
    }


    public static int problemFour(){
        List<Integer> numbers = Stream.iterate(100, n -> n + 1).limit(900).collect(Collectors.toList());
        return numbers.stream().flatMap(x -> numbers.stream().map(y -> x*y))
                .filter(Problem_004::m_IsPalindromicMultiple)
                .max(Integer::compare).orElse(-1);
    }

    public static void main(String[] args) { System.out.println(problemFour()); }
}

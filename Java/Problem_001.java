import java.util.stream.IntStream;

/**
 * 
 * @author Christian Seely
 *
 */

public class Problem_001 {

    public static int problemOne(){
        return IntStream.range(0,1000).filter(i -> i % 3 == 0 || i % 5 == 0).sum();
    }

    public static void main(String[] args) { System.out.println(problemOne()); }
}
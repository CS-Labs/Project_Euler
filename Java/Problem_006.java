import java.util.stream.IntStream;

/**
 * 
 * @author Christian Seely
 *
 */
public class Problem_006 {

	/*
	 * Find the sum of the squares of the numbers1 to n.
	 */
	private static int m_SumOfSquares(int n) { return IntStream.range(0,n).map(i -> i*i).sum(); }
	/*
	 * Find the square of the sum of the numbers 1 to n.
	 */
	private static int m_SquareOfSum(int n) { return (int) Math.pow((double) IntStream.range(0,n).sum(),2); }

	public static int problemSix() { return m_SquareOfSum(101)-m_SumOfSquares(101); }

	public static void main(String[] args) { System.out.println(problemSix()); }

}

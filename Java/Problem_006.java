/**
 * 
 * @author Christian Seely
 *
 */
public class Problem_006 {
	public static void main(String[] args) 
	{
			int answer = (squareOfSum(101)-sumOfSquares(101));
			System.out.println(answer);
	}
	/*
	 * Find the sum of the squares of the numbers1 to n.
	 */
	private static int sumOfSquares(int n)
	{
		int sum = 0;
		for(int i = 0; i < n; i++)sum+=(i*i);
		return sum;
	}
	/*
	 * Find the square of the sum of the numbers 1 to n.
	 */
	private static int squareOfSum(int n)
	{
		int sum = 0;
		for(int i = 0; i < n; i++)sum+=i;
		return (sum*sum);	
	}
	
}

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

/**
 * 
 * @author Christian Seely
 *
 */
public class Problem_005 
{
	public static void main(String[] args) 
	{
		// Range
		List<Integer> numbers = Arrays.asList(new Integer[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
				,13,14,15,16,17,18,19,20});
		// Find LCM of (1-20) recursively.
		Optional<Integer> ans = numbers.stream().reduce((a, b) -> a/gcd(a,b)*b);
		System.out.println(ans.get());
	}
	/**
	 * Function to find the Greatest Common Divisor
	 * given two numbers a and b.
	 */
	private static int gcd(int a, int b)
	{
		int r;
		while(b!=0)
		{
			r=a%b;
			a=b;
			b=r;
		}
		return a;
	}
}

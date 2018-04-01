import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.IntStream;

/**
 * 
 * @author Christian Seely
 *
 */
public class Problem_005 
{

	private static int m_gcd(int t_a, int t_b)
	{
		int r;
		while(t_b!=0)
		{
			r=t_a%t_b;
			t_a=t_b;
			t_b=r;
		}
		return t_a;
	}

	private static int problemFive()
	{
		return IntStream.range(1,20).reduce((a, b) -> a/m_gcd(a,b)*b).orElse(-1);
	}

	public static void main(String[] args) { System.out.println(problemFive()); }
}

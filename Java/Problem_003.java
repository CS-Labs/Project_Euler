/**
 * 
 * @author Christian Seely
 *
 */
public class Problem_003 {

	public static long problemThree()
	{
		long max = 0;
		int div = 2;
		long n = 600_851_475_143L;
		while(true)
		{
			if((div*div) > n)
			{
				if(n != 1 && n > max) max = n;
				break;
			}
			if(n % div == 0)
			{
				if(div > max) max = div;
				n /= div;
				while(n % div == 0) n /= div;
			}
			div++;
		}
		return max;
	}

	public static void main(String[] args) { System.out.println(problemThree()); }
}
